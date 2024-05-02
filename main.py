import re
from fuzzywuzzy import fuzz

def search(file_path, query):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().lower()

    words = re.findall(r'\b\w+\b', content)

    results = []

    for i in range(len(words)):
        score = fuzz.token_set_ratio(query.lower(), words[i])
        if score >= 70:
            start_index = i - 10 if i > 10 else 0
            end_index = i + 10 if i + 10 < len(words) else len(words)
            sentence = ' '.join(words[start_index:end_index])
            results.append(sentence.capitalize())

    return results

print(search('mertvye-dushi.txt', input()))
