import random

wordbank: list[int | str] = ["indentation", "spaces"] 
tlgstudents: list[str] = ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)
print("")
print(wordbank)

num: str = input(f"\nEnter a number between 1 and {len(tlgstudents)}: ")
student_name = tlgstudents[int(num)-1]

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")

random_student = random.choice(tlgstudents)
# random_student = tlgstudents[random.randint(0, len(tlgstudents) - 1)]  # Alternative
print("\n--- Random Student Selection ---")
print(f"{random_student} always uses {wordbank[-1]} {wordbank[1]} to indent.")
