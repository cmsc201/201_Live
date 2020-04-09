if __name__ == '__main__':
    # Take two lists of values and make a dictionary that associates the keys in one list with the values of the other list
    cats = {"tuxboy": "Jules", "tabbybro": "Tybalt", "dog-shaped": "Charlie"}

    print(cats.get("Mr. Stiles"))
    for key in cats:
        print(key)
        print(cats[key])