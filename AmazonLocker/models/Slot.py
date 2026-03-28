from AmazonLocker.enums import SlotSizeEnum


class Slot:
    id: int
    size: SlotSizeEnum
    isAvailable: bool

    def __init__(self, id: int, size: SlotSizeEnum):
        self.id = id
        self.size = size