export class Message {
    private id: string;
    private payload: string;
    private timestamp: number;

    constructor(id: string, payload: string) {
        this.id = id;
        this.payload = payload;
        this.timestamp = Date.now();
    }

    getPayload(): string{
        return this.payload;
    }
}