k=2
def part3(n,lista1, iterador):
    for i in range(n):
        if k >1:
            lista1[-1-k].insert(-(i+k),next(iterador))
        else:
            lista1[-1-k].insert(-(i+1),next(iterador))
    print(lista1)

if __name__ == "__main__":
    part3(4,[[1, 2, 3, 4, 5, 6, 7, 8], [28, 29, 30, 31, 32, 33, 34, 9], [27, 48, 49, 50, 51, 52, 35, 10], [26, 47, 53, 36, 11], [25, 46, 54, 37, 12], [24, 45, 38, 13], [23, 44, 43, 42, 41, 40, 39, 14], [22, 21, 20, 19, 18, 17, 16, 15]],iter(range(55,59)))















