import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker = SandwichMaker(resources)
cashier = Cashier()




def main():
    print("Welcome to the Sandwich Maker!")
    running = True
    options = ["1: Small sandwich", "2: Medium sandwich", "3: Large sandwich", "4: Off", "5: Report"]
    while running:
        x = input(f"{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}\n{options[4]}\nChoose an option: ")

        if x == "1":
            order = "small"
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "2":
            order = "medium"
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "3":
            order = "large"
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "4":
            print("Bye!")
            running = False
        elif x == "5":
            for item in sandwich_maker.machine_resources:
                print(f"{item}: {sandwich_maker.machine_resources[item]}")
        else:
            print("please pick a valid option")



if __name__=="__main__":
    main()
