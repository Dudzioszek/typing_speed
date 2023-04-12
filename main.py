import tkinter as tk
import time

class TypingSpeedApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed App")
        self.master.geometry("400x300")
        
        self.text = "The quick brown fox jumps over the lazy dog. " \
                    "This is a sample text to test your typing speed. " \
                    "Try to type it as quickly and accurately as possible."
        
        self.label = tk.Label(self.master, text=self.text, wraplength=380)
        self.label.pack(pady=10)
        
        self.input_entry = tk.Entry(self.master)
        self.input_entry.pack(pady=10)
        self.input_entry.bind('<Return>', self.check_typing_speed)
        
        self.start_time = None
        self.end_time = None
        
    def start_typing(self, event):
        if not self.start_time:
            self.start_time = time.time()
    
    def check_typing_speed(self, event):
        if not self.end_time:
            self.end_time = time.time()
            elapsed_time = self.end_time - self.start_time
            
            user_input = self.input_entry.get()
            words_per_minute = len(user_input.split()) / elapsed_time * 60
            self.label.config(text=f"You spent {elapsed_time:.2f} seconds on typing! Your typing speed is: {words_per_minute:.2f} words per minute.")
            
            self.input_entry.delete(0, tk.END)
            self.start_time = None
            self.end_time = None

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.bind('<KeyPress>', app.start_typing)
    root.mainloop()
