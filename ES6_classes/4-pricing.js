import Currency from "./3-currency";

export default class Pricing {
    // constructor
    constructor(amount, currency) {
        if (typeof amount !== 'number' || amount < 0) {
            throw new Error('Amount must be a positive number');
        }
        if (!(currency instanceof Currency)) {
            throw new Error('Currency must be an instance of a class currency');
        }
        this._amount = amount;
        this._currency = currency;
    }

  // Getter/Setter for amount
  get amount() {
      return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount !== 'number' || newAmount < 0) {
        throw new Error('Amount must be a positive number');
    }
    this._amount = newAmount;
  }

  // Getter/Setter for currency
  get currency() {
    return this._currency
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
        throw new Error('Currency is not an instance of class currency');
    }
    this._currency = newCurrency;
  }

  // Display full price
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Static method converting price
  static convertPrice(amount, conversionRate) {
    return amount * conversionRaate;
  }
}
