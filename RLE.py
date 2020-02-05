word = input("Enter word>")
count = 0
character = ""
result = ""
prev_character = word[0]

for i in range(len(word)):
    character = word[i]
    if prev_character == character:
        count += 1
    else: 
        result += prev_character + str(count)
        count = 1
        
    
    prev_character = character 

print(result + str(prev_character) + str(count))