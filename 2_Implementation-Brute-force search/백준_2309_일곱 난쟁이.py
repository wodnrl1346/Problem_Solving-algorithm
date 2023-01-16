from itertools import permutations

# 입력의 개수
n = 9

dwarf = []

for i in range(n):
    dwarf.append(int(input()))

dwarf.sort()

# 아홉 난쟁이의 키는 모두 다르다는 조건에 의해 permutation으로 7개의 요소를 임의로 저장하여 tuple의 형태로 저장한다. 이것들을 list에 
comb = list(permutations(dwarf, 7))

comb_sum = 0

for tuple in comb:
    comb_sum = sum(tuple)
    if(comb_sum == 100):
        for i in range(len(tuple)):
            print(list(tuple)[i])
        break