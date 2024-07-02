import tkinter as tk
from tkinter import messagebox

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.time = 0
        self.update_time()

        
        self.time_label = tk.Label(root, text=self.format_time(), font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=20)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=20)

    def update_time(self):
        if self.running:
            self.time += 1
            self.time_label.config(text=self.format_time())
        self.root.after(1000, self.update_time)

    def format_time(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def start(self):
        if not self.running:
            self.running = True

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.time_label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
