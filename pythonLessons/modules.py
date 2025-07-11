# module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# import math
# import math as m
# from math import pi
import moduleExample
# print(help("modules"))


# print(math.pi)
# print(m.pi)
# print(pi)

result = moduleExample.pi
result = moduleExample.square(3)
result = moduleExample.cube(3)
result = moduleExample.circumference(3)
result = moduleExample.area(3)

print(result)
