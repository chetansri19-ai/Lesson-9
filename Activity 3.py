b_o_c=input("Select Car or Bike (C/B): ")
if b_o_c.upper()=="C":
    car_type=input("Select Sedan or SUV (S/E): ")
    if car_type.upper()=="S":
        print("Sedan selected.")
    else:
        print("SUV selected.")

if b_o_c.upper()=="B":
    bike_type=input("Select Sports or Cruiser (S/C): ")
    if bike_type.upper()=="S":
        print("Sports Bike selected.")
    else:
        print("Cruiser Bike selected")