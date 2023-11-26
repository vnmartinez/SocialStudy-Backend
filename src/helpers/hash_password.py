import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf8'), salt)
    return hashed

def check_password(password :str, hashed):
    return bcrypt.checkpw(password, hashed)