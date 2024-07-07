n = 2520
ans = -1
while ans == -1:
    for i in range(11, 21):
        if n % i != 0:
            break
        i += 1
        if i == 21:
            ans = n
            print(n)

    n += 20
