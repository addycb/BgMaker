import os 
from dirnav import load
from gridfind import setandfill
from assemble import assemble
from scoring import scoremap
from screenlogistics import getstats, options
                            
#Create bgAlbumart folder if none exist
if not os.path.exists('bgAlbumart'):
    os.makedirs('bgAlbumart')
 
def givechoices():
    #First, Present Options:
    i=0
    screenopt=options(getstats())
    for x in screenopt:
        print('Option ['+str(i)+']:'+str(x))
        i+=1
    optionchoice=int(input('Choose an option of the form [Columns,Rows,Square Size]: '))
    chosenstats=screenopt[optionchoice]
    print('You chose '+str(chosenstats))
    return chosenstats
def findimages(chosenstats): 
    #First, take new folder   
    musicfolder = input('Enter music folder path: ')
    if musicfolder:
        piclist=load(musicfolder,chosenstats[2])
    return piclist 

def prepimages(piclist,chosenstats):
    """
    Makes all images proper size and set colors
    """
    for x in piclist:
            x.convert(chosenstats[2])
            x.setclrs()
    return piclist 

   # scoremap(piclist)
   # assemble(findmatches(piclist))   
def main():
    chosenstats=givechoices()
    piclist=(prepimages(findimages(chosenstats),chosenstats))
    scoremap(piclist)    
    filled=setandfill(piclist,chosenstats)
    assemble(filled,chosenstats)
main()

        
