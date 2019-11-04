if __name__ == '__main__':
# read in a file, find each time it says dogs and replace it with cats, write out the file
    with open("dogfest.txt", "r") as dog_file:
        with open("catfest.txt", "w") as cat_file:
            # read dog file
            dog_text = dog_file.read()
            # replace dogs with cats WITH OUT USING .replace()
            # (maybe I'll use join and split)
            cat_string = "cat".join(dog_text.lower().split("dog"))
            # write the result to cat_file
            cat_file.write(cat_string)
