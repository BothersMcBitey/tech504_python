import random

def get_yesno(question:str)->bool:
    while True:
        response = input(f"{question} (y/n)").lower()
        if response == "y" or "yes":
            return True
        elif response == "n" or "no":
            return False
        else:
            print("Invalid response. Try again.")

#===============================================================================
#  Learn if statement - Print movie rating meaning
#===============================================================================
def part_one():
    # possible film ratings are "universal", "pg", "12", "12a", "15", "18"
    film_rating = "12a"
    # use an if statement to check for "universal" rating
    if film_rating == "universal":
        print("all age groups can watch this film")
    # check if film rating is "pg"
    elif film_rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young "
              "children.")
    # check if film rating is "12" or "12a"
    elif film_rating in ["12", "12a"]:
        print("Films classified 12A and video works classified 12 contain material "
              "that is not generally suitable for children aged under 12. No one "
              "younger than 12 may see a 12A film in a cinema unless accompanied by "
              "an adult.")
    # check if film rating is "15"
    elif film_rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    # check if film rating is "18"
    elif film_rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    else:
        print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")

    # ==========================================================================
    #  Working with 'for loops'
    # ==========================================================================
    list_data = [1, 2, 3, 4, 5]
    embedded_lists = [[1, 2, 3], [4, 5, 6]]
    dict_data = {
        1: {"name": "Bronson", "money": "$0.05"},
        2: {"name": "Masha", "money": "$3.66"},
        3: {"name": "Roscoe", "money": "$1.14"}
    }
    for n in list_data: print(n*2)
    for data in embedded_lists:
        print(data)
        for datum in data:
            print(datum)
    for x in dict_data:
        print(x)
    for x in dict_data:
        print(dict_data[x])
    for x in dict_data:
        for y in dict_data[x]:
            print(dict_data[x][y])
    for x in dict_data:
        print(dict_data[x]["money"])
    for x in list_data:
        if x < 3: print('less than 3')
        if x == 3: print('I found three')
        if x > 3: print('greater than 3')

    # ==========================================================================
    #  Use 'while loops' with an int
    # ==========================================================================
    x = 0
    while x < 10:
        print(f"print x -> {x}")
        x += 1
    x = 0
    while x < 5:
        print(f"print x -> {x}")
        x += 1

    # ==========================================================================
    #  Use 'while loops' with an int
    # ==========================================================================
    user_prompt = True
    age = 0
    while user_prompt:
        age = input("What is your age? ")
        if age.isdigit() and int(age) < 118:
            user_prompt = False
        elif int(age) >= 118:
            print(f"{age} is too high. The oldest person is only 117 years old, "
                  f"so try again.")
        else:
            print(f"{age} is not a recognized format. Please enter your age in "
                  f"numeric digits")
    print(f"Your age is {age}")

# ==============================================================================
#  Practice control flow - Magic number guessing game
# ==============================================================================
def part_two():
    magic_number = random.randint(1, 100)
    max_guesses = 5
    guesses_left = max_guesses
    while guesses_left > 0:
        while True:
            guess = input("Guess the magic number (1-100): ")
            try:
                guess = int(guess)
                break
            except ValueError:
                print("Invalid number. Try again.")
        guesses_left -= 1
        if guess != magic_number and guesses_left > 0:
            direction = "low"
            if guess > magic_number: direction = "high"
            print(f"You guessed too {direction}. Try again.")
            print(f"You have {guesses_left} guesses left")
        elif guess != magic_number and guesses_left <= 0:
            print(f"Incorrect.\nYou are out of guesses. The magic number was "
                  f"{magic_number}.")
        elif guess == magic_number:
            print(f"Correct! You guessed the magic number was {magic_number} in "
                  f"{max_guesses-guesses_left} guesses.")

#===============================================================================
#  Practice control flow - Fizz Buzz
#===============================================================================
def part_three():
    def trigger_func(trigger_value, text):
        return lambda a: text if a % trigger_value == 0 else ''

    def get_number(request:str)->int:
        while True:
            answer = input(request)
            try:
                answer = int(answer)
                return answer
            except ValueError:
                print("Invalid number. Try again.")

    def get_trigger():
        word = input("What text do you want to replace the numbers with?\n")
        number = get_number(f"Which number should I {word} on?\n")
        return trigger_func(number, word)

    print("Welcome to FizzBuzz+.\nHere you can define as many substitutions as "
          "you want.")
    triggers = []
    make_more = True
    while make_more:
        print(f"Let's define trigger {len(triggers)+1}.")
        triggers.append(get_trigger())
        make_more = get_yesno(f"Trigger {len(triggers)} defined. Would you like"
                              f" to make another?")
    stop = get_number("Which number do I stop at?\n")
    for i in range(1,stop + 1):
        out = ''
        for t in triggers: out += t(i)
        if out != '':
            print(out)
        else:
            print(i)

#===============================================================================
#  Improve the movie rating meanings with user prompting
#===============================================================================
def part_four():
    # possible film ratings are "universal", "pg", "12", "12a", "15", "18"
    ratings = ["universal", "pg", "12", "12a", "15", "18"]
    def get_rating()->str:
        print("The possible film ratings are ", end='')
        for r in ratings: print(f" {r}.", end='')
        print()
        while True:
            rating = input("Enter an age rating:\n")
            if rating in ratings:
                return rating
            else:
                print("Invalid age rating. Try again.")

    keep_going = True
    while keep_going:
        film_rating = get_rating()
        if film_rating == "universal":
            print("all age groups can watch this film")
        elif film_rating == "pg":
            print("General viewing, but some scenes may be unsuitable for young "
                  "children.")
        elif film_rating in ["12", "12a"]:
            print("Films classified 12A and video works classified 12 contain material "
                  "that is not generally suitable for children aged under 12. No one "
                  "younger than 12 may see a 12A film in a cinema unless accompanied by "
                  "an adult.")
        elif film_rating == "15":
            print("No one younger than 15 may see a 15 film in a cinema.")
        elif film_rating == "18":
            print("No one younger than 18 may see an 18 film in a cinema.")
        else:
            print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
        keep_going = get_yesno("Would you like to check another movie rating?")

#part_one()
#part_two()
part_three()
#part_four()