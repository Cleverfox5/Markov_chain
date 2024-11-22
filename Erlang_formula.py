import numpy as np
import matplotlib.pyplot as plt

def E_i_i(i, A):
    if i == 0:
        return 1

    numerator = A * E_i_i(i - 1, A)
    return numerator / (i + numerator)

def E_second(V, A, v_arr=None):
    e_first = 0
    if v_arr == None:
        e_first = E_i_i(V, A)
    else:
        e_first = E_i_i(v_arr, A)

    denominator = 1 - A / V * (1 - e_first)

    return e_first / denominator

def middle_length_on_queue(V, A, v_arr=None):
    if v_arr == None:
        e_first = E_i_i(V, A)
    else:
        e_first = E_i_i(v_arr, A)

    numerator = A * e_first * V
    denominator = (V - A) + A * e_first * (V - A)

    return numerator / denominator

def unit_1_2(length, split_into, V):
    A = np.linspace(0, length, split_into)
    y = E_i_i(V, A)

    plt.plot(A, y, color='blue')
    plt.xlabel("Интенсивность поступающей нагрузки")
    plt.ylabel("Вероятность блокировки заявок")
    plt.title(f"Первая формула Эрланга для V = {V}")
    plt.grid()

    plt.show()

def unit_1_3(length, split_into, A):
    V = np.linspace(0, length, split_into, dtype=int)
    y = [E_i_i(i, A) for i in V]

    plt.plot(V, y, color='blue')
    plt.xlabel("число обслуживающих устройств")
    plt.ylabel("Вероятность блокировки заявок")
    plt.title(f"Первая формула Эрланга для A = {A}")
    plt.grid()

    plt.show()

def unit_2_2_1(start, finish, split_into, V):
    A = np.linspace(start, finish, split_into)
    y = E_second(V, A)

    plt.plot(A, y, color='blue')
    plt.xlabel("интенсивности поступающей нагрузки")
    plt.ylabel("Вероятность ожидания начала обслуживания")
    plt.title(f"Вторая формула Эрланга для V = {V}")
    plt.grid()

    plt.show()

def unit_2_2_2(start, finish, split_into, V):
    A = np.linspace(start, finish, split_into)
    y = middle_length_on_queue(V, A)

    plt.plot(A, y, color='blue')
    plt.xlabel("интенсивности поступающей нагрузки")
    plt.ylabel("средняя длина очереди")
    plt.title(f"Средняя длина очереди для V = {V}")
    plt.grid()

    plt.show()

def unit_2_3_1(start, finish, split_into, A):
    V = np.linspace(start, finish, split_into, dtype=int)
    y = [E_second(i, A) for i in V]

    plt.plot(V, y, color='blue')
    plt.xlabel("число обслуживающих устройств")
    plt.ylabel("Вероятность ожидания начала обслуживания")
    plt.title(f"Вторая формула Эрланга для A = {A}")
    plt.grid()

    plt.show()

def unit_2_3_2(start, finish, split_into, A):
    V = np.linspace(start, finish, split_into, dtype=int)
    y = [middle_length_on_queue(i, A) for i in V]

    plt.plot(V, y, color='blue')
    plt.xlabel("число обслуживающих устройств")
    plt.ylabel("средняя длина очереди")
    plt.title(f"Средняя длина очереди для A = {A}")
    plt.grid()

    plt.show()

n = 96
V = 2 * n
unit_1_2(length=10000, split_into=500, V=V)

A = n
unit_1_3(length=150, split_into=150, A=A)

unit_2_2_1(start=100, finish=V, split_into=500, V=V)
unit_2_2_2(start=100, finish=V, split_into=500, V=V)

unit_2_3_1(start=n, finish=190, split_into=150, A=A)
unit_2_3_2(start=n, finish=190, split_into=150, A=A)