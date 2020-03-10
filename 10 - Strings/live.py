if __name__ == '__main__':
    # print the first three words of a string that the user input
    # like_gouramis = input("Do you like gouramis? ")
    # if like_gouramis.lower() == "yes":
    #     print("I'm glad we agree".upper())

    statement = """
    I love dogs.  They are the best.  I think dogs could be my fave.
    """
    # Using only join and split, replace every instance of dog with cat
    print("cat".join(statement.split("dog")))

    # Ask the user for a statement.  Then print the first three words of the statment.  Tell them they are bad if they didn't say 3 words.
    statement = input("say something")
    words = statement.split()
    if len(words) < 3:
        print("Tell me more!")
    else:
        print(" ".join(words[0:3]))
