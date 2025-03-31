from ttkbootstrap.dialogs import Messagebox

from Business.explorer_business import (get_drive_list, get_folder_list, get_file_list, new_folder, open_file,
                                        copy_item,move_item,rename_item, zip_item, extract_zip)
from ttkbootstrap import *
import os
import fnmatch
from PIL import Image, ImageTk

window = Window(title="Mini Explorer")

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

explorer_treeview = Treeview(window)
image = Image.open("this-pc-icon.png")
image = image.resize((24, 24))
photo = ImageTk.PhotoImage(image)
explorer_treeview.insert("", "end", iid="ThisPC", text="This PC", image=photo)
explorer_treeview.grid(row=0, column=0, rowspan=2, pady=10, padx=10, sticky="ns")

current_path_variable = StringVar()
path_entry = Entry(window, textvariable=current_path_variable)
path_entry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="ew")

explorer_table = Treeview(window, columns=("name", "type", "size", "creation_date", "modified_date", "access_date"))
explorer_table.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="nsew")

explorer_table.heading("#0", text="NO.")
explorer_table.heading("#1", text="Name")
explorer_table.heading("#2", text="Type")
explorer_table.heading("#3", text="Size")
explorer_table.heading("#4", text="Creation Date")
explorer_table.heading("#5", text="Modified Date")
explorer_table.heading("#6", text="Access Date")

explorer_table.column("#3", anchor='center')
explorer_table.column("#4", anchor='center')
explorer_table.column("#5", anchor='center')
explorer_table.column("#6", anchor='center')

drive_list = get_drive_list()
for drive in drive_list:
    explorer_treeview.insert("ThisPC", "end", iid=drive, text=drive)


def load_children(event):
    entry_id = explorer_treeview.selection()[0]
    children = explorer_treeview.get_children(entry_id)
    for child in children:
        folder_list = get_folder_list(child)
        for entry in folder_list:
            explorer_treeview.insert(child, "end", iid=entry.full_path, text=entry.name)


explorer_treeview.bind("<<TreeviewOpen>>", load_children)

row_list = []


def load_table(event):
    for row in row_list:
        explorer_table.delete(row)
    row_list.clear()

    entry_id = explorer_treeview.selection()[0]
    current_path_variable.set(entry_id)
    folder_list = get_folder_list(entry_id)
    row_number = 1
    for folder in folder_list:
        row = explorer_table.insert("", "end",
                                    iid=folder.full_path,
                                    text=row_number,
                                    values=(
                                        folder.name, folder.entry_type, "", folder.creation_date, folder.modified_date,
                                        folder.access_date))
        row_list.append(row)
        row_number += 1

    file_list = get_file_list(entry_id)
    for file in file_list:
        row = explorer_table.insert("", "end",
                                    iid=file.full_path,
                                    text=row_number,
                                    values=(
                                        file.name, file.entry_type, file.size, file.creation_date, file.modified_date,
                                        file.access_date))
        row_list.append(row)
        row_number += 1

    # entry_id = explorer_treeview.selection()[0]
    # current_path_variable.set(entry_id)
    # current_path= current_path_variable.get()
    # return current_path


explorer_treeview.bind("<<TreeviewSelect>>", load_table)


def show_context_menu(event):
    context_menu = Menu(window, tearoff=0)
    context_menu.add_command(label="New Folder",
                             command=lambda: new_folder(explorer_treeview, current_path_variable))
    context_menu.add_command(label="Open",
                             command=lambda: open_file(explorer_treeview, current_path_variable))
    context_menu.add_separator()
    context_menu.add_command(label="Copy",
                             command=lambda: copy_item(explorer_treeview, current_path_variable))
    context_menu.add_command(label="Move",
                             command=lambda: move_item(explorer_treeview, current_path_variable))
    context_menu.add_separator()
    context_menu.add_command(label="Rename",
                             command=lambda: rename_item(explorer_treeview, current_path_variable))
    context_menu.add_separator()
    context_menu.add_command(label="ZIP",
                             command=lambda: zip_item(explorer_treeview, current_path_variable))
    context_menu.add_command(label="Extract ZIP",
                             command=lambda: extract_zip(explorer_treeview, current_path_variable))

    context_menu.post(event.x_root, event.y_root)


explorer_treeview.bind("<Button-3>", show_context_menu)


def search_files(root_path, search_pattern):
    results = []

    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in fnmatch.filter(filenames, search_pattern):
            results.append(os.path.join(dirpath, filename))

        for dirname in fnmatch.filter(dirnames, search_pattern):
            results.append(os.path.join(dirpath, dirname))

    return results


def search(event):
    search_pattern = current_path_variable.get()
    root_path = explorer_treeview.selection()[0]

    results = search_files(root_path, search_pattern)


    for row in row_list:
        explorer_table.delete(row)
    row_list.clear()

    row_number = 1
    for result in results:
        row = explorer_table.insert("", "end",
                                    iid=result,
                                    text=row_number,
                                    values=(
                                        os.path.basename(result),
                                        "File" if os.path.isfile(result) else "Folder",
                                        os.path.getsize(result) if os.path.isfile(result) else "",
                                        "",
                                        "",
                                        ""))
        row_list.append(row)
        row_number += 1

    Messagebox.show_info(f"{len(results)} items found.","Founded!")



window.mainloop()
