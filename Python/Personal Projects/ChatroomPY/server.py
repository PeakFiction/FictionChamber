#!/usr/bin/env python3
import argparse, socket, threading, sys, time, queue, os

MAX_LINE_BYTES = 4096

def clamp_line(s: str) -> str:
    # keep printable-ish, strip control chars except tab and newline
    s = ''.join(ch for ch in s if ch == '\t' or (32 <= ord(ch) <= 126) or ch == '\n')
    if len(s.encode('utf-8')) > MAX_LINE_BYTES:
        # truncate by bytes, not chars
        b = s.encode('utf-8')[:MAX_LINE_BYTES]
        try:
            s = b.decode('utf-8')
        except UnicodeDecodeError:
            s = b.decode('utf-8', errors='ignore')
    return s

def recv_loop(sock: socket.socket, out_q: queue.Queue, stop: threading.Event):
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

def send_loop(sock: socket.socket, nickname: str, stop: threading.Event):
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

def printer(out_q: queue.Queue, stop: threading.Event):
    while not stop.is_set():
        try:
            origin, msg = out_q.get(timeout=0.1)
        except queue.Empty:
            continue
        if origin == "remote":
            print(msg)

def main():
    p = argparse.ArgumentParser(description="Minimal LAN chat server (single client).")
    p.add_argument("--port", type=int, default=54545)
    p.add_argument("--nick", type=str, default=os.getenv("USER") or "server")
    args = p.parse_args()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("0.0.0.0", args.port))
    srv.listen(1)

    host_ip = socket.gethostbyname(socket.gethostname())
    print(f"[info] listening on {host_ip}:{args.port}")
    print("[info] waiting for one client to connect...")

    try:
        conn, addr = srv.accept()
    except KeyboardInterrupt:
        srv.close()
        return

    print(f"[info] client connected from {addr[0]}:{addr[1]}")
    stop = threading.Event()
    out_q = queue.Queue()

    t_recv = threading.Thread(target=recv_loop, args=(conn, out_q, stop), daemon=True)
    t_send = threading.Thread(target=send_loop, args=(conn, args.nick, stop), daemon=True)
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
        try: conn.shutdown(socket.SHUT_RDWR)
        except: pass
        try: conn.close()
        except: pass
        try: srv.close()
        except: pass

if __name__ == "__main__":
    main()
