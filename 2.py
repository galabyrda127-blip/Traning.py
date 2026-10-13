x = int(input("число 1:"))
y = int(input("число 2 :"))
def max(a, b):
    if a > b:
        return a
    else:
        return b
tob = "наибльшее"
print(tob, max(x,y))



v =str(input("Веедите текст на англиском:"))
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for c in s:
        if c in vowels:
            count += 1

    return count


label = "Кол-во гласных:"


print(label, count_vowels(v))

