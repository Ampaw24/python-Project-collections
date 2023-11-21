import bcrypt

password = b"password123"
salt = bcrypt.gensalt(rounds=15)
hashed_password = bcrypt.hashpw(password, salt)
print(hashed_password)