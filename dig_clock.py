import tkinter as tk
from time import strftime

# Create a window
root = tk.Tk()
root.title("Digital Clock")

# Function to update the time on the clock
def time():
    string = strftime('%H:%M:%S %p')  # Format for hour:minute:second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1000ms (1 second)

# Label to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='yellow')
label.pack(anchor='center')

time()  # Call the time function to start the clock

# Run the tkinter loop
root.mainloop()
