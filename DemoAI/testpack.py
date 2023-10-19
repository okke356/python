import tkinter as tk
from PIL import Image
#from PIL import Image, ImageTk
import random

table_frame = None  # Biến toàn cục để lưu trữ frame chứa bảng

def create_table():
    global table_frame
    # Lấy số hàng và số cột từ người dùng
    num_rows = int(entry_rows.get())
    num_cols = int(entry_cols.get())

    # Lấy vị trí ban đầu của máy hút bụi và bụi từ người dùng
    vacuum_row = int(entry_vacuum_row.get()) - 1
    vacuum_col = int(entry_vacuum_col.get()) - 1
    dust_positions = []
    dust_row = entry_dust_row.get().split(",")
    dust_cols = entry_dust_col.get().split(",")

    for i in range(len(dust_row)):
        dust_positions.append((int(dust_row[i]) - 1, int(dust_cols[i]) - 1))

    # Nếu bảng đã được tạo trước đó, xóa nó
    if table_frame:
        clear_table()

    # Tạo Frame chứa bảng và đặt xuống phía dưới các Entry
    table_frame = tk.Frame(root)
    table_frame.grid(row=3, column=0, columnspan=2)

    # Tạo danh sách chứa các hình ảnh máy hút bụi, bụi và virus
    vacuum_image = ImageTk.PhotoImage(Image.open("vacuum.png").resize((50, 50), Image.LANCZOS))
    bg_image = ImageTk.PhotoImage(Image.open("rac.png").resize((30, 30), Image.LANCZOS))
    dust_image = ImageTk.PhotoImage(Image.open("virus.jpg").resize((50, 50), Image.LANCZOS))

    # Hiển thị bảng và chèn hình ảnh máy hút bụi, bụi và bg vào các ô tương ứng
    for i in range(num_rows):
        for j in range(num_cols):
            if (i, j) == (vacuum_row, vacuum_col):  # Nếu là vị trí của máy hút bụi
                image = vacuum_image
            elif (i, j) in dust_positions:  # Nếu là vị trí của bụi
                image = dust_image
            else:
                image = bg_image

            cell_label = tk.Label(table_frame, image=image, borderwidth=1, relief='solid')
            cell_label.image = image  # Giữ tham chiếu đến hình ảnh để tránh bị gãy
            cell_label.grid(row=i, column=j, padx=5, pady=5)

            cell_label.bind('<Button-1>', lambda event, row=i, col=j: move_vacuum(event, row, col))


def move_vacuum(event, row, col):
    print(f'Moving vacuum to Row {row + 1}, Col {col + 1}')

def clear_table():
    global table_frame
    # Kiểm tra nếu table_frame đã được tạo, sau đó xóa các widget trong Frame
    if table_frame:
        for widget in table_frame.winfo_children():
            if widget != create_button:
                widget.destroy()


import tkinter as tk
from tkinter import font


def submit():
    column_value = column_entry.get()
    vacuum_row_value = vacuum_row_entry.get()
    vacuum_column_value = vacuum_column_entry.get()
    dust_row_value = dust_row_entry.get()
    dust_column_value = dust_column_entry.get()

    print("Số cột:", column_value)
    print("Hàng của máy hút bụi:", vacuum_row_value)
    print("Cột của máy hút bụi:", vacuum_column_value)
    print("Hàng của bụi:", dust_row_value)
    print("Cột của bụi:", dust_column_value)


# Tạo một cửa sổ giao diện
window = tk.Tk()
window.title("Thông tin")

# Tạo một LabelFrame với tiêu đề "Nhập thông tin"
info_frame = tk.LabelFrame(window, text="Nhập thông tin", font=("Arial", 12, "bold"), padx=20, pady=20)
info_frame.pack(pady=20)

# Tạo các Label và Entry box
label_font = font.Font(family="Arial", size=10)

column_label = tk.Label(info_frame, text="Nhập số cột:", font=label_font)
column_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
column_entry = tk.Entry(info_frame, font=label_font)
column_entry.grid(row=0, column=1, padx=10, pady=5)

vacuum_row_label = tk.Label(info_frame, text="Nhập hàng của máy hút bụi:", font=label_font)
vacuum_row_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
vacuum_row_entry = tk.Entry(info_frame, font=label_font)
vacuum_row_entry.grid(row=1, column=1, padx=10, pady=5)

vacuum_column_label = tk.Label(info_frame, text="Nhập cột của máy hút bụi:", font=label_font)
vacuum_column_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
vacuum_column_entry = tk.Entry(info_frame, font=label_font)
vacuum_column_entry.grid(row=2, column=1, padx=10, pady=5)

dust_row_label = tk.Label(info_frame, text="Nhập hàng của bụi:", font=label_font)
dust_row_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
dust_row_entry = tk.Entry(info_frame, font=label_font)
dust_row_entry.grid(row=3, column=1, padx=10, pady=5)

dust_column_label = tk.Label(info_frame, text="Nhập cột của bụi:", font=label_font)
dust_column_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
dust_column_entry = tk.Entry(info_frame, font=label_font)
dust_column_entry.grid(row=4, column=1, padx=10, pady=5)

# Tạo nút "Submit"
submit_button = tk.Button(window, text="Submit", font=("Arial", 12), bg="#4CAF50", fg="white", relief=tk.RAISED,
                          command=submit)
submit_button.pack(pady=10)

# Vòng lặp chạy chương trình
window.mainloop()
