class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        dollars = float(input("How many dollars?: ")) * 1
        half_dollars = float(input("How many half dollars?: ")) * .5
        quarters = float(input("How many quarters?: ")) * .25
        nickels = float(input("How many pennies?: ")) * .05
        total = quarters + half_dollars + nickels + dollars
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"You gave me ${coins}, the cost was ${cost}, your change is ${change:.2f}")
            return True
        else:
            print(f"Sorry, that's not enough money")
            return False
