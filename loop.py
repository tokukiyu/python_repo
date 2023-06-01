def function(x,y, *args):
    b=args[0]
    c=args[1]
    z=min(x,y)
    return x*2,x*y, x//y,c,b

print(function(12,3,1,2,3,4,5))