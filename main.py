import tkinter as tk
window = tk.Tk()

window.geometry("270x230")
window.title("BMI Calculator")

label = tk.Label(window, text = "Simple BMI Calculator", font = ("Impact", 20))
label.grid(row= 1, column= 2)

layout = "grid"

# Unecessary perse but makes it easier to switch between place, grid and pack.
def position_with_grid(widget, row, column, sticky=""):
    if layout == "grid":
        widget.grid(row=row, column=column, sticky=sticky)

# Input function
def get_input():
    input_text = entry.get()
    print(input_text)

# Creating the button
button = tk.Button(window, text="Calculate", command=lambda: [get_input(), switch_f()])
position_with_grid(button, row=19, column=2)

# Destroying the window dependant
current = "window"
def switch_f():
    global window2, window, current
    if current == "window":
        current = "window2"
        window.destroy()
        window2 = makeSecondWindow()
    else:
        current = "window"
        window2.destroy()
        window = makeWindow()
        window.mainloop()

# Creating a Second Page (window) and outputting results
def makeSecondWindow():
    window2 = tk.Tk()
    page2 = tk.Frame(window2)
    position_with_grid(page2, row=1, column=1, sticky="nsew")

    labelpage2 = tk.Label(page2, text="")
    position_with_grid(labelpage2, row=3, column=2)
    window2.geometry("500x240")
    window2.title("Results")
    if window2 != current:
        label2w = tk.Label(window2, text= "Hello, " + entryVAR.get() + "!", font= ("Impact", 20))
        position_with_grid(label2w, row=1, column=1) 
        label3w = tk.Label(window2, text= "BMI: " + str(float(entry2VAR.get()) // float(entry3VAR.get())**2) + "kg/m²", font= ("Impact", 15))
        position_with_grid(label3w, row=2, column=1)
        
    BMI = float(entry2VAR.get()) // float(entry3VAR.get())**2
    if BMI > 30:
        label_BMISCORE = tk.Label(window2, text= "You are CLINICALLY OBESE!", font= "Impact")
        position_with_grid(label_BMISCORE, row=3, column=1)
    elif BMI > 25 and not BMI > 30:
        label_BMISCORE2 = tk.Label(window2, text= "You are MORBIDLY OBESE!", font= "Impact")
        position_with_grid(label_BMISCORE2, row=3, column=1)
    elif BMI > 18.5 and not BMI > 25:
        label_BMISCORE3 = tk.Label(window2, text= "You are healthy!", font= "Impact")
        position_with_grid(label_BMISCORE3, row=3, column=1)
    elif BMI < 18.5:
        label_BMISCORE4 = tk.Label(window2, text= "You are ANOREXIC!", font= "Impact")
        position_with_grid(label_BMISCORE4, row=3, column=1)


    window2.mainloop()

window.rowconfigure(0, minsize=10)
window.columnconfigure(0, minsize= 10)

label2 = tk.Label(window, text = "Name", font = ("Lexend", 12))
position_with_grid(label2, row=3, column=2)

entryVAR = tk.StringVar()
entry = tk.Entry(window, textvariable= entryVAR)
position_with_grid(entry, row=5, column=2)

label3 = tk.Label(window, text = "Weight(kg)", font = ("Lexend", 12))
position_with_grid(label3, row=7, column=2)

entry2VAR = tk.StringVar()
entry2 = tk.Entry(window, textvariable= entry2VAR)
position_with_grid(entry2, row=9, column=2)

label4 = tk.Label(window, text = "Height in m", font = ("Lexend", 12))
position_with_grid(label4, row=11, column=2)

entry3VAR = tk.StringVar()
entry3 = tk.Entry(window, textvariable= entry3VAR)
position_with_grid(entry3, row=13, column=2)


window.mainloop()






