import bcrypt

class BcryptPassword():

    @staticmethod
    def encode_password(password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed

    @staticmethod
    def check_password(input_password, db_password):
        if bcrypt.hashpw(input_password.encode('utf-8'), db_password) == db_password:
            return True
        else:
            return False
