import mysql.connector
from tkinter import messagebox
class LoginManager:
    def __init__(self, config):
        self.config = config

    def login(self, username, password, clear_login, scf, play_sound):
        connection = mysql.connector.connect(**self.config)
        if connection is not None:
            try:
                cursor = connection.cursor()
                find_user = "SELECT * FROM User WHERE username = %s AND password = %s"
                cursor.execute(find_user, (username, password))
                result = cursor.fetchall()
                if result:
                    logged_in_username = result[0][1]

                    play_sound("Success")
                    messagebox.showinfo("Success!", f"You're now logged in as {logged_in_username}!")
                    clear_login()
                    # Show Content Frame
                    scf()
                    return logged_in_username  # Return the username
                else:
                    play_sound("Error")
                    messagebox.showerror("Failed!", "Please Recheck your Email/Password and try again")
            except mysql.connector.Error as error:
                messagebox.showerror("Error!", f"An error occurred: {error}")
            finally:
                cursor.close()
                connection.close()
        else:
            messagebox.showerror("Failed!", "Failed to connect to the database.")