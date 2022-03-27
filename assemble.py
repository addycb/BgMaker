from PIL import Image

def assemble(finalimages,stats):
    """
    Given list of ordered images and stats, creates and saves new background image
    """
    open=[]
    for i in range(len(finalimages)):
        finalimages[i]=str((finalimages[i]).getpath())
    open=[Image.open(x) for x in finalimages]
    oneunit=stats[2]
    totallength=stats[0]*oneunit
    totalheight=stats[1]*oneunit
    new_im = Image.new('RGB', (totallength, totalheight))
    x_offset = 0
    y_offset=0
    for img in open:
        new_im.paste(img,(x_offset,y_offset))
        x_offset+=oneunit
        y_offset+=((x_offset//totallength)*oneunit)
        x_offset%=totallength
    new_im.save('test.jpg')   

    
