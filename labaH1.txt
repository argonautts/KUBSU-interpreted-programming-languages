from collections import defaultdict, Counter

'''def isPalindrome(x: int) -> bool:
    if x < 0 or (
            x > 0 and x % 10 == 0):  # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
        return False

    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10
    return True if (x == result or x == result // 10) else False

print(isPalindrome(123321))'''

'''
Ввод : 313551
Вывод : 531135
Пояснения: 531135 — самое большое число.
который представляет собой палиндром, 135531, 315513 и другие
числа также могут быть сформированы, но нам нужны самые высокие
всех палиндромов. 

Ввод : 331
Вывод : 313

Ввод : 3444
Вывод : Палиндром не может быть сформирован 
'''

# Функция для проверки того, можно ли переставить число
# чтобы сформировать число-палиндром
def possibility(m, length, s):
    # счетчик появление нечетного числа
    countodd = 0
    for i in range(0, length):

        # если вхождение нечетное
        if m[int(s[i])] & 1:
            countodd += 1

        # если число больше 1
        if countodd > 1:
            return False

    return True


# Функция для печати наибольшего палиндромного числа
# путем перестановки цифр числа
def largestPalindrome(s):
    # длина строки
    l = len(s)

    # map который отмечает вхождение числа
    m = defaultdict(lambda: 0)
    for i in range(0, l):
        m[int(s[i])] += 1

    # проверить возможность
    # существования палиндромного числа
    if possibility(m, l, s) == False:
        print("Палиндром не может быть сформирован")
        return

    # строковый массив, в котором хранится
    # наибольшее переставленное палиндромное число
    largest = [None] * l

    # указатель спереди
    front = 0

    # начниаем с 9 до 0 и помещаем
    # большее число впереди, а нечетное посередине
    for i in range(9, -1, -1):

        # если вхождение числа нечетное
        if m[i] & 1:

            # поместите одно нечетное число в середину
            largest[l // 2] = chr(i + 48)

            # уменьшаем map
            m[i] -= 1

            # расставляем остальные числа
            while m[i] > 0:
                largest[front] = chr(i + 48)
                largest[l - front - 1] = chr(i + 48)
                m[i] -= 2
                front += 1

        else:

            # если все числа встречаются четное количество раз
            while m[i] > 0:
                # переставляем front
                largest[front] = chr(i + 48)
                largest[l - front - 1] = chr(i + 48)

                # 2 числа размещены,
                # поэтому уменьшиаем map
                m[i] -= 2

                # повысить позицию
                front += 1

    # выводим самую большую строку, сформированную таким образом
    for i in range(0, l):
        print(largest[i], end="")


# Driver Code
if __name__ == "__main__":
    input = input()
    largestPalindrome(input)
# Временная сложность: O(N), так как мы используем цикл для прохождения N раз.