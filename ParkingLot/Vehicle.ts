export enum VehicleType{
    CAR = 'CAR',
    BIKE = 'BIKE'
}

export class Vehicle{
    private id: string;
    private type: VehicleType;

    constructor(id: string, type: VehicleType){
        this.id = id;
        this.type = type;
    }

    public getVehicleType(): VehicleType{
        return this.type;
    }
}