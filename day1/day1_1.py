
def solve(input):
    l = []
    for i in input:
        if i <= '9' and i >= '0':
            l.append(i)
    
    res = ""
    if len(l) == 1:
        res += l[0]
        res += l[0]
    else:
        res += l[0]
        res += l[-1]
    return int(res)
        
        

if __name__ == "__main__":
    sum = 0
    with open("input", "r") as f:
        for line in f:
            sum += solve(line)
    print(sum)
    