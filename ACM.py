def contest_ranking():
    problems = {}  
    penalties = {} 

    while True:
        log = input().strip()
        if log == "-1":  
            break

        m, p, result = log.split()
        m = int(m)

        if p not in problems:  
            problems[p] = None
            penalties[p] = 0

        if result == "wrong" and problems[p] is None:
            penalties[p] += 1  
        
        elif result == "right" and problems[p] is None:
            problems[p] = m  
    solved_problems = 0
    total_time = 0

    for p, time in problems.items():
        if time is not None:
            solved_problems += 1
            total_time += time + (penalties[p] * 20)
    print(solved_problems, total_time)
contest_ranking()
