import networkx as nx
import matplotlib.pyplot as plt
import time

def WPGMA(fileName):
    start = time.time()
    T = nx.Graph()
    file = open(fileName, 'r')
    rows = [line.rstrip('\n') for line in file]
    file.close()
    M = []
    for i in range(len(rows)):
        M.append(rows[i].split())

    if len(M) < 3:
        print('Matrix too small error')
        return
            
    if len(M) != len(M[0]):
        print('Matrix is not square error')
        return
    
    for i in range(1,len(M)):
        for j in range(1,len(M)):
            try:
                M[i][j] = float(M[i][j])
            except:
                print('Invalid matrix error')
                return
            
    print_matrix(M)
    while True:
        n = len(M)
        if n == 2: break
        s = 0.0
        x = 1
        y = 1
        for i in range(1,n):
            for j in range(i+1,n):
                if s == 0.0:
                    s = M[i][j]
                    x = i
                    y = j
                    
                if M[i][j] < s and M[i][j] != 0.0:
                    s = M[i][j]
                    x = i
                    y = j

        species1 = M[0][x]
        species2 = M[0][y]
        for i in range(0,n):
            del M[i][y]
        v = M[y]
        del M[y]
        
        n = len(M)
        
        for i in range(1,n):
            if i != x:
                M[x][i] = (len(species1)*M[x][i] + len(species2)*v[i]) / (len(species1)+len(species2))
            else:
                M[x][i] = 0.0
                
        for i in range(1,n):
            if i != x:
                M[i][x] = (len(species1)*M[i][x] + len(species2)*v[i]) / (len(species1)+len(species2))
            else:
                M[i][x] = 0.0

        M[0][x] += v[0]
        M[x][0] += v[0]
        print_matrix(M)
        grow_tree(T,species1,species2)

    name = fileName.split('.')[0]
    nx.draw(T,node_size=1600,with_labels=True)
    plt.title('Tree solution for '+fileName)
    plt.savefig(name+'.png', format='PNG')
    stop = time.time()
    time_taken=stop-start
    print('Time taken: '+str(time_taken))
    
    
def grow_tree(T,a,b):
    if not T.has_node(a):
        T.add_node(a)
    if not T.has_node(b):
        T.add_node(b)
    if not T.has_node(a+b):
        T.add_node(a+b)

    T.add_edge(a+b,a)
    T.add_edge(a+b,b)
        
def print_matrix(M):
    print()
    for m in M:
        print(m)
    print()
        
WPGMA('matrix1.txt')
WPGMA('matrix2.txt')
