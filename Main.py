#                                   ﷽

# --------------------------- Importing Modules ---------------------------
# Importing Tkinter Library
import tkinter as tk
# from filename import classname
# Reset password Classes
from ResetPassword import PasswordChanger
# GUI Classes
import GUI as custom
# Login Classes
from LoginDB import LoginManager
# Sign Up Classes
from SignupDB import SignupManager
# Post-Comments Classes
from Post import PostPublisher
# Keyboard Shifter Classes
from BonusReplacer import BonusReplacer
# ttk for extra widgets
from tkinter import ttk
# Alerting in tkinter
from tkinter import messagebox
# Splash Screen Classes
from SplashScreener import SplashScreen
# Time built-in Module for delays
import time
# File Dialog for profile pictures
from tkinter import filedialog
# PIL for images
from PIL import ImageTk, Image, ImageDraw
# Random Ayah
from RandomAyah import RandomAyahGenerator

New_Ayah = RandomAyahGenerator().generate_randomAyah()
Ayah_2 = RandomAyahGenerator().generate_randomAyah()
Ayah_3 = RandomAyahGenerator().generate_randomAyah()
print(str(New_Ayah), str(Ayah_2), str(Ayah_3))
# DB CONFIG
config = {
    'host':'localhost',
    'database':'United_DB',
    'user':'root',
    'password':'Yeer2023'
}
# SOUNDS
# Import pygame only for sounds
# I first downloaded it using 'pip install pygame'
import pygame
def play_sound(soundName):
    # Init mixer
    pygame.mixer.init()
    # Load audio file
    pygame.mixer.music.load(f"Audio/{soundName}.mp3")
    # Play loaded file
    pygame.mixer.music.play()

# Account Killer for deleting account ##### - DELAYED
# from AccountKiller import AccountDeleter ###### - DELAYED

# Create window
window = tk.Tk()
# --------------------------- Splash Screen ---------------------------
# Window visibility - hide window for splashscreen
# Hide window temporary
window.withdraw()
# Set visibility to false (hidden)
window_visible = False
# Splash Screen Window from class
splash = SplashScreen(window)
# Set Focus to splash screen window
splash.focus_set()
# Wait until its visible
splash.wait_visibility()
# Close the splash screen after 1.5 secs 1500ms
window.after(1500, splash.destroy)
# Get time
start_time = time.time()
delay = 1.5
# If window is not visible (hidden)
while not window_visible: # if True
    # Update window
    window.update()
    # Current time - app start time, eg. 02:54:30 - 02:54:28 = 2secs
    elapsed_time = time.time() - start_time
    # If elapsed time passed the delay time
    if elapsed_time >= delay:
        # Play Intro.mp3
        play_sound("Intro")
        # Set visibility to true (Shown)
        window_visible = True
        # Show window
        window.deiconify()

