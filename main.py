from cryptography.fernet import Fernet

#generating key
key = Fernet.generate_key()

#save the key to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("Secret key generated and saved to 'secret.key'")
