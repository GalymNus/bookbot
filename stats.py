def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def get_words_num(text):
    return text.split()


def count_unique_characters(text):
    result = {}
    for char in text:
        charLower = char.lower()
        if not charLower.isalpha():
            continue
        if result.get(charLower):
            result[charLower] += 1
        else:
            result[charLower] = 1
    return result


def sort_results(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
