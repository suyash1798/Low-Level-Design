import { SnowFlakeIdGenerator } from "./SnowflakeIdGenerator/IDGenerator";

export interface IDGenerator{
    generateId(): bigint;
}


// Tests

const generator: IDGenerator = new SnowFlakeIdGenerator(123456n);


setInterval(() => {
    let id = generator.generateId();

    console.log(id);
}, 1000);


setInterval(() => {
    let id = generator.generateId();

    console.log(id);
}, 1000);