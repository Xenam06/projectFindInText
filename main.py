import re
from Levenstein import distance

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def find_sentences_with_query(text, query):
    sentences = re.split('[.!?]', text)
    matching_sentences = []
    for sentence in sentences:
        if query in sentence:
            matching_sentences.append(sentence.strip())
    return matching_sentences

def find_sentences_with_typo(text, word, max_typos=2):
    sentences = re.split('[.!?]', text)
    matching_sentences = []
    for sentence in sentences:
        words = sentence.split()
        for w in words:
            if distance(w, word) <= max_typos:
                matching_sentences.append(sentence.strip())
                break
    return matching_sentences

def find_sentences_with_multiple_words(text, words, max_typos=2):
    sentences = re.split('[.!?]', text)
    matching_sentences = []
    for sentence in sentences:
        words_in_sentence = sentence.split()
        matching_words = 0
        for word in words:
            for w in words_in_sentence:
                if distance(w, word) <= max_typos:
                    matching_words += 1
                    break
        if matching_words == len(words):
            matching_sentences.append(sentence.strip())
    return matching_sentences

def main():
    file_path = input("Enter the path to the text file: ")
    query = input("Enter the query: ")

    text = load_text(file_path)

    if " " in query:
        words = query.split()
        if len(words) == 2:
            sentences = find_sentences_with_multiple_words(text, words, max_typos=2)
        elif len(words) == 3:
            sentences = find_sentences_with_multiple_words(text, words, max_typos=1)
    else:
        sentences = find_sentences_with_query(text, query)
        if not sentences:
            sentences = find_sentences_with_typo(text, query, max_typos=2)

    print("\nMatching sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f" Sentence {i}: {sentence}")

if __name__ == "__main__":
    main()
