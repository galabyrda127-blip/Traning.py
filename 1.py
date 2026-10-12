x = int(input())
y = range(1,x+1)
sum = 0
l = 0
for i in y:
    if i  == 17:
        break
    if  i % 2 == 0:
        continue
    sum += i
    l += 1
    if  (i > 10 and i < 12):
        print("вы уже дошли по циклу до 11")
        sum += i

    print(len(range(i)))
print("колво", l)
print(f"сумма {sum}")
