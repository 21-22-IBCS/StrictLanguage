
def coffeeShop():

    name=input("What's your name?")

    order=input("Enter your order")
    Num = input("How many you would like to order?")
    return name + " has ordered " + Num + " cup of " + order

def palindrome(str):
    
    if str == str[::-1]:
        return True
    else:
        return False
        

def main():
    print(coffeeShop())
    a = input("Enter a string")
    print(palindrome(a))
    

if __name__ == "__main__":
    main()
