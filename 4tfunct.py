# Below are four different codes which shows the examples of different types of functions
method=int(input("Enter corresponding number for if you want to execute the sum in the desired type\n 1- With arguments  with return\n 2- With arguments without return\n 3- Without arguments with return\n 4- Without argument without return\n    Type your option:  "))


if method == 1:
            # Example of with arguments  with return
            def sum(a,b):
                result=a+b
                return result
            answer=sum(10,10)
            print (f"The answer is {sum(10,10)}")
elif method == 2:
            # Example for with arguments without return
            def sum(a,b):
                result=a+b
                print("The answer is ",result)
            sum(10,10)
elif method == 3:
            # Example with without arguments with return
            a = 10
            b = 10
            def sum():
                result=a+b
                return result
            answer=sum()
            print ("The answer is "+str(answer))
elif method == 4:
            # Example without argument without return
            a=10
            b=10
            def sum():
                result=a+b
                print(f"The answer is {result}")
                
            sum()
else:
            print("You can select one of the given option only")
