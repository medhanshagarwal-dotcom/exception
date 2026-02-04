while True:
    try:
        num1,num2=eval(input("Enter two numbers, separated by comma: "))
        res=num1/num2
        print(f"Result is: {res}")
    except ZeroDivisionError:
        print("Do not divide by 0")
    except SyntaxError:
        print("You forgot a comma")
    except NameError as ex:
        print("Error: ",ex)
    except:
        print("Wrong input")

    else:
        print("No error you wrote correctly")

    finally:
        print("I will run no matter what.")

