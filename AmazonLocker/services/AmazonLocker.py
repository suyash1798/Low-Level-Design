from datetime import datetime
from AmazonLocker.enums.PackageSizeEnum import PackageSizeEnum
from AmazonLocker.enums.SlotSizeEnum import SlotSizeEnum
from AmazonLocker.models.Package import Package
from AmazonLocker.models.Slot import Slot
from collections import defaultdict
from AmazonLocker.services.CodeGenerator import CodeGenerator


class AmazonLocker:
    availableSlot: dict[SlotSizeEnum, list[int]]
    slots: dict[int, Slot]
    slotToPackage: dict[int, int]
    packageToSlot: dict[int, int]
    slotToCode: dict[int, list[int, datetime]]

    ALLOWED_SIZES = {
        PackageSizeEnum.SMALL: [SlotSizeEnum.SMALL, SlotSizeEnum.MEDIUM, SlotSizeEnum.LARGE],
        PackageSizeEnum.MEDIUM: [SlotSizeEnum.MEDIUM, SlotSizeEnum.LARGE],
        PackageSizeEnum.LARGE: [SlotSizeEnum.LARGE],
    }

    def __init__(self, slots: list[Slot]):

        self.availableSlot = defaultdict(list)
        self.slots = {}
        self.slotToPackage = {}
        self.slotToCode = {}
        self.packageToSlot = {}
    
        for slot in slots:
            self.availableSlot[slot.size].append(slot.id)
            self.slots[slot.id] = slot


    def generateCode(self, packageId: int) -> int:
        code = CodeGenerator.generateCode(6)
        slotId = self.packageToSlot[packageId]

        self.slotToCode[slotId] = [code, datetime.now()]

        return code

    def deposit(self, package: Package):
        packageSize = package.size
        allowedSlotSizes = AmazonLocker.ALLOWED_SIZES[packageSize]

        slotId = -1

        for size in allowedSlotSizes:
            if len(self.availableSlot[size]) != 0:
                slotId = self.availableSlot[size].pop()
                break;

        if slotId == -1:
            raise Exception("No Slot Available")

        slot = self.slots[slotId]  
        slot.isAvailable = False

        self.slotToPackage[slot.id] = package.id
        self.packageToSlot[package.id] = slot.id
    
    def retrive(self, packageId: int, code: int) -> bool:
        
        slotId = self.packageToSlot[packageId]

        if slotId not in self.slotToCode:
            raise Exception("Generate code first")
        
        ocode, time = self.slotToCode[slotId]

        if (datetime.now() - time).total_seconds() > 120:
            raise Exception("Code Expired Generate New")
        
        if code != ocode:
            raise Exception("Wrong Code. Try Gain")
        
        slot = self.slots[slotId]

        slot.isAvailable = True

        self.availableSlot[slot.size].append(slot.id)

        del self.packageToSlot[packageId]
        del self.slotToPackage[slotId]
        del self.slotToCode[slotId]

        return True


                


