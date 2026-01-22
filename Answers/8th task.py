#Task H. Trains?

n = int(input())
trains = []

for i in range(n):
    description = input().strip()
    details = description.split()
    
    if len(details) <2 or "at" not in details:
        t_name = ""
        time_mins = -1
    else:
        t_name = details[0]
        dep_time = details[-1]
        hh,mm = map(int, dep_time.split(":"))
        time_mins =hh*60 + mm
    
    trains.append([t_name,time_mins,i,description])

for i in range(n):
    min_idx = i 
    for j in range(i + 1, n):
        if trains[j][0] < trains[min_idx][0]:
            min_idx = j
        elif trains[j][0] == trains[min_idx][0]:
            if trains[j][1] > trains[min_idx][1]:
                min_idx = j
            elif trains[j][1] == trains[min_idx][1]:
                if trains[j][2] < trains[min_idx][2]:
                    min_idx = j 
    trains[i], trains[min_idx] = trains[min_idx],trains[i]
for i in trains:
    print(i[3])        