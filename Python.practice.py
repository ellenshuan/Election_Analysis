#What is the score?
score = int(input("What is your test score?"))

#Determine the grade. 
if score >= 90: 
    print('Your grade is an A.')
else: 
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score >= 60: 
                print('Your grade is a D')
            else:
                if score >= 50:
                    print('Your grade is an F')

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    for county in counties:
        print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for i in range(len(counties)):
    print(counties[i])
    


