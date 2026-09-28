# 1st Quarter Project
"""
A SKU (pronounced SKEW) stands for stock keeping unit and is a unique
code that retailers create to track their products internally.
"""

from pyscript import document
from datetime import datetime


# Store/cart data
cart = []
total_amount = 0.0


# -----------------------------
# SKU GENERATOR
# -----------------------------
def SKU_generator(event=None):
    document.getElementById("sku_output").innerHTML = ""
    document.getElementById("skuInfo").innerHTML = ""

    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    stock_qty = document.getElementById("quantity").value

    if product_name == "" or stock_qty == "":
        document.getElementById("sku_output").innerHTML = "Please fill in all fields!"
        return

    sku = (
        category[:3].upper()
        + "-"
        + product_name.replace(" ", "")[:4].upper()
        + "-"
        + str(stock_qty)
    )

    document.getElementById("sku_output").innerHTML = sku
    document.getElementById("skuInfo").innerHTML = (
        "Category: " + category
        + "<br>Product: " + product_name
        + "<br>Stock: " + str(stock_qty)
    )


# -----------------------------
# CART
# -----------------------------
def add_item(name, code, stock, price):
    global total_amount

    item = {
        "name": name,
        "code": code,
        "stock": stock,
        "price": price
    }

    cart.append(item)
    total_amount += price
    update_cart()


def update_cart():
    cart_div = document.getElementById("cart")
    total_div = document.getElementById("totalDiv")

    if len(cart) == 0:
        cart_div.innerHTML = (
            '<p style="text-align: center; color: #999;">'
            'No items yet. Click toys to add!</p>'
        )
        total_div.style.display = "none"
        return

    html = ""

    for item in cart:
        html += '<div class="cart-item">'
        html += "<span>" + item["name"] + "</span>"
        html += '<span>₱' + format(item["price"], ".2f") + "</span>"
        html += "</div>"

    cart_div.innerHTML = html
    total_div.innerHTML = "Total: ₱" + format(total_amount, ".2f")
    total_div.style.display = "block"


# -----------------------------
# NAVIGATION
# -----------------------------
def show_section(section_name):
    document.getElementById("storeSection").style.display = "none"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "none"

    if section_name == "store":
        document.getElementById("storeSection").style.display = "flex"
    elif section_name == "about":
        document.getElementById("aboutSection").style.display = "block"
    elif section_name == "contact":
        document.getElementById("contactSection").style.display = "block"


# -----------------------------
# RECEIPT
# -----------------------------
def show_receipt(event=None):
    if len(cart) == 0:
        document.getElementById("receiptSection").innerHTML = (
            '<p style="text-align:center;">'
            'Please add items to your cart first!</p>'
        )
        return

    document.getElementById("storeSection").style.display = "none"
    document.getElementById("aboutSection").style.display = "none"
    document.getElementById("contactSection").style.display = "none"
    document.getElementById("receiptSection").style.display = "block"

    receipt_num = "RCT-" + str(int(datetime.now().timestamp()))[-8:]
    document.getElementById("receiptNum").textContent = receipt_num

    now = datetime.now()
    document.getElementById("receiptDate").textContent = now.strftime(
        "%B %d, %Y %I:%M %p"
    )

    tbody = document.getElementById("itemsList")
    tbody.innerHTML = ""

    for item in cart:
        sku = item["code"] + "-" + str(item["stock"])

        row = "<tr>"
        row += "<td>" + item["name"] + "</td>"
        row += "<td>" + sku + "</td>"
        row += "<td>₱" + format(item["price"], ".2f") + "</td>"
        row += "</tr>"

        tbody.innerHTML += row

    document.getElementById("totalAmt").textContent = (
        "₱" + format(total_amount, ".2f")
    )


def back_to_store(event=None):
    document.getElementById("receiptSection").style.display = "none"
    document.getElementById("storeSection").style.display = "flex"


# -----------------------------
# CONTACT
# -----------------------------
def send_message(event=None):
    document.getElementById("contactSection").innerHTML += (
        '<p style="text-align:center; color:#4CAF50; font-weight:bold;">'
        'Thank you! We will get back to you soon.</p>'
    )


# -----------------------------
# CONNECT HTML BUTTONS TO PYTHON
# -----------------------------
document.getElementById("homeBtn").addEventListener(
    "click", lambda event: show_section("store")
)

document.getElementById("aboutBtn").addEventListener(
    "click", lambda event: show_section("about")
)

document.getElementById("contactBtn").addEventListener(
    "click", lambda event: show_section("contact")
)

document.getElementById("generateBtn").addEventListener(
    "click", SKU_generator
)

document.getElementById("receiptBtn").addEventListener(
    "click", show_receipt
)

document.getElementById("backBtn").addEventListener(
    "click", back_to_store
)

document.getElementById("sendBtn").addEventListener(
    "click", send_message
)


# Product buttons
document.getElementById("item1").addEventListener(
    "click", lambda event: add_item("Flower Set", "GIRLS-FLW", 25, 159.99)
)
document.getElementById("item2").addEventListener(
    "click", lambda event: add_item("Princess Doll", "GIRLS-DOL", 30, 249.99)
)
document.getElementById("item3").addEventListener(
    "click", lambda event: add_item("Teddy Bear", "GIRLS-BEA", 40, 199.99)
)
document.getElementById("item4").addEventListener(
    "click", lambda event: add_item("Doll House", "GIRLS-HOU", 15, 249.99)
)
document.getElementById("item5").addEventListener(
    "click", lambda event: add_item("Race Car", "BOYS-CAR", 35, 159.99)
)
document.getElementById("item6").addEventListener(
    "click", lambda event: add_item("Robot", "BOYS-ROB", 20, 199.99)
)
document.getElementById("item7").addEventListener(
    "click", lambda event: add_item("Building Blocks", "BOYS-BLK", 50, 299.99)
)
document.getElementById("item8").addEventListener(
    "click", lambda event: add_item("RC Car", "BOYS-RCC", 25, 299.99)
)
