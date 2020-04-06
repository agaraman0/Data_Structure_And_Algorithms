def subse(string,current,index,n):
    if index == n:
        print(current)
        return;
    else:
        subse(string,current+string[index],index+1,n) #pick element and add it to output string that is current
        subse(string,current,index+1,n) #don't pick 

if __name__ == "__main__": 
    subse('abc','',0,3)
