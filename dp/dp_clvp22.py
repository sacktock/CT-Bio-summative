#!/usr/bin/python
import time
import sys


# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
def al(s1, s2):
    try:
        s1 = str(s1)
        s2 = str(s2)
    except:
        print('Invalid inputs error')
        return
    
    alignment = ['','']
    n1, n2 = len(s1), len(s2)
    SM = [[0 for i in range(n1+1)] for j in range(n2+1)]
    BM = [[0 for i in range(n1+1)] for j in range(n2+1)]

    for i in range(n1+1):
        SM[0][i] = -2*i
        BM[0][i] = 'L'

    for i in range(n2+1):
        SM[i][0] = -2*i
        BM[i][0] = 'U'

    for j in range(1,n2+1):
        for i in range(1,n1+1):
            D = c(s1[i-1],s2[j-1]) + SM[j-1][i-1]
            L = SM[j][i-1] - 2
            U = SM[j-1][i] - 2
            m = max(D,L,U)
            SM[j][i] = m
            if m == D: #prioritize diagonal 
                BM[j][i] = 'D'
            elif m == L:
                BM[j][i] = 'L'
            else:
                BM[j][i] = 'U'

    score = SM[n2][n1]

    i = n1
    j = n2
    while True:
        m = BM[j][i]
        if m == 'D':
            alignment[0] += s1[i-1]
            alignment[1] += s2[j-1]
            i = i - 1
            j = j - 1
        elif m == 'L':
            alignment[0] += s1[i-1]
            alignment[1] += '_'
            i = i - 1
        else:
            alignment[0] += '_'
            alignment[1] += s2[j-1]
            j = j - 1

        if i == 0 and j == 0:
            break
            
    alignment[0] = alignment[0][::-1]
    alignment[1] = alignment[1][::-1]

    return alignment, score
                  
def c(i,j):
    if i == j:
        if i == 'A':
            return 4
        elif i == 'C':
            return 3
        elif i == 'G':
            return 2
        else:
            return 1
    else:
        return -3
        
        
        
# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
best_alignment, best_score = al(seq1,seq2)


#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

