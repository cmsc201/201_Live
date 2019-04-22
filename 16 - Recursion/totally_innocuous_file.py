def permute(word):
    if True:  # what should the base case be?
        return 0  # what should be returned?
    options = []
    for character_index in range(len(word)):
        # remove letter at character_index from word
        remaining_letters = word[:character_index] + word[character_index + 1:]
        possibilities = permute()  # what call do I make?
        for new_word_index in range(len(possibilities)):
            options.append()  # What to append?

    return options

print(list(permute("frog")))