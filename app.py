import matplotlib.pyplot as plt
import math

# sizes = [*range(1,5)]# X  list(range(1,5))
sizes = [x/100 for x in range(1, 400)]
constant = [1 for values in sizes] #Y 
# print(math.log(10))
logN = [math.log(n) for n in sizes]
NlogN = [n * math.log(n) for n in sizes]
N_square = [n ** 2 for n in sizes]
N_exp = [math.e ** n for n in sizes]
# Gamma(n) = (n-1)!; math.gamma()
# Gamma(n + 1) = (n)!;
N_fac = [math.gamma(n+1) for n in sizes]


plt.plot(sizes, constant, label='Constant')
plt.plot(sizes, logN, label='logN')
plt.plot(sizes, NlogN, label='NlogN')
plt.plot(sizes, sizes, label='linear')
plt.plot(sizes, N_square, label='N^2')
plt.plot(sizes, N_exp, label='exp')
plt.plot(sizes, N_fac, label='N!')
plt.xlabel('Size')
plt.ylabel('TIME')
plt.legend()

""" 
# sizes = [*range(1,5)]# X  list(range(1,5))
sizes = [x/100 for x in range(1, 400)]
constant = [1 for values in sizes] #Y 
# print(math.log(10))
logN = [math.log(n) for n in sizes]
NlogN = [n * math.log(n) for n in sizes]
N_square = [n ** 2 for n in sizes]
N_exp = [math.e ** n for n in sizes]
# Gamma(n) = (n-1)!; math.gamma()
# Gamma(n + 1) = (n)!;
N_fac = [math.gamma(n+1) for n in sizes]


plt.plot(sizes, constant, label='Constant')
plt.plot(sizes, logN, label='logN')
plt.plot(sizes, NlogN, label='NlogN')
plt.plot(sizes, sizes, label='linear')
plt.plot(sizes, N_square, label='N^2')
plt.plot(sizes, N_exp, label='exp')
plt.plot(sizes, N_fac, label='N!')
plt.xlabel('Size')
plt.ylabel('TIME')

plt.legend() """

""" import time
        
# decorator to measure the time of our binary-search algorithm
def decorator_factory(cycles=3):
    def aver_clock(func):
        def inner(*x):
            results = []
            for i in range(cycles):
                t0 = time.perf_counter()
                func(*x)
                elapsed = time.perf_counter() - t0
                results.append(elapsed)
            return sum(results)/cycles  # average time of how long my func takes
        return inner
    return aver_clock

@decorator_factory()
def binary_search(x, num):
    while True:
        middle = len(x) // 2
        if x[middle] > num:
            x = x[:middle]
        elif x[middle] < num:
            x = x[middle + 1:]
        else:
            return x[middle]


binary_search(range(1,11), 1)

def plot(X, Y, label):
    plt.plot(X, Y, label=label)
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


def measure(upper_num=5):
    X = [10 ** n for n in range(1, upper_num)]
    Y=[]
    for size in X:
        sized_range = range(1, size)
        result_in_sec = binary_search(sized_range, 1)
        Y.append(result_in_sec)
    plot(X,Y, 'binary_search O(logN)')

measure(6) """


# Task 0
""" import random


def generate_number(N):
    x = random.choice(range(1,N+1))
    return x


if __name__ == "__main__":
    print(generate_number(10))
    print(generate_number(100))
    print(generate_number(1000))
    print(generate_number(10000))
    print(generate_number(100000))
    print(generate_number(1000000))
    print(generate_number(10000000))

print()
# Task 1
def guess_number_linear(N, verbose=True):
    secret_num = generate_number(1000)
    
    for i in guess_number_linear:
        if verbose == True:
            print(f'secr num {secret_num}')
        else:
            pass


if __name__ == "__main__":
    guess_number_linear(1000)

print() """
# Task 2
