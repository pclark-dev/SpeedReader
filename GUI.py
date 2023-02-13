import customtkinter

class GUI(customtkinter.CTk):
    def __init__(self):

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("800x500")
        self.root.title("Speed Read")

        self.buttonframes = customtkinter.CTkFrame(master=self.root)
        self.buttonframes.pack()
        self.buttonframes.grid_rowconfigure(1, weight=1)
        self.buttonframes.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)

        self.input_type = customtkinter.StringVar()
        self.text_input =customtkinter.CTkRadioButton(self.buttonframes, text="Text", variable=self.input_type, value="text")
        self.url_input = customtkinter.CTkRadioButton(self.buttonframes, text="URL", variable=self.input_type, value="url")
        self.text_input.grid(row=0, column=0, sticky="ew")
        self.url_input.grid(row=0, column=1, sticky="ew")

        self.fontsize = customtkinter.StringVar()
        self.fontin = customtkinter.CTkEntry(self.buttonframes, width=2, textvariable=self.fontsize)
        self.bldpercentage = customtkinter.StringVar()
        self.bldin = customtkinter.CTkEntry(self.buttonframes, width=2, textvariable=self.bldpercentage)
        self.fontin.grid(row=0, column=2, sticky="ew")
        self.bldin.grid(row=0, column=3, sticky="ew")

        self.root.mainloop()

GUI()