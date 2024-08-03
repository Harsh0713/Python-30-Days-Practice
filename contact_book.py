
def add_contact(contacts,name,phone,email):
    if name in contacts:
        #file handling
        print(f"Contact with name '{name}' already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added.")
        
def view_contact(contacts):
    if not contacts:
        print("No contact available.")
    else:
        for name, details in contacts.items():
            print(f"Name {name}, Phone: {details['phone']}, Email: {details['email']}")
            
def search_contact(contacts, name):
    if not contacts:
        print("No contact available.")
    else:
        found = False
        for name_, details in contacts.items():
            if name_ == name:
                found = True
                print(f"Name {name}, Phone: {details['phone']}, Email: {details['email']}")
                break
        if not found:
            print(f"{name} not found in your contacts")

def update_contact(contacts, name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if not phone and not email:
            print("Give some details to update")
        else:
            print(f"Contact {name} updated.")
    else:
        print("Contact not found.")
        
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")