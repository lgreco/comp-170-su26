""" Here's what I'd like to draw:

         *
        ***
       *****
      *******
     *********
     *********
      *******
       *****
        ***
         *

or 

   *
   *
   **
   ***
   ****
   *****
   ******
   *******
   *
******************
 ****************
   *************
~~~~~~~~~~~~~~~~~~~~

"""


# Naive way to print a triangle

print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

""" Recipe for a triangle with X lines

start with line 1, print 1 star
  increase lines and stars until X
"""

symbol = "*"
print(symbol*1)
print(symbol*2)
print(symbol*3)
print(symbol*4)

X = 10
for i in range(X):
  print(symbol*i)
