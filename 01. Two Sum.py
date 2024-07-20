numbers = [2, 4, 7, 5]
target = 11
result = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            result.append((i, j))

print(result)

        
    
    
    
