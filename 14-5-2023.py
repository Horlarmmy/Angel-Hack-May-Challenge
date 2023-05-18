letter_counts = {}
sentence = 'kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor'
for letter in sentence:
    if letter in letter_counts:
        letter_counts[letter] +=1
    else:
        letter_counts[letter] = 1
sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
print(sentence)
print(sorted_counts)