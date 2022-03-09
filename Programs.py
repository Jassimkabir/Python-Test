import string

#Count
def count(s):
    d = {}
    for i in s: 
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d            

#Panagram
def panagram(s):
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True

#Average
def average(s):
    sum=0
    if len(s) == 0:
        return None
    for i in s:
        sum= sum+i
    return sum/len(s)    
    