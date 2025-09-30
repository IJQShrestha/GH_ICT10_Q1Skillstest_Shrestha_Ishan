from pyscript import display, document

def generate(e):
    # Customer info
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    phone_number = document.getElementById("phone").value

    # Menu
    menu = document.getElementById("menu").value

    # Display order summary
    display(f"Name: {name}", target="output")
    display(f"Address: {address}", target="output")
    display(f"Phone Number: {phone_number}", target="output")
    display(f"Total order: {menu}", target="output")