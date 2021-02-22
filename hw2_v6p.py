print("Welcome to the San Diego Community Survey")
new_analysis="yes"
print()
print("Let's get started!")
print()
while new_analysis.lower().strip() =="yes":
    num_ppl_in_households=[]
    ppl_income_total=[]
    household_income_total_list = []
    num_households=int(input("How many households would you like to report? "))
    print()
    for i in range(0,num_households,1):
        household_n=int(input("How many people in household {}? ".format(i+1)))
        num_ppl_in_households.append(household_n)

        print()
        household_income_total =0
        for i in range(0,household_n,1):
            x=float(input("What was person {}'s income last year? ".format(i+1)))
            ppl_income_total.append(x)
            household_income_total = household_income_total + x

        household_income_total_list.append(household_income_total)

        print()
    print()
    print("_________________________________________________________")
    print("Households analyzed: ", num_households)
        
    num_ppl_total = sum(num_ppl_in_households)
    print("Number of people in census:", num_ppl_total)
    average = num_ppl_total / num_households
    print("Average people per household:", average)
    print()
    print("Average individual income: $",round(sum(ppl_income_total)/num_ppl_total,2))

    print("Average household income: $",round(sum(ppl_income_total)/num_households,2))
    print()
    print("Income distribution: ")

    counter_0 = 0
    counter_l = 0
    counter_2 = 0
    counter_3 = 0
    counter_4 = 0
    for element in household_income_total_list:
        #print(element)
        if element < 20000:
            counter_0 = counter_0 + 1
        elif 20000 <= element < 40000:
            counter_l = counter_l + 1
        elif 40000 <= element < 60000:
            counter_2 = counter_2 + 1 
        elif 60000 <= element <80000:
            counter_3 = counter_3 + 1
        elif 80000 <= element:
            counter_4 = counter_4 + 1
    
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

