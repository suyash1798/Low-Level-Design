import { Vehicle, VehicleType } from "./Vehicle";

export class Spot{
    private id: string;
    private type: VehicleType;
    private isOccupied: boolean;
    private vehicle: Vehicle | null;

    constructor(id: string, type: VehicleType){
        this.id = id;
        this.type = type;
        this.isOccupied = false;
        this.vehicle = null;
    }

    public park(vehicle: Vehicle): boolean{
        if(this.isOccupied === true){
            throw new Error('Spot already occupied');
        }
        if(this.type !== vehicle.getVehicleType()){
            throw new Error("Spot doesn't match vehicle type");
        }
        this.vehicle = vehicle;
        this.isOccupied = true;

        return true;
    }

    public unpark(): boolean {
        if(this.isOccupied === false){
            throw new Error('Spot is empty');
        }
        this.vehicle = null;
        this.isOccupied = false;

        return true;
    }

    public getType(): VehicleType{
        return this.type;
    }

    public getIsOccupied(): boolean{
        return this.isOccupied;
    }

    public getId(): string{
        return this.id;
    }
}