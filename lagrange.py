
def lagrange(list_p,term):
    result = 0
    for i in range(0,len(list_p)):
        y = list_p[i][1]
        for j in range(0,len(list_p)):
            if j != i:
                y = (term - list_p[j][0])*y / (list_p[i][0] - list_p[j][0])
        result += y
    return result

def inputUser():
    list_p = [] 
    n = int(input("Quantidade de Pontos : ")) 
    for _ in range(0, n): 
        e = [int(input("X:")), int(input("Y:"))] 
        list_p.append(e) 

    
    print() 
    print("DataSet:",list_p)
    return list_p 

def main():

    lst = inputUser()
    n = int(input("Dado para Previsão: "))

    print(f'[ {n}, {lagrange(lst,n):.2f} ]')
    
if __name__ == "__main__":
    main()
