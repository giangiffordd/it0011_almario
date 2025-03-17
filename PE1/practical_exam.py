word_list = []
word_counter = []
string_statement = input("Enter a String Statement: ")
word = string_statement.split()
exclude = ["and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"]
total_word_filter = 0

i = 0
while i < len(word):
    temp_word = word[i]
    temp_word_lower = temp_word.lower()
    
    if temp_word_lower not in exclude:
        found = False
        index = 0
        while index < len(word_list):
            if word_list[index].lower() == temp_word_lower:
                word_counter[index] += 1
                total_word_filter += 1
                found = True
                break
            index += 1
            
        if not found:
            word_list.append(temp_word)
            word_counter.append(1)
            total_word_filter += 1
    i += 1

unique_words = []
for w in word_list:
    if w.lower() not in unique_words:
        unique_words.append(w.lower())

word_lower = []
word_upper = []
for word in unique_words:
    total = 0
    for j in range(len(word_list)):
        if word_list[j].lower() == word:
            total += word_counter[j]
    
    if word[0].islower():
        word_lower.append((word, total))
    else:
        word_upper.append((word, total))

word_lower.sort()
word_upper.sort()

i = 0
while i < len(word_lower):
    print(word_lower[i][0], "-", word_lower[i][1])
    i += 1

i = 0
while i < len(word_upper):
    print(word_upper[i][0], "-", word_upper[i][1])
    i += 1
    
print("Total words filtered: ", total_word_filter)