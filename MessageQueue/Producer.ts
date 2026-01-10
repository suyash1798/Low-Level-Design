import { Message } from "./Message";
import { Queue } from "./Queue";

export class Producer {
    private readonly queue: Queue;

    constructor(queue: Queue) {
        this.queue = queue;
    }

    send(topic: string, payload: string) {
        let message = new Message(crypto.randomUUID(), payload);

        this.queue.produce(topic, message);
    }
}