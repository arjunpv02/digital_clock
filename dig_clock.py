import tkinter as tk
from time import strftime

# Create a window
root = tk.Tk()
root.title("Digital Clock tkinter")

# Set window size (width x height) and background color
root.geometry("400x200")  # Width: 400px, Height: 200px
root.configure(bg='white')  # Background color

# Function to update the time on the clock
def time():
    string = strftime('%H:%M:%S %p')  # Format for hour:minute:second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update the time every 1000ms (1 second)

# Heading Label
heading = tk.Label(root, text="Digital Clock", font=('calibri', 20, 'bold'), background='white', foreground='black')
heading.pack(anchor='n', pady=10)

# Label to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='white', foreground='yellow')
label.pack(anchor='center')



# Run the tkinter loop
root.mainloop()
