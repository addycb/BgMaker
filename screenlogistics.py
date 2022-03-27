import tkinter as tk

#Here, we have dictionary of our options for different screen aspect ratios.
screenoptions={}               #Length, Height, Size
screenoptions[.5625]=[[32,18,50],[16,9,100],[8,5,200]]                   #16:9
screenoptions[.625]=[[32,20,50],[16,10,100],[8,5,200]]                     #16:10
screenoptions[.75]=[[32,24,50],[16,12,100],[8,6,200]]                   #4:3

def getstats():
    """
    Returns screen info
    """
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return [screen_width,screen_height]

def options(screenstats):
    """
    Finds ratio using given screen info, gives options for background tile counts
    """
    ratio=(screenstats[1]/screenstats[0])
    return (screenoptions[ratio])
