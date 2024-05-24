import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes("-toolwindow", True)
        self.window.title('Calculator')
        self.window.geometry('385x450')
        self.window.resizable(False, False)

        self.padding: dict = {'padx': 10, 'pady': 10}
        but = {'width': 7, 'height': 3}

        self.input_field = tk.Entry(self.window, font=('Arial', 24), borderwidth=2)
        # self.input_field.configure(state='readonly')
        self.input_field.grid(row=0, column=0, columnspan=4, **self.padding)

        self.button1 = tk.Button(self.window, text='1', width=but['width'], height=but['height'], command=lambda x='1': self.click_event(x))
        self.button1.grid(row=1, column=0, **self.padding)
        self.button2 = tk.Button(self.window, text='2', width=but['width'], height=but['height'], command=lambda x='2': self.click_event(x))
        self.button2.grid(row=1, column=1, **self.padding)
        self.button3 = tk.Button(self.window, text='3', width=but['width'], height=but['height'], command=lambda x='3': self.click_event(x))
        self.button3.grid(row=1, column=2, **self.padding)
        self.button_plus = tk.Button(self.window, text='+', width=but['width'], height=but['height'], command=lambda x='+': self.click_event(x))
        self.button_plus.grid(row=1, column=3, **self.padding)

        self.button4 = tk.Button(self.window, text='4', width=but['width'], height=but['height'], command=lambda x='4': self.click_event(x))
        self.button4.grid(row=2, column=0, **self.padding)
        self.button5 = tk.Button(self.window, text='5', width=but['width'], height=but['height'], command=lambda x='5': self.click_event(x))
        self.button5.grid(row=2, column=1, **self.padding)
        self.button6 = tk.Button(self.window, text='6', width=but['width'], height=but['height'], command=lambda x='6': self.click_event(x))
        self.button6.grid(row=2, column=2, **self.padding)
        self.button_minus = tk.Button(self.window, text='-', width=but['width'], height=but['height'], command=lambda x='-': self.click_event(x))
        self.button_minus.grid(row=2, column=3, **self.padding)

        self.button7 = tk.Button(self.window, text='7', width=but['width'], height=but['height'], command=lambda x='7': self.click_event(x))
        self.button7.grid(row=3, column=0, **self.padding)
        self.button8 = tk.Button(self.window, text='8', width=but['width'], height=but['height'], command=lambda x='8': self.click_event(x))
        self.button8.grid(row=3, column=1, **self.padding)
        self.button9 = tk.Button(self.window, text='9', width=but['width'], height=but['height'], command=lambda x='9': self.click_event(x))
        self.button9.grid(row=3, column=2, **self.padding)
        self.button_div = tk.Button(self.window, text='/', width=but['width'], height=but['height'], command=lambda x='/': self.click_event(x))
        self.button_div.grid(row=3, column=3, **self.padding)

        self.button0 = tk.Button(self.window, text='0', width=but['width'], height=but['height'], command=lambda x='0': self.click_event(x))
        self.button0.grid(row=4, column=0, **self.padding)
        self.buttonC = tk.Button(self.window, text='C', width=but['width'], height=but['height'], command=self.clear_entry)
        self.buttonC.grid(row=4, column=1, **self.padding)
        self.buttonCE = tk.Button(self.window, text='CE', width=but['width'], height=but['height'], command=self.clear_all)
        self.buttonCE.grid(row=4, column=2, **self.padding)
        self.button_mul = tk.Button(self.window, text='*', width=but['width'], height=but['height'], command=lambda x='*': self.click_event(x))
        self.button_mul.grid(row=4, column=3, **self.padding)

        self.button_equal = tk.Button(self.window, text='=', width=but['width'], height=but['height'], command=lambda x='=': self.click_event(x))
        self.button_equal.grid(row=5, column=3, **self.padding)

    def click_event(self, key):
        if key == '=':
            try:
                result = eval(self.input_field.get())
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, str(result))
            except Exception as e:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, 'Invalid Input')
        else:
            self.input_field.insert(tk.END, key)

    def clear_entry(self):
        self.input_field.delete(len(self.input_field.get()) - 1, tk.END)

    def clear_all(self):
        self.input_field.delete(0, tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.run()