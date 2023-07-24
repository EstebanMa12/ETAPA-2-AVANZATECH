buscada = "avanzatech"
count = 0
def SopaLetras(arr):

    #HORIZONTALES
    def horizontal(fila,columna):
        result = ""
        if len(arr[fila])-columna>9:
            for i in range (10):
                result += arr[fila][columna]
                columna +=1
                print(result)
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1 
    def reverseHorizontal(fila,columna):
        result = ""
        if columna>=9:
            for i in range (10):
                result += arr[fila][columna]
                columna -=1
                print(result)
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1
    #VERTICALES
    def vertical(fila,columna):
        result = ""
        if (fila+10)<= len(arr):
            for i in range (10):
                result += arr[fila][columna]
                fila +=1
                print(result)
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1
    def reversevertical(fila,columna):
        result = ""
        if (fila-9)>=0:
            for i in range (10):
                result += arr[fila][columna]
                fila -=1
                print(result)
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1

    #DIAGONALES
    def diagonalDU(fila,columna):
        result = ""
        if len(arr[fila])-columna>9 and (fila-9)>=0:
            for i in range (10):
                result += arr[fila][columna]
                columna +=1
                fila -=1
               
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1


    def diagonalUD(fila,columna):
        result = ""
        if len(arr[fila])-columna>9 and (fila+10)<= len(arr):
            for i in range (10):
                result += arr[fila][columna]
                columna +=1
                fila +=1
                
            print(buscada in result.lower())
            result
            if(buscada in result.lower()):
                global count 
                count +=1
    #DIAGONALES AL REVÉS

    def diagonalDUR(fila,columna):
        result = ""
        if columna>=9 and (fila+10)<= len(arr) :
            for i in range (10):
                result += arr[fila][columna]
                columna -=1
                fila +=1
                
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1
    def diagonalUDR(fila,columna):
        result = ""
        if columna>=9 and (fila-9)>=0:
            for i in range (10):
                result += arr[fila][columna]
                columna -=1
                fila -=1
                
            print(buscada in result.lower())
            if(buscada in result.lower()):
                global count 
                count +=1    


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if( arr[i][j]== "a" or "A"):
                fila = i
                columna = j
                print(fila, columna)

                horizontal(fila,columna)
                reverseHorizontal(fila,columna)
                diagonalUD(fila,columna)
                diagonalDU(fila,columna)
                diagonalDUR(fila,columna)
                diagonalUDR(fila,columna)
                vertical(fila,columna)
                reversevertical(fila,columna)
               
    print(count)
    
if __name__ == "__main__":
    SopaLetras(["...........Hh",
                "...avanzatech",
                "ah........eE.",
                "vvc......t.T.",
                "a.ae....a..A.",
                "n..nt..z...Z.",
                "z...zan....N.",
                "a....az....A.",
                "t...v.tn...V.",
                "e..a...ea..A.",
                "c.......cv...",
                "h........ha..",
                "...hcetaznavF"
                ])