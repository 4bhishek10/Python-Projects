n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
    
    
#1. User must first enter the value of the integer and store it in a variable.
#2. The value of the integer is then stored in another temporary variable.
#3. The while loop is used and the last digit of the number is obtained by using the modulus operator.
#4. The last digit is then stored at the one’s place, second last at the ten’s place and so on.
#5. The last digit is then removed by truly dividing the number with 10.
#6. This loop terminates when the value of the number is 0.
#7. The reverse of the number is then compared with the integer value stored in the temporary variable.
#8. If both are equal, the number is a palindrome.
#9. If both aren’t equal, the number isn’t a palindrome.
#10. The final result is then printed.