from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import numpy as np


getcontext().prec = 28


#генератор
class little_frog_gen:
    def __init__(self, first=Decimal('1'), r=Decimal('32'), M=Decimal('1234567891'), m=100):
        self.A = first
        self.r = r
        self.mod = Decimal('2') ** r
        self.M = pow(M, m, self.mod)
        self.m = m

    def next(self):
        self.A = (self.M * self.A) % self.mod
        return self.A / self.mod

generator = little_frog_gen()

#количество итераций
n = 500000

selection = [generator.next() for _ in range(n)]

##########
#Рассчёт математического ожидания и Дисперсии


#математическое ожидание
math_expect = sum(selection) / n
exp_math_expect = Decimal('0.5')

#Дисперсия
dispersion = sum((x - math_expect) * (x + math_expect) for x in selection) / n
exp_dispersion = Decimal('1') / Decimal('12')

print(f"Вычисленное M: {math_expect}")
print(f"Теоретическое M: {exp_math_expect}")
print(f"Погрешность M: {(abs(exp_math_expect - math_expect) / exp_math_expect  * 100):.2f}%")
print(f"Вычисленная D: {dispersion}")
print(f"Теоретическое D: {exp_dispersion}")
print(f"Погрешность D: {(abs(exp_dispersion - dispersion) / exp_dispersion * 100):.2f}%")

k = 10

#гистограмма для нашей выборки:
plt.hist(selection, bins=k, range=(0, 1), edgecolor='black', rwidth=0.8, alpha=0.7)
plt.title('Гистограмма распределения случайных величин')
plt.xlabel('Интервалы')
plt.ylabel('Относительная частота')
plt.grid(True)

#линия показывающая уровень теоритичесокй частоты
plt.axhline(y=50000.0, color='red', linestyle='--', label='Теоретическая частота (50000)')
plt.legend()
plt.show()

##########
#oценка независимости
def calculate_correlation(sequence, s, n):
    sum_product = 0
    for i in range(n-s):
        sum_product += sequence[i] * sequence[i + s]

    R = Decimal('12') / (n - s) * sum_product - Decimal('3')
    return R

step = [2, 5, 10]

#от 100 до 100000 - 100 занчений
sample_n = np.linspace(100, 500000, 100, dtype=int)

plt.figure()

for s in step:
    R_values = []
    for n in sample_n:
        #на большой последовательности тестируем все n
        R = calculate_correlation(selection, s, n)
        R_values.append(R)
    
    plt.plot(sample_n, R_values, label=f's = {s}')

plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
plt.title('Зависимость коэффициента корреляции R от размера выборки n')
plt.xlabel('Размер выборки (n)')
plt.ylabel('Коэффициент корреляции (R)')
plt.legend()
plt.grid(True)
plt.show()
