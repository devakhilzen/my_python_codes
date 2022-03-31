def fib():
    x, y, z = 0, 1, ["0", "1"]
    for i in range(lim):
        z.append(str(x + y))
        x, y = y, x + y
        return ",".join(z[ : (len(z) - 2)])
print("Series are ", *fib(int(input("Enter Limit: "))), ".")


fib()
