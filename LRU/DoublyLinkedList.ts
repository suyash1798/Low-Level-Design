import { SingleNode } from "./Node";

export class DoublyLinkedList {
    head: SingleNode;
    tail: SingleNode;
    capacity: number;
    size: number;

    constructor(capacity: number) {
        this.head = new SingleNode('', 0); // Dummy head
        this.tail = new SingleNode('', 0); // Dummy tail
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.capacity = capacity;
        this.size = 0;
    }

    addToFront(node: SingleNode): void {
        node.prev = this.head;
        node.next = this.head.next;
        node.next!.prev = node;

        this.head.next = node;
        this.size++;

        if (this.size > this.capacity) {
            this.delete(this.tail.prev!);
        }
    }

    delete(node: SingleNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
        this.size--;
    }

    getNode(key: string): SingleNode | null {
        let node: SingleNode | null = this.head.next;

        while(node){
            if(node.key === key) return node;
            node = node.next;
        }

        return null;
    }

    getSize() {
        return this.size;
    }
}