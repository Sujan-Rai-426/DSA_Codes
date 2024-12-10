

# Leetcode Problem No:- 9. Palindrome Number

#  Checkout if the number is valid palindrome or not 

# Time Complexity: O(n) — Where n is number input digits,      ---->linear time to check the number.
# Space Complexity: O(1) — constant space usage, aside from the input string.

def Is_Palindrome_Number(num):
    l, r = 0, len(num)-1
    while l<r:
        if num[l] != num[r]:
            return False
        l+=1
        r-=1
    return True
    
input_num = input("Enter the number:")
print("Given number is Palindrome =>",Is_Palindrome_Number(input_num))