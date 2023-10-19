counter = 0 

with open("sample.ini") as file:
    data = file.read()
for letters in data:
    if letters in ['a' ,'e', 'i' ,'o' ,'u']:
        counter = counter + 1
print(f"total vowel count is {counter}")