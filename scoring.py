import numpy as np
from images import image
 
def score(color1,color2):
    """
    Higher score: more contrasting or similiar. More fun in image comparision. 
    """
    absdiff=abs(np.subtract(color1,color2))
    medianclr=[127,127,127]
    y=abs(np.subtract(absdiff,medianclr))
    return y

def totalscore(image1: image,image2: image):
    """
    Checks best match between each color in x and color in y, 
    each x maps to a single y, each y can map from 0 to multiple x
    """
    bestls=[0,0,0]
    for cnt1 in range(3):
        x=image1.getcolors()[cnt1]
        bestdist=0
        for cnt2 in range(3):
            y=image2.getcolors()[cnt2]
            if bestdist<sum(score(x,y)):    
                bestdist=sum(score(x,y))
                bestls[cnt1]=sum(score(x,y))
    return sum(bestls) 

def scoremap(images):    
    """
    Maps scores from each images to each other images
    """
    for x in range(len(images)):
        for y in range(len(images)):
            if y>x:
                image1=images[x]
                image2=images[y]
                score=totalscore(image1,image2)
                image1.addscore(score,image2)
                image2.addscore(score,image1)
    image1.sortscores()   
