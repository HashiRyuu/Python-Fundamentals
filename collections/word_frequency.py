word = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair"

word = word.lower()
wordList = word.split()
Count = {}

for letter in wordList:
    if letter in Count:
        Count[letter] = Count[letter] + 1
    else: Count[letter] = 1
    
    
for key, value in sorted(Count.items()):
    print(f"{key}: {value}")
