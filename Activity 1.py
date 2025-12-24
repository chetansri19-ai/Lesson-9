medical_condition=input("Do you have a medical condition? (Y or N)")

if medical_condition.upper()=="Y":
    print("You are allowed to take the exam")
else:
    if medical_condition.upper()=="N":
        attendance=int(input("Enter how many classes you have attended:"))
    if attendance >=75:
        print("You are permitted to take the exam")
    else:
        print("You are not permitted to take the exam")