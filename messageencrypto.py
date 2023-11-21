import bcrypt

message = bytes(input("Enter Message to be encrypted\n"),'utf-8')

saltedVal = bcrypt.gensalt(rounds=16)
encrpyted_message = bcrypt.hashpw(password=message,salt=saltedVal)
print("\nEncrypted message is: ", encrpyted_message)
