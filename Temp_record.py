import tkinter as tk

class DailySmogLog:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Daily Smog Log")
        self.master.configure(bg='#a1dbcd')
        
        self.smog_label = tk.Label(self.master, text="Smog Level:", font=("Helvetica", 14), bg='#a1dbcd')
        self.smog_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.log_button = tk.Button(self.master, text="Log", font=("Helvetica", 14), bg='#74c476', command=self.log_smog)
        self.display_label = tk.Label(self.master, text="Smog Log:", font=("Helvetica", 14), bg='#a1dbcd')
        self.smog_log = tk.Listbox(self.master, font=("Helvetica", 14), bg='#74c476')

        self.smog_label.pack()
        self.smog_entry.pack()
        self.log_button.pack()
        self.display_label.pack()
        self.smog_log.pack(fill=tk.BOTH, expand=True)

    def log_smog(self):
        smog_level = self.smog_entry.get()
        self.smog_log.insert(tk.END, smog_level)

if __name__ == "__main__":
    root = tk.Tk()
    app = DailySmogLog(root)
    root.mainloop()
