import customtkinter

class main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #window theme
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        #window config
        self.geometry("800x500")
        self.title("Speed Read")

        #grid config
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0,1,2), weight=1)

        #radio buttons for input
        self.radiobutton_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.radiobutton_frame.grid(row=0, column=0, pady=5, sticky='N', ipadx=20, ipady=5)

        self.radiobutton_frame.grid_columnconfigure((0,1), weight=1)
        self.radiobutton_frame.grid_rowconfigure((0,1), weight=1)

        self.input_label = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Input", fg_color="transparent", width=30, font=('Arial', 18))
        self.input_label.grid(row=0, columnspan=2)

        self.input_type = customtkinter.StringVar()
        self.text_input =customtkinter.CTkRadioButton(self.radiobutton_frame, text="Text", variable=self.input_type, value="text", height=30, width=30)
        self.text_input.grid(row=1, column=0, pady=2)

        self.url_input = customtkinter.CTkRadioButton(self.radiobutton_frame, text="URL", variable=self.input_type, value="url", height=30, width=40, )
        self.url_input.grid(row=1, column=1, pady=2)

        #customization and conversion menu
        self.customization_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.customization_frame.grid(row=0, column=1, pady=5, sticky='N', ipadx=20, ipady=5)

        self.customization_frame.grid_columnconfigure((0,1,2), weight=1)
        self.customization_frame.grid_rowconfigure((0,1), weight=1)

        self.processing_label=customtkinter.CTkLabel(master=self.customization_frame, text="Processing", fg_color="transparent", font=('Arial', 18))
        self.processing_label.grid(row=0, columnspan=3)
        
        #TODO: figure out how to only allow the entry of 2 numbers and display hint text
        self.fontsize = customtkinter.IntVar()
        self.fontin = customtkinter.CTkEntry(self.customization_frame, width=40, textvariable=self.fontsize, placeholder_text="12pt.", insertwidth=2)
        self.fontin.grid(row=1, column=0, padx=5, pady=2.5)

        self.bldpercentage = customtkinter.StringVar()
        self.bldin = customtkinter.CTkEntry(self.customization_frame, width=40, textvariable=self.bldpercentage, placeholder_text="25%", placeholder_text_color="White")
        self.bldin.grid(row=1, column=1, padx=5, pady=2.5)

        self.process_button = customtkinter.CTkButton(master=self.customization_frame, text="Submit", width=100, height=30)
        self.process_button.grid(row=1, column=2, padx=5, pady=2.5)

        #export menu
        self.export_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.export_frame.grid(row=0, column=2, pady=5, sticky='N', ipadx=20, ipady=5)

        self.export_frame.grid_columnconfigure((0,1), weight=1)
        self.export_frame.grid_rowconfigure((0,1), weight=1)

        self.export_label = customtkinter.CTkLabel(master=self.export_frame, text="Export", fg_color="transparent", font=('Arial', 18))
        self.export_label.grid(row=0, columnspan=2)

        self.pdf_button = customtkinter.CTkButton(master=self.export_frame, text="PDF", width=75, height=30)
        self.pdf_button.grid(row=1, column=0, padx=5, pady=2.5)

        self.docx_button = customtkinter.CTkButton(master = self.export_frame, text="DOCX", width=75, height=30)
        self.docx_button.grid(row=1, column=1, padx=5, pady=2.5)

        

if __name__ == "__main__":
    app = main()
    app.mainloop()
