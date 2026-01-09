import { TokenBucketRateLimiter } from "./TokenBucket/TokenBucketRateLimiter";

export interface RateLimiterInterface{
    allow(key: string): boolean;
}

// Tests

const limiter = new TokenBucketRateLimiter(2, 0.1); // 2 tokens, 1 token / 10s

console.log(limiter.allow('user1')); // true (2 → 1)
console.log(limiter.allow('user1')); // true (1 → 0)
console.log(limiter.allow('user1')); // false (0 tokens)

setTimeout(() => {
    console.log(limiter.allow('user1')); // false (only 0.5 token)
}, 5000);

setTimeout(() => {
    console.log(limiter.allow('user1')); // true (1 token refilled)
}, 10000);