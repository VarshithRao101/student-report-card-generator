print(" WELCOME TO THE REPORT CARD GENERATOR ")
print("=========================================")
print("Please enter the following details to generate your report card.")
print("=========================================")
print(input(" press enter to continue..."))


#now taking details of the user

student_name = input("Enter your name: ")

# subject wise marks

css_marks = int(input("Enter your marks in CSS: "))
if css_marks < 0 or css_marks > 100:
    print("Invalid marks for Telugu. Please enter a value between 0 and 100.")
    telugu_marks = int(input("Enter your marks in Telugu: "))
hindi_markd=int(input("Enter your marks in hindi: "))
if hindi_markd < 0 or hindi_markd > 100:
    print("Invalid marks for Hindi. Please enter a value between 0 and 100.")
    hindi_markd = int(input("Enter your marks in Hindi: "))
english_marks = int(input("Enter your marks in English: "))
if english_marks < 0 or english_marks > 100:
    print("Invalid marks for English. Please enter a value between 0 and 100.")
    english_marks = int(input("Enter your marks in English: "))
maths_marks = int(input("Enter your marks in Maths: "))
if maths_marks < 0 or maths_marks > 100:
    print("Invalid marks for Maths. Please enter a value between 0 and 100.")
    maths_marks = int(input("Enter your marks in Maths: "))
science_marks = int(input("Enter your marks in Science: "))
if science_marks < 0 or science_marks > 100:
    print("Invalid marks for Science. Please enter a value between 0 and 100.")
    science_marks = int(input("Enter your marks in Science: "))
social_marks = int(input("Enter your marks in Social: "))
if social_marks < 0 or social_marks > 100:
    print("Invalid marks for Social. Please enter a value between 0 and 100.")
    social_marks = int(input("Enter your marks in Social: "))

#now calculating the marks

total_marks = css_marks + hindi_markd + english_marks + maths_marks + science_marks + social_marks
max_marks = 600
percentage = (total_marks / max_marks) * 100
print("=========================================")
print("GEnerating your report card...")
print("=========================================")


# calculating individual percentage
css_percentage = (css_marks / 100) * 100
hindi_percentage = (hindi_markd / 100) * 100
english_percentage = (english_marks / 100) * 100
maths_percentage = (maths_marks / 100) * 100
science_percentage = (science_marks / 100) * 100
social_percentage = (social_marks / 100) * 100


print(f"your percentage in css is : {css_percentage}%")
print(f"your percentage in hindi is : {hindi_percentage}%")
print(f"your percentage in english is : {english_percentage}%")
print(f"your percentage in maths is : {maths_percentage}%")
print(f"your percentage in science is : {science_percentage}%")
print(f"your percentage in social is : {social_percentage}%")

print("=========================================")



# subject wise percentage 
list_of_subject_percenteges = [
                    css_percentage,
                 hindi_percentage,
                 english_percentage,
              maths_percentage,
            science_percentage,
         social_percentage
]
print(f"Your total percentage is : {percentage}%")

print("=========================================")
print(f"Total Marks Obtained: {total_marks} out of {max_marks}")


# grading system 
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'



print(f"Your grade is: {grade}")
if any(percentage < 60 for percentage in list_of_subject_percenteges):
    print("You have failed in one or more subjects.")
    print("Please review your performance and work on the areas that need improvement.")
else:
    print("You have passed in all subjects. Well done!")

 


print("=========================================")

print("Thank you for using the Report Card Generator!")
