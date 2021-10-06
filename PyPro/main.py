import tkinter as tk
from compressionalgo import compress, decompress


def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


window = tk.Tk()

window.title("Compression Engine")
window.geometry("600x400")

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
compress_button = tk.Button(window, text="Compress", command=lambda: compression(input_entry.get(), output_entry.get()))
decompress_button = tk.Button(window, text="Decompress", command=lambda: decompression(input_entry.get(), output_entry.get()))

input_label = tk.Label(window, text = "Enter the file to be compressed or decompressed:")
input_label.grid(row=0, column=0)

output_label = tk.Label(window, text="Enter name of the compressed or decompressed file:")
output_label.grid(row=1, column=0)

input_entry.grid(row=0, column=1)
output_entry.grid(row=1, column=1)
compress_button.grid(row=3, column=1)
decompress_button.grid(row=3, column=2)



window.mainloop()
