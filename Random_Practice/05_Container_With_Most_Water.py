

# Leetcode Problem No:- 11. Container with most water  --> in 2 Dimension

# Example case:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The value are represented by array [1,8,6,2,5,4,8,3,7] is height of wall in sequential order and index represent length. In this max water is stored by container between the wall of height 8 and 7 at index 1 and 8 because it contain most area---> [8...Max Water...7].


# Time complexity: O(n) -> where n is the number of input height values in list/array
# Space Complexity: O(1)

def mostWater ( height ):
    
    maxArea = int()
    l, r = 0, len(height)-1
    
    while l<r:
        
        area = (r-1) * min(height[l], height[r])
        maxArea = max(area, maxArea)
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    
    return maxArea


input_string = input("Enter integers separated by spaces: ")

# Converting the input string into a list of integers
input_int = list(map(int, input_string.split()))
print("The integer array is:", mostWater(input_int))

