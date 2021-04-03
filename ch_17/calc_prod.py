import time

def calcProd():
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

start_time = time.time()
prod = calcProd()
end_time = time.time()

print('The results is %s digits long.' % len(str(prod)))
print('Took %s seconds to calculate' % round(end_time - start_time, 3))