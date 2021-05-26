# 시간초과 코드
# 저는 C++로 비슷한 알고리즘 써 풀긴 했는데 Python으로 더 나은 알고리즘을 모르겠어서 PR넣어주세여

from sys import stdout


def b(x, y, z):
    if (x // z) % 3 == 1 and (y // z) % 3 == 1:
        stdout.write(" ")
    else:
        if not z // 3:
            stdout.write("*")
        else:
            b(x, y, z // 3)


a = int(input())
for i in range(a):
    for j in range(a):
        b(i, j, a)
    stdout.write("\n")
