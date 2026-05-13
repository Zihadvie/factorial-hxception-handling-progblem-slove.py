# Question 1 — Factorial + Exception Handling
#
# Take a number as input from the user.
#
# Rules:
#
# If the user enters a string → Invalid Input
#
# If the user enters a negative number → Factorial possible na
#
# Otherwise, calculate the factorial using a function.
#
# Display the final result in 2 lines:
#
# The factorial value.
#
# Whether the number is even or odd.
try :

        n = int(input())
        if (n > 0):
            for a in range(1, n + 1):

             r = 1
            for b in range(1, a + 1):
                r = r * b
            print("Factorial value : ", r)



            if r % 2 == 0:

                print("Number even")
            else:
                print("Number odd")
        else:
            print("Factorial possible na")
except Exception as e:
               print(e)

finally:
    print("wow")





