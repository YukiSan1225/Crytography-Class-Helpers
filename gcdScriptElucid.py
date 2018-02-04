# This is for CS 547, helps calculating GCD

print("How many times do you want to use this program?")
times = input()
times = int(times)

while(times != 0):
    print("This is the GCD calculator. Please input your values\nGCD(a,b)")
    a = input()
    b = input()

    number1 = int(a)
    number2 = int(b)

    def gcd(a,b):
        if b == 0:
            return a
        else:
            return gcd(b,a%b)

    print("The GCD values of " +a+" & "+b+" is "+str(gcd(number1,number2)))

    times-=1