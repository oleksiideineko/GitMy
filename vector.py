import vector
def size_vector(x):
    return len(x)
###def norma_vector(x):
    ###norma = 0
    ###for element in x:
        ###norma += element ** 2\
    ###return (norma ** 1/2)
def norma_vector(x):
    norma = sum ([element ** 2 for element in x])
    return norma ** 0,5

def skalar(x,y):
    try:
        assert size_vector(x) == size_vector(y), f"розмірності векторів {x} та {y} різні"
        skaldob = 0
        for i in size_vector(x):
            skaldob += x[i] * y[i]
        return skaldob
    except AssertionError as e:
        print(e)
        return skaldob

def perpend(x,y):
    if skalar(x,y) == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    a = [2, 2, 5]
    print(norma_vector(a))
    b = [1, 2]
    c = [1, 0, -1]
    print(skalar(a, b))
    print(skalar(a, c))
