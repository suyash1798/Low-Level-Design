from MessageQueue.Message import Message

class Queue:
    queue: list[Message]
    lastMessageId: int

    def __init__(self):
        self.queue = []
        self.lastMessageId = -1

    def addMessage(self, message):
        lastMessageId = self.lastMessageId

        message = Message(lastMessageId+1, message)

        self.lastMessageId = lastMessageId+1

        self.queue.append(message)
    
    def consumeMessage(self, afterMessageIndex: int, limit) -> list[list[Message], int]:
        count = 0
        messages = []
        index = afterMessageIndex + 1

        while(count < limit and len(self.queue) > index):
            message = self.queue[index]

            messages.append(message)
            count += 1
            
            index += 1
        
        return [messages, index-1]
    
    def clearAll(self):
        self.queue = []
        self.lastMessageId = -1