from AmazonLocker.enums.PackageSizeEnum import PackageSizeEnum


class Package:
    id: int
    size: PackageSizeEnum

    def __init__(self, id: int, size: PackageSizeEnum):
        self.id = id
        self.size = size