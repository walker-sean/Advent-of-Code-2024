import heapq

heap1, heap2 = [], []

with open('input', 'r') as input:
    lines = input.readlines()

    
    for line in lines:
        [num1, num2] = map(lambda n : int(n.strip()), line.split('   '))
        heapq.heappush(heap1, num1)
        heapq.heappush(heap2, num2)

sum = 0

while len(heap1):
    num1, num2 = heapq.heappop(heap1), heapq.heappop(heap2)
    sum += abs(num1 - num2)

print(sum)
        