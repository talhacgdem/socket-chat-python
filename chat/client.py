import socket
import threading

import rsa

public_key, private_key = rsa.newkeys(512)
# print(public_key)
# print(private_key)


def encrypt_text(plain_text):
    plain_text = plain_text.encode('utf8')
    encrypted_text = rsa.encrypt(plain_text, public_key)
    return encrypted_text


def decrypt_text(encrypted_text):
    decrypted_text = rsa.decrypt(encrypted_text, private_key)
    return decrypted_text.decode("utf-8")


# testing
# plain_text = "Hello this is an important message"
#
# encrypted_text = encrypt_text(plain_text)
# print("Encrypted text is = %s" % (encrypted_text))
#
# decrypted_text = decrypt_text(encrypted_text)
# print("Decrypted text is = %s" % (decrypted_text))


# Choosing Nickname
nickname = input("Choose your nickname: ")
key = "talhaaaa"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
