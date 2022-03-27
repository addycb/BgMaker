import cv2 as cv


def imagecheck(filepath,size):
  """
  Checks if file is rgb and is square with a minimum side len of size
  """ 
  file=cv.imread(filepath,cv.IMREAD_UNCHANGED)
  if(isrgb(file) and issquaremin(file,size)):
    return True
  return False 

def isrgb(file):
  """
  Checks if file has 3 color channels
  """
  if(len(file.shape)==3):
    return True
  return False 

def issquaremin(file,size):
  """
  Checks is file is square with a minimum side len of size
  """
  if file.shape[0]==file.shape[1] and file.shape[0]>=size:
    return True 
  return False 

  