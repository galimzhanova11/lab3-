def my_function(fun):
   return (5 / 9 * (fun - 32))

fun=int(input())
centigrade=my_function(fun)
print ("{0} fahrenheit is {1} centigrade".format(fun, centigrade ))