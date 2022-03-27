from pathlib import Path
from images import image
from imagecheck import imagecheck

def load(musicfolder,size):
    """
    Returns all .jpg img paths in folder
    """
    allimgs=[]
    for path in Path(musicfolder).rglob('*.jpg'):
                #Check for square rgb image of minimum size 
                if(imagecheck(str(path),size)):
                    #print(str(path)+" is square and rgb")
                    #Convert all square images to 400x400m, Save in App Folder
                    newimg=image(path)                  #Create image object
                    allimgs.append(newimg)              #Add image object to list
    return allimgs