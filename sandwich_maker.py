
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

    def process_order(self, order, recipe, cashier):
        if self.check_resources(recipe[order]["ingredients"]):
            y = cashier.process_coins()
            if cashier.transaction_result(y, recipe[order]["cost"]):
                self.make_sandwich(recipe[order], recipe[order]["ingredients"])
                print(f"{order} sandwich is ready!")