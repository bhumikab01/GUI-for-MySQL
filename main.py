import tkinter as tk
from tkinter import messagebox
import mysql.connector as msc


class MySQLDatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MySQL Database GUI")
        self.root.geometry("720x6003")

        self.label = tk.Label(self.root, text="MySQL CRUD Operations", font=("Arial", 14))
        self.label.pack(pady=10)

        self.connection_label = tk.Label(self.root, text="Not connected", fg="red")
        self.connection_label.pack(pady=5)

        self.connect_btn = tk.Button(self.root, text="Connect to MySQL", command=self.connect_mysql)
        self.connect_btn.pack(pady=10)

        self.crud_frame = tk.Frame(self.root)
        self.crud_frame.pack(pady=20)

        self.insert_btn = tk.Button(self.crud_frame, text="Insert", command=self.insert_data, state="disabled")
        self.insert_btn.pack(side="left", padx=10)

        self.update_btn = tk.Button(self.crud_frame, text="Update", command=self.update_data, state="disabled")
        self.update_btn.pack(side="left", padx=10)

        self.delete_btn = tk.Button(self.crud_frame, text="Delete", command=self.delete_data, state="disabled")
        self.delete_btn.pack(side="left", padx=10)

        self.select_btn = tk.Button(self.crud_frame, text="Select", command=self.select_data, state="disabled")
        self.select_btn.pack(side="left", padx=10)

        self.show_all_btn = tk.Button(self.crud_frame, text="Show All", command=self.show_all_data, state="disabled")
        self.show_all_btn.pack(side="left", padx=10)

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.pack(pady=5)

        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack(pady=5)

    def connect_mysql(self):
        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
            )
            crs = db.cursor()
            db.autocommit = True

            q1 = "create database if not exists gui"
            crs.execute(q1)
            q2 = 'use gui'
            crs.execute(q2)
            q3 = "create table if not exists gui(Name varchar(100), Age int(2))"
            crs.execute(q3)

            if db.is_connected():
                self.connection_label.config(text="Connected to MySQL", fg="green")
                self.enable_crud_buttons()

        except msc.Error as err:
            messagebox.showerror("Connection Error", f"Error: {err}")
            self.connection_label.config(text="Not connected", fg="red")


    def enable_crud_buttons(self):
        self.insert_btn.config(state="normal")
        self.update_btn.config(state="normal")
        self.delete_btn.config(state="normal")
        self.select_btn.config(state="normal")
        self.show_all_btn.config(state="normal")


    def insert_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        if not name or not age:
            messagebox.showwarning("Input Error", "Both Name and Age must be filled out!")
            return

        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
                database="gui"
            )
            cursor = db.cursor()
            cursor.execute("INSERT INTO gui (name, age) VALUES (%s, %s)", (name, age))
            db.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
            self.clear_entries()

        except msc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def update_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        if not name or not age:
            messagebox.showwarning("Input Error", "Both Name and Age must be filled out!")
            return

        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
                database="gui"
            )
            cursor = db.cursor()
            cursor.execute("UPDATE gui SET age = %s WHERE name = %s", (age, name))
            db.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Data updated successfully")
            else:
                messagebox.showinfo("Not Found", "No matching record found to update")
            self.clear_entries()
        except msc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def delete_data(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showwarning("Input Error", "Name must be filled out to delete!")
            return

        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
                database="gui"
            )
            cursor = db.cursor()
            cursor.execute("DELETE FROM gui WHERE name = %s", (name,))
            db.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Data deleted successfully")
            else:
                messagebox.showinfo("Not Found", "No matching record found to delete")

            self.clear_entries()

        except msc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def select_data(self):
        name = self.name_entry.get()

        if not name:
            messagebox.showwarning("Input Error", "Name must be filled out to query!")
            return

        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
                database="gui"
            )
            cursor = db.cursor()
            cursor.execute("SELECT name, age FROM gui WHERE name = %s", (name,))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Data Found", f"Name: {result[0]}\nAge: {result[1]}")
            else:
                messagebox.showinfo("Not Found", "No matching record found")

        except msc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def show_all_data(self):
        try:
            db = msc.connect(
                host="localhost",
                user="root",
                password="634237",
                database="gui"
            )
            cursor = db.cursor()
            cursor.execute("SELECT * FROM gui")
            result = cursor.fetchall()

            if result:
                data_str = "\n".join([f"Name: {row[0]}, Age: {row[1]}" for row in result])
                messagebox.showinfo("All Data", data_str)
            else:
                messagebox.showinfo("No Data", "No records found")

        except msc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)


if __name__=="__main__":
    root = tk.Tk()
    app = MySQLDatabaseGUI(root)
    root.mainloop()



