def shuff(word):
    if len(word) == 1:
        return [word]
    options = []
    for character_index in range(len(word)):
        possibilities = shuff(word[:character_index] + word[character_index + 1:])
        for w in range(len(possibilities)):
            options.append(word[character_index] + possibilities[w])

    return options

print(list(shuff("dog man person")))