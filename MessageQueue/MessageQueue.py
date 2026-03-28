from MessageQueue.Message import Message
from MessageQueue.Queue import Queue 

class MessageQueue:
    userToQueueMap: dict[int, Queue]
    consumerToUserQueueIndexMap: dict[str, int]

    def __init__(self):
        self.userToQueueMap = {}
        self.consumerToQueueIndexMap = {}
    
    def addMessageToQueueByUser(self, userId: int, message: str):
        if userId not in self.userToQueueMap:
            self.userToQueueMap[userId] = Queue()
        
        self.userToQueueMap[userId].addMessage(message)
    
    def consumeMessageByUser(self, userId: int, consumerId: int, limit: int) -> list[Message]:
        if userId not in self.userToQueueMap:
            return []
        
        consumerKey = str(consumerId) + '-' + str(userId)

        if consumerKey not in self.consumerToQueueIndexMap:
            self.consumerToQueueIndexMap[consumerKey] = -1
        
        messages, lastIndex = self.userToQueueMap[userId].consumeMessage(self.consumerToQueueIndexMap[consumerKey], limit)
        self.consumerToQueueIndexMap[consumerKey] = lastIndex

        return messages