TCP Command Execution Server:
This project implements a basic TCP Socket Server in Python. It is designed to listen for incoming client connections, receive commands, and execute them on the host system using the subprocess module.

Features
Socket Communication: Utilizes the socket library to handle network connections.

Command Execution: Employs subprocess.Popen to run received data as shell commands.

Error Handling: Includes try-except-finally blocks to manage execution flow and ensure resource cleanup.

Address Reuse: Configured with SO_REUSEADDR to allow immediate restarting of the server on the same port.

Prerequisites
Python 3.x

Operating System: Windows, Linux, or macOS (Note: Shell commands are OS-dependent).

Component,Configuration
Host,localhost
Port,80
Protocol,TCP (SOCK_STREAM)
Backlog,10 simultaneous connections
