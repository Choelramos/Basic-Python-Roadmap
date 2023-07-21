"""This way the function woll receive a tuple of arguments, and can access the items accordingly"""


def myfunction(*name):
    print("The name is " + name[1])


myfunction("Jo", "Ju", "Ma")


"""Arbitrary Keyword Arguments, **kwargs
The way the function will receive a dictionary of arguments,
and can access the items accordingly:"""


def my_other_functio(**name):
    print("Hes first name is: " + name["first"])


my_other_functio(name="Ju Ju", first="Ju")


"""Default parameter Value
If we call the function without argument, it uses the default value"""


def another_function(country="Brasil"):
    print("I am from " + country)


another_function()
another_function("Japan")


"""A sample list of arguments"""


def function_list(food):
    for x in food:
        print(x)


fruits = ["Banana", "Aple", "Orange"]
function_list(fruits)

"""Using the return value"""


def return_values(x):
    return 5 ** 2 + x


print(return_values(2))
print()

"""Recursion.
Recursion is a common mathematical and programming concept. It means that a functin calls itself.
This has the benefit of meaning that you can loop through data to reach a result.
I trying to understand how its works writing various exemples bellow"""


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


houses = ["Joel's house", "Julia's houses", "Matias's houses"]


def deliver_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to", house)
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)


deliver_presents_recursively(houses)


"Recursive function implemented in Python for calcula n!"


def recursion(n):
    # case: 1! = 1
    if n == 1:
        return n
    # n * (n - 1)!
    else:
        return n * recursion(n - 1)


print(recursion(5))
