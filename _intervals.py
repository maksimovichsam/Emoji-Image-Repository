from os import listdir
from os.path import isfile, join

################################################
# Intervals.py
# - Given all the emojis in the emoji-repository, we gather all emoji code points and
# split them into intervals
# - This is so that we can easily detect if a character is an emoji, by checking its 
# code point is in one the intervals
################################################

repo_path = 'C:\\Users\\maksi\\Desktop\\Projects\\emoji-repository'
onlyfiles = [f for f in listdir(repo_path) if isfile(join(repo_path, f))]
print(len(onlyfiles))

numbers = set()
for file in onlyfiles:
    if "-" in file:
        prefix = file.split("-")[0]
        numbers.add(int(prefix, 16))

# Lazy interval implementation
numbers = list(numbers)
numbers.sort()
intervals = []
start = 0
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1] + 1:
        intervals.append([numbers[start], numbers[i - 1]])
        start = i
intervals.append([numbers[start], numbers[-1]])

print(intervals)
print(len(intervals))