word = (input("Enter a word : "))

reverseWord= ""   
count = len(word) 

while count > 0:   
    reverseWord = reverseWord + word[ count - 1 ]   
    count = count - 1  
    
    
print("Reversed word : ",reverseWord)