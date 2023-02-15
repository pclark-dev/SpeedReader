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

        self.bldin = customtkinter.CTkEntry(self.customization_frame, width=40, placeholder_text="30%")
        self.bldin.grid(row=1, column=1, padx=5, pady=2.5)
        self.bld = self.bldin.get()

        self.process_button = customtkinter.CTkButton(self.customization_frame, text="Submit", width=100, height=30, command=self.process_text)
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

    
    def process_text(self):
        self.input = self.input_textbox.get("1.0", 'end-1c')    #read input data

        #defaults bold percentage
        if(self.bld==''):
            self.int_bldp=30
        else:
             self.int_bldp = int(self.bld)

        self.formatted_text = ""

        #loops through array to format text with bold tags
        for word in self.input.split():
            eindex=0
            eindex = round(len(word)*(self.int_bldp/100))   #calculates the section to bold

            self.formatted_word = ("<b>"+word[:eindex]+"</b>"+word[eindex:])  #formats text with corresponding tags
            self.formatted_text += self.formatted_word + " "    #formats word

        #creates output file
        with open('tagged_text.txt', 'w') as f:
            f.write(self.formatted_text)

        f.close #close output file

        self.input_textbox.delete("1.0", "end")

        #TODO: Fix bolding and output
        self.input_textbox.tag_config("bold", font=("Arial", 12, "bold"))

        for word in self.formatted_text.split():
            start = word.find('<b>')+3
            end = word.find('</b>')+3

            cutword = word[start:end]
            leftover = word[end:len(word)]

            removedstartb = cutword.replace('<b>', '')
            removedendb = removedstartb.replace('</b>', '')
            
            self.input_textbox.insert('end', removedendb, "bold")
            self.input_textbox.insert('end', leftover+' ')
        

        


if __name__ == "__main__":
    app = main()
    app.mainloop()
