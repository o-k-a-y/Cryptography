def discrete_logs(b, y, p):
    disc_logs = []
    for i in range(1, p):
        print(i)
        memes = (b^i)
        if memes % y == p:
            disc_logs.append(i)
    return disc_logs



#log base b of y
b = int(input("Enter base: "))
y = int(input("Enter y: "))
p = int(input("Enter mod: "))

logs = discrete_logs(b, y, p)
print(logs)