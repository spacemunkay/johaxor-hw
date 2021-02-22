print("Welcome to the San Diego Community Survey")
total_people=[]
total_households=[]
total=[]
count=0
income_total_list = []
income_range_count=[0,0,0,0]
new_analysis="yes"
print()
print("Let's get started!")
print()
while new_analysis.lower().strip() =="yes":
    houses=int(input("How many households would you like to report? "))
    print()
    for i in range(0,houses,1):
        household_n=int(input("How many people in household {}? ".format(i+1)))
        total_households.append(household_n)

        print()
        income_total =0
        for i in range(0,household_n,1):
            x=float(input("What was person {}'s income last year? ".format(i+1)))
            total_people.append(household_n)
            total.append(x)
            income_total = income_total + x
            income_total_list.append(income_total)

        print()
    print()
    print("_________________________________________________________")
    count = len(total_households)
    print("Households analyzed: ", count)
    running_total = 0
    for element in total_households :
        running_total = running_total + element
        
    print("Number of people in census:", running_total)
    average = sum(total_households) / count
    print("Average people per household:", round(average))
    print()
    print("Average individual income: $",round(sum(total)/len(total),2))

    print("Average household income: $",round(sum(total)/len(total_households),2))
    print()
    print("Income distribution: ")
    for element in income_total_list:

           
        counter_0 = 0
        counter_l = 0
        counter_2 = 0
        counter_3 = 0
        counter_4 = 0
    
    for element in income_total_list:
        #print(element)
        if element < 20000:
            counter_0 = counter_0 + 1
        elif 20000 <= element < 40000:
            counter_l = 1
        elif 40000 <= element < 60000:
            counter_2 = 1 
        elif 60000 <= element <80000:
            counter_3 = 1
        elif 80000 <= element :
            counter_4 = 1
    
    print(f"    Less than $20,000: {counter_0} household(s)")
    print(f"    At least $20,000 but less than $40,000: {(counter_l)} household(s)")
    print(f"    At least $40,000 but less than $60,000: {(counter_2)} household(s)")
    print(f"    At least $60,000 but less than $80,000: {(counter_3)} household(s)")
    print(f"    At least $80,000: {(counter_4)} household(s)")
    print()
    new_analysis= input("Would you like to analyze another area (yes/no)?: ")
    print()
    print("_________________________________________________________")

print("Thanks for participating in our survey!")

