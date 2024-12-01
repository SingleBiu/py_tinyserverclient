'''
Author: SingleBiu
Date: 2024-12-01 15:09:18
LastEditors: SingleBiu
LastEditTime: 2024-12-01 15:12:20
Description: file content
'''
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8888))

message = "Hello server!"

client.send(message.encode())

response = client.recv(1024).decode()
print(f"Server response:{response}")

client.close()