import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    url = url_entry.get()
    if url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.config(text=f"Shortened URL: {short_url}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {e}")
    else:
        messagebox.showwarning("Input Error", "Please enter a valid URL")

root = tk.Tk()
root.title("URL Shortener")

# URL entry label and field
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()