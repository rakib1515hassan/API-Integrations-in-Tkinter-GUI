import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class FacebookLikesApp:
    def __init__(self, root):
        self.root = root
        self.root.resizable(0, 0)
        self.root.title("Facebook likes v. 1.0")

        frame = tk.Frame(root)
        frame.pack(padx=10,pady=20)

        ##! Frame for URL, Amount and Profiles
        infoFrame = tk.Frame(frame)
        infoFrame.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

        ##? URL Entry
        tk.Label(infoFrame, text="URL:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.url_entry = tk.Entry(infoFrame, width=60, font=('Microsoft Yahei UI Light', 11, 'bold'))
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        ##? Amount Entry
        tk.Label(infoFrame, text="Amount:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.amount_entry = tk.Entry(infoFrame, width=60, font=('Microsoft Yahei UI Light', 11, 'bold'))
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5)

        ##? Profiles Entry
        tk.Label(infoFrame, text="Profiles:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.profiles_entry = tk.Entry(infoFrame, width=60, font=('Microsoft Yahei UI Light', 11, 'bold'))
        self.profiles_entry.grid(row=2, column=1, padx=10, pady=5)




        ##! Frame for Type and Instances
        typeFrame = tk.Frame(frame)
        typeFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        ##? Type Dropdown
        tk.Label(typeFrame, text="Type:").grid(row=0, column=0, padx=20, pady=5, sticky='e')
        self.type_var = tk.StringVar()
        self.type_dropdown = ttk.Combobox(typeFrame, textvariable=self.type_var, values=["Type1", "Type2", "Type3"], width=20, font=('Microsoft Yahei UI Light', 11, 'bold'))
        self.type_dropdown.grid(row=0, column=1, padx=10, pady=5)

        ##? Instances Dropdown
        tk.Label(typeFrame, text="Instances:").grid(row=0, column=2, padx=10, pady=5, sticky='e')
        self.instances_var = tk.StringVar()
        self.instances_dropdown = ttk.Combobox(typeFrame, textvariable=self.instances_var, values=["1", "2", "3", "4", "5"], width=20,font=('Microsoft Yahei UI Light', 11, 'bold'))
        self.instances_dropdown.grid(row=0, column=3, padx=10, pady=5)


        ##! Button and Progress Bar
        ##? Start Button
        self.start_button = tk.Button(frame, text="Start", command=self.start_process, width=10)
        self.start_button.grid(row=0, column=2, rowspan=2, padx=10, pady=5, sticky='nsew')

        ##? Progress Bar
        self.progress = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=4, column=0, columnspan=4, padx=10, pady=5)




    def start_process(self):
        # Placeholder function to start the process
        print("Start button clicked")
        print("URL:", self.url_entry.get())
        print("Amount:", self.amount_entry.get())
        print("Profiles:", self.profiles_entry.get())
        print("Type:", self.type_var.get())
        print("Instances:", self.instances_var.get())





if __name__ == "__main__":
    root = tk.Tk()
    app = FacebookLikesApp(root)
    root.mainloop()
