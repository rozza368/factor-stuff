"""

INPUT number
ARRAY factors
mult = 1

FOR i IN (2 TO INT SQRT number)
    IF number % i^2 EQUALS 0
        SET number TO number / i^2
        SET mult TO mult * i
PRINT mult number
    

"""

def main():
    number = int(input("Number: "))
    root = number ** 0.5
    mult = 1
    available = True

    if root % 1:
        print("Not a square")
        while available:
            available = False
            for i in range(2, int(root+1)):
                print(f"testing {i} {i**2}")
                # number divides evenly by square
                if not number % i**2:
                    number //= i**2
                    mult *= i
                    available = True
                    break

    else:
        mult = int(root)
        number = 1
       
    # todo
    print(f"{mult if mult > 1 else ''}{' root ' if not number == 1 else ''}{number if number > 1 else ''}")
    print()

while True:
    main()
