 # 1st Quarter Project """
A SKU (pronounced SKEW) stands for stock keeping unit and is a unique code that retailers create to track their products internally. It’s usually up to eight characters long and made from alphanumeric digits (a mix of letters and numbers). Every size, color, or style of an item gets its own SKU, making it easier to understand what is selling and what needs reordering. 
""" 
from pyscript import document 
 
 
def SKU_generator(e): 
    document.getElementById('sku_output').innerHTML = " " 
    category = document.getElementById('category').value 
    product_name = document.getElementById('product_name').value 
    stock_qty = document.getElementById('quantity').value 
 
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty) 
 
    document.getElementById("sku_output").innerHTML = "SKU: " + sku
    document.getElementById("skuDisplay").style.display = "block" 
 
 
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
 
 
    # Calculate total by multiplying value by checked status (1 or 0) 
    # Calculate subtotal, tax, and total 
    subtotal = (
        (float(prod1.value) if prod1.checked else 0) +
        (float(prod2.value) if prod2.checked else 0) +
        (float(prod3.value) if prod3.checked else 0) +
        (float(prod4.value) if prod4.checked else 0) +
        (float(prod5.value) if prod5.checked else 0) +
        (float(prod6.value) if prod6.checked else 0) +
        (float(prod7.value) if prod7.checked else 0) +
        (float(prod8.value) if prod8.checked else 0)
    )
     
    tax_rate = 0.12  # 12% VAT, no need for excise tax. too complicated 
    tax = subtotal * tax_rate 
    total = subtotal + tax 
 
    receipt = f""" 
    <h3>==== Receipt ====</h3> 
    <p>Subtotal: ₱{subtotal:.2f}</p> 
    <p>Tax: ₱{tax:.2f}</p> 
    <p><strong>Total: ₱{total:.2f}</strong></p> 
    """ 
 
    document.getElementById("show").innerHTML = receipt  # use this instead of display to avoid displaying the HTML tags
 so the names and prices don't overlap anymore.

**Important:** the fixed HTML now points to `main_fixed.py`, so don't rename just one of the files.

[1]: https://docs.pyscript.net/2025.2.3/api/?utm_source=chatgpt.com "Built-in APIs - PyScript"
