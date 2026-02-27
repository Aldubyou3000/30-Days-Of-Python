# ===== DAY 4: STRINGS ACTIVITY - SOLUTION GUIDE =====
# Use this to check your work!

# Activity 1: Creating and Concatenating Strings
print("=== Activity 1: String Creation & Concatenation ===")
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)


# Activity 2: String Length and Case Methods
print("\n=== Activity 2: Length & Case Methods ===")
message = "Hello Python"
print("Length:", len(message))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())


# Activity 3: Indexing and Slicing
print("\n=== Activity 3: Indexing & Slicing ===")
word = "Python"
print("First char:", word[0])
print("Last char:", word[-1])
print("First 3 chars:", word[0:3])
print("Reversed:", word[::-1])


# Activity 4: Escape Sequences
print("\n=== Activity 4: Escape Sequences ===")
sentence_with_newline = "I love learning Python.\nCoding is so much fun!"
text_with_tab = "Name\tAge\tCity\nAlice\t25\tNew York"
print(sentence_with_newline)
print(text_with_tab)


# Activity 5: String Formatting
print("\n=== Activity 5: String Formatting ===")
name = "Alice"
age = 25
city = "New York"
formatted_sentence = f"My name is {name}, I am {age} years old, and I live in {city}"
print(formatted_sentence)


# Activity 6: String Methods
print("\n=== Activity 6: String Methods ===")
text = "learning python is fun"
print("Capitalized:", text.capitalize())
print("Title case:", text.title())
print("Count 'n':", text.count('n'))
print("Replaced:", text.replace('python', 'coding'))
print("Split:", text.split())


# Activity 7: Practical Challenge
print("\n=== Activity 7: Practical Challenge ===")
company = "Tech Company"
employee_name = "Sarah"
role = "developer"
years = 3

profile = f"""
{company.upper()}
Employee: {employee_name.capitalize()}
Role: {role.capitalize()}
Experience: {years} years
Company uses: {company}
"""
print(profile)


# BONUS: Mini Challenge
print("=== BONUS: Mini Challenge ===")
favorite_hobby = "coding"
your_name = "alex"
sentence = your_name.capitalize() + " loves " + favorite_hobby + "!\nCoding is awesome!"
print(sentence)
