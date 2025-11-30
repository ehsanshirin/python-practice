class test:
    pass

t1 = test()
t2 = test()

t1.x = 5
print(hasattr(t2,'x'))