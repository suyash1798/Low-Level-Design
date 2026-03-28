from AmazonLocker.enums.PackageSizeEnum import PackageSizeEnum
from AmazonLocker.enums.SlotSizeEnum import SlotSizeEnum
from AmazonLocker.models.Package import Package
from AmazonLocker.models.Slot import Slot
from AmazonLocker.services.AmazonLocker import AmazonLocker

slots = []

for i in range(10):
    slot = Slot(len(slots)+1, SlotSizeEnum.SMALL)
    slots.append(slot)

    slot = Slot(len(slots)+1, SlotSizeEnum.MEDIUM)
    slots.append(slot)

    slot = Slot(len(slots)+1, SlotSizeEnum.LARGE)
    slots.append(slot)

packages = []

for i in range(2):
    package = Package(len(packages)+1, PackageSizeEnum.SMALL)
    packages.append(package)

    package = Package(len(packages)+1, PackageSizeEnum.MEDIUM)
    packages.append(package)

    package = Package(len(packages)+1, PackageSizeEnum.LARGE)
    packages.append(package)

al = AmazonLocker(slots)

for package in packages:
    al.deposit(package)

package = Package(len(packages)+1, PackageSizeEnum.LARGE)
packages.append(package)

for package in packages:
    code = al.generateCode(package.id)
    print('Code for package id ' + str(package.id) + ' ' + str(code))

    al.retrive(package.id, code)