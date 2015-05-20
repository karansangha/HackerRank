#!/bin/python
## Link to challenge - https://www.hackerrank.com/challenges/saveprincess
def displayPathtoPrincess(n,grid):
    m_row = (n/2) + 1
    m_column = (n/2) + 1
    p_row = 0
    p_column = 0
    i = 0
    j = 0
    
    #Locating Princess
    while (i<(n)):
        while (j<(n)):
            #print "J = "+str(j)
            if grid[i][j] =='p':
                p_row = i+1
                p_column = j+1
                break
            j+=1
        i+=1
        j=0
    
    n_down = 0
    n_up = 0
    n_left = 0
    n_right = 0
    if (p_row < m_row):
        n_up = m_row - p_row

    elif (p_row > m_row):
        n_down = p_row - m_row

    if (p_column < m_column):
        n_left = m_column - p_column

    elif (p_column > m_column):
        n_right = p_column - m_column
    #print "Position of princess = "+str(p_row)+","+str(p_column)
    #print "Position of me = "+str(m_row)+","+str(m_column)
    #Print moves

    if n_down > 0:
        for i in xrange(0,n_down):
            print "DOWN"

    if n_up > 0:
        for i in xrange(0,n_up):
            print "UP"

    if n_left > 0:
        for i in xrange(0,n_left):
            print "LEFT"

    if n_right > 0:
        for i in xrange(0,n_right):
            print "RIGHT"
        

m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())
displayPathtoPrincess(m,grid)
