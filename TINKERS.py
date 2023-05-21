import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit = float(ent_temperature.get())
    celsius = (fahrenheit - 32) * 5/9
    lbl_result["text"] = f"{celsius} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

ent_temperature = tk.Entry(window, width=10)
ent_temperature.grid(row=0, column=0)

btn_convert = tk.Button(window, text="Convert")
btn_convert.grid(row=0, column=1)
btn_convert["command"] = fahrenheit_to_celsius

lbl_result = tk.Label(window)
lbl_result.grid(row=0, column=2)

window.mainloop()
