def call_back(num):
    if num == 0:
        return 1
    
    return num * call_back(num-1)

n = int(input())
print(call_back(n)) 
