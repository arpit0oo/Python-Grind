text = "hello World"
dic = {}
for char in text:
    if char in dic: 
        dic[char] = dic[char] + 1  
    else:
        dic[char] = 1 
print(dic)
text = "hello"
freq = {}

for char in text:
    freq[char]=1
print(freq)
