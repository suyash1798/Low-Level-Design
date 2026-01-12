export class Ticket{
    private id: string;
    private floorId: string;
    private spotId: string;

    constructor (id: string, floorId: string, spotId: string){
        this.id = id;
        this.floorId = floorId;
        this.spotId = spotId;
    }

    getFloorId(): string{
        return this.floorId;
    }

    getSpotId(): string{
        return this.spotId;
    }
}