# --------------------------- Configuring Window ---------------------------
# Configure to resize proportionally
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# App ICON
window.iconphoto(False, tk.PhotoImage(file='assets/APPICON.ico'))
# CURSOR
window.config(cursor='wait')
# Height and Width
height = 650
width = 1240
# Dimensions tuple
dimensions = (height, width)
# Get user screen dimensions to center window on screen
x = (window.winfo_screenwidth() // 2) - (dimensions[1] // 2)
y = (window.winfo_screenheight() // 4) - (dimensions[0] // 4)
window.geometry('{}x{}+{}+{}'.format(dimensions[1], dimensions[0], x, y))
window.resizable(False, False)
# Window Title
window.title("UNITED Platform | Yellow Hole")
# Root Colors
theme_color = '#F4BC21'
ground_color = "#272A37"

# --------------------------- Fade In Animation ---------------------------
def fade_in_animation(frame, duration):
    # #F4BC21 divided to six red: F4, green: BC, blue: 21 and converted to tuples
    target_color = (0xF4, 0xBC, 0x21)
    # Gradually set to target color
    for i in range(0, 256):
        alpha = int(255 * (i / 255) ** 2)
        color = '#%02x%02x%02x' % (
            int(target_color[0] * (alpha / 255)),
            int(target_color[1] * (alpha / 255)),
            int(target_color[2] * (alpha / 255))
        )
        frame.after(duration * i, frame.config, {'bg': color})

# --------------------------- Frames ---------------------------
# Frames
sign_in = tk.Frame(window)
sign_up = tk.Frame(window)
homepage = tk.Frame(window)
# Now initial frame is moved to line 572
# Instead of doing x.grid... y.grid... z.grid...: for b in xyz: b.grid...
for frame in (sign_in, sign_up, homepage):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise() # tkraise frame
    fade_in_animation(frame, 4)
    # Set title according to frame shown
    if frame == sign_up:
        window.title("UNITED Platform | Sign Up Gate")
        firstName_entry.focus_set()
    elif frame == sign_in:
        window.title("UNITED Platform | Account Login Gate")
        Login_emailName_entry.focus_set()
    elif frame == homepage:
        window.title("UNITED Platform | Homepage")
        scrollbox.focus_set()

# Show Login Frame
def slf():
    show_frame(sign_in)

# ------------------------------------ Signup ----------------------------------------------------
# -------------------------------------------------------------------------------

# Signup StringVars
FirstName = tk.StringVar()
LastName = tk.StringVar()
Email = tk.StringVar()
Password = tk.StringVar()
ConfirmPassword = tk.StringVar()
Role = tk.StringVar()
# --------------------------- GUI MODULAR CLASSES -------------------------
# BG Color
sign_up.configure(bg=theme_color)
# bg img
backgroundImage_Load = tk.PhotoImage(file="assets/image_1.png")
bg_image = custom.BackgroundImageLabel(sign_up, image=backgroundImage_Load, bg=theme_color)
bg_image.place(x=120, y=28)
# bg_image is the parent for all other widgets

# LOGO panel on left
# Logo img
LogoImgLeft_Load = tk.PhotoImage(file="assets/headerText_image.png")
LogoImgLeft = custom.LogoImg(bg_image, image=LogoImgLeft_Load, bg=ground_color)
LogoImgLeft.place(x=55, y=40)
# Logo text
Logo_HeaderText = custom.LogoText(bg_image, "UNITED")
Logo_HeaderText.place(x=110, y=45)
# Smiley face - Slogan
SloganImgRight_Load = tk.PhotoImage(file="assets/SloganIMG.png")
SloganImgRight = custom.SloganImg(bg_image, SloganImgRight_Load)
SloganImgRight.place(x=400, y=36)
# Slogan Text
Slogan_Text = custom.SloganHeader(bg_image, '-Where the world gets United-')
Slogan_Text.place(x=450, y=45)
# Create Account Header
account_header = custom.AccountHeaderLabel(bg_image, 'Create A New Account!')
account_header.place(x=75, y=121)

# Continue as guest btn
guest = custom.GuestBtn(bg_image, ground_color, lambda:scf(), tk.DISABLED)
guest.place(x=320, y=185, width=130, height=35)

SwitchText = custom.SwitchText(bg_image, "Already a member?")
SwitchText.place(x=75, y=187)

SwitchLoginButton = custom.SwitchAuthButton(bg_image, "Login", lambda: show_frame(sign_in))
SwitchLoginButton.place(x=230, y=185, width=50, height=35)


# FN GUI
firstName_image = tk.PhotoImage(file="assets/input_img.png")
firstName_image_label = custom.IconLabel(bg_image, firstName_image, ground_color)
firstName_image_label.place(x=80, y=242)

firstName_text = custom.EntryLabel(firstName_image_label, 'Your First Name👇🏿:', theme_color)
firstName_text.place(x=25, y=0)

firstName_icon = tk.PhotoImage(file="assets/name_icon.png")
firstName_icon_Label = custom.IconLabel( firstName_image_label, image=firstName_icon, bg=theme_color)
firstName_icon_Label.place(x=159, y=15)

# FN entry
# Text variable dynamically updates
firstName_entry = custom.EntryConstructor(firstName_image_label, FirstName, theme_color, '')
firstName_entry.place(x=8, y=17, width=140, height=27)

# LN GUI
lastName_image = tk.PhotoImage(file="assets/input_img.png")
lastName_image_Label = custom.IconLabel(bg_image, image=lastName_image, bg=ground_color)
lastName_image_Label.place(x=293, y=242)

lastName_text = custom.EntryLabel(lastName_image_Label, 'Now ur Last Name ⤵:', theme_color)
lastName_text.place(x=25, y=0)

lastName_icon = tk.PhotoImage(file="assets/name_icon.png")
lastName_icon_Label = tk.Label( lastName_image_Label, image=lastName_icon, bg=theme_color)
lastName_icon_Label.place(x=159, y=15)
# LN entry
lastName_entry = custom.EntryConstructor(lastName_image_Label, LastName, theme_color, '')
lastName_entry.place(x=8, y=17, width=140, height=27)

# EN GUI
emailName_image = tk.PhotoImage(file="assets/email.png")
emailName_image_Label = custom.IconLabel(bg_image, image=emailName_image, bg=ground_color)
emailName_image_Label.place(x=80, y=311)

emailName_text = custom.EntryLabel(emailName_image_Label, 'Your Email ✉️:', theme_color)
emailName_text.place(x=25, y=0)

emailName_icon = tk.PhotoImage(file="assets/email-icon.png")
emailName_icon_Label = tk.Label( emailName_image_Label, image=emailName_icon, bg=theme_color)
emailName_icon_Label.place(x=370, y=15)

# EN entry
emailName_entry = custom.EntryConstructor(emailName_image_Label, Email, theme_color, '')
emailName_entry.place(x=8, y=17, width=354, height=27)

# Password GUI
passwordName_image = tk.PhotoImage(file="assets/input_img.png")
passwordName_image_Label = tk.Label( bg_image, image=passwordName_image, bg=ground_color)
passwordName_image_Label.place(x=80, y=380)

passwordName_text = custom.EntryLabel(passwordName_image_Label, 'Choose a Password 🤫:', theme_color)
passwordName_text.place(x=25, y=0)

passwordName_icon = tk.PhotoImage(file="assets/pass-icon.png")
passwordName_icon_Label = tk.Label(passwordName_image_Label, image=passwordName_icon, bg=theme_color)
passwordName_icon_Label.place(x=159, y=15)
# Password entry
passwordName_entry = custom.EntryConstructor(passwordName_image_Label, Password, theme_color, '•')
passwordName_entry.place(x=8, y=17, width=140, height=27)

# CP GUI
confirm_passwordName_image = tk.PhotoImage(file="assets/input_img.png")
confirm_passwordName_image_Label = tk.Label( bg_image, image=confirm_passwordName_image, bg=ground_color)
confirm_passwordName_image_Label.place(x=293, y=380)

confirm_passwordName_text = custom.EntryLabel(confirm_passwordName_image_Label, 'Confirm Password:', theme_color)
confirm_passwordName_text.place(x=25, y=0)

confirm_passwordName_icon = tk.PhotoImage(file="assets/pass-icon.png")
confirm_passwordName_icon_Label = custom.IconLabel(confirm_passwordName_image_Label, image=confirm_passwordName_icon, bg=theme_color)

# CP entry
confirm_passwordName_entry = custom.EntryConstructor(confirm_passwordName_image_Label, ConfirmPassword, theme_color, '•')
confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

# Role GUI
RoleName_image = tk.PhotoImage(file="assets/input_img.png")
RoleName_image_Label = tk.Label( bg_image, image=RoleName_image, bg=ground_color)
RoleName_image_Label.place(x=580, y=380)

RoleName_icon = tk.PhotoImage(file="assets/pass-icon.png")
RoleName_icon_Label = tk.Label( RoleName_image_Label, image=RoleName_icon, bg=theme_color)
RoleName_icon_Label.place(x=150, y=15)

# Role entry
RoleName_entry = custom.EntryConstructor(RoleName_image_Label, Role, theme_color, '')
RoleName_entry.insert(0, "Admin/Member")
RoleName_entry.config(fg='navy', font=("Comic Sans MS Bold", 17 * -1))
RoleName_entry.place(x=8, y=17, width=140, height=27)

# SHOW HIDE PASSWORD
checkboximgHID = tk.PhotoImage(file="assets/HidePass.png")
checkboximgSHOW = tk.PhotoImage(file="assets/ShowPass.png")

# Toggle variable
x = True
def toggle_password_visibility():
    global x
    if x == True:
        confirm_passwordName_entry.config(show="")
        passwordName_entry.config(show="")
        show_password_check.config(image=checkboximgSHOW)
        x = False
    elif x == False:
        confirm_passwordName_entry.config(show='•')
        passwordName_entry.config(show='•')
        show_password_check.config(image=checkboximgHID)
        x = True

show_password_check = tk.Label(confirm_passwordName_image_Label, image=checkboximgHID, bd=0, bg=theme_color, cursor='pointinghand')
show_password_check.bind("<Button-1>", lambda event: toggle_password_visibility())
show_password_check.place(x=150, y=15, height=30, width=40)

# -------------------------- UPLOADING PROFILE PICTURE -----------------------------
image_path_final = "assets/UserIMG.png"
# Setting fixed size for the image
fixed_size = (200, 200)
# UPLOAD IMAGE
def change_default_image(event, image_path):
    file_path = filedialog.askopenfilename(filetypes=[("Image files","*.png"), ("Image files","*.jpeg"), ("Image files","*.jpg"), ("Image files","*.gif"), ("Image files","*.ico"), ("Image files","*.webp")])
    image = Image.open(file_path)
    image = image.resize(fixed_size, Image.ANTIALIAS)
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, image.width, image.height), fill=255)
    image = Image.composite(image, Image.new("RGBA", image.size, 0), mask)
    image_tk = ImageTk.PhotoImage(image)
    profile_img.configure(image=image_tk)
    profile_img.image = image_tk
    image_path = file_path
    return image_path

