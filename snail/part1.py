k=2
def part1(n,lista1,iterador):
    for i in iter(range(n)):  
        lista1[k].insert(i+k,next(iterador))
    print(lista1)






if __name__ == "__main__":
    part1(4,[[1, 2, 3, 4, 5, 6, 7, 8], [28, 29, 30, 31, 32, 33, 34, 9], [27, 48, 35, 10], [26, 47, 36, 11], [25, 46, 37, 12], [24, 45, 38, 13], [23, 44, 43, 42, 41, 40, 39, 14], [22, 21, 20, 19, 18, 17, 16, 15]],iter(range(49,53)))














