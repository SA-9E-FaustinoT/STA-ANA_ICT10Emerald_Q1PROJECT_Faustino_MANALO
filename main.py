# 1st Quarter Project 
""" 
A SKU (pronounced SKEW) stands for stock keeping unit and is a unique code that retailers create to track their products internally. It’s usually up to eight characters long and made from alphanumeric digits (a mix of letters and numbers). Every size, color, or style of an item gets its own SKU, making it easier to understand what is selling and what needs reordering. 
""" 
from pyscript import document 
 
 
def SKU_generator(e): 
    # Clear output first and retrieve inputs cleanly
    document.getElementById('sku_output').innerHTML = " " 
    category = document.getElementById('category').value.strip() 
    product_name = document.getElementById('product_name').value.strip() 
    stock_qty = document.getElementById('quantity').value.strip() 
 
    sku = f"{category[:3].upper()}-{product_name[:4].upper()}-{stock_qty}"
 
    document.getElementById("sku_output").innerHTML = f"SKU: {sku}"
    document.getElementById("skuDisplay").style.display = "block" 
 
 
def create_order(e): 
    subtotal = 0.0

    # Dynamically process items 1 to 8 with safety checks
    for i in range(1, 9):
        item = document.getElementById(f"item{i}")
        if item and item.checked:
            try:
                subtotal += float(item.value)
            except (ValueError, TypeError):
                pass  # Skip non-numeric values safely
     
    tax_rate = 0.12  # 12% VAT
    tax = subtotal * tax_rate 
    total = subtotal + tax 
 
    receipt = f""" 
    <h3>==== Receipt ====</h3> 
    <p>Subtotal: ₱{subtotal:.2f}</p> 
    <p>Tax: ₱{tax:.2f}</p> 
    <p><strong>Total: ₱{total:.2f}</strong></p> 
    """ 
 
    document.getElementById("show").innerHTML = receipt
