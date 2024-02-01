from sys import stdin as s
# s=open("input.txt","rt")

test_case =int(s.readline())

words: set = set()

for test in range(test_case):
    words.add(s.readline().strip())
words= list(words)
words.sort(key=lambda x: (len(x), x))

print("\n".join(words))


