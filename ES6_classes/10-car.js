export default class Car {
    // constructor
    constructor (brand, motor, color) {
        this._brand = brand;
        this._motor = brand;
        this._color = color;
    }

  // Getter
  get brand() {
    return this._brand
  }
}