default_image_path = "assets/UserIMGDRAFT.png"
default_image = Image.open(default_image_path)

# Resize the new uploaded image
default_image = default_image.resize(fixed_size, Image.ANTIALIAS)

mask = Image.new("L", default_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, default_image.width, default_image.height), fill=255)
default_image = Image.composite(default_image, Image.new("RGBA", default_image.size, 0), mask)

default_image_tk = ImageTk.PhotoImage(default_image)
profile_img = tk.Label(sign_up, bg=ground_color, image=default_image_tk, cursor='pointinghand')
profile_img.place(x=700, y=190)
image_textguide = custom.EntryLabel(sign_up, 'Upload Profile Pic', ground_color)
image_textguide.configure(fg="white", font=("Comic Sans MS Bold", 19 * -1),)
image_textguide.place(x=710, y=150)

# Bind the change_default_image function to the label's click event
profile_img.bind("<Button-1>", lambda event: change_default_image(event, image_path_final))
# SUBMIT BTN
submit_buttonImage = tk.PhotoImage(
    file="assets/button_1.png")

submit_button = custom.SubmitButton(bg_image, lambda:SignupManager(config).signupDB(firstName_entry.get(), lastName_entry.get(), passwordName_entry.get(), emailName_entry.get(), confirm_passwordName_entry.get(), RoleName_entry.get(), clear_signup, slf, play_sound, image_path_final), submit_buttonImage, ground_color)
submit_button.place(x=130, y=460, width=333, height=65)

