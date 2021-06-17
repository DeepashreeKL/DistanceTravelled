distance = int(input("Input the distance travelled:"))
value = input("Input type ie:K for Kilometers or M for Miles:")

if value.upper() == "K":
    convert = distance/1.609
    print(f"You have travelled this {convert} Miles")

elif value.upper() == "M":
    convert = distance * 1.069
    print(f"You have travelled this {convert} Kilometer")

else :
    print("Wrong input")