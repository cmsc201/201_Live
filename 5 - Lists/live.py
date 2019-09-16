
if __name__ == '__main__':
    # chameleon_color = "green"
    # tail_coil_factor = 0.2
    #
    # # if the chameleon is green and has a relaxed tail, print I'm chillin
    # if chameleon_color == "green" and tail_coil_factor < 0.4:
    #     print("I'm chillin")
    # # if the chameleon is any other color and has relaxed tail, print i'm pretty
    # elif chameleon_color != "green" and \
    #         tail_coil_factor < 0.4:
    #     print("I'm pretty!")
    # # in any other case, say I'm hiding
    # else:
    #     print("I'm hiding!")

    # A user must guess my favorite movie animals

    # create of list of my favorite movie animals
    # my_fave_movie_animals = ["elephant", "groot", "rocket racoon", "squirrels", "baloo"]
    # # ask the user to guess one
    # guess = input("Which movie animal?")
    # # tell them if they are correct
    # if guess in my_fave_movie_animals:
    #     print("you got it!")
    # else:
    #     print("Nope!  Rerun to try again!")

    # A user can remove an item from a list of grocery items

    # make a list of grocery items
    grocery_items = ["galangal", "chives", "turnips", "aubergine", "taro root", "chicken (not live)"]
    # show it to the user
    print(grocery_items)
    # ask the user for a grocery item
    item = input("What do you want to remove?")
    # remove the item if it's there, otherwise, tell them the item isn't on the list
    if item in grocery_items:
        grocery_items.remove(item)
        print("It's gone!  Here's the new list:", grocery_items)
    else:
        print("I don't have that on the list.")

    # A user inputs a series of numbers and then we print the list of numbers with their average


