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

        self.input_label = customtkinter.CTkLabel(self.radiobutton_frame, text="Input", fg_color="transparent", width=30, font=('Arial', 18, 'bold'))
        self.input_label.grid(row=0, columnspan=2)

        self.input_type = customtkinter.StringVar()
        self.text_input =customtkinter.CTkRadioButton(self.radiobutton_frame, text="Text", variable=self.input_type, value="text", height=30, width=30)
        self.text_input.grid(row=1, column=0, pady=2)

        self.url_input = customtkinter.CTkRadioButton(self.radiobutton_frame, text="URL", variable=self.input_type, value="url", height=30, width=40, )
        self.url_input.grid(row=1, column=1, pady=2)

        #input textbox
        self.input_textbox = customtkinter.CTkTextbox(self, font=('Arial', 12))
        self.input_textbox.grid(row=1, columnspan=3, sticky="NSEW")
        self.input = self.input_textbox.get("0.0", "end")

        #customization and conversion menu
        self.customization_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.customization_frame.grid(row=0, column=1, pady=5, sticky='N', ipadx=20, ipady=5)

        self.customization_frame.grid_columnconfigure((0,1,2), weight=1)
        self.customization_frame.grid_rowconfigure((0,1), weight=1)

        self.processing_label=customtkinter.CTkLabel(self.customization_frame, text="Processing", fg_color="transparent", font=('Arial', 18, 'bold'))
        self.processing_label.grid(row=0, columnspan=3)

        #TODO: validate input
        self.fontin = customtkinter.CTkEntry(self.customization_frame, width=40, placeholder_text="12pt.")
        self.fontin.grid(row=1, column=0, padx=5, pady=2.5)

        self.bldin = customtkinter.CTkEntry(self.customization_frame, width=40, placeholder_text="25%")
        self.bldin.grid(row=1, column=1, padx=5, pady=2.5)
        self.bld = self.bldin.get()

        self.process_button = customtkinter.CTkButton(self.customization_frame, text="Submit", width=100, height=30, command=self.process_text(self.input, self.bld))
        self.process_button.grid(row=1, column=2, padx=5, pady=2.5)

        #export menu
        self.export_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.export_frame.grid(row=0, column=2, pady=5, sticky='N', ipadx=20, ipady=5)

        self.export_frame.grid_columnconfigure((0,1), weight=1)
        self.export_frame.grid_rowconfigure((0,1), weight=1)

        self.export_label = customtkinter.CTkLabel(self.export_frame, text="Export", fg_color="transparent", font=('Arial', 18, 'bold'))
        self.export_label.grid(row=0, columnspan=2)

        self.pdf_button = customtkinter.CTkButton(self.export_frame, text="PDF", width=75, height=30)
        self.pdf_button.grid(row=1, column=0, padx=5, pady=2.5)

        self.docx_button = customtkinter.CTkButton(self.export_frame, text="DOCX", width=75, height=30)
        self.docx_button.grid(row=1, column=1, padx=5, pady=2.5)

        

    #TODO: fix writing to file
    def process_text(self, input: str, bldp: str):
        if(bldp==''):
            self.int_bldp=25
        else:
             self.int_bldp = int(bldp)
       
        #opens new file to write formatted input text
        self.taggedfile = open("tagged_text.txt", "w+")

        #splits text into array of words
        self.split_text = input.split()

        #loops through array to format text with bold tags
        for word in self.split_text:
            eindex=0
            eindex = round(word.len()*(self.int_bldp/100))   #calculates the section to bold

            self.taggedfile.write("<b>"+word[:eindex]+"<b>"+word[eindex:]+" ")  #formats text with corresponding tags

        #closes txt file
        self.taggedfile.close()



if __name__ == "__main__":
    app = main()
    app.mainloop()
