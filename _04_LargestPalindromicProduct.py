import math

n1 = 999
n2 = 999


def isPalindromic(n):
    s = ""
    while n > 0:
        s += str(n % 10)
        n = math.floor(n / 10)

    i1 = 0
    j1 = len(s) - 1

    while i1 < j1:
        if s[i1] != s[j1]:
            return False
        i1 += 1
        j1 -= 1

    return True


ans = 0
for i in range(100, n1):
    for j in range(100, n2):
        temp = i * j
        if isPalindromic(temp):
            ans = max(temp, ans)

print(ans)
