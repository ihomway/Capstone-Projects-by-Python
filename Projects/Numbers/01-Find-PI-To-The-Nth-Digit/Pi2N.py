'''
Find PI to the Nth Digit

Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.
'''

import math
from decimal import Decimal

def calculatePiTo(num):
    constant = 426880 * math.sqrt(10005)

    def sigma_func(k):
        def m_func(k):
            return math.factorial(6 * k) / (math.factorial((3 * k)) * math.factorial(k)**3)

        def l_func(k):
            return 545140134 * k + 13591409

        def x_func(k):
            return (-2625374122640768000)**k

        return m_func(k) * l_func(k) / x_func(k)

    sum = 0
    for i in range(num):
        sum += sigma_func(i)

    return constant * sum ** -1
    

if __name__ == '__main__':
    piStr = str(calculatePiTo(10))
    a = Decimal(piStr)
    a = round(a,10)
    print(a)