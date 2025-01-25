def match_words(words):
    char = 0
    list = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            char += 1
            list.append(word)
    print("List of words with first and the last characters same\n", list)
    return char

add = match_words(["ahh","baa","moo","mom","dad"])
print("Number of words having first and lasr character same:", add)