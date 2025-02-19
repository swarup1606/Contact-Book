## CONTACT BOOK APP ##

import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry widgets for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons for different actions
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=7, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number:")
        if search_term:
            results = [contact for contact in self.contacts
                       if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
            if results:
                contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete", "Enter name or phone number to delete:")
        if search_term:
            results = [contact for contact in self.contacts
                       if search_term.lower() in contact["Name"].lower() or search_term in contact["Phone"]]
            if results:
                confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
                if confirm:
                    self.contacts.remove(results[0])
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
