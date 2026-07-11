import tkinter as tk

library = []

# ---------------- FUNCTIONS ----------------

def add_book():
    name = entry.get()

    if name != "":
        library.append({"name": name, "status": "available"})
        result.set("Book added successfully!")
        entry.delete(0, tk.END)
    else:
        result.set("Enter a book name!")

def view_books():
    if len(library) == 0:
        result.set("No books in library")
    else:
        text = ""
        for i, book in enumerate(library):
            text += f"{i+1}. {book['name']} - {book['status']}\n"
        result.set(text)

def issue_book():
    name = entry.get()
    found = False

    for book in library:
        if book["name"].lower() == name.lower():
            if book["status"] == "available":
                book["status"] = "issued"
                result.set("Book issued successfully!")
            else:
                result.set("Book already issued")
            found = True
            break

    if not found:
        result.set("Book not found")

    entry.delete(0, tk.END)

def return_book():
    name = entry.get()
    found = False

    for book in library:
        if book["name"].lower() == name.lower():
            if book["status"] == "issued":
                book["status"] = "available"
                result.set("Book returned successfully!")
            else:
                result.set("Book was not issued")
            found = True
            break

    if not found:
        result.set("Book not found")

    entry.delete(0, tk.END)

# ---------------- UI ----------------

root = tk.Tk()
root.title("Library Management System")
root.geometry("500x500")
root.configure(bg="#f0f8ff")   # light background

# Title
title = tk.Label(
    root,
    text="📚 Library System",
    font=("Arial", 18, "bold"),
    bg="#f0f8ff",
    fg="#2c3e50"
)
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=35, font=("Arial", 12))
entry.pack(pady=10)

# Buttons (colored)
tk.Button(root, text="Add Book", width=20, command=add_book,
          bg="#2ecc71", fg="white").pack(pady=3)

tk.Button(root, text="View Books", width=20, command=view_books,
          bg="#3498db", fg="white").pack(pady=3)

tk.Button(root, text="Issue Book", width=20, command=issue_book,
          bg="#e67e22", fg="white").pack(pady=3)

tk.Button(root, text="Return Book", width=20, command=return_book,
          bg="#9b59b6", fg="white").pack(pady=3)

# Output label
result = tk.StringVar()

output = tk.Label(
    root,
    textvariable=result,
    justify="left",
    fg="#2c3e50",
    bg="#ecf0f1",
    font=("Arial", 11),
    width=50,
    height=10,
    anchor="nw",
    relief="solid"
)
output.pack(pady=20)

root.mainloop()