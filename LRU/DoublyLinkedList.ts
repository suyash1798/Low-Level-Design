import { SingleNode } from "./Node";

export class DoublyLinkedList {
    head: SingleNode;
    tail: SingleNode;
    size: number;

    constructor() {
        this.head = new SingleNode('', 0); // Dummy head
        this.tail = new SingleNode('', 0); // Dummy tail
        this.head.next = this.tail;
        this.tail.prev = this.head;
        this.size = 0;
    }

    addToFront(node: SingleNode): void {
        node.prev = this.head;
        node.next = this.head.next;
        node.next!.prev = node;

        this.head.next = node;
        this.size++;
    }

    delete(node: SingleNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
        this.size--;
    }

    deleteFromLast(): string | null {
        if(this.size === 0) return null;

        let deleteNode = this.tail.prev!;
        this.delete(deleteNode);

        return deleteNode.key;
    }

    getSize() {
        return this.size;
    }
}