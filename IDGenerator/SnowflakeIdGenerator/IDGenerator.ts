import { IDGenerator } from "../IDGenerator";

export class SnowFlakeIdGenerator implements IDGenerator {

    private static readonly EPOCH = 1700000000000n;

    private static readonly TIMESTAMP_BITS = 41n;
    private static readonly SERVER_ID_BITS = 10n;
    private static readonly SEQUENCE_BITS = 12n;

    private static readonly MAX_SEQUENCE = (1n << SnowFlakeIdGenerator.SEQUENCE_BITS) - 1n;

    private lastTimestamp = -1n;
    private sequence = 0n;

    constructor(private readonly serverId: bigint) {}

    public generateId(): bigint {
        let timestamp = BigInt(Date.now());

        if (timestamp < this.lastTimestamp) {
            throw new Error("Clock moved backwards");
        }

        if (timestamp === this.lastTimestamp) {
            this.sequence = (this.sequence + 1n) & SnowFlakeIdGenerator.MAX_SEQUENCE;

            if (this.sequence === 0n) {
                timestamp = this.waitNextMillis(timestamp);
            }
        } else {
            this.sequence = 0n;
        }

        this.lastTimestamp = timestamp;
        this.sequence += 1n;

        return (
            ((timestamp - SnowFlakeIdGenerator.EPOCH) << (SnowFlakeIdGenerator.SERVER_ID_BITS + SnowFlakeIdGenerator.SEQUENCE_BITS)) |
            (this.serverId << SnowFlakeIdGenerator.SEQUENCE_BITS) |
            this.sequence
        );
    }

    private waitNextMillis(ts: bigint): bigint {
        let now = BigInt(Date.now());
        while (now <= ts) {
            now = BigInt(Date.now());
        }
        return now;
    }
}
