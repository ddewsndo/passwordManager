#git add .
#git commit -m "Your commit message here"
#git push


from cryptography.fernet import Fernet
import os 

print("Vault file path:", os.path.abspath("vault.txt"))


#load existing key or generate if it doesnt exist
keyFilePath = "secret.key"

if os.path.exists(keyFilePath):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
else:
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Secret key generated and saved to 'secret.key'")


fernet = Fernet(key)


#create vault.txt
#Save multiple passwords with usernames
with open("vault.txt","ab") as vault:
    while True:
        account = input("\nEnter your account name / email (enter quit to exit): ").strip()
        if account.lower() == "quit":
            break
        password = input(f"\nEnter password for {account}: ")
        encrypted = fernet.encrypt(password.encode())
        vault.write(f"{account}:{encrypted.decode()}\n".encode())
        print("Password encrypted and saved!")

#view and decrypt by account name
#key is already loaded previously
#read and decrypt
account2Find = input("Enter the account name to decrypt: ")

found = False

with open("vault.txt", "rb") as vault:
    for line in vault:
        line = line.decode().strip()
        if ":" in line:
            account, encryptedPassword = line.split(":", 1)
            if account.strip().lower() == account2Find.lower():
                decrypted = fernet.decrypt(encryptedPassword.encode()).decode()
                print(f"\nDecrypted password for '{account}': {decrypted}")
                found = True
                break
if not found:
    print("Account not found.")

                      