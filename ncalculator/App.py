from tkinter import ttk, Tk, StringVar


class App():
    SPECIAL_BUTTONS = ["MC", "MR", "M+", "M-", "MS"]
    BUTTONS = ["%", "√", "x²", "1/x",
               "CE", "C",  "⌫", "/",
               "7", "8", "9", "*",
               "4", "5", "6", "－",
               "1", "2", "3", "+",
               "+", "0", ".", "="]
    FONT = ("Arial", 20, "bold")
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.frame = ttk.Frame(self.window)
        self.window.geometry("410x500+20+20")
        self.window.resizable(False, True),
        self.__text_field()
        self.__buttons()

    def __text_field(self):
        entry = ttk.Label(justify="left", anchor="se", 
                          text="12314", background="#FFFFFF", padding=(30, 10), font=self.FONT)
        entry.grid(row=0, column=0, columnspan=20, sticky="nsew")
        self.window.grid_rowconfigure(0, weight=2)
        for i in range(len(self.SPECIAL_BUTTONS)):
            btn_text = self.SPECIAL_BUTTONS[i]
            ttk.Button(self.window, text=btn_text).grid(row=1, column=i * 4, sticky="snwe", columnspan=4)
            # self.window.grid_columnconfigure(i, minsize=10, weight=2)
        row = 2
        first_button_on_row = True
        for i in range(len(self.BUTTONS)):
            col = i % 4 
            btn_text = self.BUTTONS[i]
            ttk.Button(self.window, text=btn_text).grid(row=row, column=col * 5, sticky="snwe", columnspan=5)
            # self.window.grid_columnconfigure(i, minsize=30, weight=2)
            # self.window.co
            if (i + 1) % 4 == 0 and not first_button_on_row:
                row += 1
                first_button_on_row = True
            else:
                first_button_on_row = False
        
        # entry.pack()
        # ttk.Label(self.window, text="hello", font=("Arial", 20, "bold"),
        #           background="red", foreground="#FFFFFF",
        #           padding=(50, 50), justify="center", anchor="n").pack(anchor="e")
        # ttk.Label(self.window, text="hello", font=("Arial", 20, "bold"),
        #           background="red", foreground="#FFFFFF",
        #           padding=(50, 50), justify="center", anchor="n").pack(anchor="w")

    
    def __buttons(self):
        pass
    
    def __validate():
        pass
    
    def run(self):
        self.window.mainloop()
