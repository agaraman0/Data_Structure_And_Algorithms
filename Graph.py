#Adjacency Matrix Reprsentation
def graphM():
    n = int(input('Value of Max. Node: '))
    e = int(input('Edge: '))
    matrix = [0] * (n+1)
    for i in range(n+1):
        matrix[i] = [0] * (n+1)
    typ = input('Type Of Graph: ')
    chk = input('Weighted Or Non Weighted: ')
    if chk =='W' and typ =='D':
        for i in range(e):
            n1,n2,v = map(int,input().split())
            matrix[n1][n2] =v
    elif chk =='W' and typ =='U':
         for i in range(e):
            n1,n2,v = map(int,input().split())
            matrix[n1][n2] =v
            matrix[n2][n1] =v
    elif chk =='NW' and typ =='U':
        for i in range(e):
            n1,n2 = map(int,input().split())
            matrix[n1][n2] =1
            matrix[n2][n1] =1
    elif chk =='NW' and typ =='D':
        for i in range(e):
            n1,n2 = map(int,input().split())
            matrix[n1][n2] =1
    return print(matrix)

graphM()
