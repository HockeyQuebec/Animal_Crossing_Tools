from fuzzysearch import find_near_matches

bells_you_have_str = input("How many bells? ")
bells_you_have = int(bells_you_have_str)

while True:

    menu_choice = input("\n" + "Choose an option:\n 1) compute years\n 2) compute max interest \n 3) Fish prices \n "
                               "4) Exit \n")

    if menu_choice == "1":
        interest_year = 0.00006

        yearly_interest = bells_you_have * interest_year

        yearly_interest_str = str(yearly_interest)

        print("Bells per year: " + yearly_interest_str)
        bells_with_interest = bells_you_have
        max_out_interest = 9999
        years = 1
        while bells_with_interest < bells_you_have + max_out_interest:
            bells_with_interest = (bells_with_interest * interest_year) + bells_with_interest
            years = years + 1
        print("if you time travel 1 year at a time")
        print("\n" + "Total bells including interest " + str(round(bells_with_interest)))
        print("Years to max out interest: " + str(years))
        print("\n" + "If you just go straight there")
        print("\n" + "Years to max out interest: " + str(round(max_out_interest / yearly_interest)))

    elif menu_choice == "2":

        interest_year = 0.00006

        yearly_interest = (interest_year * bells_you_have)

        yearly_interest_str = str((interest_year * bells_you_have))

        print("Bells of interest per year: " + yearly_interest_str)

        bells_with_interest = bells_you_have

        bells_with_interest = float(bells_with_interest) + 0.0

        inerest_over_input_years: str = input("How many years would you like to time travel: ")
        inerest_over_input_years = float(inerest_over_input_years) + 0.0

        for i in range(1, int(inerest_over_input_years)):
            bells_with_interest = (bells_with_interest * interest_year) + bells_with_interest

        print("if you time travel 1 year at a time")
        print("\n" + "You earned " + str(round(bells_with_interest - bells_you_have)) + " bells in interest")
        print("You will have " + str(round(bells_with_interest)) + " bells")

        print("\n" + "If you just go straight there")
        straight_there_interst = float(yearly_interest) * float(inerest_over_input_years)
        print("You earned " + str(straight_there_interst) + " bells in interest")
        print("You will have " + str(round(bells_you_have + straight_there_interst)) + " bells")

    elif menu_choice == "3":
        fish = input("What fish?")
        lower_fish = fish.lower()
        print('\n')
        with open('fish.txt', 'r') as f:
            for line in f:

                stripped = line.strip()
                lower = stripped.lower()
                match = find_near_matches(lower_fish, lower, max_l_dist=0)
                if match:
                    print(stripped)

    else:
        print("Exit")
        break
