def solution(n):
    answer = 0
    n_length = bin(n).count('1')
    
    for i in range(n+1, 1000001):   #n부터 1,000,000 값에 대하여
        if bin(i).count('1') == n_length:
            answer = i
            break
            
    return answer