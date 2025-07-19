# A program where three students marks are entered,their remarks and topper is displayed
student_a = input("ENTER 1st STUDENT's NAME:")
subjects = {
    "english" : int(input("ENTER YOUR MARKS IN ENGLISH:")),
    "science" : int(input("ENTER YOUR MARKS IN SCIENCE:")),
    "maths" : int(input("ENTER YOUR MARKS IN MATHS:")),
    "social" : int(input("ENTER YOUR MARKS IN SOCIAL SCIENCE:"))
}
print()
print("Student's Name - " + student_a)
print("ENGLISH: " + str(subjects["english"]))
print("SCIENCE: " + str(subjects["science"]))
print("MATHS: " + str(subjects["maths"]))
print("SOCIAL SCIENCE: " + str(subjects["social"]))
total_a = sum(subjects.values())
print("STUDENT's TOTAL MARKS:" , total_a)
average_a = (total_a/4)
print("STUDENT's AVERAGE:" , average_a)
a= ("REMARK:")
if (average_a>90):
    print( a,"EXCELLENENT!")
elif(average_a>80 and average_a<90):
    print(a,"GOOD!, KEEP TRYING.")
elif (average_a>70 and average_a<80):
    print(a,"COULD DO BETTER.")
elif(average_a>60 and average_a<70):
    print(a,"PASSED ON CONSIDERATION.")
elif(average_a>50 and average_a<60):
    print(a,"WORK HARD. PASSED ON CONSIDERATION.")
else:
    print(a,"FAIL.")
print()
print()
student_b = input("ENTER 2nd STUDENT's NAME:")
subjects = {
    "english" : int(input("ENTER YOUR MARKS IN ENGLISH:")),
    "science" : int(input("ENTER YOUR MARKS IN SCIENCE:")),
    "maths" : int(input("ENTER YOUR MARKS IN MATHS:")),
    "social" : int(input("ENTER YOUR MARKS IN SOCIAL SCIENCE:"))
}
print()
print("Student's Name - " + student_b)
print("ENGLISH: " + str(subjects["english"]))
print("SCIENCE: " + str(subjects["science"]))
print("MATHS: " + str(subjects["maths"]))
print("SOCIAL SCIENCE: " + str(subjects["social"]))
total_b = sum(subjects.values())
print("STUDENT's TOTAL MARKS:" , total_b)
average_b = (total_b/4)
print("STUDENT's AVERAGE:" , average_b)
a= ("REMARK:")
if (average_b>90):
    print( a,"EXCELLENENT!")
elif(average_b>80 and average_b<90):
    print(a,"GOOD!, KEEP TRYING.")
elif (average_b>70 and average_b<80):
    print(a,"COULD DO BETTER.")
elif(average_b>60 and average_b<70):
    print(a,"PASSED ON CONSIDERATION.")
elif(average_b>50 and average_b<60):
    print(a,"WORK HARD. PASSED ON CONSIDERATION.")
else:
    print(a,"FAIL.")
print()
print()
student_c = input("ENTER 3rd STUDENT's NAME:")
subjects = {
    "english" : int(input("ENTER YOUR MARKS IN ENGLISH:")),
    "science" : int(input("ENTER YOUR MARKS IN SCIENCE:")),
    "maths" : int(input("ENTER YOUR MARKS IN MATHS:")),
    "social" : int(input("ENTER YOUR MARKS IN SOCIAL SCIENCE:"))
}
print()
print("Student's Name - " + student_c)
print("ENGLISH: " + str(subjects["english"]))
print("SCIENCE: " + str(subjects["science"]))
print("MATHS: " + str(subjects["maths"]))
print("SOCIAL SCIENCE: " + str(subjects["social"]))
total_c= sum(subjects.values())
print("STUDENT's TOTAL MARKS:" , total_c)
average_c = (total_c/4)
print("STUDENT's AVERAGE:" , average_c)
a= ("REMARK:")
if (average_c>90):
    print( a,"EXCELLENENT!")
elif(average_c>80 and average_c<90):
    print(a,"GOOD!, KEEP TRYING.")
elif (average_c>70 and average_c<80):
    print(a,"COULD DO BETTER.")
elif(average_c>60 and average_c<70):
    print(a,"PASSED ON CONSIDERATION.")
elif(average_c>50 and average_c<60):
    print(a,"WORK HARD. PASSED ON CONSIDERATION.")
else:
    print(a,"FAIL.")
print()

if(average_a>average_b and average_a>average_c):
    print("THE TOPPER IS:", student_a )
elif(average_b>average_a and average_b>average_c):
    print("THE TOPPER IS:", student_b )
else:
    print("THE TOPPER IS:" , student_c)


