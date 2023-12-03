


def solve(input):
    l = []
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for idx, i in enumerate(input):
        if i <= '9' and i >= '0':
            l.append((i, idx))
        if idx >= 5:
            for digit_idx ,digit in enumerate(digits):
                res_idx = input[idx-5:idx].find(digit)
                if res_idx != -1:
                    l.append((str(digit_idx), res_idx + idx - 5))
                    break

        l = sorted(l, key=lambda x: x[1])
                
    #print(l)         
                
    
    res = ""
    if len(l) == 1:
        res += l[0][0]
        res += l[0][0]
    else:
        res += l[0][0]
        res += l[-1][0]
    
    return int(res)
        
        

if __name__ == "__main__":
    sum = 0
    with open("input", "r") as f:
        for line in f:
            #print(solve(line))
            sum += solve(line)
    print(sum)
    