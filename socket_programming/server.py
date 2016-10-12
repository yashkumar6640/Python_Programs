import socket;
import sys;

# Create Socket(Allows two computers to connect)
def socket_create():
    try:
        global host;
        global port;
        global s;
        host='';
        port=9989;
        s = socket.socket();
    except socket.error as msg:
        print("Socket creation error: " + str(msg));


# Bind socket to port and wait for connection from the client
def socket_bind():
    try:
        global host;
        global port;
        global s;
        print("Binding socket to port: " + str(port));
        s.bind((host, port));
        s.listen(5);
    except socket.error as msg:
        print("Socket Binding error: " + str(msg) + "\n" + "Retrying...");
        socket_bind();

# Establish a connection with client (socket must be listening for them)
def socket_accept():
    conn, address=s.accept();
    print("Connection has been established | " + " IP "+ address[0] + " | Port " + str(address[1]));
    send_commands(conn);
    conn.close();
# Send commands
def send_commands(conns):
    while True:
        cmd = input();
        if cmd == 'quit':
            conns.close();
            s.close();
            sys.exit();
        if len(str.encode(cmd)) > 0:
            conns.send(str.encode(cmd));
            client_response = str(conns.recv(1024), "utf-8");
            print(client_response, end="");

def main():
    socket_create();
    socket_bind();
    socket_accept();

main()