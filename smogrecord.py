import tkinter as ttk

class DailySmogLog:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("บันทึกค่าหมอกควัน ในจังหวัดลำปาง")
        self.master.configure(bg='#CD5C5C')
        
        self.smog_label = ttk.Label(self.master, text="ระดับค่าหมอกควัน:", font=("Pattaya", 35), bg='#a1dbcd')
        self.smog_entry = ttk.Entry(self.master, font=("Pattaya", 16))
        self.log_button = ttk.Button(self.master, text="บันทึกค่า", font=("Pattaya",20), bg='#74c476', command=self.log_smog)
        self.display_label = ttk.Label(self.master, text="แสดงค่าข้อมูลย้อนหลัง:", font=("Pattaya", 14), bg='#a1dbcd')
        self.smog_log = ttk.Listbox(self.master, font=("Pattaya", 16), bg='#D3D3D3')

        self.smog_label.pack()
        self.smog_entry.pack()
        self.log_button.pack()
        self.display_label.pack()
        self.smog_log.pack(fill=ttk.BOTH, expand=True)

    def log_smog(self):
        smog_level = self.smog_entry.get()
        self.smog_log.insert(ttk.END, smog_level)

if __name__ == "__main__":
    root = ttk.Tk()
    app = DailySmogLog(root)
    root.mainloop()
