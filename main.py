flag=True
gradebook = {}
testGradebook = {}
while flag == True:
    print ("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Add Grade
    5.Get Class Average
    6.Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        name = input("Enter a name")
        gradebook[name] = {}
        print(gradebook)

        print("\n Student Added")
    elif ans=="2":
        name = input("What is the students name")

        del gradebook[name]
        print(gradebook)

        print("\n Student Deleted")
    elif ans=="3":
        name = input("What student do you want to look up")
        try:
            print(gradebook[name])
        except:
            print("Student doesnt exist")


    elif ans=="4":
        name = input("Enter a name")
        assignment = input("enter assignment name")
        grade = int(input("enter assignment grade"))
        gradebook[name][assignment] = grade
        print(gradebook)
        print("grade added")
    elif ans == "5":
        studentAverages = []
        for student in gradebook:
            print(gradebook[student])
            studentGrades = []
            for grade in gradebook[student]:
                print(gradebook[student][grade])
                studentGrades.append(gradebook[student][grade])
            print(studentGrades)
            average = sum(studentGrades)/len(studentGrades)
            print(average)



    elif ans == "6":
        flag = False

        print("\n Goodbye")
    elif ans !="":
      print("\n Not Valid Choice Try again")










