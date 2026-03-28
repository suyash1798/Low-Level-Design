from MessageQueue.MessageQueue import MessageQueue

mq = MessageQueue()
mq.addMessageToQueueByUser(1, 'Hello First Message')
mq.addMessageToQueueByUser(2, 'Hello First Message')
mq.addMessageToQueueByUser(3, 'Hello First Message')
mq.addMessageToQueueByUser(2, 'You Won')
mq.addMessageToQueueByUser(1, 'You lost')
mq.addMessageToQueueByUser(3, 'You lost')
mq.addMessageToQueueByUser(1, 'Finished')
mq.addMessageToQueueByUser(2, 'Finished')
mq.addMessageToQueueByUser(3, 'Finished')

import time

for message in mq.consumeMessageByUser(1, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(2, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(3, 1, 1):
    print(message.msg)

time.sleep(5)

for message in mq.consumeMessageByUser(1, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(2, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(3, 1, 1):
    print(message.msg)

time.sleep(5)

for message in mq.consumeMessageByUser(1, 2, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(2, 2, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(3, 1, 1):
    print(message.msg)

time.sleep(5)

for message in mq.consumeMessageByUser(1, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(2, 1, 1):
    print(message.msg)
for message in mq.consumeMessageByUser(3, 2, 1):
    print(message.msg)

