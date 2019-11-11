# def proportion(a, b):
#     c = a / b
#     return c

def proportion(population_list):
    result = 0
    num = 0
    for i in population_list:
        if (i % 2) == 0:
            num = num + 1
        #result = division(num, len(population_list))
        result = num / len(population_list)
    return result



#given that Y is directly prop to X
#e.g y = 20 , x = 4
# y = kx
# 20 / k (4)
# y = 20 / 4
# y = 5x
# so Y = 5x, where K is the gradient