# read in a file, find each time it says dogs and replace it with cats, write out the file

if __name__ == '__main__':

    with open("dogfest.txt", "r") as dogfile:
        with open("catfest.txt", "w") as catfile:
            dog_text = dogfile.read().lower()
            cat_text = "cat".join(dog_text.split("dog"))
            catfile.write(cat_text)
