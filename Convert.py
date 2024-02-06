import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


def Resize(image, W=80):
    
    width, height = image.size
    ratio = height/width/2  
    H = int(W * ratio)

    image = image.resize((W, H)).convert("L")   #To grayscale

    return image


def ToAscii(image):
    
    pixels = image.getdata()  #Gets all pixel's data

    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])  #for 11 indexes
    return(characters)    


def start(img, W=80):
    
    IMAGE = PIL.Image.fromarray(img)  #to PIL 
    IMAGE = ToAscii(Resize(IMAGE, W))  
    
    pixel_count = len(IMAGE)       #image[0, W]
    IMAGE = "\n".join([IMAGE[ind:(ind+W)] for ind in range(0, pixel_count, W)])
                    
    
    return IMAGE
