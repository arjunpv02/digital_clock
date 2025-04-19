import tkinter as tk
from time import strftime

# Create a window
root = tk.Tk()
root.title("Digital Clock")




# Label to display the time
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='yellow')
label.pack(anchor='center')


# Run the tkinter loop
root.mainloop()