
import rsa

public_key, private_key = rsa.newkeys(512)
print(public_key)
print(private_key)


def encrypt_text(plain_text):
    plain_text = plain_text.encode('utf8')
    encrypted_text = rsa.encrypt(plain_text, public_key)
    return encrypted_text


def decrypt_text(encrypted_text):
    decrypted_text = rsa.decrypt(encrypted_text, private_key)
    return decrypted_text.decode("utf-8")


# testing
plain_text = "Hello this is an important message"

encrypted_text = encrypt_text(plain_text)
print("Encrypted text is = %s" % (encrypted_text))

decrypted_text = decrypt_text(encrypted_text)
print("Decrypted text is = %s" % (decrypted_text))