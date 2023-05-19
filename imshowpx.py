import cv2,plotly,plotly.express as px,skimage
def imshowPx(im,cv=True,gray=False):
    fig=px.imshow(im[:,:,::-1]if cv else im,binary_string=gray)
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    plotly.io.show(fig)
    
a=cv2.imread('C:/Users/user/Pictures/me1.jpg')
imshowPx(a,cv=False)    
blue=a[:,:,-1].copy()   
gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY) 

blueimg=cv2.subtract(blue,gray)
imshowPx(blueimg,cv=False)
blueb3=skimage.morphology.remove_small_holes()
#
#img=skimage.data.cat()
#