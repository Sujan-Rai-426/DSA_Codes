
# Leetcode Problem No:- 344. Reverse String

# Reverse the given string

def Reverse_String(strs):
    strs=list(strs)
    l , r = 0 , len(strs)-1 
    while l<=r:
        hold = strs[l]
        strs[l] = strs[r]
        strs[r] = hold
        l+=1
        r-=1
    return strs

input_strs = input("Enter any strings or number : ")
print("Reversed String is : ", Reverse_String(input_strs))