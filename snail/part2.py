k=2
def part2(n,lista1,iterador):
    j=1+k
    for i in range(n-2):
        lista1[j].insert(len(lista1[j])//2,next(iterador))
        j +=1
    print(lista1) 
    for i in lista1:
        print(i) 

if __name__ == "__main__":
    part2(4,[[1, 2, 3, 4, 5, 6, 7, 8], [28, 29, 30, 31, 32, 33, 34, 9], [27, 48, 49, 50, 51, 52, 35, 10], [26, 47, 36, 11], [25, 46, 37, 12], [24, 45, 38, 13], [23, 44, 43, 42, 41, 40, 39, 14], [22, 21, 20, 19, 18, 17, 16, 15]],iter(range(53,55)))


 










