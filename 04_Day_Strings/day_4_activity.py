# ===== DAY 4: STRINGS BEGINNER ACTIVITY =====
# Complete the activities below to practice string concepts

# Activity 1: Creating and Concatenating Strings
print("=== Activity 1: String Creation & Concatenation ===")
first_name = "John"
last_name = "Doe"
# TODO: Concatenate first_name and last_name with a space between them
# and store in a variable called full_name
space = " "
full_name = first_name + space + last_name

#Uncomment and complete:
print("Full name:", full_name)


# Activity 2: String Length and Case Methods
print("\n=== Activity 2: Length & Case Methods ===")
message = "Hello Python"
# TODO: Print the length of the message
# TODO: Print the message in UPPERCASE
# TODO: Print the message in lowercase

# Uncomment and complete:
print("Length:", len(message))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())


# Activity 3: Indexing and Slicing
print("\n=== Activity 3: Indexing & Slicing ===")
word = "Python"
# TODO: Get the first character (index 0)
# TODO: Get the last character (using negative index)
# TODO: Get the first 3 characters (slice)
# TODO: Reverse the word using slice

# Uncomment and complete:
print("First char:", word[0])
print("Last char:", word[-1])
print("First 3 chars:", word[0:3])
print("Reversed:", word[::-1])


# Activity 4: Escape Sequences
print("\n=== Activity 4: Escape Sequences ===")
# TODO: Create a string with a newline between two sentences
# Example format:
# "Sentence 1.
#  Sentence 2."

# TODO: Create a string with a tab to align text

# Uncomment and complete:
sentence_with_newline = "I'm so handsome. \nAlways will be!"
text_with_tab = "\t\t I'm a tabbed sentence."
print(sentence_with_newline)
print(text_with_tab)


# Activity 5: String Formatting
print("\n=== Activity 5: String Formatting ===")
name = "Alice"
age = 25
city = "New York"

# Using f-strings (simplest for beginners)
# TODO: Create a sentence using f-strings
# Format: "My name is [name], I am [age] years old, and I live in [city]"

# Uncomment and complete:
formatted_sentence = f"My name is {name} and I'm {age} years old, I lived in {city}. It's nice to meet you!"
print(formatted_sentence)


# Activity 6: String Methods
print("\n=== Activity 6: String Methods ===")
text = "learning python is fun"

# TODO: Use capitalize() to capitalize the first letter
# TODO: Use title() to capitalize each word
# TODO: Use count() to count how many times 'n' appears
# TODO: Use replace() to replace 'python' with 'coding'
# TODO: Use split() to split the text into words

# Uncomment and complete:
print("Capitalized:", text.capitalize())
print("Title case:", text.title())
print("Count 'n':", text.count("n"))
print("Replaced:", text.replace("python", "coding"))
print("Split:", text.split())


# Activity 7: Practical Challenge
print("\n=== Activity 7: Practical Challenge ===")
# Task: Create a simple profile card
# Use string concatenation, formatting, and methods

company = "Tech Company"
employee_name = "Sarah"
role = "developer"
years = 3

# TODO: Create a profile string using f-strings that displays:
# TECH COMPANY
# Employee: Sarah
# Role: Developer (capitalize first letter)
# Experience: 3 years
# Company uses: Tech Company

# Hint: Use .upper(), .capitalize(), and f-strings

# Uncomment and complete:
profile = f"""
{company.upper()}
Employee: {employee_name}
Role: {role.capitalize()}
Experience: {years} years
Company uses: {company}
"""
print(profile)


# ===== BONUS CHALLENGE (Optional) =====
print("\n=== BONUS: Mini Challenge ===")
# Create a simple sentence about yourself using:
# - String concatenation
# - At least one string method
# - One escape sequence (\n or \t)

# Example structure:
favorite_hobby = "gaming"
your_name = "lewel"
sentence = your_name.capitalize() + " loves " + favorite_hobby + "!\nCoding is awesome!"
print(sentence)
