#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if type(discount) is int and 0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Track each sale as one transaction while storing every item sold.
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity,
        })

    def apply_discount(self):
        if self.discount == 0 or self.total == 0:
            print("There is no discount to apply.")
            return

        self.total -= self.total * (self.discount / 100)
        self.total = round(self.total, 10)
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()
        self.total -= transaction["price"] * transaction["quantity"]
        self.total = round(self.total, 10)
        self._remove_transaction_items(
            transaction["item"],
            transaction["quantity"],
        )

    def _remove_transaction_items(self, item, quantity):
        # Remove the most recently added matching items for the voided sale.
        removed = 0
        for index in range(len(self.items) - 1, -1, -1):
            if self.items[index] == item:
                self.items.pop(index)
                removed += 1

                if removed == quantity:
                    break
