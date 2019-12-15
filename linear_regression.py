def linear_regression(list_p):
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    for i in list_p:
        sum_x += i[0]
        sum_y += i[1]
        sum_xy += (i[0]*i[1])
        sum_x2 += (i[0]*i[0])
    tam = len(list_p)
    aux = tam * sum_xy
    aux -= sum_x * sum_y
    aux2 = tam * sum_x2
    aux2 -= sum_x * sum_x
    b = aux / aux2
    aux, aux2 = 0, 0

    aux = sum_y / tam
    aux -= b * (sum_x / tam)
    a = aux

    list_r = [a,b]
    return list_r

def calc_regression(list_p, term):
    lst = linear_regression(list_p)
    result = lst[0] + lst[1] * term
    print(f"y = {lst[1]:.4f}x + {lst[0]:.4f}")
    
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

def load_file():
    lineList = [line.rstrip('\n') for line in open('data.txt')]
    e = list(map(int,lineList))
    lst = []
    for i in range(0, len(e)-1, 2):
        aux = [e[i],e[i+1]]
        lst.append(aux)
    return lst

def main():

    lst = load_file()
    #lst = inputUser()
    print(lst)
    n = int(input("Dado para Previsão: "))
    print(f'[ {n}, {calc_regression(lst,n):.2f} ]')
        

if __name__ == "__main__":
    main()
