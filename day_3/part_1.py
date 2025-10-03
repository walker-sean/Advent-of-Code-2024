import re

with open('input.txt', 'r') as input_file:
    sum = 0
    
    mul_command = re.compile(r"mul\(([0-9]+),([0-9]+)\)")
    input = input_file.read()
    matches = mul_command.findall(input)
    
    for match in matches:
        num1, num2 = match
        num1, num2 = int(num1), int(num2)
        
        sum += num1 * num2
    
    print(sum)
    