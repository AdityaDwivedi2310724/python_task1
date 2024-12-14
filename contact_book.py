import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")
        
        self.contacts = {}

        # UI Setup
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        tk.Label(self.root, text="Contact Book", font=("Arial", 24)).pack(pady=10)
        
        # Add Contact Frame
        add_frame = tk.Frame(self.root)
        add_frame.pack(pady=10)
        
        tk.Label(add_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(add_frame, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(add_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(add_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(add_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(add_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(add_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Button(add_frame, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        
        # View Contacts
        self.contact_list = tk.Listbox(self.root, width=50, height=10)
        self.contact_list.pack(pady=10)
        
        # Contact Options
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="View Contact", command=self.view_contact).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update Contact", command=self.update_contact).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Contact", command=self.delete_contact).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Search Contact", command=self.search_contact).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Clear Search", command=self.display_contacts).grid(row=0, column=4, padx=5)
        
        # Display Contacts
        self.display_contacts()
    
    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        
        if name and phone:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
            self.display_contacts()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    
    def view_contact(self):
        try:
            selected_contact = self.contact_list.get(self.contact_list.curselection())
            name = selected_contact.split(' - ')[0]
            contact = self.contacts[name]
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        except:
            messagebox.showerror("Error", "Please select a contact to view.")
    
    def update_contact(self):
        try:
            selected_contact = self.contact_list.get(self.contact_list.curselection())
            name = selected_contact.split(' - ')[0]
            contact = self.contacts[name]
            
            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, contact['phone'])
            self.email_entry.insert(0, contact['email'])
            self.address_entry.insert(0, contact['address'])
            
            self.add_contact_button.config(text="Update Contact", command=lambda: self.update_existing_contact(name))
        except:
            messagebox.showerror("Error", "Please select a contact to update.")
    
    def update_existing_contact(self, old_name):
        new_name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        
        if new_name and phone:
            del self.contacts[old_name]
            self.contacts[new_name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
            self.display_contacts()
            self.add_contact_button.config(text="Add Contact", command=self.add_contact)
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
    
    def delete_contact(self):
        try:
            selected_contact = self.contact_list.get(self.contact_list.curselection())
            name = selected_contact.split(' - ')[0]
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.display_contacts()
        except:
            messagebox.showerror("Error", "Please select a contact to delete.")
    
    def search_contact(self):
        search_term = self.name_entry.get().strip().lower()
        if search_term:
            found_contacts = {name: details for name, details in self.contacts.items() if search_term in name.lower() or search_term in details['phone']}
            self.display_contacts(found_contacts)
        else:
            messagebox.showerror("Error", "Please enter a name or phone number to search.")
    
    def display_contacts(self, contacts=None):
        self.contact_list.delete(0, tk.END)
        contacts = contacts if contacts else self.contacts
        for name, details in contacts.items():
            self.contact_list.insert(tk.END, f"{name} - {details['phone']}")
    
    def clear_entries(self):
        self.name_entry.delete(0, 'end')
        self.phone_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')

# Run the Contact Book application
root = tk.Tk()
app = ContactBook(root)
root.mainloop()
