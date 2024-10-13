
def single_root_words(root_word, *other_words):
    same_wods = []
    root_word_lower = str(root_word).lower()
    for word in other_words:
        word_lower = str(word).lower()
        if (root_word_lower in word_lower) or (word_lower in root_word_lower):
            same_wods.append(word)

    return same_wods


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
