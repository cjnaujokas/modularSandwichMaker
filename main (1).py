### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        ## loops through passed ingredient list, and checks the machine resources to see if
        ## there is enough.
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = float(input("How many dollars?: "))
        half_dollars = float(input("How many half dollars?: ")) * .5
        quarters = float(input("How many quarters?: ")) * .25
        nickels = float(input("How many pennies?: ")) * .05
        total = quarters + half_dollars + nickels + dollars
        return total

    @staticmethod
    def transaction_result(coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"You gave me ${coins}, the cost was ${cost}, your change is ${change:.2f}")
            return True
        else:
            print(f"Sorry, that's not enough money")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

    def process_order(self, order):
        if sandwich_machine.check_resources(recipes[order]["ingredients"]):
            y = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(y, recipes[order]["cost"]):
                sandwich_machine.make_sandwich(recipes[order], recipes[order]["ingredients"])
                print(f"{order} sandwich is ready!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)
print("Welcome to the Sandwich Maker!")
running = True

## Print list of options
options = ["1: Small sandwich", "2: Medium sandwich", "3: Large sandwich", "4: Off","5: Report"]

## Gets and stores user input
while running:
    x = input(f"{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}\n{options[4]}\nChoose an option: ")

## Case where small is picked
    if x == "1":
        order = "small"
        sandwich_machine.process_order(order)
    elif x == "2":
        order = "medium"
        sandwich_machine.process_order(order)
    elif x == "3":
        order = "large"
        sandwich_machine.process_order(order)
    elif x == "4":
        print("Bye!")
        running = False
    elif x == "5":
        for item in sandwich_machine.machine_resources:
            print(f"{item}: {sandwich_machine.machine_resources[item]}")
    else:
        print("please pick a valid option")


"""
sandwich_machine = SandwichMachine(resources)
## checks case if there are enough ingredients
print(sandwich_machine.check_resources(recipes["small"]["ingredients"]))
## Checks case where there are NOT enough ingredients
print(sandwich_machine.check_resources({
            "bread": 28,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        }))
"""

## test for process_coins, should return correct added number of coins
"""
sandwich_machine = SandwichMachine(resources)
print(sandwich_machine.process_coins())
"""


## testing transaction result
"""
print(SandwichMachine.transaction_result(.45,.50))
print(SandwichMachine.transaction_result(.50,.20))
"""

# Testing for make_sandwich()
"""
sandwich_machine = SandwichMachine(resources)
for item in sandwich_machine.machine_resources:
    print(sandwich_machine.machine_resources[item])
sandwich_machine.make_sandwich("medium", recipes["medium"]["ingredients"])
for item in sandwich_machine.machine_resources:
    print(sandwich_machine.machine_resources[item])
"""