export default class ShipType {
  type: string;
  name: string;
  size: number;
  count: number;

  constructor({
    type,
    name,
    size,
    count,
  }: {
    type: string;
    name: string;
    size: number;
    count: number;
  }) {
    this.type = type;
    this.name = name;
    this.size = size;
    this.count = count;
  }
}
