import tkinter as tk
# Importing pillow or python image library to show tk images and manage gif frames
from PIL import Image, ImageTk
class SplashScreen(tk.Toplevel):
    # super() constructs widgets
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # Height and Width
        height = 300
        width = 500
        # Dimensions tuple
        dimensions = (height, width)
        # Get user screen dimensions to center window on screen
        x = (self.winfo_screenwidth() // 2) - (dimensions[1] // 2)
        y = (self.winfo_screenheight() // 4) - (dimensions[0] // 4)
        self.geometry('{}x{}+{}+{}'.format(dimensions[1], dimensions[0], x, y))
        self.resizable(False, False)
        # Window Title
        self.title("UNITED Platform | Yellow Hole")
        self.configure(background="black")
        # Configure to resize proportionally
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # App ICON
        self.iconphoto(False, tk.PhotoImage(file='assets/APPICON.ico'))
        # CURSOR
        self.config(cursor='wait')

        self.gif_image = Image.open("assets/SPLASH.gif")
        self.gif_frame = ImageTk.PhotoImage(self.gif_image)

        self.label = tk.Label(self, image=self.gif_frame, bg='black')
        self.label.pack()

        self.parent.withdraw()  # Hide the main Tk window

        # Destroy Splash Screen after 1.5 seconds
        self.after(1500, self.close_splash_screen)

    def close_splash_screen(self):
        # Destroy Window
        self.destroy()
        self.parent.deiconify()  # Show the main Tk window