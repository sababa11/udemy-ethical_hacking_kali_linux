"""
nc -vv -l -p 8080  #Listen to the 8080 port locally
"""
import socket, os, time, threading, sys
from ipaddress import ip_address
from queue import Queue

decode_utf8 = lambda s: s.decode('utf-8')

send = lambda data: conn.send(data)
recv = lambda buffer: conn.recv(buffer)


def recv_all(buffer):
    while True:
        byte_data = b""
        while len(byte_data) < len(buffer):
            byte_part = recv(buffer)
            byte_data += byte_part

def create_socket(config_dict):
    try:
        config_dict['obj_socket'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        config_dict['obj_socket'].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error as e:
        print("Socket creation error: ", e)

def socket_bind(config_dict):
    obj_socket = config_dict['obj_socket']
    ip_address = config_dict['ip_address']
    int_port = config_dict['int_port']
    try:
        obj_socket.bind((ip_address, int_port))
        print("Listening on port: ", obj_socket.getsockname())
        obj_socket.listen()
        return True
    except socket.error as e:
        print("Socket binding error: ", e)
        return False


def socket_accept(config_dict):
    obj_socket = config_dict['obj_socket']
    arr_conn = config_dict['arr_conn']
    arr_address = config_dict['arr_address']
    int_buff = config_dict['int_buff']
    while True:
        try:
            print("accepting socket: ", obj_socket.getsockname())
            conn, address = obj_socket.accept()
            conn.setblocking(1)  # no timeout
            arr_conn.append(conn)
            client_info = decode_utf8(conn.recv(int_buff))
            arr_address.append(address)
            print("Connection established: ", address)
            return True
        except socket.error as e:
            print("Socket accepting error: ", e)
            return False


def work(config_dict):
    config_dict['arr_conn'] = []
    config_dict['arr_address'] = []
    while True:
        int_value = config_dict['queue'].get()
        if int_value == 1:
            create_socket(config_dict)
            socket_bind(config_dict)
            if not socket_accept(config_dict):
                return False
        elif int_value == 2:
            while True:
                time.sleep(0.2)
                if len(config_dict['arr_address']) > 0:
                    break
        config_dict['queue'].task_done()
        return True

def create_threads(obj_socket, ip_address, int_port, int_buff, queue, int_threads):
    for i in range(int_threads):
        obj_thread = threading.Thread(target=work, args=(obj_socket, ip_address, int_port, int_buff))
        obj_thread.daemon = True
        obj_thread.start()
    queue.join()

def create_jobs(queue, int_threads, array_jobs):
    for i in range(array_jobs):
        queue.put(int_threads)
    queue.join()

def list_connections(arr_connections, arr_address):
    if len(arr_connections) > 0:
        clients = ''
        for i, conn in arr_connections:
            clients += str(i) + 4*" " + str(arr_address[arr_address[i][0]] +"\n")
            print(clients)

def close(arr_conn, arr_address):
    if len(arr_address) == 0:
        return True
    for i, conn in enumerate(arr_conn):
        conn.send(b'exit')
        conn.close()
    return True

def main_menu(arr_conn, arr_address):
    while True:
        str_choice = input("\n >>>")
        if str_choice == "--l":
            # list connections
            list_connections(arr_conn, arr_address)
        elif str_choice == "--x":
            # close
            close(arr_conn, arr_address)
            break
        else:
            print("Invalid choice, ")
            print("\n " + "--help")
            print("\n " + "--l    (List all connections)")
            print("\n " + "--x    (Close all connections))")

def main():
    config_dict = {}
    config_dict['int_threads'] = 2
    config_dict['array_jobs'] = [1, 2]
    config_dict['queue'] = Queue()
    for i, job in enumerate(config_dict['array_jobs']):
        config_dict['queue'].put(job)

    config_dict['ip_address'] = '127.0.0.1'
    config_dict['int_port'] = 8080
    config_dict['int_buff'] = 1024

    config_dict['obj_socket'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if not work(config_dict):
        return 1

    create_threads(config_dict)

    create_jobs(config_dict)

if __name__ == "__main__":
    error_code = main()
    sys.exit(error_code)
