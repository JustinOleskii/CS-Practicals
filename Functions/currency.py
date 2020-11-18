def finder(dict):
    ch = input("Enter name of country: ")
    print("The currency is: {}".format(dict[ch]))

currencies = {}
n = int(input("How many currencies would you like to input?\n "))
for i in range(0, n):
    key = input("Enter country: ")
    value = input("Enter currency: ")
    currencies[key] = value

finder(currencies)