# Header Text Bottom
BottomHeader = custom.bottomHeader(bg_image, ground_color)
BottomHeader.place(x=700, y=500)

# CLEAR - RESET SIGN UP FIELDS
def clear_signup():
    FirstName.set("")
    LastName.set("")
    Email.set("")
    Password.set("")
    ConfirmPassword.set("")
    Role.set("Admin/Member")

# ------------------------------------ Login ----------------------------------------------------
# -------------------------------------------------------------------------------
# Login stringvars
email = tk.StringVar()
password = tk.StringVar()

# BG Color
sign_in.configure(bg=theme_color)

# Frame BG Image
Login_backgroundImage = tk.PhotoImage(file="assets/image_1.png")
bg_imageLogin = custom.BackgroundImageLabel(sign_in, Login_backgroundImage, theme_color)
bg_imageLogin.place(x=120, y=28)

# Header Text left
Login_headerText_image_left = tk.PhotoImage(file="assets/headerText_image.png")
Login_headerText_image_label1 = custom.LogoImg(bg_imageLogin, image=LogoImgLeft_Load, bg=ground_color)
Login_headerText_image_label1.place(x=55, y=40)

Login_headerText1 = custom.LogoText(bg_imageLogin, "UNITED")

Login_headerText1.place(x=110, y=45)

# Header Text Right
Login_headerText_image_right = tk.PhotoImage(file="assets/SloganIMG.png")
Login_headerText_image_label2 = custom.SloganImg(bg_imageLogin, SloganImgRight_Load)
Login_headerText_image_label2.place(x=400, y=36)

Login_headerText2 = custom.SloganHeader(bg_imageLogin, '-Where the world gets United-')
Login_headerText2.place(x=450, y=45)

# Login Header
loginAccount_header = custom.AccountHeaderLabel(bg_imageLogin, 'Welcome Back! Login To Continue...')
loginAccount_header.place(x=75, y=121)

# Not a member header
loginText = custom.SwitchText(bg_imageLogin, "Not a member?")
loginText.place(x=75, y=187)

# Go to Sign Up
SwitchSignupButton = custom.SwitchAuthButton(bg_imageLogin, "Sign Up", lambda: show_frame(sign_up))
SwitchSignupButton.place(x=220, y=185, width=70, height=35)
# Guest Button
guest2 = custom.GuestBtn(bg_imageLogin, ground_color, lambda:scf(), tk.DISABLED)
guest2.place(x=320, y=185, width=130, height=35)

# Email
Login_emailName_image = tk.PhotoImage(file="assets/email.png")
Login_emailName_image_Label = tk.Label(bg_imageLogin, image=Login_emailName_image, bg=ground_color)
Login_emailName_image_Label.place(x=76, y=242)

