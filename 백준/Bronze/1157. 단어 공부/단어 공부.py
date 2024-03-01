from sys import stdin as s


word = s.readline().strip().upper()
if word:
    letter_counts = {letter: word.count(letter) for letter in set(word)}
    max_count = max(letter_counts.values())
    most_frequent_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    print('?' if len(most_frequent_letters) > 1 else most_frequent_letters[0])
else:
    print("?")