if __name__ == '__main__':
    # print the first three words of a string that the user input
    fact = "Dr. Johnson probably needs a nap."
    output = ''

    for letter in fact:
        if letter != 'o':
            output += letter

    fact = output

    print(fact)


