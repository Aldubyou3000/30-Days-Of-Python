name = input("Enter your name: ")
grade_1 = int(input("Enter marks for Subject 1: "))
grade_2 = int(input("Enter marks for Subject 2: "))
grade_3 = int(input("Enter marks for Subject 3: "))

total = grade_1 + grade_2 + grade_3
avg = total / 3

print("---Grade Report---")
print(f"Student: {name.capitalize()}")
print(f"Total marks: {total}")
print(f"Average: {avg:.2f}")

status = ["FAILED", "PASS"][avg >= 50]
print(f"Status {status}")