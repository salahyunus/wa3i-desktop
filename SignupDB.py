import mysql.connector
from tkinter import messagebox
from ID_Generator import UserIDGenerator
from PIL import Image, ImageTk, ImageDraw
# REGEX:
import re

class SignupManager:
    def __init__(self, config):
        self.config = config

    def signupDB(self, first_name, last_name, password, email, confirm_password, role, clear_signup, scf, play_sound, image_path):
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, image.width, image.height), fill=255)
        image = Image.composite(image, Image.new("RGBA", image.size, 0), mask)
        image_data = image.tobytes()
        print(image_data)
        if first_name == "" or last_name == "" or password == "" or email == "" or confirm_password == "":
            play_sound("Error")
            messagebox.showerror("Error", "All Fields Are Required!")
        elif not re.search(r"[a-z]", first_name) or not re.search(r"[a-z]", last_name) or not re.search(r"[a-z]", email):
            play_sound("Error")
            messagebox.showerror("Error", "All Fields Are Required!")
        elif password != confirm_password:
            play_sound("Error")
            messagebox.showerror("Error", "Passwords don't match!")
        elif len(password) < 8:
            play_sound("Error")
            messagebox.showerror("Error", "Password should be at least 8 characters")
            # \d means digit (number)
        elif not re.search(r"\d", password):
            play_sound("Error")
            messagebox.showerror("Error", "Password should contain at least one number character")
        elif not re.search(r"[A-Z]", password):
            play_sound("Error")
            messagebox.showerror("Error", "Password should contain at one or more uppercase letter")
        elif email.find("@") == -1 or email.find(".com") == -1:
            play_sound("Error")
            messagebox.showerror("Error", "Please use a valid email. Example: exampleemail@exmple.com")
        elif role != "Admin" and role != "Member":
            play_sound("Error")
            messagebox.showerror("Error", "Your Role must be either 'Admin' or 'Member'!")
        else:
            connection = mysql.connector.connect(**self.config)
            if connection is not None:
                cursor = connection.cursor()
                random_user_id = UserIDGenerator().generate_user_id(999)

                query = "INSERT INTO User (userID, username, password, fullName, role, Image) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (random_user_id, email, password, first_name + " " + last_name, role, image_data))

                # Commit the changes to the database
                connection.commit()

                username = email 

                connection.close()
                clear_signup()
                play_sound("Success")
                messagebox.showinfo("Success!", "New Account Created Successfully!")
                scf()
                return username
