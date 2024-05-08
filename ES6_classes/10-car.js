const cloneSymbol = Symbol('clone');

export default class Car {
    // constructor
    constructor (brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

  // Getter
  get brand() {
    return this._brand
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  [cloneSymbol]() {
    return new Car(this._brand, this._motor, this._color);
  }

  cloneCar() {
    return this[cloneSymbol]();
  }
}
