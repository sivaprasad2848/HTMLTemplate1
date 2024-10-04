#File Operations
def create_contact():
    name=input("Enter the name")
    email=input("Enter email")
    mobile=input("Mobile")
    data=name+" "+email+" "+mobile+"\n"
    f=open("data","a")
    f.write(data)
    f.close()
def display_contact():
    f=open("data","r")
    data=f.read()
    print(data)
    f.close()
i=0
while(i==0):
    print("******Contact Program ********")
    print("1->Create a contact")
    print("2->Display contacts")
    opt=int(input("Enter the option"))
    if(opt==1):
        create_contact()
    if(opt==2):
        display_contact()
    print("Do you want to continue?")
    i=int(input("Press 0 for continue"))
