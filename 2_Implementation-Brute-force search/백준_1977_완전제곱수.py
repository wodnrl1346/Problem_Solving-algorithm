m = int(input())
n = int(input())

total = 0
perfect_square_list = list()

for i in range(1, 101):
    perfect_square = i ** 2
    if m <= perfect_square <= n:
        perfect_square_list.append(perfect_square)

if(perfect_square_list == []):
    print(-1)

else:
    print(sum(perfect_square_list))
    print(min(perfect_square_list))