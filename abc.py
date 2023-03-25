n = [2,5,13,7,6,4]
size = 6
index = 0
max_idx = 0
max = n[max_idx]



while index < size:
    if n[index] > max:
        max_idx = index
        max = n[index]
    index= index +1
n[max_idx] = n[size-1]
n[size-1]=max
print(n)
