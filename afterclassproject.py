import colorama 


while True:
    try:
        n=int(input("Enter age(Enter 0 to exit): "))
        if n<0:
            raise ValueError ("Age cannot be negative")
        
        if n==0:
            break

        if n%2==0:
            print("Even")
        else:
            print("odd")
    except ValueError as ex:
        print("Exception ", ex)

