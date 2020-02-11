# A user must guess my favorite movie animals

if __name__ == '__main__':
    my_favorite_animals = ["charlie", "jules", "tybalt", "tawny frogmouth", "octopodes", "rook"]

    guess = input("What is your guess?")

    if guess in my_favorite_animals:
        print("You got it, because you pretty and smart and not bad like wasps.")
    else:
        print("You must be a goose.")
