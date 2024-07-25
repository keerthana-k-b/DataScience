def is_perfect_number(n):
    factors = [i for i in range(1, n) if n % i == 0]
    if sum(factors) == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

# test the function
num = int(input("Enter a number: "))
is_perfect_number(num)