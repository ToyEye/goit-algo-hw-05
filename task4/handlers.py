from decorators import input_error

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact exist"

@input_error
def change_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Conctact not exist"
    
@input_error
def show_phone(args, contacts):
    name = args[0]

    contacts_phone = contacts.get(name)

    if contacts_phone:
        return contacts_phone

    else:
        return "Conctact not exist"
    
@input_error
def show_all(contacts):
    return contacts