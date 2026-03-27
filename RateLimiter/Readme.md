Requiremnts

1. API able to consume a token if available
2. System should refill bucket as per the fill rate 10/min
3. Refill should be capped to 5 tokets
4. System should support multiple user buckets
5. All operations should be in O(1)


Entities

1. Rate Limiter
    - userToBucket (user, bucket)
    - refill()
    - consume()
    - addUserBucket(userId, bucket)
    - getTokensCount()
2. Bucket
    - tokens
    - max
    - rate
    - lastRefill
    - addTokens()
    - popToken()


Flow

1. addUserBucket
    - check if user already exists If no
    - Create new bucket with max & initial (rate)
    - add it to map

2. consume
    - call refill first
    - check if tokens available
    - decrement token
    - return true

3. Refill
    - Check time passed since last refill
    - calculate token to be granted as per bucket rate
    - add calculated tokens


