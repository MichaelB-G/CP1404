"""
Word Occurrences
Estimate: 20 minutes
Actual:   <fill this in>
"""

text = input("Text: ")
words = text.split()

word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

longest_word_length = max(len(word) for word in word_to_count)

for word in sorted(word_to_count):
    print(f"{word:{longest_word_length}} : {word_to_count[word]}")
