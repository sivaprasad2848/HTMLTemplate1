#Fruit Price List Program
product=[]
pid=1
i=0
def menu():
    print("What operation do you want to perform?")
    print("1->For enter a new product")
    print("2->For list all products")
    print("3->For remove a product")
    print("4- For update a product")
    op=int(input("Enter the operation code"))
    return op
def add_product():
    pname=input("Enter the product name")
    price=input("Enter product Price")
    product.append((pid,pname,price))
def product_list():
    if(len(product)>0):
        print(" Id    ProductName   Price")
        for item in product:
            print(str(item[0])+"  "+item[1]+"   "+item[2])
    else:
        print("There are no Items added yet")

while(i==0):
    opt=int(menu())
    if(opt==1):
        add_product()
        pid=pid+1
    if(opt==2):
        product_list()
    if(opt==3):
        print("You choosed Product delete")
    if(opt==4):
        print("You choosed update a product option")
    print("Do you want to continue?")
    i=int(input("Press 0 for continue"))