Login_emailName_text = custom.LoginEntryLabel(Login_emailName_image_Label, "Your Email ✉️:")
Login_emailName_text.place(x=25, y=0)

Login_emailName_icon = tk.PhotoImage(file="assets/email-icon.png")
Login_emailName_icon_Label = tk.Label(Login_emailName_image_Label, image=Login_emailName_icon, bg=theme_color)
Login_emailName_icon_Label.place(x=370, y=15)
# email entry
Login_emailName_entry = custom.LoginEntryConstructor(Login_emailName_image_Label, email, theme_color, '')
Login_emailName_entry.place(x=8, y=17, width=354, height=27)

# Password
Login_passwordName_image = tk.PhotoImage(file="assets/email.png")
Login_passwordName_image_Label = tk.Label(bg_imageLogin, image=Login_passwordName_image, bg=ground_color)
Login_passwordName_image_Label.place(x=80, y=330)

Login_passwordName_text = custom.LoginEntryLabel(Login_passwordName_image_Label, "Password 🤫")
Login_passwordName_text.place(x=25, y=0)

Login_passwordName_icon = tk.PhotoImage(file="assets/pass-icon.png")
Login_passwordName_icon_Label = tk.Label( Login_passwordName_image_Label, image=Login_passwordName_icon, bg=theme_color)
Login_passwordName_icon_Label.place(x=370, y=15)

# password entry
Login_passwordName_entry = custom.LoginEntryConstructor(Login_passwordName_image_Label, password, theme_color, '•')
Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

# HIDE SHOW PASSWORD TOGGLE
y = True
def toggle_password_visibilityLOGIN():
    global y
    if y == True:
        Login_passwordName_entry.config(show="")
        show_password_checkLOGIN.config(image=checkboximgSHOW)
        y = False
    elif y == False:
        Login_passwordName_entry.config(show='•')
        show_password_checkLOGIN.config(image=checkboximgHID)
        y = True

show_password_checkLOGIN = tk.Label(Login_passwordName_image_Label, image=checkboximgHID, bd=0, bg=theme_color, cursor='pointinghand')
show_password_checkLOGIN.bind("<Button-1>", lambda event: toggle_password_visibilityLOGIN())
show_password_checkLOGIN.place(x=360, y=15, height=30, width=40)
# Clear Login Form
def clear_login():
    email.set("")
    password.set("")

# Login DB
Login_button_image_1 = tk.PhotoImage(
    file="assets/button_1.png")
LoginSubmitButton = custom.SubmitButton(bg_imageLogin, lambda: login_button_click(), Login_button_image_1, ground_color)
LoginSubmitButton.place(x=120, y=445, width=333, height=65)

# Storing username forever
def handle_login_result(username):
    global logged_in_username 
    logged_in_username = username
    if username is not None:
        logged_in_username = username  
        set_username_for_post(username)
    else:
        pass

def set_username_for_post(username):
    global usernameforpost
    usernameforpost = username

def login_button_click():
    username = Login_emailName_entry.get()
    password = Login_passwordName_entry.get()
    # db config dict:
    config = {
        "host": "localhost",
        "user": "root",
        "password": "Yeer2023",
        "database": "United_DB"
    }
    login_manager = LoginManager(config)
    logged_in_username = login_manager.login(username, password, clear_login, scf, play_sound)
    
    # store username
    handle_login_result(logged_in_username)

Login_headerText3 = custom.bottomHeader(bg_imageLogin, ground_color)
Login_headerText3.place(x=700, y=500)

# ### # ### FORGOT PASSWORD
# Using Toplevel
def forgot_password():
    win = tk.Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    win.configure(background='#272A37')
    win.resizable(False, False)

# Email
    email_entry3 = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), highlightthickness=1, insertbackground=theme_color,
                         bd=0)
    email_entry3.place(x=40, y=80, width=256, height=50)
    email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = tk.Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                         font=("Comic Sans MS", 11, 'bold'))
    email_label3.place(x=40, y=50)

# New Password
    new_password_entry = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), show='•', highlightthickness=1, insertbackground=theme_color, bd=0)
    new_password_entry.place(x=40, y=180, width=256, height=50)
    new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    new_password_label = tk.Label(win, text='• New Password', fg="#FFFFFF", bg='#272A37',
                               font=("Comic Sans MS", 11, 'bold'))
    new_password_label.place(x=40, y=150)

