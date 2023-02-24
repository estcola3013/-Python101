import tkinter as tk
import datetime
import csv

# Create a dictionary to store attendance data
attendance = {}

# Define a function to record attendance
def record_attendance():
    name = name_entry.get()
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if name in attendance:
        if attendance[name]['check_in'] is None:
            attendance[name]['check_in'] = time
        else:
            attendance[name]['check_out'] = time
    else:
        attendance[name] = {'check_in': time, 'check_out': None}
    update_display()

# Define a function to update the display
def update_display():
    display_text.delete('1.0', tk.END)
    display_text.insert(tk.END, 'Name\tCheck-In\tCheck-Out\n')
    for name, data in attendance.items():
        check_in = data['check_in'] if data['check_in'] is not None else ''
        check_out = data['check_out'] if data['check_out'] is not None else ''
        display_text.insert(tk.END, f'{name}\t{check_in}\t{check_out}\n')
    save_button['state'] = tk.NORMAL

# Define a function to save attendance data to a CSV file
def save_data():
    with open('attendance.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Check-In', 'Check-Out'])
        for name, data in attendance.items():
            check_in = data['check_in'] if data['check_in'] is not None else ''
            check_out = data['check_out'] if data['check_out'] is not None else ''
            writer.writerow([name, check_in, check_out])
    save_button['state'] = tk.DISABLED

# Create the main window
window = tk.Tk()
window.title('Time Attendance Program')
window.configure(bg='yellow')

# Create the widgets
name_label = tk.Label(window, text='Name:', bg='blue')
name_entry = tk.Entry(window)
check_in_label = tk.Label(window, text='Check-In:', bg='green')
check_in_entry = tk.Entry(window, state=tk.DISABLED)
check_out_label = tk.Label(window, text='Check-Out:', bg='red')
check_out_entry = tk.Entry(window, state=tk.DISABLED)
record_button = tk.Button(window, text='Check-In&Check-Out', command=record_attendance)
display_text = tk.Text(window, width=50, height=10)
save_button = tk.Button(window, text='Save Data', command=save_data, state=tk.DISABLED)

# Position the widgets using the grid geometry manager
name_label.grid(row=0, column=0, sticky='e')
name_entry.grid(row=0, column=1)
check_in_label.grid(row=1, column=0, sticky='e')
check_in_entry.grid(row=1, column=1)
check_out_label.grid(row=2, column=0, sticky='e')
check_out_entry.grid(row=2, column=1)
record_button.grid(row=3, column=0, columnspan=2)
display_text.grid(row=4, column=0, columnspan=2)
save_button.grid(row=5, column=0, columnspan=2)

# Start the main event loop
window.mainloop()
