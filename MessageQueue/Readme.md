Requirements

1. Able to add messages
2. Consume Messages
3. Ordering shoud be maintained
4. Clear messages
5. Limit message consumed in a single call
6. Clear space once message consumed
7. Should be in avg O(1)
8. Message should not be repeated


Entities

1. MessageQueue
    - userToQueueMap
    - addMessage(message)
    - addMessageByUser(userId, message)
    - consumeMessageByUser(userId, limit, lastMessageId)
    - clearAllMessageByUser(userId)

2. Queue
    - list
    - addMessage(message)
    - consumeMessage(afterMessageId, limit)
    - clearAll()


Flow

1. Add Message
    - Id will be assigned to new message based on last message
    - message will be pushed into queue

2. Consume Message
    - Check for index with message Id greater than lastMessageId
    - return all message with a limit passed