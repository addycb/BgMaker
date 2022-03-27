import random
from collections import defaultdict

def randompick(imglist):
    """
    Picks random image from imagelist
    """
    return imglist[random.randint(0,(len(imglist)-1))]

def bestchoice(finalindex,adj,final):
    """
    Given an index in the final grid, a list of adjacent images to that spot,
    and a list of the already used images, find the best unused images based
    on adjacent images.
    """
    counter_dic=defaultdict(int) #Create scoring dictionary
    for x in final:                              #Remove all already used images 
            counter_dic[x]=99999999
    for neighbor in adj[finalindex]:
        if final[neighbor]!=-1:                    #For every filled slot adj to current
            scoreslist=final[neighbor].getscores() #Select scorelist of slot adj
            for i in range(len(scoreslist)):
                counter_dic[scoreslist[i][1]]+=i #Add all imgs in scorelist to counter
    return min(counter_dic, key=counter_dic.get)  #Find min key


def setadj(chosenstats):
    """
    Sets adjacent tiles for each tile in grid of chosenstats
    """
    length=chosenstats[0]
    height=chosenstats[1]
    gridsize=length*height
    adj=[]        
    for x in range(gridsize):
        adj.append([-1,-1,-1,-1])
        if(x>=length):
            adj[x][0]=x-length          #Not on top row, set top neighbor
            #adj[x][0]='topset'
        if x%length!=0:
            adj[x][1]=x-1               #Not on Left Edge, set Left Neighbor 
            #adj[x][1]='leftset'
        if (x+1)%length!=0: 
            adj[x][2]=x+1               #Not on Right Edge, set Right Neighbor 
            #adj[x][2]='rightset'
        if x<((length*height)-length):
            adj[x][3]=x+length          #Not on bottom row, set bottom neighbor 
            #adj[x][3]='bottomset'
    return adj

def fill(num,adj,imglist): 
    """
    Finds bestchoice for each tile, iteratively (random for first img, continues by row)
    """
    final=[]
    finallen=len(adj)
    for x in range(finallen):
        final.append(-1)
    if num==0:
        final[0]=randompick(imglist)
    for i in range(1,finallen):
        x=bestchoice(i,adj,final)
        final[i]=x       
    return final 

def setandfill(imglist,chosenstats):
    """
    Sets adjacency list for each tile, Fills grid
    """
    adj=setadj(chosenstats)
    return fill(0,adj,imglist)


















"""

16,10
. . . . . . . . .
.               .
.               .
.               . 
.               .
. . . . . . . . .


8x5 (200)

[x       
   * [z] = [1600 1000]
 y]
8*200
5*200
 1600
 1000

16*10






16,9
16x9 (100x100)

. . . . . . . . . . . . . . . . . .
.
.
.
.
.
.
.
.






4,3


bonus::
21,9


"""
"""
16:10       Assuming 1600x1000
+++++
32x20 50x50
16x10 100x100
8x5 200x200

16:9        Assuming 1600x900
+++++
32x18 50x50
16x9 100x100
8x5 200x200  (Slightly cropped longways)

4:3 (16:12)  Assuming 1600x1200
32x24 50x50
16x12 100x100
8x6 200x200
"""




    
            




