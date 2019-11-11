def proportion(population_list):
    result = 0
    num = 0
    for i in population_list:
        if (i % 2) == 0:
            num = num + 1

        result = num / len(population_list)
    return result


