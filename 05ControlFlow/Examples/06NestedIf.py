print("Menu:\n3 - Level 3\n4 - Level 4")

def exam_level():
    n = int(input("Enter level:"))
    if n == 3 or n == 4:
        if n == 3:
            mark = int(input("Enter level 3 mark: "))
            if mark > 65:
                print("Level 3 exam passed.")
            else:
                print("Level 3 exam fail.")
        elif n == 4:
            if mark > 65:
                print("Level 4 exam passed.")
            else:
                print("Level 4  exam fail.")
    else:
        print("Invalid.")
    return
    
exam_level()
