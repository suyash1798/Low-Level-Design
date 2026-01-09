export class TokenBucket {
    private lastRefill: number;
    private refillRate: number;
    private maxToken: number;
    private tokens: number;

    constructor(refillRate: number, maxToken: number) {
        this.lastRefill = Date.now();
        this.refillRate = refillRate;
        this.maxToken = maxToken;
        this.tokens = maxToken;
    }

    consume(): boolean {
        this.refill();

        if (this.tokens < 1) return false;

        this.tokens--;

        return true;
    }

    private refill(): void {
        let time = Math.floor((Date.now() - this.lastRefill) / 1000);
        let addToken = time * this.refillRate;

        this.lastRefill += time * 1000;
        this.tokens = Math.min(this.maxToken, this.tokens + addToken);
    }
}