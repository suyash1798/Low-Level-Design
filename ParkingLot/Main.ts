import { Floor } from "./Floor";
import { ParkingLot } from "./ParkingLot";
import { Spot } from "./Spot";
import { Vehicle, VehicleType } from "./Vehicle";

const floors = new Array(3).fill(0).map(() => 
    new Floor(crypto.randomUUID(), 
    [...new Array(2).fill(1).map(() => new Spot(crypto.randomUUID(), VehicleType.BIKE)),
        ...new Array(2).fill(1).map(() => new Spot(crypto.randomUUID(), VehicleType.CAR))
    ]
));

const parkingLot = new ParkingLot(floors);
const vehicle1 = new Vehicle(crypto.randomUUID(), VehicleType.CAR);
const vehicle2 = new Vehicle(crypto.randomUUID(), VehicleType.BIKE);
const vehicle3 = new Vehicle(crypto.randomUUID(), VehicleType.CAR);
const vehicle4 = new Vehicle(crypto.randomUUID(), VehicleType.CAR);
const vehicle5 = new Vehicle(crypto.randomUUID(), VehicleType.BIKE);
const vehicle6 = new Vehicle(crypto.randomUUID(), VehicleType.CAR);


const t1 = parkingLot.park(vehicle1);
const t2 = parkingLot.park(vehicle2);
const t3 = parkingLot.park(vehicle3);
const t4 = parkingLot.park(vehicle4);
const t5 = parkingLot.park(vehicle5);
const t6 = parkingLot.park(vehicle6);


console.log(t1);
console.log(t2);
console.log(t3);
console.log(t4);
console.log(t5);
console.log(t6);

const unp1 = parkingLot.unpark(t1);
console.log(unp1);

const unp2 = parkingLot.unpark(t2);
console.log(unp2);

const unp3 = parkingLot.unpark(t3);
console.log(unp3);

const unp4 = parkingLot.unpark(t4);
console.log(unp4);

const unp5 = parkingLot.unpark(t5);
console.log(unp5);

const unp6 = parkingLot.unpark(t6);
console.log(unp6);




