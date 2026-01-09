import { RateLimiterInterface } from "../RateLimiter";
import { TokenBucket } from "./TokenBucket";

export class TokenBucketRateLimiter implements RateLimiterInterface {
    private readonly buckets: Map<string, TokenBucket>;
    private maxToken: number;
    private refillRate: number;

    constructor(maxToken: number, refillRate: number) {
        this.buckets = new Map<string, TokenBucket>();
        this.maxToken = maxToken;
        this.refillRate = refillRate;
    }

    allow(key: string): boolean {
        if (this.buckets.has(key) === false) {
            this.buckets.set(key, new TokenBucket(this.refillRate, this.maxToken));
        }

        return this.buckets.get(key)!.consume();
    }
}