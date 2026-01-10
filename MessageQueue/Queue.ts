import { Consumer } from "./Consumer";
import { Message } from "./Message";
import { Producer } from "./Producer";

type topicType = string;

export class Queue{
    private readonly topics: Map<topicType, Message[]>;
    private readonly topicsOffSet: Map<topicType, number>;

    constructor(){
        this.topics = new Map<topicType, Message[]>();
        this.topicsOffSet = new Map<topicType, number>();
    }

    public produce(topic: topicType, message: Message): void{
        if(this.topics.has(topic) === false){
            this.topics.set(topic, []);
            this.topicsOffSet.set(topic, -1);
        }

        this.topics.get(topic)!.push(message);
    }

    public consume(topic: topicType): Message | null {
        if(this.topics.has(topic) === false) {
            return null;
        }

        let offset = this.topicsOffSet.get(topic)! + 1;
        let messages = this.topics.get(topic)!;

        if(messages.length > offset){
            this.topicsOffSet.set(topic, offset);

            return messages[offset];
        }

        return null;
    }
}



// Tests

const queue = new Queue();
const producer = new Producer(queue);
const consumer = new Consumer(queue);

setInterval(() => {
    producer.send('payment', 'payment of 1K done at ' + Date.now());
}, 2000);

setInterval(() => {
    producer.send('profile', 'profile of user updated at ' + Date.now());
}, 3000);

setInterval(() => {
    let message = consumer.poll('payment');

    if(message) console.log(message.getPayload());
}, 1000);

setInterval(() => {
    let message = consumer.poll('profile');

    if(message) console.log(message.getPayload());
}, 5000);
