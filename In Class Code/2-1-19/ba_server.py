
from socket import socket
from bank_account import BankAccount

PORT = 12345

# get a socket object
listener = socket()
# we are server, we request to use a particular port
listener.bind(('', PORT))

# we listen
listener.listen(0)

while True:
        # The following function call waits until there is a connection
        # When a connection is made, this function returns with information
        # about the connection
        (conn, address) = listener.accept()
        # conn is a socket that we will use to communicate with the client

        data_bytes = b""

        receivedB = conn.recv(2048)

        while len(receivedB) > 0:
            data_bytes += receivedB
            receivedB = conn.recv(2048)

        data_string = data_bytes.decode('UTF-8')
        print("data_string", data_string)

        if len(data_string) == 0:
                reply = 'Error: empty command'
        else:
                cmd = data_string[0]        #first character
                parameter = data_string[1:] #therest
        
                if cmd == 'z':
                    bank_account = BankAccount()
                    reply = 'OK reset'
                elif cmd == 'w':
                    try:
                        amount = float(parameter)
                        bank_account.withdraw(amount)
                        reply = "OK withdrawl made"
                    except ValueError as ve:
                        reply = 'Error: ' + str(ve)

                elif cmd == 'd':
                    try:
                        amount = float(parameter)
                        bank_account.deposit(amount)
                        reply = "OK deposit made"
                    except ValueError as ve:
                        reply = 'Error: ' + str(ve)

                elif cmd == 'b':
                    bal = bank_account.get_balance()
                    reply = 'OK{:.2}'.format(bal)
                else:
                    reply = 'Error: invalid command code'

        conn.sendall(reply.encode('UTF-8'))
        conn.shutdown(1)

        conn.shutdown(0)
        conn.close()

        
listener.close()
