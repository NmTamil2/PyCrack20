def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Create the input list
s = ["h", "e", "l", "l", "o"]

# Print the original list
print("Original list:", s)

# Reverse the list
reverseString(s)

# Print the reversed list
print("Reversed list:", s)
