import re

with open('input.txt', 'r') as input_file:
    sum = 0
    
    input = input_file.read()
    
    active = True
    
    commands = re.compile(r"mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))")
    
    input_commands = commands.findall(input)
    
    for input_command in input_commands:
        num1, num2, do, dont = input_command
        
        if do:
            active = True
            continue
        
        if dont:
            active = False
            continue
        
        if active:
            num1, num2 = int(num1), int(num2)
            sum += num1 * num2
    
    print(sum)