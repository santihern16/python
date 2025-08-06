import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: #comprueba si el numero es par, por lo tanto no es primo
        return False
    for i in range(3, int(math.sqrt(n))+1, 2): #solo numeros impares
        if n % i == 0:
            return False
    return True
    
if __name__ == "__main__":
    num = 113
    result = is_prime(num)
    print(result)
