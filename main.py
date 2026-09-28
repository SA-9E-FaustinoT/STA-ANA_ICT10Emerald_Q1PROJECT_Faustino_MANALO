# 1st Quarter Project 
""" 
A SKU (pronounced SKEW) stands for stock keeping unit and is a unique code that retailers create to track their products internally. It’s usually up to eight characters long and made from alphanumeric digits (a mix of letters and numbers). Every size, color, or style of an item gets its own SKU, making it easier to understand what is selling and what needs reordering. 
""" 
from pyscript import document, window, when
from datetime import datetime


# Product names used on the receipt.
PRODUCTS = {
    "item1": "Flower Set",
    "item2": "Princess Doll",
    "item3": "Teddy Bear",
    "item4": "Doll House",
    "item5": "Race Car",
    "item6": "Robot Transformer",
    "item7": "Building Blocks",
    "item8": "Remote Control Car"
}


@when("click", "#homeBtn")
def show_home(e):
    e.preventDefault()
    document.getElementById("storeSection").style.display = "flex"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "none"


@when("click", "#aboutBtn")
def show_about(e):
    e.preventDefault()
    document.getElementById("storeSection").style.display = "none"
    document.getElementById("aboutSection").style.display = "block"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "none"


@when("click", "#contactBtn")
def show_contact(e):
    e.preventDefault()
    document.getElementById("storeSection").style.display = "none"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "block"
    document.getElementById("receiptSection").style.display = "none"


@when("click", "#SKU_generate")
def SKU_generator(e):
    document.getElementById("sku_output").innerHTML = ""
    document.getElementById("skuInfo").innerHTML = ""

    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value.strip()
    stock_qty = document.getElementById("quantity").value

    if product_name == "" or stock_qty == "":
        document.getElementById("sku_output").innerHTML = "Please enter a product name and stock quantity."
        document.getElementById("skuDisplay").style.display = "block"
        return

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    document.getElementById("sku_output").innerHTML = "SKU: " + sku
    document.getElementById("skuInfo").innerHTML = (
        "Category: " + category + " | Product: " + product_name + " | Stock: " + str(stock_qty)
    )
    document.getElementById("skuDisplay").style.display = "block"


@when("click", "#receiptBtn")
def create_order(e):
    # Get input values
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")
    prod6 = document.getElementById("item6")
    prod7 = document.getElementById("item7")
    prod8 = document.getElementById("item8")

    products = [prod1, prod2, prod3, prod4, prod5, prod6, prod7, prod8]
    selected_items = []
    subtotal = 0

    for product in products:
        if product.checked:
            price = float(product.value)
            subtotal = subtotal + price
            selected_items.append((PRODUCTS[product.id], price))

    if len(selected_items) == 0:
        document.getElementById("show").innerHTML = "<p>Please select at least one toy before generating a receipt.</p>"
        return

    # Calculate subtotal, tax, and total
    tax_rate = 0.12  # 12% VAT, no need for excise tax. too complicated
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""
    <h3>==== Receipt ====</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>Tax: ₱{tax:.2f}</p>
    <p><strong>Total: ₱{total:.2f}</strong></p>
    """

    document.getElementById("show").innerHTML = receipt

    # Build the official receipt.
    rows = ""
    for name, price in selected_items:
        rows += f"<tr><td>{name}</td><td>—</td><td>₱{price:.2f}</td></tr>"

    now = datetime.now()
    receipt_number = now.strftime("%Y%m%d%H%M%S")

    document.getElementById("receiptNum").innerHTML = receipt_number
    document.getElementById("receiptDate").innerHTML = now.strftime("%B %d, %Y %I:%M %p")
    document.getElementById("itemsList").innerHTML = rows
    document.getElementById("totalAmt").innerHTML = "₱" + f"{total:.2f}"

    document.getElementById("storeSection").style.display = "none"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "block"


@when("click", "#backBtn")
def back_to_store(e):
    document.getElementById("storeSection").style.display = "flex"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "none"


@when("click", "#printBtn")
def print_receipt(e):
    window.print()


@when("click", "#sendBtn")
def send_message(e):
    name = document.getElementById("contactName").value.strip()
    email = document.getElementById("contactEmail").value.strip()
    message = document.getElementById("contactMessage").value.strip()

    if name == "" or email == "" or message == "":
        document.getElementById("messageStatus").innerHTML = "Please fill in all contact fields."
        return

    document.getElementById("messageStatus").innerHTML = "Thank you, " + name + "! Your message has been received."
    document.getElementById("contactName").value = ""
    document.getElementById("contactEmail").value = ""
    document.getElementById("contactMessage").value = ""
