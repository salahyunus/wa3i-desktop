# Just examples of how to use classes for gui, not that good
import tkinter as tk
class SloganHeader(tk.Label):
    def __init__(self, parent, texter):
        super().__init__(
            parent,
            anchor="nw",
            text=texter,
            fg="#FFFFFF",
            font=("Comic Sans MS Bold", 20),
            bg="#272A37"
        )
class AccountHeaderLabel(tk.Label):
    def __init__(self, parent, textfor):
        super().__init__(
            parent,
            text=textfor,
            fg="#FFFFFF",
            font=("Comic Sans MS Bold", 28),
            bg="#272A37"
        )
class SwitchText(tk.Label):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            fg="#FFFFFF",
            font=("Comic Sans MS Regular", 15),
            bg="#272A37"
        )
class SloganImg(tk.Label):
    def __init__(self, parent, image):
        super().__init__(
            parent,
            image=image,
            bg="#272A37"
        )
class LogoText(tk.Label):
    def __init__(self, parent, text):
        super().__init__(
            parent,
            text=text,
            fg="#FFFFFF",
            font=("Comic Sans MS bold", 20 * -1, 'bold'),
            bg="#272A37"
        )
class LogoImg(tk.Label):
    def __init__(self, parent, image, bg):
        super().__init__(parent, image=image, bg=bg)
class BackgroundImageLabel(tk.Label):
    def __init__(self, parent, image, bg):
        super().__init__(parent, image=image, bg=bg)
class SwitchAuthButton(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command, fg="#206DB4",
                         font=("Comic Sans MS Regular", 15 * -1), bg="#272A37",
                         bd=0, cursor="hand2", activebackground="#272A37",
                         activeforeground="#ffffff")
class IconLabel(tk.Label):
    def __init__(self, parent, image, bg):
        super().__init__(parent, image=image, bg=bg)
class BackButton(tk.Button):
    def __init__(self, parent, command, textf):
        super().__init__(
            parent,
            text=textf,
            fg="#206DB4",
            font=("Comic Sans MS", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command= command
        )
class GuestBtn(tk.Button):
    def __init__(self, parent, bg, command, status):
        super().__init__(
            parent,
            text="Continue as Guest",
            fg="#206DB4",
            font=("Comic Sans MS", 15 * -1),
            bg=bg,
            bd=0,
            cursor="X_cursor",
            activebackground=bg,
            activeforeground="#ffffff",
            command= command,
            # Disabled for now
            state=status
        )
class EntryLabel(tk.Label):
    def __init__(self, parent, textfor, bg):
        super().__init__(
            parent,
            text=textfor,
            fg="#272A37",
            font=("Comic Sans MS Bold", 13 * -1),
            bg=bg
        )
class SubmitButton(tk.Button):
    def __init__(self, parent, command, img, bg):
        super().__init__(
        parent,
        image=img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground=bg,
        cursor="pointinghand",
        command= command
        )
class bottomHeader(tk.Label):
    def __init__(self, parent, bg):
        super().__init__(
        parent,
        text="Salah, Belal & Karim 👨‍💻",
        fg="#FFFFFF",
        font=("Comic Sans MS bold", 20 * -1),
        bg=bg
        )
class EntryConstructor(tk.Entry):
    def __init__(self, parent, textvariable, bg, showvar):
        super().__init__(
        parent,
        bd=0,
        bg=bg,
        highlightthickness=0,
        font=("Comic Sans MS SemiBold", 17 * -1),
        # Text variable dynamically updates
        textvariable=textvariable,
        show=showvar
        )
class LoginEntryLabel(tk.Label):
    def __init__(self, parent, textfor):
        super().__init__(
            parent,
            text=textfor,
            fg="#FFFFFF",
            font=("Comic Sans MS", 13 * -1),
            bg='#F4BC21'
        )
class LoginEntryConstructor(tk.Entry):
    def __init__(self, parent, textvariable, bg, showvar):
        super().__init__(
        parent,
        bd=0,
        bg=bg,
        highlightthickness=0,
        font=("Comic Sans MS Bold", 16 * -1),
        # Text variable dynamically updates
        textvariable=textvariable,
        show=showvar
        )