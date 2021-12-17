def countingValleys(steps, path):
    # Write your code here
    level=0
    s=[]
    valley=0
    for i in path:
        if i=="D":
            level-=1
            s.append(level)
        else:
            level+=1
    for i in range(len(s)):
        if s[i]==-1:
            valley+=1
    return valley    