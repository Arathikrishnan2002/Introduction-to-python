def hey():
  print("HEllO WORLD")
 
hey()

#argument passing
def one(name,age):
  print("My name is "+name+ " and age is "+str(age))
 
def two():
  print("hello")
 
value = "Ajith"
two()
one(value,1)

#more 

def hello():
    print("hello")

def hai(*values):
    print("First"+values[0]+"Second"+values[1])
    
hello()
hai("ANJU","AKKU")
