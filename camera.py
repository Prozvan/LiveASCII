import cv2 as cv

class Camera:
    def __init__(self):
        self.CAMERA = cv.VideoCapture(0)

        self.WIDTH = self.CAMERA.get(cv.CAP_PROP_FRAME_WIDTH)
        self.HEIGHT = self.CAMERA.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        if self.CAMERA.isOpened(): self.CAMERA.release()  

    def Get_Image(self):
    
        
        if self.CAMERA.isOpened():
            stanje, slika_zaslona = self.CAMERA.read()

            if stanje: 
                return(stanje, cv.cvtColor(slika_zaslona, cv.COLOR_BGR2RGB))

