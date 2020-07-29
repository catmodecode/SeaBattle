import Point from "./Point";
import ShipType from "./ShipType";

export default class Ship {
  name: string;
  size: number;
  direction: boolean;
  position: Point;

  constructor(type: ShipType, direction = true) {
    this.name = type.name;
    this.size = type.size;
    this.direction = direction;
    this.position = new Point(0, 0);
  }
}
