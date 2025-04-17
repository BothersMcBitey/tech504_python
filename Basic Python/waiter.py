starters = [{"name": "crackers", "price" : 1.50},
                {"name": "samosas", "price" : 4.90},
                {"name": "soup of the day", "price" : 5.0}]
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
			[i for i in menu[course] if i["name"].capitalize() == selection]
		)

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