def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2

    elif (number % 2) == 1:
        result = (3 * number + 1)
        print(result)
        return result

userinput = (input("enter a number\n"))

##result = collatz(userinput) 

while userinput != 1:
    userinput = collatz(int(userinput))