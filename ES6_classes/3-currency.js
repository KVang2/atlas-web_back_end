class Currency {
    constructor(code, name) {
      this._code = typeof code === 'string' ? code : '';
      this._name = typeof name === 'string' ? name : '';
}

// Getter and setter for code
get code() {
    return this._code;
}
set code(newCode) {
    if (typeof newCode === 'string') {
        this._code = newCode;
    }
}

// Getter and setter for name
get name() {
  return this._name;
}
set name(newName) {
  if (typeof newName === 'string') {
      this._name = newName;
  }
}

displayFullCurrency() {
    return`${this._name} (${this._code})`;
  }
}