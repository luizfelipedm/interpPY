from numpy import array, linalg

def interpolate(list_p,term):
    list_px = [] 
    list_py = [] 
    for i in range(0, len(list_p)):
        x = list_p[i][0]
        y = list_p[i][1]
        e = [1, x]
        if(len(list_p) > 2):
            for _ in range(2, len(list_p)):
                x *= x
                e.append(x) 
        list_px.append(e)
        list_py.append(y)

    f = array(list_px)
    r = array(list_py)

    list_s = linalg.solve(f,r)
    show_pol(list_s)
    result = list_s[0]
    for i in range(1, len(list_s)):
        if(i == 1):
            result += list_s[i] * term
        if(i > 1): 
            for _ in range(2, len(list_p)):
                term *= term
                result += list_s[i] * term
    return result

    
    
def show_pol(list_s):
    for i in range(0, len(list_s)):
        print(f"({list_s[i]:.2f})", end = '')
        if(i == 1):
            print("x", end = '')
        if(i > 1):
            print(f"x^{i}", end = '')
        if (i != len(list_s)-1):
            print(" + ", end = '')
        else:
            print()

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
    print(f'[{n}, {interpolate(lst,n):.2f}]')
    
if __name__ == "__main__":
    main()
