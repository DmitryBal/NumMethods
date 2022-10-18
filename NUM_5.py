import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def vector(x, y, n):
    arr = [None] * n
    for i in range(n):
        arr[i] = sum(np.power(x, i) * y)
    return arr


def matrix(x,y,n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = sum(np.power(x,i+j))
    return list(reversed(np.linalg.solve(matrix,vector(x,y,n))))


def point(func, point):
    return np.polyval(func, point)


def plot(f,x,y):
    XNEW = np.linspace(np.min(x), np.max(x), 100)
    YNEW1 = point(f, XNEW)
    plt.plot(XNEW, YNEW1)
    for i in range(6):
        plt.plot(x[i], y[i], 'ro')
    plt.grid(True)
    plt.show()


def mnk(x,y,f,len):
    p = [0]*len
    for i in range(len):
        p[i] = y[i] - point(f,x[i])
    return sum(np.power(p,2))


if __name__ == '__main__':
    x = [None] * 6
    y = [None] * 6
    x = [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0]
    y = [-0.5,0.0,0.5,0.86603,1.0,0.86603]
    f1 = matrix(x, y, 2)
    f2 = matrix(x, y, 3)
    f3 = matrix(x, y, 4)
    print("Многочлен 1-ой степени:",f1[0],"*x +",f1[1])
    print("Многочлен 2-ой степени:", f2[0], "*x^2 +", f2[1],"*x +",f2[2])
    print("Многочлен 3-ей степени:", f3[0], "*x^3 +", f3[1],"*x^2 +",f3[2],"*x +",f3[3])
    print("Квадратичное отклонение 1ой степени:", mnk(x, y, f1, 6))
    print("Квадратичное отклонение 2ой степени:", mnk(x, y, f2, 6))
    print("Квадратичное отклонение 3ей степени:", mnk(x, y, f3, 6))
    plt.title("Многочлен 1-ой степени:")
    plot(f1,x,y)
    plt.title("Многочлен 2-ой степени:")
    plot(f2,x,y)
    plt.title("Многочлен 3-ей степени:")
    plot(f3,x,y)
