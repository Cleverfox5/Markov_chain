from decimal import Decimal, getcontext

getcontext().prec = 28

a_i = [
    Decimal('0.263'),
    Decimal('0.263'),
    Decimal('0.2105'),
    Decimal('0.2105'),
    Decimal('0.053')
]

t_i = [
    Decimal('0.2'),
    Decimal('0.25'),
    Decimal('0.3'),
    Decimal('0.32'),
    Decimal('0.4')
]

k_i = [
    Decimal('4'),
    Decimal('12'),
    Decimal('15'),
    Decimal('12'),
    Decimal('6')
]

j =  Decimal('1')

l_pre_i = [
    Decimal('0'),
    Decimal('0'),
    Decimal('0'),
    Decimal('0'),
    Decimal('0')
]

h_pre = Decimal('0')
t_pr = Decimal('0')
rate = Decimal('0')

t_pr_i = list()

while(rate <= Decimal('0.9')):
    print(f"j = {j}; l_pre = {l_pre_i[0]}; {l_pre_i[1]}; {l_pre_i[2]}; {l_pre_i[3]}; {l_pre_i[4]}; h_pre = {h_pre}")
    t_pr_i = list()

    for i in range(0, 5):
        value = t_i[i] * (1 + (l_pre_i[i] / k_i[i]))
        t_pr_i.append(value)

    #for i in range(0, 5):
    #    print(f"t_pr_{i + 1} = {t_pr_i[i]}")

    t_pr = Decimal('0')
    for i in range(0, 5):
        t_pr += a_i[i] * t_pr_i[i]

    #print(f"t_pr = {t_pr}")


    h = j / t_pr
    #print(f"throughput capacity = {h}")


    l_i = list()

    for i in range(0, 5):
        value = h * a_i[i] * t_pr_i[i]
        l_i.append(value)

    #for i in range(0, 5):
    #    print(f"l_{i+1} = {l_i[i]}")

    rate = h_pre / h


    #print(f"rate = {rate}")


    h_pre = h
    l_pre_i = l_i.copy()
    j += 1

print(f"\nk = [{k_i[0]}, {k_i[1]}, {k_i[2]}, {k_i[3]}, {k_i[4]}]\n")

for i in range(0, 5):
    print(f"t_pr_{i + 1} = {t_pr_i[i]}   ({t_pr_i[i] - t_i[i]})")

print("\n")

for i in range(0, 5):
    print(f"l_{i+1} = {l_pre_i[i]}")

if (t_pr < Decimal("0.325")):
    print("YES")

print(f"\n {t_pr}")
