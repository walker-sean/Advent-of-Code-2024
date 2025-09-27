with open('input.txt', 'r') as input:
    reports = input.readlines()
    
    safe_reports = 0
    
    for report in reports:
        levels = list(map(int, report.split(' ')))
        
        increasing = levels[1] > levels[0]
        safe = True
        
        for i, level in enumerate(levels[:-1]):
            next_level = levels[i + 1]
            
            if level == next_level:
                safe = False
                break
            elif level < next_level:
                if not increasing or next_level - level > 3:
                    safe = False
                    break
            else:
                if increasing or level - next_level > 3:
                    safe = False
                    break
        
        if safe:
            safe_reports += 1
    
    print(safe_reports)
    