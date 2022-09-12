counter = 20

tens = []
vowels = []
while counter <= 70:
    if counter % 10 == 0 :
        tens.append(counter)
    c = chr(counter)
    #print(c)
    if c.lower() in ('a', 'e', 'i', 'o', 'u'):
        vowels.append(c)
    counter = counter + 1
    
print("Tens List : ",tens)
print("Vowels List : ",vowels)    