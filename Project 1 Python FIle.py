# What task do you want to do? (1: temp, 2: weight, 3: distance 0 for quit): 3 <br>
# OK, let's convert distance in feet to meter <br>
# Enter distance in feet: 3 <br>
# Result: 3.0 feet is 0.9144000000000001 meter

while True:
    choice = int(input(f"Please choose a conversion (1 = temperature, 2 = distance, 3 = weight, 4 = time, 5 = volume, 0 = stop): "))
    if choice == 1:
        print(f"Lets convert celcius to fahrenheit")
        Fahrenheit = float(input(f"Enter temperature in Fahrenheit: "))
        Celsius = (Fahrenheit - 32) * 5/9
        print(f"Answer: {Fahrenheit} degrees F is {Celsius} degrees Celcius")

    elif choice == 2:
        print(f"Lets convert feet to meters")
        Feet = float(input(f"Enter a distance in feet: "))
        Meters = (Feet/.305)
        print(f"Answer: There are {Meters} meters in {Feet} feet")

    elif choice == 3:
        print(f"Lets convert pounds to kilograms")
        Pounds = float(input(f"Enter weight in pounds: "))
        Kilograms = (Pounds/.454)
        print(f"Answer: There are {Kilograms} kgs in {Pounds} lbs")

    elif choice == 4:
        print(f"Lets convert seconds into minutes")
        Seconds = float(input(f"Enter seconds: "))
        Minutes = Seconds/60
        print(f"Answer: There are {Seconds} seconds in {Minutes} minutes")
    
    elif choice == 5:
        print(f"Lets convert teaspoons to tablespoons")
        Teaspoons = float(input(f"Enter teaspoons: "))
        Tablespoons = Teaspoons/3
        print(f"Answer: There are {Teaspoons} teaspoons in {Tablespoons} tablespoons")
    elif choice == 0:
        print(f"Thank you for converting!")
        break
    else:
        print(f" Invalid option, try again")