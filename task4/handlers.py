def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if contacts.get(name):
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Conctact not exist"

def show_phone(args, contacts):
    name = args[0]

    contacts_phone = contacts.get(name)

    if contacts_phone:
        return contacts_phone

    else:
        return "Conctact not exist"

def show_all(contacts):
    return contacts