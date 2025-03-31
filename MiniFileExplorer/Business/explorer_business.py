import os
import shutil
from tkinter import simpledialog, filedialog, messagebox

from ttkbootstrap.dialogs import Messagebox

from Entities.explorer_entry import ExploreEntry
from datetime import datetime


def get_drive_list():
    drive_list = []
    drive_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for drive_name in drive_names:
        name = f"{drive_name}:\\"
        if os.path.exists(name):
            drive_list.append(name)
    return drive_list


def get_folder_list(parent_path):
    folder_list = []
    for entry in os.scandir(parent_path):
        if entry.is_dir():
            entry_info = entry.stat()
            creation_date = str(datetime.fromtimestamp(entry_info.st_birthtime))
            modified_date = str(datetime.fromtimestamp(entry_info.st_mtime))
            access_date = str(datetime.fromtimestamp(entry_info.st_atime))
            explorer_entry = ExploreEntry(entry.name, entry.path, "Folder", "", creation_date, modified_date,
                                          access_date)
            folder_list.append(explorer_entry)
    return folder_list


def get_file_list(parent_path):
    file_list = []
    for entry in os.scandir(parent_path):
        if entry.is_file():
            entry_info = entry.stat()
            size = round(entry_info.st_size / 1024)
            creation_date = str(datetime.fromtimestamp(entry_info.st_birthtime))
            modified_date = str(datetime.fromtimestamp(entry_info.st_mtime))
            access_date = str(datetime.fromtimestamp(entry_info.st_atime))
            explorer_entry = ExploreEntry(entry.name, entry.path, "File", f"{size} KB", creation_date, modified_date,
                                          access_date)
            file_list.append(explorer_entry)
    return file_list


def new_folder(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    row_list = []

    folder_name = simpledialog.askstring("New Folder", "Enter a name for the new folder:")
    if folder_name:
        folder_path = os.path.join(current_path, folder_name)
        if not os.path.exists(folder_path):
            try:
                os.mkdir(folder_path)
                Messagebox.show_info(f"Folder '{folder_name}' created successfully!", "Success")

                row = explorer_treeview.insert("", "end", iid=folder_path, text=len(row_list) + 1,
                                               values=(folder_name, "Folder", "", "", "", ""))
                row_list.append(row)
            except FileExistsError:
                messagebox.showerror("Error", f"The folder '{folder_name}' already exists.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            Messagebox.show_error("Please select or navigate to a folder first.", "Error")
    else:
        Messagebox.show_warning("No new name was provided!", "Warning")


def open_file(explorer_treeview, path):
    selected_path = str(path)
    if os.path.exists(selected_path):
        os.startfile(selected_path)
    else:
        Messagebox.show_error("No path selected!", "Error")


def copy_item(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    destination = filedialog.askdirectory(title="Copy To")
    if destination:
        try:
            if os.path.isdir(current_path):
                shutil.copytree(current_path, os.path.join(destination, os.path.basename(current_path)))
                Messagebox.show_info(f"'{os.path.basename(current_path)}' copied successfully to '{destination}'.",
                                     "Success")
            else:
                shutil.copy2(current_path, destination)
                Messagebox.show_info(f"'{os.path.basename(current_path)}' copied successfully to '{destination}'.",
                                     "Success")

        except Exception as e:
            Messagebox.show_error(f"An error occurred: {e}", "Error")


def move_item(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    destination = filedialog.askdirectory(title="Select Destination Folder")
    if destination:
        try:
            shutil.move(current_path, destination)
            Messagebox.show_info(f"'{os.path.basename(current_path)}' moved successfully to '{destination}'.", "Success")
        except Exception as e:
            Messagebox.show_error(f"An error occurred: {e}", "Error")


def rename_item(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    current_name = os.path.basename(current_path)
    new_name = simpledialog.askstring("Rename Item", f"Enter new name for '{current_name}':")
    if new_name:
        destination_path = os.path.join(os.path.dirname(current_path), new_name)
        try:
            os.rename(current_path,destination_path)
            Messagebox.show_info(f"'{current_name}' renamed successfully to '{new_name}'.", "Success")
            explorer_treeview.item(current_path, text=new_name)
        except FileExistsError:
            messagebox.showerror("Error", f"A file or folder named '{new_name}' already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    else:
        Messagebox.show_warning("No new name was provided!", "Warning")


def zip_item(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    zip_name = os.path.basename(current_path)
    zip_path = os.path.join(os.path.dirname(current_path), zip_name)
    try:
        shutil.make_archive(base_name=zip_path, format='zip', root_dir=current_path)
        Messagebox.show_info(f"'{zip_name}' was created successfully!","Success")
    except Exception as e:
        Messagebox.show_error(f"An error occurred while creating the ZIP file:{str(e)}", "Error")


def extract_zip(explorer_treeview, path):
    entry_id = explorer_treeview.selection()[0]
    path.set(entry_id)
    current_path = path.get()
    if os.path.isfile(current_path) and current_path.endswith('.zip'):
        extract_path = os.path.basename(current_path).replace(".zip","")
        try:
            shutil.unpack_archive(current_path,extract_path)
            Messagebox.show_info(f"Files extracted successfully to {extract_path}!","Success")
        except Exception as e:
            Messagebox.show_error(f"An error occurred while extracting: {e}", "Error")


