#ex1
def fibunocci_generator():
    x=1
    y=1
    yield 1
    yield 1
    while True:
        yield x+y
        z=x+y
        x=y
        y=z

gen=fibunocci_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#ex2
def unique_letters_generator(args):
    index=0
    # set(args)
    while index<len(args):
        yield set(args[index])
        index+=1

list=['ayala','dvora','lali','adasa']
leters=unique_letters_generator(list)
print(next(leters))
