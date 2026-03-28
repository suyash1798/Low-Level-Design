Requirements

1. Able to deposit a package
2. Able to Retrive a package
3. Generate a unique code for retrival (TTL 2 mins)
4. Once code entered package will be marked as delivered
5. After delivery, locker must be available for new deposit
6. Should support different size slot for different size package


Entities

1. AmazonLocker
    - availableSlots
    - slotToPackage
    - packageToSlot
    - slotToCode (slotId, [code, time])
    - generateCode(packageId)
    - deposit(packageId) -> slotId
    - retrieve(slot, code) -> packageId

2. Slot
    - id
    - isAvailable
    - size

3. Package
    - id
    - size

4. SlotSizeEnum
    - Small
    - Medium
    - Large

5. PackageSizeEnum
    - small
    - medium
    - large

6. SlotSizeAvailableForPackage
    - small = [small, medium, large]
    - medium = [medium, large]
    - large = [large ]


FLow

1. Deposit
    - A deposit request with package
    - Check for slot size available for package size
    - Remove slot from available slot and mark it as isAvailable = false
    - add entry into slotToPackage

2. Generate Code
    - Check if package is in any slot packageToSlot
    - genrate a 4 digit random code and add it to slotToCode

3. Retrive
    - Check entered code if its older than 2 mins reject request
    - If not, then remove package from slotToPackage, packageToSlot
    - Also, remove slotToCode and add slot back to available slots and mark isAvailable = true
