from typing import List

with open('input.txt', 'r') as input:
    safe_levels = 0
    reports = input.readlines()
    
    def unsafe_level_index(levels: List[int]):
        increasing = levels[1] > levels[0]
        
        for i, level in enumerate(levels[:-1]):
            next_level = levels[i + 1]
            
            if level == next_level:
                return i
            elif level < next_level:
                if not increasing or next_level - level > 3:
                    return i
            else:
                if increasing or level - next_level > 3:
                    return i
        return None
    
    def problem_dampener(report: str):
        global safe_levels
        levels = list(map(int, report.split(' ')))
        unsafe_index = unsafe_level_index(levels)
        
        if unsafe_index is None:
            safe_levels += 1
            return
        
        unsafe_level_index(levels[:unsafe_index] + levels[unsafe_index + 1:])
        
        if unsafe_level_index(levels[:unsafe_index] + levels[unsafe_index + 1:]) is None:
            safe_levels += 1
            return
        
        if unsafe_level_index(levels[:unsafe_index + 1] + levels[unsafe_index + 2:]) is None:
            safe_levels += 1
            return
        
        if unsafe_level_index(levels[1:]) is None:
            safe_levels += 1
    
    for report in reports:
        problem_dampener(report)
        
    print(safe_levels)