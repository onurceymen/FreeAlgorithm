import tkinter as tk

def calculate_inflation():
    try:
        current_price_index = float(current_price_index_entry.get())
        previous_price_index = float(previous_price_index_entry.get())

        inflation_rate = ((current_price_index - previous_price_index) / previous_price_index) * 100

        result_label.config(text=f"Inflation Rate: {inflation_rate:.2f}%")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Inflation Calculator")

# Create interface elements
current_price_index_label = tk.Label(window, text="Current Price Index:")
current_price_index_label.pack()
current_price_index_entry = tk.Entry(window)
current_price_index_entry.pack()

previous_price_index_label = tk.Label(window, text="Previous Price Index:")
previous_price_index_label.pack()
previous_price_index_entry = tk.Entry(window)
previous_price_index_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_inflation)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
