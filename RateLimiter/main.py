from datetime import datetime
import time

class Bucket:
    tokens: int
    lastReill: datetime
    maxTokens: int
    rate: int # per minute

    def __init__(self, rate: int, maxTokens: int):
        self.tokens = min(rate, maxTokens)
        self.maxTokens = maxTokens
        self.lastReill = datetime.now()
        self.rate = rate
    
    def addTokens(self, tokens: int):
        self.tokens = min(self.tokens + tokens, self.maxTokens)
        self.lastReill = datetime.now()

    def popToken(self):
        if self.tokens == 0:
            return False
        
        self.tokens -= 1

        return True

class RateLimiter:
    userToBucket: dict[int, Bucket]


    def __init__(self):
        self.userToBucket = {}
    
    def addUserBucket(self, userId: int, rate: int, maxTokens: int) -> bool:
        if userId in self.userToBucket:
            return False

        bucket = Bucket(rate, maxTokens)
        self.userToBucket[userId] = bucket

        return True
    
    def consume(self, userId) -> bool:
        if userId not in self.userToBucket:
            return False

        self.refill(userId)

        bucket = self.userToBucket[userId]

        return bucket.popToken()
    
    def refill(self, userId):
        if userId not in self.userToBucket:
            return

        bucket = self.userToBucket[userId]
        timepassed = (datetime.now() - bucket.lastReill).total_seconds() / 60

        tokens = int(bucket.rate * timepassed)

        bucket.addTokens(tokens)


rl = RateLimiter()

rl.addUserBucket(1, 10, 15)
rl.addUserBucket(2, 10, 15)

for i in range(10):
    print('Allow User 1') if rl.consume(1) == True else print('Not Allowed User 1')
    print('Allow User 2') if rl.consume(2) == True else print('Not Allowed User 2')

time.sleep(15)

for i in range(10):
    print('Allow User 1') if rl.consume(1) == True else print('Not Allowed User 1')
    print('Allow User 2') if rl.consume(2) == True else print('Not Allowed User 2')

