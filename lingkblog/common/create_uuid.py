import uuid

class CreateUUID():

    @staticmethod
    def get_uuid():
        return "".join(str(uuid.uuid1()).split("-")).upper()