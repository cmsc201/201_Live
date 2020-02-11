if __name__ == '__main__':
    chameleon_color = input("What color is our little friend?")
    tail_coiled_factor = float(
        input("On a scale from 0 to 1, how coiled is their tail?"))

    """
    How would I write code that prints "This lizard is chillin" if the color is "green" and the coiled factor is less than 0.4
Otherwise if the tail is still less than 0.4 but it's not green print "I'm feeling pretty"
In any other case, print "I'm hiding!"
"""

    if chameleon_color == "green" and tail_coiled_factor < 0.4:
        print("I'm hiding!")
    elif tail_coiled_factor < 0.4:
        print("Feeling fabulous!")
    else:
        print("I'm hiding")