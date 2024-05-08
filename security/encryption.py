import bcrypt


class Encryption:
    @staticmethod
    def hash_password(password):
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password

    @staticmethod
    def check_password(password, hashed_password):
        # Check if the password matches the hashed password
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
