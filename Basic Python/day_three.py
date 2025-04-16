#===============================================================================
#  Working with a list
#===============================================================================
def part_one():
    shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
    print(shopping_list)
    print(shopping_list[0])
    print(shopping_list[-2])
    shopping_list[1] = "rice"
    print(shopping_list[1])

    shopping_list.append("carrots")
    print(len(shopping_list))

    shopping_list.extend(["toffee", "coffee"])
    print(shopping_list)

    shopping_list.remove("bananas")
    print(shopping_list)

    shopping_list.pop()
    print(shopping_list)

    #===============================================================================
    #  Mix data
    #===============================================================================
    name = input("gimme yer name: ")
    age = int(input("gimme yer age: "))
    dob = input("gimme yer DoB: ")

    user_details_list = [name, age, dob]
    print(f"User name: {user_details_list[0]}, Age: {user_details_list[1]}, "
          f"Date of Birth: {dob}")
    print(f"Type of age in list is {type(user_details_list[1])}")

    height = float(input("gimme yer height (cm): "))
    user_details_list.append(height)
    print(user_details_list[3])

    #===============================================================================
    #  Test you can slice lists
    #===============================================================================
    mixture = [1, 2, 3,"one", "two", "three"]
    print(mixture)
    print(mixture[1:2])
    print([mixture[i] for i in range(len(mixture)) if i % 2 == 0])
    #or if you're being sensible
    print(mixture[::2])
    print(mixture[-1:-3:-1])

    #===============================================================================
    #  Learn tuples - finish the "Stranded on a Desert Island" game
    #===============================================================================
    # "Stranded on a Desert Island" game
    # Rationale: Practice tuples
    # Type of exercise: Finish the code
    print("You are stranded on a desert island. You can take only THREE items.")
    essential_item1 = input("What is an essential item you would take? ")
    essential_item2 = input("What is an essential item you would take? ")
    essential_item3 = input("What is an essential item you would take? ")
    # save the items as a tuple
    essentials_tuple = (essential_item1, essential_item2, essential_item3)
    # print the tuple
    print("Here are your items as a tuple:", essentials_tuple)
    print("")
    print("I lied. You can take one more item.")
    essential_item4 = input("What is one more essential item you would take? ")
    # try to add the 4th item to the tuple
    # if you can't add the 4th item, work out how to save the 4th item to the tuple
    essentials_tuple += (essential_item4,)
    print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)

    #===============================================================================
    #  Working with dictionaries
    #===============================================================================
    student_1 = {
        "name": "susan",
        "stream": "tech",
        "completed_lessons": 4,
        "completed_lesson_names": ["variables",
                                   "data_types",
                                   "set up"]
    }
    print(student_1)
    print(type(student_1))
    print(student_1["stream"])
    print(student_1["completed_lesson_names"])
    print(type(student_1["completed_lesson_names"]))
    print(student_1["completed_lesson_names"][0])
    student_1["completed_lessons"] = 3
    print(student_1)
    student_1["completed_lesson_names"].remove("data_types")
    print(student_1.keys())

#===============================================================================
#  Consolidation Task: Practice lists - Waiter Helper
#===============================================================================
# Outcome (By doing this you should): Practice using lists and dictionaries
# Script should act like a waiter at a restaurant taking orders
def part_two():
    starters = [
        {"name": "crackers", "price" : 1.50},
        {"name": "samosas", "price" : 4.90},
        {"name": "soup of the day", "price" : 5.0}
        ]
    mains = [
        {"name": "big ol\' roast", "price" : 15.10},
        {"name": "fish \'n\' chips", "price" : 7.85},
        {"name": "more soup", "price" : 4.50}
        ]
    desserts = [
        {"name": "affagato", "price" : 6.0},
        {"name": "ice cream", "price" : 3.5},
        {"name": "yet more soup", "price" : 20.90}
        ]
    menu = {
        "starter" : starters,
        "main" : mains,
        "dessert" : desserts
    }
    customer_order_list = []

    def is_on_menu(dish, course):
        for x in course:
            if dish.capitalize() == x["name"].capitalize():
                return True
        return False

    print("Hello there.")
    for course in menu:
        order_done = False
        while not order_done:
            print(f"Please choose a {course}:")
            for x in menu[course]:
                print("\t", x["name"].capitalize(), f"\t£{x["price"]:.2f}")
            selection = input("Enter choice: ").capitalize()
            while not is_on_menu(selection, menu[course]):
                selection = input("Invalid selection. Enter choice: ").capitalize()
            customer_order_list.extend(
                [i for i in menu[course] if i["name"].capitalize() == selection])

            response = ""
            response_valid = False
            while not response_valid:
                response = input(f"Would you like any more {course}s? (y/n)\n").lower()
                if response == "y":
                    response_valid = True
                if response == "n":
                    response_valid = True
                    order_done = True

    print("Your bill is:")
    total_cost = 0.0
    for dish in customer_order_list:
        print(f"\t{dish["name"].capitalize()}\t£{dish["price"]:.2f}")
        total_cost += dish["price"]
    print(f"\tTotal: £{total_cost:.2f}")

#===============================================================================
#  Consolidation Task: Practice dictionaries - Hero Story
#===============================================================================
def part_three ():
    story1 = {
        "start": "You are in a forest.",
        "middle": "You go North",
        "end": "Night has fallen. The vampires have won.",
        "character" : "You"
    }

    print(story1)
    print(type(story1))
    print(story1.keys())
    print(story1.values())
    #for x in story1.keys():
    #    print(story1[x])
    print()
    print(story1["start"])
    print(story1["middle"])
    print(story1["end"])
    print()
    print(f"The end I hope you enjoyed the story about {story1["character"]}!")

#===============================================================================
#  Task: Working with sets
#===============================================================================
def part_four():
    fruits = {"apple", "banana", "cherry"}
    print(fruits)
    fruits.add("orange")
    print(fruits)
    fruits.remove("banana")
    print(fruits)
    fruits.add("apple")
    print(fruits)

#===============================================================================
#  Task: Working with frozen sets
#===============================================================================
    frozen_set = frozenset({"hello","world"})
    normal_set = {"let\'s", "learn"}
    normal_set.add(frozen_set)
    print(normal_set)

#===============================================================================
# definitely NOT __main__
#===============================================================================
#part_one()
part_two()
#part_three()
#part_four()