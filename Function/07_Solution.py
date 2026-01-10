def Sum_all (* args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)
print(Sum_all(1,2,3))