def Checkprime(Num):
    count = 0
    for i in range (1, Num+ 1):
        if Num % i == 0:
            count = count + 1
    
    if count == 2:
        return True
    else:
        return False


