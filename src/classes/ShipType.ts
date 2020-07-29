export default class ShipType {
  name: string;
  size: number;
  count: number;

  constructor(name, size, count) {
    this.name = name;
    this.size = size;
    this.count = count;
  }
}
