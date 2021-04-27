###############################################
# Как работает изменение <Y>, по измененным <X>
###############################################

# произвольная функция
def func(x1, x2):
    return x1*2 + x2**2

# производная от функции def func() по x1
def func_x1(x1, x2):
    return 2

# производная от функции def func() по x2
def func_x2(x1, x2):
    return 2*x2

x1 = 2
x2 = 5
print(func(x1, x2))

# значения изменились на..
dx1 = 0.1
dx2 = 0.2

# градиент, показывает на сколько изменится <Y> если изменится X1, X2
# формула градиента работает только при малых изменениях входных [x1, x2]
# может работать для многих входных X
# формула показывает изменения по 2ум частным производным одновременно, а частная производная
# показывает изменения Y только по одной величине
dy = func_x1(x1, x2) * dx1 + func_x2(x1, x2) * dx2
print(dy)

# как будет меняться Y, при изменениях X
# в нейронных мы должны понять наоборот как изменятся X1 и X2, когда мы получили такой Y
new_x1 = x1+dx1
new_x2 = x2+dx2

# изменение искомой величины -> Y
new_y = func(new_x1, new_x2)
print(new_y)