
#from binarysearch import insert
from PIL import Image
from sklearn.cluster import KMeans
from pathlib import Path
import operator
    
class image:
    """
    Class of image objects
    """
    
    colors=[]
    scores=[]
    


    def __init__(self,path: Path):
        """
        Initializes image object with path and name attributes
        """
        self.path=path
        self.name=path.name 
                     

    def convert(self,size):
        """
        Converts image file to wanted size, changes image object path to converted image file
        """
        self.name=(str((self.path.parts)[len(self.path.parts)-2]+' '+self.path.name)) #Change image name 
        with Image.open(str(self.path)) as im:
            im.thumbnail([size,size])             #Convert image
            im.save('bgAlbumart/'+self.name)    #Save image with new name
            self.path=('bgAlbumart/'+self.name) #Set new image path

    def setclrs(self):
        """
        Sets image objects 3 domininat colors using kmeans clustering
        """
        with Image.open(str(self.path)) as im:    
            colors = im.getdata()               #Get image data
            colors=KMeans(n_clusters=3).fit(colors).cluster_centers_  #Set image object dominant colors
            self.colors=colors
                      
    
    def addscore(self,score,image2):
        """
        Adds comparision score of itself and other image to own images scorelist
        """
        self.scores.append([score,image2])

    def sortscores(self):
        """
        Sorts image scorelist
        """
        self.scores.sort(key=operator.itemgetter(0))


    def getpath(self):
        """
        Access image path
        """
        return self.path
    
    def getcolors(self):
        """
        Access image colors
        """
        return self.colors
    
    def getscores(self):
        """
        Access image scores
        """
        return self.scores
    