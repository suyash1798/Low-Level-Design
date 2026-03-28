class Message:
    msg: str
    id: int

    def __init__(self, id, msg):
        self.id = id
        self.msg = msg