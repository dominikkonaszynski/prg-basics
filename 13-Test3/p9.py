def f(x,y,d):
    result = any(map(lambda num: d in str(num), range(x,y+1)))
    return result
        
print(f(10,15,"14"))
print(f(205,210,"04"))