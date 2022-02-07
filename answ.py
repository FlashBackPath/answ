import pandas as pd
import numpy as np

df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
#Первое решение
l1 = []
l2 = []
l3 = []
for i in df.values:
    if i[0] == 'a':
        l1.append(i[-1])
    elif i[0] == 'b':
        l2.append(i[-1])
    else:
        l3.append(i[-1])
a_sum = 0
b_sum = 0
c_sum = 0

for i in range(3):
    a_sum += max(l1)
    l1.remove(max(l1))

    b_sum += max(l2)
    l2.remove(max(l2))

    c_sum += max(l3)
    l3.remove(max(l3))
print(a_sum, b_sum, c_sum)

#Второе решение
df.sort_values('vals',ascending=False, inplace=True)
df.sort_values('grps', inplace=True)
xl = df.vals.values

res = []
for i in range(len(xl)-1):
    t = 0
    if xl[i] < xl[i+1]:

        t += xl[i+1] + xl[i+2] + xl[i+3]
        res.append(t)
    elif i == 0:
        t += xl[i] + xl[i + 1] + xl[i + 2]
        res.append(t)

groups = df.grps.unique()
for i in range(len(res)):
    print(f'Сумма 3 наибольших значений в группе {groups[i]} = {res[i]}')