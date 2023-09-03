# import mysql.connector
# from tkinter import messagebox

# class AccountDeleter:
#     def __init__(self, config):
#         self.config = config

#     def DeleteYourAccount(self, password_input, getoutFrame, userId):
#         print(userId)
#         connection = mysql.connector.connect(**self.config)
#         cursor = connection.cursor()
#         if connection is not None:
#             select_statement = f"SELECT userId FROM User WHERE username = '{userId}'"
#             cursor.execute(select_statement)
#             result = cursor.fetchall()

#             if result:
#                 user_id = result[0][0]
#                 postdelete_statement = f"DELETE FROM Post WHERE userId = {user_id}"
#                 cursor.execute(postdelete_statement)
#                 connection.commit()
#             statement_one = "ALTER TABLE Post DROP FOREIGN KEY userId;"
#             delete_statement = f"DROP TABLE User "

#             select_query = f"SELECT * FROM User WHERE password = %s"
#             cursor.execute(select_query, (password_input,))
#             row = cursor.fetchall()
#             if row:
#                 cursor.execute(statement_one, delete_statement)
#                 messagebox.showinfo("Bye...", "Your Account was successfully deleted ):")
#                 getoutFrame
#             else:
#                 messagebox.showerror("Error!", "Invalid Password Entered")

#             connection.commit()
#             cursor.commit()
#             cursor.close()