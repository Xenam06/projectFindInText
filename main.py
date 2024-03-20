import requests
from fuzzywuzzy import fuzz

def search(file_path, query):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()

    words = content.split()

    results = []

    for word in words:
        score = fuzz.token_set_ratio(query.lower(), word)
        if score >= 70:
            # эта строка кода преобразует каждое слово в строке так, чтобы оно начиналось с большой буквы, а за ним следовали все слова до следующего слова, начинающегося с большой буквы.
            results.append(word.capitalize() + ' ' + ' '.join(words[words.index(word) + 1: words.index(words[words.index(word) + 1]) if words.index(word) + 1 < len(words) else len(words)]))

    return results

print(search('mertvye-dushi.txt', input()))
