def ExamGrade(examLvl, examGrade):
    
    if examLvl > 1 or examLvl < 4:
        if examLvl == 1 or examLvl == 2:
            if examGrade >= 85:
                print("You earned a Dist.")
            elif examGrade >=75:
                print("You earned a Merit.")
            elif examGrade >=65:
                print("You earned a Pass.")
            else:
                print("Invalid")
        if examLvl == 3:
            if examGrade >=80:
                print("You earned a Dist.")
            elif examGrade >=70:
                print("You earned a Merit.")
            elif examGrade >=60:
                print("You earned a Pass.")
            else:
                print("Invalid")
        if examLvl == 4:
            if examGrade >= 70:
                print("You earned a Dist.")
            elif examGrade >=60:
                print("You earned a Merit.")
            elif examGrade >= 50:
                print("You earned a Pass.")
            else:
                print("Invalid")
    else:
        print("InvalidLvl")
        return 
    
YourLvl=int(input("Enter your level: "))
YourGrade=int(input("Enter your grade: "))

ExamGrade(YourLvl, YourGrade)
    
