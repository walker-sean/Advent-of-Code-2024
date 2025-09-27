list_1 = []
list_2_counts = {}

with open('input', 'r') as input:
    lines = input.readlines()
    
    for line in lines:
        [num1, num2] = map(int, line.split('   '))
        list_1.append(num1)
        list_2_counts[num2] = 1 if num2 not in list_2_counts else list_2_counts[num2] + 1
    
    similarity_score = 0
    
    for num in list_1:
        similarity_score += num * (list_2_counts[num] if num in list_2_counts else 0)
    
    print(similarity_score)
        