import { DoublyLinkedList } from "./DoublyLinkedList";
import { SingleNode } from "./Node";

export class LRU {
    private list: DoublyLinkedList;

    constructor(size: number) {
        this.list = new DoublyLinkedList(size);
    }

    getValue(key: string): number | null {
        let node: SingleNode | null = this.list.getNode(key);

        if (node) {
            this.list.delete(node);
            this.list.addToFront(node);

            return node.value;
        }

        return null;
    }

    removeValue(key: string): boolean {
        let node: SingleNode | null = this.list.getNode(key);

        if (node) {
            this.list.delete(node);

            return true;
        }

        return false;
    }

    addValue(key: string, value: number){
        let node: SingleNode | null = this.list.getNode(key);

        if(node === null){
            node = new SingleNode(key, value);
        }else{
            node.value = value;
            this.list.delete(node);
        }

        this.list.addToFront(node);
    }
}


/// Tests

let lru = new LRU(5);

lru.addValue('user1', 123);
lru.addValue('user2', 345);
lru.addValue('user3', 567);
lru.addValue('user4', 789);
lru.addValue('user5', 123);
lru.addValue('user6', 345);

let value;

value = lru.getValue('user1');
console.log(value);

value = lru.getValue('user2');
console.log(value);

value = lru.getValue('user3');
console.log(value);

lru.addValue('user2', 456);
lru.addValue('user7', 666);

value = lru.getValue('user2');
console.log(value);

value = lru.getValue('user3');
console.log(value);

// user 4 not used or update, it should be removed till now
value = lru.getValue('user4');
console.log(value);