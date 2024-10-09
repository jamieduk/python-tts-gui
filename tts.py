import subprocess
import tkinter as tk
from tkinter import ttk

class TextToSpeechApp:
    def __init__(self, root):
        self.root=root
        self.default_voice='en'
        self.tts_box=tk.Text(self.root, height=10, width=40)
        self.tts_box.pack()
        self.say_button=tk.Button(self.root, text="Say it", command=self.speak_text)
        self.say_button.pack()
        self.voice_var=tk.StringVar(self.root)
        self.voice_var.set(self.default_voice)  # default value
        self.voices_menu=ttk.Combobox(self.root, values=['en'], textvariable=self.voice_var)
        self.voices_menu.pack()

    def speak_text(self):
        text=self.tts_box.get('1.0', tk.END)
        if text:
            voice_name=self.voice_var.get()
            subprocess.call(["/usr/bin/espeak", "-v", f"{voice_name}", text])

if __name__ == "__main__":
    root=tk.Tk()
    app=TextToSpeechApp(root)
    root.mainloop()
