import re

num_sentences = int(input("Enter the number of sentences: "))

sentences = []
for i in range(num_sentences):
    sentences.append(input(f"Enter sentence {i + 1}: "))

words_in_sentences = [
    [word.strip() for word in re.split(r'[,\.\?!: ]+', sentence.lower()) if word]
    for sentence in sentences
]

num_words = int(input("Enter the number of words to search for: "))

words_to_search = []
for i in range(num_words):
    word = input(f"Enter word {i + 1}: ").lower().strip()
    words_to_search.append(word)

output = {word: [0] * num_sentences for word in words_to_search}

for i, words in enumerate(words_in_sentences):
    for word in words:
        if word in output:
            output[word][i] += 1

sorted_output = {}
for word, occurrences in output.items():
    sentence_indices = [i for i in range(len(occurrences)) if occurrences[i] > 0]
    sentence_indices.sort(key=lambda i: (-occurrences[i], i))
    sorted_output[word] = sentence_indices

for word, indices in sorted_output.items():
    print(f"{word}: {indices}")
