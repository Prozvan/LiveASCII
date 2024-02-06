import Convert
import camera
import customtkinter as ctk
import tkinter as tk


class Main:
    def __init__(self):
        self.WINDOW = ctk.CTk(fg_color="black")
        self.WINDOW.title("ASCII")
        self.CAMERA = camera.Camera()

        self.DELAY = 16
        self.SIZE = [100, 36]  #Size of ASCII text


        #GUI
        self.text_widget = ctk.ctk_tk.tkinter.Text(self.WINDOW, wrap=tk.WORD,
                                    height=self.SIZE[1], width=self.SIZE[0],
                                      bg="black", fg="white")
        

        self.text_widget.grid(row=0, column=1, padx=20, pady=20)

        self.WINDOW.attributes("-topmost", True)
        self.Update()
        self.WINDOW.mainloop()
        
    

    def Update(self):
        stanje, self.picture = self.CAMERA.Get_Image()  # Gets the current frame

        self.text_widget.delete(1.0, tk.END)  # deletes previus ASCII image
        self.text_widget.insert(1.0, Convert.start(self.picture, W=self.SIZE[0])) #ASCII image

        self.WINDOW.after(self.DELAY, self.Update) #Updates

    


if __name__ == "__main__":
    Main()




