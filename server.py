'''
Author: SingleBiu
Date: 2024-12-01 15:12:31
LastEditors: SingleBiu
LastEditTime: 2024-12-01 15:25:08
Description: file content
'''
import socketserver

class ThreadedTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data = self.request.recv(1024).strip()
            if not data:
                break
            response = f"Server recv:{data.decode()}"
            self.request.sendall(response.encode())

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(
        ("0.0.0.0",8888),
        ThreadedTCPHandler
    )
    print("Server is running.")
    server.serve_forever()