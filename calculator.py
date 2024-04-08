
def add(a,b):
    a = float(a)
    b = float(b)

    return a+b

def subtract(a,b):
    a = float(a)
    b = float(b)

    return a-b

def multiply(a,b):
    a = float(a)
    b = float(b)

    return a*b

def divide(a,b):
    a = float(a)
    b = float(b)

    if b==0: 
        
        return "None"
    else:
        return a/b

def power(a,b):
    a = float(a)
    b = float(b)

    return a^b

def remainder(a,b):
    a = float(a)
    b = float(b)

    return a%b

def select_op(choice):
    if choice=="#":
        return -1
      
list = []

def history(list):
    print(*list,sep="\n")

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
  

    
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)


    if(select_op(choice) == -1):
        print("Done. Terminating")
        exit()

    a = input("Enter first number: ")
    print(a)
    if "$" in a:
        continue
    elif "#" in a:
        print("Done. Terminating")
        exit()
    else:
        b = input("Enter second number: ")
        print(b)
        if "$" in b:
            continue
        elif "#" in b:
            print("Done. Terminating")
            exit()
        else:
            try:
                if choice=="+":
                    print(a,"+",b,"=",add(a,b))
                    list.append(a,choice,b,"=",add(a,b))
                elif choice=="-":
                    print(a,"-",b,"=",subtract(a,b))
                    list.append(a,choice,b,"=",subtract(a,b))
                elif choice=="*":
                    print(a,"*",b,"=",multiply(a,b))
                    list.append(a,choice,b,"=",multiply(a,b))
                elif choice=="/":
                    print(a,"/",b,"=",divide(a,b))
                    list.append(a,choice,b,"=",divide(a,b))
                    if b==0:
                        print("float division by zero")
                elif choice=="^":
                    print(a,"^",b,"=",power(a,b))
                    list.append(a,choice,b,"=",power(a,b))
                elif choice=="%":
                    print(a,"%",b,"=",remainder(a,b))
                    list.append(a,choice,b,"=",remainder(a,b))
                elif choice=="?":
                    history(list)
                else:
                    print("Unrecognized operation")

               
             
            except:
                continue