package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"io"
	"log"
	"net"

	"github.com/quic-go/quic-go"
	"jarkom.cs.ui.ac.id/h01/project/utils"
)

func Handler(packet utils.LRTPIDSPacket) string {
	if packet.IsTrainArriving {
		return "Attention, the train to " + packet.Destination + " will arrive at Platform 1"
	} else if packet.IsTrainDeparting {
		return "Attention, the train to " + packet.Destination + " will depart from Platform 1 "
	}
	return ""
}

const (
	serverIP      = "10.138.0.2"
	serverPort    = "6790"
	serverType    = "udp4"
	bufferSize    = 2048
	appLayerProto = "lrt-jabodebek-2206046790"
)

func main() {
	localUdpAddress, err := net.ResolveUDPAddr(serverType, net.JoinHostPort(serverIP, serverPort))
	if err != nil {
		log.Fatalln(err)
	}
	socket, err := net.ListenUDP(serverType, localUdpAddress)
	if err != nil {
		log.Fatalln(err)
	}

	defer socket.Close()

	fmt.Printf("QUIC Server Socket Program Example in Go\n")
	fmt.Printf("[%s] Preparing UDP listening socket on %s\n", serverType, socket.LocalAddr())

	tlsConfig := &tls.Config{
		Certificates: utils.GenerateTLSSelfSignedCertificates(),
		NextProtos:   []string{appLayerProto},
	}
	listener, err := quic.Listen(socket, tlsConfig, &quic.Config{})
	if err != nil {
		log.Fatalln(err)
	}

	defer listener.Close()

	fmt.Printf("[quic] Listening QUIC connections on %s\n", listener.Addr())

	for {
		connection, err := listener.Accept(context.Background())
		if err != nil {
			log.Fatalln(err)
		}

		go handleConnection(connection)
	}
}

func handleConnection(connection quic.Connection) {
	fmt.Printf("[quic] Receiving connection from %s\n", connection.RemoteAddr())

	for i := 0; i < 2; i++ {
		stream, err := connection.AcceptStream(context.Background())
		if err != nil {
			log.Fatalln(err)
		}
		go handleStream(connection.RemoteAddr(), stream)
	}
}

func handleStream(clientAddress net.Addr, stream quic.Stream) {
	fmt.Printf("[quic] [Client: %s] Receive stream open request with ID %d\n", clientAddress, stream.StreamID())

	_, err := io.Copy(logicProcessorAndWriter{stream}, stream)
	if err != nil {
		fmt.Println(err)
	}
}

type logicProcessorAndWriter struct{ io.Writer }

func (lp logicProcessorAndWriter) Write(receivedMessageRaw []byte) (int, error) {

	receivedMessage := utils.Decoder(receivedMessageRaw)
	receivedMessage.IsAck = true

	response := utils.Encoder(receivedMessage)
	fmt.Printf("[quic] Receive message: %s\n", Handler(receivedMessage))

	writeLength, err := lp.Writer.Write([]byte(response))
	return writeLength, err
}
