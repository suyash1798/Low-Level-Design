import { Spot } from "./Spot";
import { VehicleType } from "./Vehicle";

export class Floor{
    private id: string;
    private spots: Spot[];

    constructor(id: string, spots: Spot[]){
        this.id = id;
        this.spots = spots;
    }

    getAvailableSpot(type: VehicleType): Spot | null{
        let availableSpot: Spot | null = null;

        for(let spot of this.spots){
            if(spot.getType() === type && spot.getIsOccupied() === false){
                availableSpot = spot;
                break;
            }
        }

        return availableSpot;
    }

    getId(): string{
        return this.id;
    }

    getSpots(): Spot[]{
        return this.spots;
    }
}