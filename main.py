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
    ## Used to keep program running until it's told to shut off
    running = True
    ## Options to choose from
    options = ["1: Small sandwich", "2: Medium sandwich", "3: Large sandwich", "4: Off", "5: Report"]
    ## Switch to control what the user wants to do.
    while running:
        ## Prints the options, and places user input as x
        x = input(f"{options[0]}\n{options[1]}\n{options[2]}\n{options[3]}\n{options[4]}\nChoose an option: ")
        # User chooses small sandwich
        if x == "1":
            order = "small"
            ## sandwich maker object is passed its cashier and recipe data, and what sandwich to make
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "2":
            order = "medium"
            ## sandwich maker object is passed its cashier and recipe data, and what sandwich to make
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "3":
            order = "large"
            ## sandwich maker object is passed its cashier and recipe data, and what sandwich to make
            sandwich_maker.process_order(order, recipes, cashier)
        elif x == "4":
            print("Bye!")
            ## Sends signal to stop the while loop and end the program
            running = False
        elif x == "5":
            ## lists off the resources left
            for item in sandwich_maker.machine_resources:
                print(f"{item}: {sandwich_maker.machine_resources[item]}")
        else:
            print("please pick a valid option")



if __name__=="__main__":
    main()
