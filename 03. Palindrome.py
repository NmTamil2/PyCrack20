lst = ['eve','i used', 'used', 'to', 'play', 'cricket', 'asper', 'madam','instruction']

palindrome =[]
for i in lst:
    if i == i[::-1]:
        palindrome.append(i)
print(palindrome)
        
