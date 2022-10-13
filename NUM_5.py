import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def vector(x,y,len,n):
    arr = [None]*n
    arr[0] = Sum(y,len)
    for i in range(1,n):
        arr[i] = arr[i-1]*Sum(np.power(x,i),len)
    return arr


def Sum(arr,n):
    sum = 0
    for i in range(1,n):
        sum+=arr[i]
    return sum


def matrix(x,n,len):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            degree = abs(n+1 - (i+j))
            matrix[i][j] = Sum(np.power(x,degree),len)
    return matrix


def point(func, point):
    return np.polyval(func, point)


def plot(y,x):
    XNEW = np.linspace(np.min(x), np.max(x), 100)
    YNEW1 = point(y, XNEW)
    plt.plot(XNEW, YNEW1)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    x = [None] * 6
    y = [None] * 6
    x = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    y = [-0.5, 0.0, 0.5, 0.86603, 1.0, 0.86603]
    f1 = np.linalg.solve(matrix(x,2,6),vector(x,y,6,2))
    f2 = np.linalg.solve(matrix(x,3,6),vector(x,y,6,3))
    f3 = np.linalg.solve(matrix(x,4,6),vector(x,y,6,4))
    print("Многочлен 1-ой степени:",f1[0],"*x +",f1[1])
    print("Многочлен 2-ой степени:", f2[0], "*x^2 +", f2[1],"*x +",f2[2])
    print("Многочлен 3-ей степени:", f3[0], "*x^3 +", f3[1],"*x^2 +",f3[2],"*x +",f3[3])
    plt.title("Многочлен 1-ой степени:")
    plot(f1,x)
    plt.title("Многочлен 2-ой степени:")
    plot(f2, x)
    plt.title("Многочлен 3-ей степени:")
    plot(f3, x)
