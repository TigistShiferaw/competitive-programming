 numSwap=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                numSwap += 1
               
               
    firstElement = a[0]
    lastElement =  a[-1]
    print("%s%d%s" % ("Array is sorted in
 ", numSwap," swaps." ))              
    print("%s%d" % ("First Element: ", firstElement ))            
    print("%s%d" % ("Last Element: ", lastElement ))  