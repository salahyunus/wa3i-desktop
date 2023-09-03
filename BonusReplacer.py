import tkinter as tk
class BonusReplacer:
    letterReplacer = {
        "q": "ض",
        "w": "ص",
        "e": "ث",
        "r": "ق",
        "t": "ف",
        "y": "غ",
        "u": "ع",
        "i": "ه",
        "o": "خ",
        "p": "ح",
        "[": "ج",
        "]": "ة",
        "a": "ش",
        "s": "س",
        "d": "ي",
        "f": "ب",
        "g": "ل",
        "h": "ا",
        "j": "ت",
        "k": "ن",
        "l": "م",
        ";": "ك",
        "z": "ظ",
        "x": "ط",
        "c": "ذ",
        "v": "د",
        "b": "ز",
        "n": "ر",
        "m": "و"
        }
    def convert_to_ar(self, post_text, postbox):
        shifted_post = ""
        if post_text != "Write your first post for today..." and post_text != 'Another Post...':
            for char in post_text:
                if char in self.letterReplacer:
                    shifted_post += self.letterReplacer[char]
                else:
                    shifted_post += char
            postbox.delete("1.0", tk.END)
            postbox.insert("1.0", shifted_post) 

            print(shifted_post)
            return shifted_post