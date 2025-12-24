elec_units=int(input("Enter the number of electricity units consumed: "))

if elec_units <=50:
    bill_amount=(elec_units*2.60)+25
    print("The total electricity bill is: ",bill_amount)
else:
    if elec_units <=100:
        bill_amount=(elec_units*3.25)+35
        print("The total electricity bill is: ",bill_amount)
    else: 
        if elec_units <=200:
            bill_amount=(elec_units*2.56)+45
            print("The total electricity bill is: ",bill_amount)
        else:
                bill_amount=(elec_units*8.45)+75
                print("The total electricity bill is: ",bill_amount)