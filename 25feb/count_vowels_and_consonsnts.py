# Count Vowels and Consonants

text = input("Enter a string: ").lower()

vowels = "aeiou"
v_count = 0
c_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)