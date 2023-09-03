"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Main.py']
DATA_FILES = [
    "assets/12.png",
    "assets/54.jpeg",
    "assets/APPICON.ico",
    "assets/BACKGROUND.png",
    "assets/button_1.png",
    "assets/custom_cursor.png",
    "assets/database final project .pdf",
    "assets/email-icon.png",
    "assets/email.png",
    "assets/headerText_image.png",
    "assets/HidePass.png",
    "assets/image_1.png",
    "assets/input_img.png",
    "assets/name_icon.png",
    "assets/pass-icon.png",
    "assets/ShowPass.png",
    "assets/SloganIMG.png",
    "assets/SPLASH.gif",
    "assets/UserIMG.png",
    "assets/UserIMGDRAFT.png",
    "GUI.py",
    "ID_Generator.py",
    "LoginDB.py",
    "ResetPassword.py",
    "SignupDB.py",
    "RandomAyah.py",
    "SplashScreener.py",
    "Post.py",
    "audio/Click.mp3",
    "audio/Error.mp3",
    "audio/Intro.mp3",
    "audio/Key.mp3",
    "audio/Success.mp3"
]
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)