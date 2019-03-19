def main():
    doc_js_favorite_birds = ["kingfisher", "peregrine", "common swift", "frogmouth"]
    your_favorite_birds = doc_js_favorite_birds

    print("Oh hey, I love starlings")
    your_favorite_birds.append("starlings")

    print("Doc J, do you like starlings")
    if "starlings" in doc_js_favorite_birds:
        print("Why yes I do! They are totally not nest-wrecking jerks and very much belong here.")
    else:
        print("Whoa, starlings? Gross!  They are fine where they came from, but they are meanies here in the US.")


main()