# Update Password
    update_pass = tk.Button(win, fg='#f8f8f8', text='Update Password', bg='#1D90F5', font=("Comic Sans MS", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=lambda: PasswordChanger().forgot_password_db(email_entry3.get(), new_password_entry.get(), win))
    update_pass.place(x=40, y=260, width=256, height=45)

forgotPassword = tk.Button(
    bg_imageLogin,
    text="Forgot Password",
    fg="#206DB4",
    font=("Comic Sans MS", 15 * -1),
    bg=ground_color,
    bd=0,
    activebackground=ground_color,
    activeforeground="#ffffff",
    cursor="hand2",
    command= forgot_password,
)
forgotPassword.place(x=210, y=400, width=150, height=35)

# Initial frame
inital_frame = sign_in
show_frame(inital_frame)

# Content ====================================
# Window BG Image

bg_imageMai = tk.PhotoImage(file="assets/image_1.png")
bg_imageMain = tk.Label(
    homepage,
    image=bg_imageMai,
    bg=theme_color,
)
bg_imageMain.place(x=0, y=0, relwidth=1, relheight=1)
# Calculate the half width and half height of the image
half_width = int((width - 270) / 2)
half_height = int((height - 100) / 2)

Post = tk.StringVar()
Comment = tk.StringVar()

# Get the width and height of the image
image_width = bg_imageMai.width()
image_height = bg_imageMai.height()

# Calculate the half width and half height of the image
half_width = int(image_width / 2)
half_height = int(image_height / 2)

entry_width = half_width
entry_height = half_height

post_entry = tk.Text(
    bg_imageMain,
    font=("Comic Sans MS", 24),
    bg="black",
    fg="#FFFFFF",
    insertbackground=theme_color
)
post_entry.place(relx=0.49, rely=0.05, width=entry_width, height=entry_height)

placeholder_text = "Write your first post for today..."

def clear_placeholder(event):
    if post_entry.get("1.0", "end-1c") == placeholder_text:
        post_entry.delete("1.0", "end")

def restore_placeholder(event):
    if not post_entry.get("1.0", "end-1c"):
        post_entry.delete("1.0", tk.END)
        post_entry.insert("1.0", placeholder_text)


post_entry.bind("<FocusIn>", clear_placeholder)
post_entry.bind("<FocusOut>", restore_placeholder)

# Profile Picture
image_path_final2 = "assets/UserIMG.png"
# Setting fixed size for the image
fixed_size2 = (200, 200)
# UPLOAD IMAGE
def change_default_image2(event, image_path2):
    file_path2 = filedialog.askopenfilename(filetypes=[("Image files","*.png"), ("Image files","*.jpeg"), ("Image files","*.jpg"), ("Image files","*.gif"), ("Image files","*.ico"), ("Image files","*.webp")])
    image2 = Image.open(file_path2)

    image2 = image2.resize(fixed_size2, Image.ANTIALIAS)
    mask2 = Image.new("L", image2.size, 0)
    draw2 = ImageDraw.Draw(mask2)
    draw2.ellipse((0, 0, image2.width, image2.height), fill=255)
    image2 = Image.composite(image2, Image.new("RGBA", image2.size, 0), mask2)
    image_tk2 = ImageTk.PhotoImage(image2)
    profile_imgposts.configure(image=image_tk2)
    profile_img.configure(image=image_tk2)
    profile_imgposts.image = image_tk2
    image_path2 = file_path2
    return image_path2

default_image_path2 = "assets/UserIMGDRAFT.png"
default_image2 = Image.open(default_image_path2)

# Resize the new uploaded image
default_image2 = default_image2.resize(fixed_size2, Image.ANTIALIAS)

mask2 = Image.new("L", default_image2.size, 0)
draw2 = ImageDraw.Draw(mask2)
draw2.ellipse((0, 0, default_image2.width, default_image2.height), fill=255)
default_image2 = Image.composite(default_image2, Image.new("RGBA", default_image2.size, 0), mask2)

default_image_tk2 = ImageTk.PhotoImage(default_image2)
profile_imgposts = tk.Label(homepage, bg=ground_color, image=default_image_tk2, cursor='pointinghand')
profile_imgposts.place(x=700, y=400)
profile_imgposts.bind("<Button-1>", lambda event: change_default_image2(event, image_path_final2))

def typewriter_effect(text_widget, text, delay):
    if len(text) > 0:
        text_widget.insert('end', text[0])
        play_sound('Key')
        text_widget.see('end')
        text_widget.update()
        text_widget.after(delay, typewriter_effect, text_widget, text[1:], delay)

print(set_username_for_post)

def clear_post():
    post_entry.delete("1.0", tk.END)
    typewriter_effect(post_entry, 'Another Post...', 10)

from tkinter import scrolledtext

scrollbox = scrolledtext.ScrolledText(bg_imageMain, width=57, height=40)
scrollbox.pack(side="left", padx=150, pady=0)

label_frame = tk.Frame(scrollbox)

def update_posts(usernameforpost):
    global label_frame
    if label_frame:
        label_frame.destroy()
    label_frame = tk.Frame(scrollbox)

    post_publisher = PostPublisher(config, play_sound)
    posts = post_publisher.get_posts()

    title = tk.Label(label_frame, text='POSTS:')
    title.pack(fill="x")

    for post in posts:
        postName = post[0]
        postContent = post[1]
        postId = post[2]
        comments = post[3]

        post_text = f"Publisher: {postName}\nPost: {postContent}\nComments: {comments}\n\n"
        post_label = tk.Label(label_frame, text=post_text, wraplength=400, anchor="nw", justify="left")
        delete_button = tk.Button(label_frame, text="Delete Post", cursor="hand2", command=lambda postId=postId, postName=postName: verify_post(postId, postName))
        edit_button = tk.Button(label_frame, text="Edit Post", cursor="hand2", command=lambda postId=postId, postName=postName: edit_post(postId, postName))
        comment_button = tk.Button(label_frame, text="Add Comment", cursor="hand2", command=lambda postId=postId, postName=postName: add_comment(postId, postName))

        post_label.pack(fill="x")
        delete_button.pack(fill=tk.X, expand=True)
        edit_button.pack(fill=tk.X, expand=True)
        comment_button.pack(fill=tk.X, expand=True, pady=(0, 30))
        post_label.configure(font=("Comic Sans MS", 18))
        post_label.configure(background="black")

    scrollbox.window_create("1.0", window=label_frame)

scrollbox.configure(state='disabled')

def verify_post(postId, usernameforpost):
    print(postId)
    win = tk.Toplevel()
    window_width = 350
    window_height = 200
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Enter password to delete post...')
    win.configure(background='#272A37')
    win.resizable(False, False)

    delpost_password_entry = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), show='•', highlightthickness=1,
                               bd=0)
    delpost_password_entry.place(x=40, y=60, width=256, height=50)
    delpost_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    del_password_label = tk.Label(win, text='• Password', fg="#FFFFFF", bg='#272A37',
                               font=("Comic Sans MS", 11, 'bold'))
    del_password_label.place(x=40, y=30)

    del_pass = tk.Button(win, fg='#f8f8f8', text='Delete Post', bg='#1D90F5', font=("Comic Sans MS", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=lambda: PostPublisher(config, play_sound).delete_post(postId, usernameforpost, delpost_password_entry.get(), win, update_posts))
    del_pass.place(x=40, y=130, width=256, height=45)
def edit_post(postId, usernameforpost):
    win = tk.Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Enter password to edit post:')
    win.configure(background='#272A37')
    win.resizable(False, False)

    editpost_pass_entry = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), highlightthickness=1,
                         bd=0, show='•')
    editpost_pass_entry.place(x=40, y=80, width=256, height=50)
    editpost_pass_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label3 = tk.Label(win, text='• Password', fg="#FFFFFF", bg='#272A37',
                         font=("Comic Sans MS", 11, 'bold'))
    email_label3.place(x=40, y=50)

    edited_entry = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), highlightthickness=1,
                               bd=0)
    edited_entry.place(x=40, y=180, width=256, height=50)
    edited_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    del_password_label = tk.Label(win, text='• Edited Post', fg="#FFFFFF", bg='#272A37',
                               font=("Comic Sans MS", 11, 'bold'))
    del_password_label.place(x=40, y=150)

    del_pass = tk.Button(win, fg='#f8f8f8', text='Save Post', bg='#1D90F5', font=("Comic Sans MS", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=lambda: PostPublisher(config, play_sound).edit_post(postId, usernameforpost, editpost_pass_entry.get(), edited_entry.get(), win, update_posts))
    del_pass.place(x=40, y=260, width=256, height=45)
    update_posts(set_username_for_post)
def add_comment(postId, username):
    win = tk.Toplevel()
    window_width = 350
    window_height = 150
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Comment')
    win.configure(background='#272A37')
    win.resizable(False, False)

    comment_entry = tk.Entry(win, bg="#3D404B", font=("Comic Sans MS", 12), highlightthickness=1, insertbackground=theme_color,
                               bd=0)
    comment_entry.place(x=40, y=50, width=256, height=40)
    comment_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    del_password_label = tk.Label(win, text='• Write your Comment:', fg="#FFFFFF", bg='#272A37',
                               font=("Comic Sans MS", 11, 'bold'))
    del_password_label.place(x=40, y=20)

    del_pass = tk.Button(win, fg='#f8f8f8', text='Share Comment', bg='#1D90F5', font=("Comic Sans MS", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5", command=lambda: PostPublisher(config, play_sound).add_comment(postId, username, comment_entry.get(), win, update_posts))
    del_pass.place(x=40, y=100, width=256, height=30)
    update_posts(set_username_for_post)
update_posts(set_username_for_post)
print(set_username_for_post)
Post_publishbtn = tk.Button(
    bg_imageMain,
    text="Publish Post",
    cursor="hand2",
    command=lambda: PostPublisher(config, play_sound).publish_post(usernameforpost, post_entry.get("1.0", "end-1c"), placeholder_text, clear_post, update_posts)
)
Post_publishbtn.place(relx=0.77, rely=0.523, width=90, height=40)
ShiftKeyBoard_BTN = tk.Button(
    bg_imageMain,
    text="Wrong Keyboard?",
    cursor="shuttle",
    command=lambda: BonusReplacer().convert_to_ar(post_entry.get("1.0", "end-1c"), post_entry)
)
ShiftKeyBoard_BTN.place(relx=0.67, rely=0.523, width=120, height=40)


# Show Content Frame
def scf():
    show_frame(homepage)
    post_entry.delete("1.0", tk.END)
    typewriter_effect(post_entry, placeholder_text, 10)
    scrollbox.focus_set()
    
# FROM INTERNET
class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = ttk.Label(self.tooltip, text=self.text, background="#FFFFE0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
tooltip = Tooltip(guest, "Coming Soon...")
tooltip = Tooltip(guest2, "Coming Soon...")
tooltip = Tooltip(profile_img, "Click to upload your photo...")
tooltip = Tooltip(profile_imgposts, "Click to upload your photo...")

# TAB SYSTEM
def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    play_sound("Click")
    return "break"

window.option_add('*tearOff', False)
window.bind("<Tab>", focus_next_widget)

# Click SFX
def on_window_click(event):
    play_sound("Click")
window.bind("<Button-1>", on_window_click)

# QUIT
def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

# ENTER KEY BIND
def handle_enter(event):
    if isinstance(event.widget, tk.Entry) and event.widget in (Login_emailName_entry, Login_passwordName_entry):
        LoginSubmitButton.invoke()
    if isinstance(event.widget, tk.Entry) and event.widget in (firstName_entry, lastName_entry,  RoleName_entry, emailName_entry, passwordName_entry, confirm_passwordName_entry):
        submit_button.invoke()
    if isinstance(event.widget, tk.Entry) and event.widget in (post_entry):
        Post_publishbtn.invoke()

window.bind('<Return>', handle_enter)

# RANDOM AYAH
ayah_label = tk.Label(window, text="", font=("Comic Sans MS Bold", 19), fg="white")
ayah_label.place(x=510, y=580)

# Start updating the label
AYAH_SU = custom.EntryLabel(sign_up, RandomAyahGenerator().generate_randomAyah(), ground_color)
AYAH_SU.configure(fg="white", font=("Comic Sans MS Bold", 16 * -1),)
AYAH_SU.place(x=200, y=565)
RandomAyahGenerator().update_ayah(AYAH_SU)

AYAH_SI = custom.EntryLabel(sign_in, RandomAyahGenerator().generate_randomAyah(), ground_color)
AYAH_SI.configure(fg="white", font=("Comic Sans MS Bold", 16 * -1),)
AYAH_SI.place(x=200, y=565)
RandomAyahGenerator().update_ayah(AYAH_SI)

# SOUND
def handle_key(event):
    play_sound('Key')
window.bind("<Key>", handle_key)
# SELECT COLOR
post_entry.tag_configure("sel", background=theme_color, foreground=ground_color)

def backfunc():
    if messagebox.askokcancel("Sign Out", "Are you sure you want to sign out now?"):
        show_frame(sign_in)
        loginAccount_header.config(text="You're logged out! re-login to continue...")
# Navigation & Deletion-Draft-Code
backbtn = custom.BackButton(homepage, command=lambda: backfunc(), textf="Sign Out")
backbtn.place(x=5, y=5, width=100, height=35)
delbtn = custom.BackButton(homepage, command=lambda: 
                        #    AccountDeleter(config).DeleteYourAccount("NEW1AAAA", show_frame(sign_in), usernameforpost),
                        show_frame(sign_in),
                        textf="Delete Account")
delbtn.place(x=980, y=560, width=120, height=50)

window.mainloop()
#                            والحمد لله رب العلمين