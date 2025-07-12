def count_total_words(text):
    word_count = len(text.split())

    return word_count


def character_count(text):
    characters = {}

    for character in text:
        if character.lower() not in characters:
            characters[character.lower()] = 1
        else:
            characters[character.lower()] += 1

    return characters


def sort_characters(character_dictionary):
    characters_list = []

    for character, count in character_dictionary.items():
        characters_list.append({"character": character, "num": count})

    characters_list.sort(reverse=True, key=lambda x: x["num"])

    return characters_list
