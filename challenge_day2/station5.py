def solution_station_5(student):
    team = None
    
    lt_1 = ["tiara","ebony","nandini","nathan","ben","muni","lula","tobit","zoe","klemtanyna", "julia",]
    lt_2 = ["bill","pol"]
    lt_3 = ["mac","flax"]

    if student in lt_1:
        team = 1
    elif student in lt_2:
        team = 2
    elif student in lt_3:
        team = 3
    else:
        team = 4
        
    
    return print(team)


solution_station_5("noah")