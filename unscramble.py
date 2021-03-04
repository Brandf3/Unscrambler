filename = input("Filename: ")
file = open(filename, 'r')
sortedList = []
unsortedList = []
for line in file:
    stripped = line[:-1].lower()
    unsortedList.append(stripped)
    sortedList.append(sorted(stripped))

word = ""
while word != "q":
    word = input("Enter Word (q to quit): ")
    word = sorted(word)
    for i in range(0, len(sortedList)):
        if sortedList[i] == word:
            print(unsortedList[i])
            break
