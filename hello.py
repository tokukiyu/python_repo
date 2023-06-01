from loop import function
def functin(x,y, *args):
    b=args[0]
    c=args[1]
    z=min(x,y)
    return x*2, x//y,c,b

if __name__=='__main__':
    print(function(2, 3, 4, 1, 2, 4))
else:
    print(functin(2, 3, 4, 1, 2, 4))