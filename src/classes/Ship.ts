import playField from "@/constants/playField.json";
import Point from "./Point";
import ShipType from "./ShipType";

export default class Ship {
  type: string;
  size: number;
  direction: boolean;
  position: Point;
  static num = 0;

  constructor(type: ShipType, direction = true) {
    this.type = type.type;
    this.size = type.size;
    this.direction = direction;
    this.position = new Point(0, 0);
  }

  static fromShip(ship: Ship) {
    return new this(
      new ShipType({
        type: ship.type,
        name: ship.type,
        size: ship.size,
        count: 0,
      }),
      ship.direction
    );
  }

  isIntersect(ship: Ship) {
    const shipPoints = [
      new Point(ship.position.x - 1, ship.position.y - 1),
      new Point(
        ship.position.x + (ship.direction ? ship.size : 1),
        ship.position.y + (ship.direction ? 1 : ship.size)
      ),
    ];

    const selfPoints = [
      new Point(this.position.x, this.position.y),
      new Point(
        this.position.x + (this.direction ? this.size - 1 : 0),
        this.position.y + (this.direction ? 0 : this.size - 1)
      ),
    ];

    return (
      selfPoints.find((point) => {
        return (
          point.x >= shipPoints[0].x &&
          point.x <= shipPoints[1].x &&
          point.y >= shipPoints[0].y &&
          point.y <= shipPoints[1].y
        );
      }) !== undefined
    );
  }

  setPosition(pos: Point) {
    const xLength = playField.horizontalMarks.length;
    const yLength = playField.verticalMarks.length;
    const maxX = xLength - 1 - (this.direction ? this.size - 1 : 0);
    const maxY = yLength - 1 - (this.direction ? 0 : this.size - 1);
    if (pos.x >= 0 && pos.x <= maxX && pos.y >= 0 && pos.y <= maxY) {
      this.position = pos;
    }
  }
}
