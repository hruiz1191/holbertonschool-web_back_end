import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency instance');
    }

    this._amount = amount;
    this._currency = currency;
  }

  // Getter y setter para amount
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }

  // Getter y setter para currency
  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError('Currency must be a Currency instance');
    }
    this._currency = newCurrency;
  }

  // Método de instancia
  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  // Método estático
  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Both arguments must be numbers');
    }
    return amount * conversionRate;
  }
}
