import networkx as nx

def WPGMA(fileName):
    T = nx.Graph()
    file = open(fileName, 'r')
    rows = [line.rstrip('\n') for line in file]
    M = []
    for i in range(len(rows)):
        M.append(rows[i].split())

    for i in range(1,len(M)):
        for j in range(1,len(M)):
            M[i][j] = float(M[i][j])
    print_matrix(M)

    while True:
        n = len(M)
        s = 0.0
        x = 1
        y = 1
        for i in range(1,n):
            for j in range(1,n):
                if s == 0.0:
                    s = M[i][j]
                    x = i
                    y = j
                    
                if M[i][j] < s and M[i][j] != 0.0:
                    s = M[i][j]
                    x = i
                    y = j
        if s == 0:
            break

        species1 = M[0][x]
        species2 = M[0][y]
        for i in range(0,n):
            del M[i][y]
        v = M[y]
        del M[y]
        
        n = len(M)
        
        for i in range(1,n):
            if i != x:
                M[x][i] = (M[x][i] + v[i]) / 2
            else:
                M[x][i] = 0.0
                
        for i in range(1,n):
            if i != x:
                M[i][x] = (M[i][x] + v[i]) / 2
            else:
                M[i][x] = 0.0

        M[0][x] += v[0]
        M[x][0] += v[0]
        print_matrix(M)
        grow_tree(T,species1,species2)
    print(T.edges())
    #draw T into a file somehow
    
def grow_tree(T,a,b):
    if not T.has_node(a):
        T.add_node(a)
    if not T.has_node(b):
        T.add_node(b)
    if not T.has_node(a+b):
        T.add_node(a+b)

    T.add_edge(a,a+b)
    T.add_edge(b,a+b)
        
def print_matrix(M):
    print()
    for m in M:
        print(m)
    print()
        
WPGMA('matrix1.txt')
WPGMA('matrix2.txt')
