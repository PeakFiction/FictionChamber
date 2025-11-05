#!/usr/bin/env python3
import argparse, socket, threading, sys, time, queue, os

MAX_LINE_BYTES = 4096

def clamp_line(s: str) -> str:
    s = ''.join(ch for ch in s if ch == '\t' or (32 <= ord(ch) <= 126) or ch == '\n')
    if len(s.encode('utf-8')) > MAX_LINE_BYTES:
        b = s.encode('utf-8')[:MAX_LINE_BYTES]
        try:
            s = b.decode('utf-8')
        except UnicodeDecodeError:
            s = b.decode('utf-8', errors='ignore')
    return s

def recv_loop(sock, out_q, stop):
    f = sock.makefile('r', encoding='utf-8', newline='\n')
    try:
        for line in f:
            if stop.is_set():
                break
            out_q.put(("remote", line.rstrip('\n')))
    except Exception:
        pass
    finally:
        stop.set()
        try: f.close()
        except: pass

def send_loop(sock, nickname, stop):
    f = sock.makefile('w', encoding='utf-8', newline='\n')
    current_nick = nickname
    try:
        while not stop.is_set():
            try:
                line = input()
            except EOFError:
                line = "/quit"
            line = clamp_line(line).rstrip('\n')
            if not line:
                continue
            if line.startswith("/nick "):
                newnick = line[6:].strip()
                if newnick:
                    current_nick = newnick
                    print(f"[local] nickname set to {current_nick}")
                continue
            if line == "/quit":
                stop.set()
                break
            timestamp = time.strftime("%H:%M:%S")
            msg = f"[{timestamp}] {current_nick}: {line}"
            f.write(msg + "\n")
            f.flush()
    except BrokenPipeError:
        pass
    finally:
        stop.set()
        try: f.close()
        except: pass

def printer(out_q, stop):
    while not stop.is_set():
        try:
            origin, msg = out_q.get(timeout=0.1)
        except queue.Empty:
            continue
        if origin == "remote":
            print(msg)

def main():
    p = argparse.ArgumentParser(description="Minimal LAN chat client.")
    p.add_argument("--host", required=True, help="Server LAN IP")
    p.add_argument("--port", type=int, default=54545)
    p.add_argument("--nick", type=str, default=os.getenv("USER") or "client")
    args = p.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((args.host, args.port))
    except Exception as e:
        print(f"[error] connect failed: {e}")
        return

    print(f"[info] connected to {args.host}:{args.port}")
    print("[info] commands: /nick NEWNAME, /quit")

    stop = threading.Event()
    out_q = queue.Queue()

    t_recv = threading.Thread(target=recv_loop, args=(sock, out_q, stop), daemon=True)
    t_send = threading.Thread(target=send_loop, args=(sock, args.nick, stop), daemon=True)
    t_print = threading.Thread(target=printer, args=(out_q, stop), daemon=True)
    for t in (t_recv, t_send, t_print):
        t.start()

    try:
        while not stop.is_set():
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        try: sock.shutdown(socket.SHUT_RDWR)
        except: pass
        try: sock.close()
        except: pass

if __name__ == "__main__":
    main()
