drinks=[
    {'latte':{'ingredient': {'water': 200, 'coffe': 10, 'milk': 50},'cost': 2.5}},
    {'americano': {'ingredient': {'water': 180, 'coffe': 12, 'milk': 60},  'cost': 2.6}},
    {'cappuchino':{'ingredient': {'water': 200,'coffe': 15, 'milk': 70}, 'cost': 2.8}},
      ]

while True:
    drink_choice = input("Choose drinks: 0 for latte, 1 for americano, 2 for cappuchino: ")
    if drink_choice == "c":
        print("Bye, come again")
        break
    elif int(drink_choice) not in range(0,3):
        print("Invalid Input, please follow instructions")
        break
    else:
        for drinks_name,drinks_info in drinks[int(drink_choice)].items():
            print(f"\nYour selected drinks is {drinks_name}.")

            for ingredient_name,ingredient_price in drinks_info["ingredient"].items():
                print(f"\t {ingredient_name}: ${ingredient_price}")
        break



