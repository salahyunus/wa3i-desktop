# SQL Connector
import mysql.connector
# Message box for alerting
from tkinter import messagebox

class PasswordChanger():
    # Function for saving to database
    def forgot_password_db(self, email, new_password, window):
        # Closing window
        def exitWindow(window):
            window.destroy()
        # Check if email and password fields has input
        if email == "" or new_password == "":
            # Show error if left empty
            messagebox.showerror("Error!", "Why did u leave it empty?!")
            # Close window
            exitWindow(window)
            return
        # Connecting to database
        db = mysql.connector.connect(
            host='localhost',
            database='United_DB',
            user='root',
            password='Yeer2023'
            )
        # cursor
        cursor = db.cursor()
        # Query
        query = 'SELECT * FROM User WHERE username = %s'
        cursor.execute(query, [(email)])
        # Fetch username only use with select
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror("Error!", "Invalid Email 🤨!")
            exitWindow(window)
            return
        query = '''UPDATE User SET Password = %s WHERE username = %s'''
        cursor.execute(query, [new_password, email])
        # commit changes to db
        db.commit()
        # close db
        db.close()
        # show success alert
        messagebox.showinfo("Success!", "Password was successfully changed!")
        exitWindow(window)