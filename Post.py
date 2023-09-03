import mysql.connector
from tkinter import messagebox
from ID_Generator import UserIDGenerator

class PostPublisher:
    def __init__(self, config, play_sound):
        self.config = config
        self.play_sound = play_sound

    def publish_post(self, usernameforpost, text, placeholder_text, clear_post, updateposts):
        connection = mysql.connector.connect(**self.config)
        cursor = connection.cursor()

        # user ID based on the username
        print(usernameforpost)
        cursor.execute("SELECT userId FROM User WHERE username = %s", (usernameforpost,))
        result = cursor.fetchone()
        print(cursor.statement)
        cursor.close()
        connection.close()

        if result:
            user_id = result[0]
            self.publish_post_db(usernameforpost, user_id, text, placeholder_text, clear_post)
            updateposts(usernameforpost)
        else:
            messagebox.showerror("Error!", "Invalid user selected!")

    def publish_post_db(self, username, user_id, text, placeholder_text, clear_post):
        if text == "" or text == placeholder_text or text == " " or text == 'Another Post...':
            self.play_sound('Error')
            messagebox.showerror("Error!", "You can't publish an empty post :/")
        else:
            connection = mysql.connector.connect(**self.config)
            if connection is not None:
                cursor = connection.cursor()
                random_post_id = UserIDGenerator().generate_user_id(2000)

                # Insert the post into the Post table with the username as the post name and user ID
                query = "INSERT INTO Post (postId, postName, postContent, userId, comments) VALUES (%s, %s, %s, %s, '')"
                cursor.execute(query, (random_post_id, username, text, user_id))

                connection.commit()
                cursor.close()
                connection.close()
                self.play_sound('Success')
                messagebox.showinfo("Congrats!", "You published a new post!")
                clear_post()

    def get_posts(self):
        connection = mysql.connector.connect(**self.config)
        cursor = connection.cursor()

        cursor.execute("SELECT p.postName, p.postContent, p.postId, p.comments FROM Post p JOIN User u ON p.userId = u.userId")
        posts = cursor.fetchall()

        cursor.close()
        connection.close()

        return posts

    def delete_post(self, postId, email, password, window, updator):
         # Closing window
        def exitWindow(window):
            window.destroy()
        # Check if email and password fields has input
        if password == "":
            # Show error if left empty
            self.play_sound('Error')
            messagebox.showerror("Error!", "Why did u leave it empty?!")
            # Close window
            exitWindow(window)
            return
        if email == None:
            # Show error if none
            self.play_sound('Error')
            messagebox.showerror("Error!", "Re-login and try again ): ")
            # Close window
            exitWindow(window)
            return    

        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()

        query = "SELECT * FROM User WHERE username = %s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if password != user[2]:
            self.play_sound('Success')
            messagebox.showerror("Error!", "Incorrect password")
            exitWindow(window)
            return
        
        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()

        query = "SELECT * FROM Post WHERE postId = %s"
        cursor.execute(query, (postId,))
        post = cursor.fetchone()
        if post is None:
            self.play_sound('Success')
            messagebox.showerror("Error!", "Process failed")
            exitWindow(window)
            return

        delete_query = "DELETE FROM Post WHERE postId = %s"
        cursor.execute(delete_query, (postId,))
        db.commit()

        cursor.close()
        db.close()
        self.play_sound('Success')
        messagebox.showinfo("Success!", "Post deleted successfully!")
        updator(email)
        exitWindow(window)

    def edit_post(self, postId, email, password, editedPost, window, updator):
        # Closing window
        def exitWindow(window):
            window.destroy()

        # Check if email and password fields have input
        if password == "" or editedPost == "":
            # Show error if left empty
            self.play_sound('Error')
            messagebox.showerror("Error!", "Why did you leave it empty?!")
        # Close window
            exitWindow(window)
            return

        if email is None:
            # Show error if None
            self.play_sound('Error')
            messagebox.showerror("Error!", "Re-login and try again ): ")
            # Close window
            exitWindow(window)
            return

        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()

        query = "SELECT * FROM User WHERE username = %s"
        print(email)
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user is None:
            self.play_sound('Error')
            messagebox.showerror("Error!", "User not found")
            exitWindow(window)
            return
        if password != user[2]:
            self.play_sound('Success')
            messagebox.showerror("Error!", "Incorrect password")
            exitWindow(window)
            return

        query = "SELECT * FROM Post WHERE postId = %s"
        cursor.execute(query, (postId,))
        post = cursor.fetchone()

        if post is None:
            self.play_sound('Error')
            messagebox.showerror("Error!", "Process failed")
            exitWindow(window)
            return

        edit_query = "UPDATE Post SET postContent = %s WHERE postId = %s"
        cursor.execute(edit_query, (editedPost, postId))
        db.commit()

        cursor.close()
        db.close()
        self.play_sound('Success')
        messagebox.showinfo("Success!", "Post edited successfully!")
        updator(email)
        exitWindow(window)

    def add_comment(self, postId, email, comment_text, window, updator):
        # Closing window
        def exitWindow(window):
            window.destroy()

        # Check if email and password fields have input
        if comment_text == "":
            # Show error if left empty
            self.play_sound('Error')
            messagebox.showerror("Error!", "Why did you leave it empty?!")
        # Close window
            exitWindow(window)
            return

        if email is None:
            # Show error if None
            self.play_sound('Error')
            messagebox.showerror("Error!", "Re-login and try again ): ")
            # Close window
            exitWindow(window)
            return

        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()

        query = "SELECT * FROM Post WHERE postId = %s"
        cursor.execute(query, (postId,))
        post = cursor.fetchone()

        if post is None:
            self.play_sound('Error')
            messagebox.showerror("Error!", "Process failed")
            exitWindow(window)
            return
        current_comments = post[4]
        postName = post[1]
        updated_comments = f"\n{email}: \n {comment_text}\n\n {current_comments}"

        comments_query = "UPDATE Post SET comments = %s WHERE postId = %s"
        cursor.execute(comments_query, (updated_comments, postId))
        db.commit()

        cursor.close()
        db.close()
        self.play_sound('Success')
        messagebox.showinfo("Success!", "Your comment was saved!")
        updator(email)
        exitWindow(window)

    def get_image_data(self, username):
            connection = mysql.connector.connect(**self.config)
            if connection is not None:
                cursor = connection.cursor()

                query = "SELECT Image FROM User WHERE username = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()

                if result:
                    image_data = result[0]
                    return image_data

                connection.close()

            return None