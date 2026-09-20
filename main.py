from unittest import result

from Project.sku import sku
from pyscript import document, display   # importing document and display pakeage




def adding_numbers(e): 
    document.getElementById("output1").innerHTML = ""  # clear previous output

    num1 = float(document.getElementById("category").value)  # getting value from an input field
    num2 = float(document.getElementById("product").value)
    num3 = float(document.getElementById("stock").value)
    result = num1 = num2 + num3
display(result, target="output1") # displaying result in webpage

def create_order(e):
    prod1 = document.getElementById("item1")

   # calculating total
    subtotal = float(prod1.value) * prod1.checked
    display(subtotal, target="show")

    food = document.getElementById('food')
    food_price = float(food.value)

def generate_sku(e):
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("stock").value # getting value from webpage
  

document.getElementById("sku").innerText = "SKU: " + sku