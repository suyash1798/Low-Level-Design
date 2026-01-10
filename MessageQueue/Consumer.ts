import { Queue } from "./Queue";

export class Consumer{
    private queue: Queue;
    
    constructor(queue: Queue){
        this.queue = queue;
    }

    poll(topic: string){
        return this.queue.consume(topic);
    }
}