def permute(word):
    if len(word) == 1:  # what should the base case be?
        return [word] # what should be returned?
    options = []
    for character_index in range(len(word)):
        # remove letter at character_index from word
        remaining_letters = word[:character_index] + word[character_index + 1:]
        possibilities = permute(remaining_letters)  # what call do I make?
        for possibility in possibilities:
            options.append(word[character_index] + possibility)  # What to append?

    return options

print(list(permute("frogs!!!?@")))
