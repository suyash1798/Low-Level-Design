export class SingleNode {
    key: string;
    value: number;
    prev: SingleNode | null;
    next: SingleNode | null;

    constructor(key: string, value: number) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}