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
    # ELSE IF STATEMENT GOES HERE
    print("Films classified 12A and video works classified 12 contain material "
          "that is not generally suitable for children aged under 12. No one "
          "younger than 12 may see a 12A film in a cinema unless accompanied by "
          "an adult.")
    # check if film rating is "15"
    # ELSE IF STATEMENT GOES HERE
    print("No one younger than 15 may see a 15 film in a cinema.")
    # check if film rating is "18"
    # ELSE IF STATEMENT GOES HERE
    print("No one younger than 18 may see an 18 film in a cinema.")
    # ELSE STATEMENT GOES HERE
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")