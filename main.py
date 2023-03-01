import math
import tkinter as tk
import urllib.request
import bs4 as bs
import customtkinter
import nltk
from nltk.corpus import stopwords
import subprocess
import sys

nltk.download('punkt')
nltk.download('stopwords')

class main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

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
        self.input_type.set("text")
        self.text_input =customtkinter.CTkRadioButton(self.radiobutton_frame, text="Text", variable=self.input_type, value="text", height=30, width=30)
        self.text_input.grid(row=1, column=0, pady=2)

        self.url_input = customtkinter.CTkRadioButton(self.radiobutton_frame, text="URL", variable=self.input_type, value="url", height=30, width=40, )
        self.url_input.grid(row=1, column=1, pady=2)

        #input textbox
        self.input_textbox = tk.Text(self, font=('Arial', 12))
        self.input_textbox.configure(background=('#242424'),foreground='white', insertbackground='white')
        self.input_textbox.grid(row=1, columnspan=3, sticky="NSEW")
        

        #customization and conversion menu
        self.customization_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.customization_frame.grid(row=0, column=1, pady=5, sticky='N', ipadx=20, ipady=5)

        self.customization_frame.grid_columnconfigure((0,1,2), weight=1)
        self.customization_frame.grid_rowconfigure((0,1), weight=1)

        self.processing_label=customtkinter.CTkLabel(self.customization_frame, text="Processing", fg_color="transparent", font=('Arial', 18, 'bold'))
        self.processing_label.grid(row=0, columnspan=3)

        #TODO: validate input
        self.fontin = customtkinter.CTkEntry(self.customization_frame, width=40, placeholder_text="15pt.")
        self.fontin.grid(row=1, column=0, padx=5, pady=2.5)
        self.fontsize = self.fontin.get()

        self.bldin = customtkinter.CTkEntry(self.customization_frame, width=40, placeholder_text="30%")
        self.bldin.grid(row=1, column=1, padx=5, pady=2.5)
        self.bld = self.bldin.get()

        self.process_button = customtkinter.CTkButton(self.customization_frame, text="Submit", width=100, height=30, command=self.process_input_type)
        self.process_button.grid(row=1, column=2, padx=5, pady=2.5)

        #clear menu
        self.clear_frame = customtkinter.CTkFrame(self, corner_radius=5)
        self.clear_frame.grid(row=0, column=2, pady=5, sticky='N', ipadx=20, ipady=5)

        self.clear_frame.grid_columnconfigure((0), weight=1)
        self.clear_frame.grid_rowconfigure((0,1), weight=1)

        self.export_label = customtkinter.CTkLabel(self.clear_frame, text="Clear", fg_color="transparent", font=('Arial', 18, 'bold'))
        self.export_label.grid(row=0, columnspan=2)

        self.pdf_button = customtkinter.CTkButton(self.clear_frame,text='', width=75, height=30, command=self.clear)
        self.pdf_button.grid(row=1, column=0, padx=5, pady=2.5)



    def process_input_type(self):
        if self.input_type.get() == "text":
            self.process_text()
        elif self.input_type.get() == "url":
            self.process_url()


    def process_text(self):
        self.input = self.input_textbox.get("1.0", 'end-1c')    #read input data
        self.formatted_text = ""   

        #defaults bold percentage
        if(self.bld==''):
            self.int_bldp=30
        else:
             self.int_bldp = int(self.bld)

        #defaults font size
        if(self.fontsize==''):
            self.int_fontsize=15
        else:
            self.int_fontsize = int(self.fontsize)

        #bold text with tags <b> and </b>
        bold = customtkinter.CTkFont(family="Arial",size=15,weight="bold")
        normal = customtkinter.CTkFont(family="Arial",size=15,weight="normal")
        self.input_textbox.tag_config("normal", font=normal)
        self.input_textbox.tag_config("bold", font=bold)

        #loops through array to format text with bold tags
        for word in self.input.split():
            eindex=0
            eindex = math.ceil(len(word)*(self.int_bldp/100))   #calculates the section to bold

            self.formatted_word = ("<b>"+word[:eindex]+"</b>"+word[eindex:])  #formats text with corresponding tags
            self.formatted_text += self.formatted_word + " "    #formats word

        #creates output file
        with open('tagged_text.txt', 'w') as f:
            f.write(self.formatted_text)

        self.input_textbox.delete("1.0", "end")

        #inserts formatted text into textbox
        for word in self.formatted_text.split():
            start = word.find('<b>')+3
            cut = word.find('</b>')+4
            end = len(word)

            leftover = word[cut:len(word)]
            beginning = word[0:cut-4]

            removedstartb = beginning.replace('<b>', '')
            removedendb = removedstartb.replace('</b>', '')

            self.input_textbox.insert('end', removedendb, "bold")
            self.input_textbox.insert('end', leftover+' ', "normal")

        self.input_textbox.configure(font=('Arial', self.int_fontsize))
        
    def process_url(self):
        #read in url and parse text
        with urllib.request.urlopen(self.input_textbox.get("1.0", 'end-1c')) as url:
            source = url.read()
        soup = bs.BeautifulSoup(source, 'lxml')

        #remove all script and style elements
        text = ""
        for paragraph in soup.find_all('p'):
            text += paragraph.text

        #split text into sentences
        sentences = nltk.sent_tokenize(text)

        #clear textbox
        self.input_textbox.delete("1.0", "end")
        
        #insert sentences into textbox
        for sentence in sentences:
            self.input_textbox.insert('end', sentence)

        #process text
        self.process_text()

    def clear(self):
        self.input_textbox.delete("1.0", "end")

if __name__ == "__main__":
    app = main()
    app.mainloop()
