package main

import (
	"context"
	"crypto/tls"
	"fmt"
	"log"
	"net"
	"os"

	"github.com/quic-go/quic-go"
	"jarkom.cs.ui.ac.id/h01/project/utils"
)

const (
	serverIP          = "35.230.103.122"
	serverPort        = "6790"
	serverType        = "udp4"
	bufferSize        = 2048
	appLayerProto     = "lrt-jabodebek-2206046790"
	sslKeyLogFileName = "ssl-key.log"
)

func main() {
	destination := "Harjamukti"
	packet := utils.LRTPIDSPacket{
		LRTPIDSPacketFixed: utils.LRTPIDSPacketFixed{
			TransactionId:     0x01,
			IsAck:             false,
			IsNewTrain:        false,
			IsUpdateTrain:     false,
			IsDeleteTrain:     false,
			IsTrainArriving:   true,
			IsTrainDeparting:  false,
			TrainNumber:       42,
			DestinationLength: uint8(len(destination)),
		},
		Destination: destination,
	}
	packet2 := utils.LRTPIDSPacket{
		LRTPIDSPacketFixed: utils.LRTPIDSPacketFixed{
			TransactionId:     0x56,
			IsAck:             false,
			IsNewTrain:        false,
			IsUpdateTrain:     false,
			IsDeleteTrain:     false,
			IsTrainArriving:   false,
			IsTrainDeparting:  true,
			TrainNumber:       42,
			DestinationLength: uint8(len(destination)),
		},
		Destination: destination,
	}
	packet3 := utils.LRTPIDSPacket{
		LRTPIDSPacketFixed: utils.LRTPIDSPacketFixed{
			TransactionId:     0x57,
			IsAck:             false,
			IsNewTrain:        false,
			IsUpdateTrain:     false,
			IsDeleteTrain:     false,
			IsTrainArriving:   false,
			IsTrainDeparting:  false,
			TrainNumber:       42,
			DestinationLength: uint8(len(destination)),
		},
		Destination: destination,
	}
	result := utils.Encoder(packet)
	fmt.Println(result)
	fmt.Println(utils.Decoder(result))

	sslKeyLogFile, err := os.Create(sslKeyLogFileName)
	if err != nil {
		log.Fatalln(err)
	}
	defer sslKeyLogFile.Close()

	fmt.Printf("QUIC Client Socket Program Example in Go\n")

	tlsConfig := &tls.Config{
		InsecureSkipVerify: true,
		NextProtos:         []string{appLayerProto},
		KeyLogWriter:       sslKeyLogFile,
	}
	connection, err := quic.DialAddr(context.Background(), net.JoinHostPort(serverIP, serverPort), tlsConfig, &quic.Config{})
	if err != nil {
		log.Fatalln(err)
	}

	defer connection.CloseWithError(0x0, "No Error")

	fmt.Printf("[quic] Dialling from %s to %s\n", connection.LocalAddr(), connection.RemoteAddr())

	fmt.Printf("[quic] Creating receive buffer of size %d\n", bufferSize)
	receiveBuffer := make([]byte, bufferSize)

	fmt.Printf("[quic] Input message to be sent to server: ")

	stream, err := connection.OpenStreamSync(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Opened bidirectional stream %d to %s\n", stream.StreamID(), connection.RemoteAddr())

	_, err = stream.Write([]byte(utils.Encoder(packet)))
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Message sent\n", stream.StreamID())

	receiveStream, err := connection.AcceptStream(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Accepted stream %d from server\n", receiveStream.StreamID())

	receiveLength, err := receiveStream.Read(receiveBuffer)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Received %d bytes of message from server\n", receiveStream.StreamID(), receiveLength)

	response := receiveBuffer[:receiveLength]
	fmt.Printf("[quic] [Stream ID: %d] Received message: '%s'\n", receiveStream.StreamID(), response)

	////////////////////////////

	stream, err = connection.OpenStreamSync(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Opened bidirectional stream %d to %s\n", stream.StreamID(), connection.RemoteAddr())

	_, err = stream.Write([]byte(utils.Encoder(packet2)))
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Message sent\n", stream.StreamID())

	receiveStream, err = connection.AcceptStream(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Accepted stream %d from server\n", receiveStream.StreamID())

	receiveLength, err = receiveStream.Read(receiveBuffer)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Received %d bytes of message from server\n", receiveStream.StreamID(), receiveLength)

	response = receiveBuffer[:receiveLength]
	fmt.Printf("[quic] [Stream ID: %d] Received message: '%s'\n", receiveStream.StreamID(), response)

	///////////////////

	stream, err = connection.OpenStreamSync(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Opened bidirectional stream %d to %s\n", stream.StreamID(), connection.RemoteAddr())

	_, err = stream.Write([]byte(utils.Encoder(packet3)))
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Message sent\n", stream.StreamID())

	receiveStream, err = connection.AcceptStream(context.Background())
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] Accepted stream %d from server\n", receiveStream.StreamID())

	receiveLength, err = receiveStream.Read(receiveBuffer)
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("[quic] [Stream ID: %d] Received %d bytes of message from server\n", receiveStream.StreamID(), receiveLength)

	response = receiveBuffer[:receiveLength]
	fmt.Printf("[quic] [Stream ID: %d] Received message: '%s'\n", receiveStream.StreamID(), response)

}
