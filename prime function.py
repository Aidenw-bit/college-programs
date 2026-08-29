def is_prime(n):
    i = 1
    num_of_factors = 0
    
    while i <= n:
        if n % i == 0:
            num_of_factors = num_of_factors + 1
        i += 1
    if num_of_factors == 2:
        return 1
    else:
        return 0
    
def main():
    max = int(input("Please enter the amount of prime numbers you would like to see. "))
    n = 1
    count = 0
    
    while count < max:
        if is_prime(n) == 1:
            print(n)
            count += 1
            n += 1
        else:
            n += 1
    print('Ending Program...')
main()
