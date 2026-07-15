# CREATING A CALCULATOR USING FUCTIONS

#while True:
print("\n--- WELCOME TO MY FUNCTIONS CALCULATOR ---")
print("1.ADDITION")
print("2.MULTIPLICATION")
print("3.SUBTRACTION")
print("4.DIVISION")
      
first_number = int(input("ENTER YOUR FIRST NUMBER: "))
second_number = int(input("ENTER YOUR SECOND NUMBER: "))

choice = int(input("ENTER YOUR NUMBER OF OPERATOR: "))
    
if choice == 1 :
        def my_add(*args):
             for i in args:
                 sum = first_number + second_number
                 print(f"Your sum is: {sum}")
                #  print("Your sum is:",sum)
                 return sum
        my_add(first_number)

elif choice == 2 :
     	def my_mult(*args) :
             for i in args :
                 multiplication = first_number * second_number
                 print(f"Your product is: {multiplication}")
                #  print("Your product is:",multiplication)
                 return multiplication
             my_mult(first_number)

elif choice == 3 :
        def my_sub(*args) :
             for i in args :
                 subtraction = first_number - second_number
                 print(f"Your difference is: {subtraction}")
                #  print("Your difference is:",subtraction)
                 return subtraction
        my_sub(first_number)
             
elif choice == 4 :
        def my_div(*args) :
             for i in args :
                 division = first_number / second_number
                 print(f"Your result is: {division}")
                #  print("Your result is:",division)
                 return division
        my_div(first_number)

else :
        print("Invalid choice")
        