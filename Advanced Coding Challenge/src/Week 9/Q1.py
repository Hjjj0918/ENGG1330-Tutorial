def readData(products:dict):
    command = input().split()
    while (command[0] != "END"):
        products[int(command[0])] = [command[1], float(command[2])]
        command = input().split()
    return products

def showMenu(products):
    print("-Menu-")
    for k in products:
        v = products[k]
        item = v[0]
        price = v[1]
        print(f"{k} : {item} $ {price}")
    print("------")

def purchase(products):
    showMenu(products)
    product_code = int(input("Product code:"))
    quantity = int(input("Quantity:"))
    product_data = products[product_code]
    price = product_data[1]*quantity
    print ("Added $",price)
    return price

def checkout(total):
    plusTax = total * 1.05
    print("Purchase $",total)
    print("Tax $",total * 0.05)
    print("Total $",plusTax)
    print("Thank you!")

def main():
    products = {}
    readData(products)
    
    print("****************************************")
    print("*  Welcome to ENGG1330's supermarket!  *")
    print("****************************************")
    
    choice = 0
    total = 0
    while( choice != 3 ):
        print("------------------------")
        print("\t 1: Purchase. ")
        print("\t 2: Checkout. ")
        print("\t 3: Exit. ")
        print("------------------------")
           
        choice=int(input("Please select:"))

        if ( choice == 1 ):
            total += purchase(products)
            print("Current amount $", total)
        elif( choice == 2 ):
            checkout(total)
            break
        elif ( choice == 3 ):
            return

main()