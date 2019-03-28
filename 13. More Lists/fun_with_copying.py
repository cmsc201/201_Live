def add_bird(bird_list, bird):
    bird_list.append(bird)


def main():
    doc_js_favorite_birds = ["kingfisher", "peregrine", "common swift", "frogmouth"]
    your_favorite_birds = []

    # deep list copy
    index = 0
    while index < len(doc_js_favorite_birds):
        your_favorite_birds.append(doc_js_favorite_birds[index])
        index += 1

    print("Oh hey, I love starlings.")
    add_bird(your_favorite_birds, "ducks")
    your_favorite_birds.append("starlings")

    print("Doc J, do you like starlings")
    if "starlings" in doc_js_favorite_birds:
        print("Why yes I do! They are totally not nest-wrecking jerks and very much belong here.")
    else:
        print("Whoa, starlings? Gross!  They are fine where they came from, but they are meanies here in the US.")

    print(your_favorite_birds)

main()
