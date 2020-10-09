def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

def get_divisors(x, U):
    if is_prime(U) == True:
        U = U - 1
    divisors = []
    for i in range(1, U + 1):
        if U % i == 0:
            divisors.append(i)
    return divisors

def get_orders(x, U, divisors):
    orders = []
    for i in range(0, len(divisors)):
        x_to_the_divisor = pow(x, divisors[i])
        print(x_to_the_divisor % U)
        if x_to_the_divisor % U == 1:
            orders.append(divisors[i])
    return orders

x = int(input("Enter order: "))
U = int(input("Enter U: "))

divisors = get_divisors(x, U)
print(divisors)

orders = get_orders(x, U, divisors)
print(orders)
