import { Floor } from "./Floor";
import { Ticket } from "./Ticket";
import { Vehicle } from "./Vehicle";

export class ParkingLot{
    private floors: Floor[];

    constructor(floors: Floor[]){
        this.floors = floors;
    }

    public park(vehicle: Vehicle): Ticket {
        let availableSpot = null;
        let floorId = null;

        for(let floor of this.floors){
            availableSpot = floor.getAvailableSpot(vehicle.getVehicleType());
            floorId = floor.getId();
            if(availableSpot) break;
        }

        if(availableSpot === null){
            throw new Error('No spot available');
        }

        availableSpot.park(vehicle);

        let ticket = new Ticket(crypto.randomUUID(), floorId!, availableSpot.getId());

        return ticket;
    }

    public unpark(ticket: Ticket): boolean {
        let floor = null;

        for(let flr of this.floors){
            if(ticket.getFloorId() === flr.getId()){
                floor = flr;
                break;
            }
        }

        if(floor === null){
            throw new Error('Floor not exists');
        }

        let spot = null;

        for(let spt of floor.getSpots()){
            if(spt.getId() === ticket.getSpotId()){
                spot = spt;
                break;
            }
        }

        if(spot === null){
            throw new Error('Spot not exists');
        }

        return spot.unpark();
    }
}