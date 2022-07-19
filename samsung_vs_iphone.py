def phone(selection):
    
    if selection == "samsung":
        samsung =[]
        samsung.append("Samsung Galaxy S10,           2019")
        samsung.append("Samsung Galaxy S10e,          2019")
        samsung.append("Samsung Galaxy S10+,          2019")
        samsung.append("Samsung Galaxy S10 5G,        2019")
        samsung.append("Samsung Galaxy S20,           2020")
        samsung.append("Samsung Galaxy S20,           2020")
        samsung.append("Samsung Galaxy S20+,          2020")
        samsung.append("Samsung Galaxy S20 Ultra,     2020")
        samsung.append("Samsung Galaxy S21,           2021")
        samsung.append("Samsung Galaxy S21+,          2021")
        samsung.append("Samsung Galaxy S21 Ultra,     2021")
        samsung.append("Samsung Galaxy S22,           2022")
        samsung.append("Samsung Galaxy S22+,          2022")
        samsung.append("Samsung Galaxy S22 Ultra,     2022")



        print("      Model      " "         Release year     ")
        while len(samsung) > 0:
            
            print(samsung.pop())

  
    if selection == "iphone":
        iphone =[]
        iphone.append("iPhone 11,                  2019")
        iphone.append("iPhone 11 Pro,              2019")
        iphone.append("iPhone 11 Pro Max,          2019")
        iphone.append("iPhone 12,                  2020")
        iphone.append("iPhone 12 Mini,             2020")
        iphone.append("iPhone 12 Pro Max,          2020")
        iphone.append("iPhone 13,                  2021")
        iphone.append("iPhone 13 Mini,             2021")
        iphone.append("iPhone 13 Pro,              2021")
        iphone.append("iPhone 13 Pro Max,          2021")

        print("      Model      " "       Release year     ")
        while len(iphone) > 0:
            print(iphone.pop())
    

while True:
    user_selection = input("Between iPhone and Samsung Galaxy, which models (in the past three years) would you like to be displayed?: ")   
    phone(user_selection.lower())

    question = input("would you like to choose again? [Y/N] ")
    if question.lower() == "y":
        None
    else:
        break


        


    
    
    
    
