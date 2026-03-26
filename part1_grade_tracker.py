# STUDENT GRADE TRACKER

# TASK 1: Data Parsing & Profile Cleaning
print("\n Task 1: Data Parsing & Profile Cleaning \n")
raw_students = [ {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
 {"name": "ROHIT verma","roll": "102", "marks_str": "55, 68, 49, 72, 61"},
 {"name": "  Priya Nair  ","roll": "103", "marks_str": "91, 85, 88, 94, 79"},
 {"name": "karan MEHTA","roll": "104", "marks_str": "40, 55, 38, 62, 50"},
 {"name": " Sneha pillai ","roll": "105", "marks_str": "75, 80, 70, 68, 85"}]

cleaned_students =[]
for student in raw_students:
  #Clean Name
  name = student["name"].strip().title()
  #Roll converted to int
  roll = int(student["roll"])
  #Convert marks string to list of integers
  marks = list(map(int, student["marks_str"].split(", ")))

  #Validity of Name (To check for alphabetical characters only)
  valid = all(word.isalpha() for word in name.split())
  if valid:
    print(f"{name} ✓ Valid name")
  else:
    print(f"{name} ✗ Invalid name")

  # Store cleaned data
  cleaned_students.append({"name": name,"roll": roll,"marks": marks})

  #Formatted Profile Data (Print)
  print("=" *32)
  print(f"Student : {name}")
  print(f"Roll No : {roll}")
  print(f"Marks   : {marks}")
  print("=" *32)
  
  # Print ALL CAPS & lowercase (roll 103)
for student in cleaned_students:
    if student["roll"] == 103:
        print("\nOutput:")
        print(student["name"].upper())
        print(student["name"].lower())
#
#
#
# TASK 2: Marks Analysis Using Loops & Conditionals
print("\n Task 2: Marks Analysis Using Loops & Conditionals \n")
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Print grades of each subject
for i in range(len(subjects)):
    scores = marks[i]
    if scores >= 90:
        grade = "A+"
    elif scores >= 80:
        grade = "A"
    elif scores >= 70:
        grade = "B"
    elif scores >= 60:
        grade = "C"
    else:
        grade = "F"
    print(f"{subjects[i]}: {scores} ({grade})")

# Calculation of Marks
total = sum(marks)
average = round(total / len(marks), 2)
max_marks = max(marks)
min_marks = min(marks)

highest_sub= subjects[marks.index(max_marks)]
lowest_sub= subjects[marks.index(min_marks)]

print("Total Marks: ", total)
print("Average Marks: ", average)
print(f"Highest: {highest_sub} ({max_marks})")
print(f"Lowest: {lowest_sub} ({min_marks})")

# While loop to add the subjects
new_count = 0
while True:
    sub= input("Enter the required subject name (or type 'done'): ")
    if sub.lower() == "done":
        break

    marks_input = input("Enter marks (0-100): ")
    if not marks_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    score = int(marks_input)
    if score < 0 or score > 100:
        print("Marks should be between 0 and 100.")
        continue
    sub.append(subject)
    marks.append(score)
    new_count +=1

print("New subjects added:", new_count)
updated_avg = round(sum(marks) / len(marks), 2)
print("Updated Average is:", updated_avg)
#
#
#
# TASK 3: Class Performance Summary
print("\n Task 3: Class Performance Summary \n")
class_data = [("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85])]
print("Name                 | Average | Status ")
print("----------------------------------------")

pass_ct = 0
fail_ct = 0
average = []

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    average.append(avg)
    status = "Pass" if avg >= 60 else "Fail"
    if status == "Pass":
        pass_ct += 1
    else:
        fail_ct += 1
    print(f"{name:<18}   | {avg:^7} | {status}")

# Summary of Performance
top_avg = max(average)
topper = class_data[average.index(top_avg)][0]

class_avg = round(sum(average) / len(average), 2)

print("Passed:", pass_ct)
print("Failed:", fail_ct)
print(f"Topper: {topper} ({top_avg})")
print("Class Average:", class_avg)
#
#
#
#TASK 4: String Manipulation Utility
print("\n Task 4: String Manipulation Utility \n")
essay = "python is a versatile language. it supports object oriented,functional, and procedural programming. python is widely used in data science and machine learning."

# Step 1
clean_essay = essay.strip()
print("1.Clean Essay: ", clean_essay)
print()
# Step 2
print("2.Title Case: ", clean_essay.title())
print()
# Step 3
ct = clean_essay.count("python")
print("3.'python' count:", ct)
print()
# Step 4
replaced = clean_essay.replace("python", "Python 🐍")
print("4.Replaced: ", replaced)
print()
# Step 5
sentences = clean_essay.split(". ")
print("5.Sentence List: ", sentences)
print()
# Step 6
print("6.Numbered Sentences: ")
for i, j in enumerate(sentences, 1):
    if not j.endswith("."):
        j += "."
    print(f"{i}.{j}")
