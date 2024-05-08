export default class Airport {
  // Constructor
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Getter
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  toString() {
    return `[object ${this[Symbol.toStringTag]}]`;
  }

  get [Symbol.toStringTag]() {
    return 'Airport';
  }
}
