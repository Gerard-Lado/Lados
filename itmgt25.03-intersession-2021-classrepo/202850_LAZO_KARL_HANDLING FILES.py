#!/usr/bin/env python
# coding: utf-8

# # Assignment: Handling Files
# 
# This assignment serves as a general synthesis for Module 4. It also serves as your introduction to using files and to coding Python _outside_ of Jupyter.  
# 
# Please follow all instructions precisely. This is especially important in this assignment, which will ask you to submit a `.py` file instead of a `.ipynb` file.

# ## Context
# 
# **CoffeePython** is a specialty coffee place along Katipunan. It commissioned students to build a crude character-mode terminal based on Python and it ran pretty well.  
# 
# Due to the Covid-19 Pandemic that forced businesses to shut down, however, it had to pivot its business to online deliveries. The direction, however, is to make sure that the current Point-of-Sale (POS) system being used in the branches still works. There are some missing pieces that need to be reprogrammed again.  
# 
# CoffeePython has the following products:  
# 
# | Code | ProductName | Price |
# | --- | --- | --- |
# | americano | Americano | 150.00 |
# | brewedcoffee | Brewed Coffee | 150.00 |
# | cappuccino | Cappuccino | 150.00 |
# | dalgona | Dalgona | 150.00 |
# | espresso | Espresso | 150.00 |
# | frappuccino | Frappuccino | 150.00 |  
# 
# The old programmers of Coffee Python encoded this data in a dictionary:

# In[4]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}


# ## Problem 1: Product Information Lookup
# 
# Write a function called `get_product` that takes one positional argument (str) `code` that is a product code of one of Coffee Python's products. The function should return the dictionary containing the information about the product whose code was passed to the function.  
# 
# For example,  
# `get_product("espresso")`  
# 
# should return
# 
# `{"name":"Espresso","price":140.00}`

# In[5]:


# CODE CELL
def get_product(code):
    for k, v in products.items():
        if k == code:
            return v
        else:
            pass
    
get_product("espresso") 
# PROBLEM 1


# ## Problem 2: Product Property Lookup
# 
# Write a function called `get_property` that takes two positional arguments: (str) `code` and (str) `property`. The function should return the value appropriate property for the product code entered.  
# 
# For example,  
# `get_property("espresso", "price")`  
# 
# should return  
# 
# `140.0` or an equivalent float.  

# In[6]:


# CODE CELL
def get_property(code, property):
    for l, m in products.items():
        if l == code:
            return m[property]
        else:
            pass
get_property("espresso", "name")
# PROBLEM 2


# ## Problem 3: The Point-of-Sale Terminal
# 
# Write a function called `main` that takes no positional arguments. This function should not return anything.  
# 
# When this function is called, it should begin a session. The session should prompt its user, the clerk, to input data about a customer's orders until the clerk enters the string `"/"`.  
# 
# Each line of input consists of two elements: the product code and the quantity. Lines of input are formatted as follows: `"{product_code},{quantity}"`.  
# 
# It is up to you how you will store data about orders. Please use your functions from Problem 1 and Problem 2 in answering this problem.  
# 
# The function should _write a file_ called `receipt.txt` that provides a summarized report of the session. The receipt should be formatted as follows:  

# In[7]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# ADJUST THE NUMBER OF TABS AS NECESSARY TO FORMAT IT NICELY.
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}

Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')


# In[8]:


# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# Example:
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
cappuccino\t\tCappuccino\t\t1\t\t\t\t170.0
brewedcoffee\t\tBrewed Coffee\t\t5\t\t\t\t550.0

Total:\t\t\t\t\t\t\t\t\t\t720.0
==
''')


# Specifications:
# 1. The receipt should provide a summary of all the orders made during the session.  
# 2. A product must only appear if it has been ordered at least once during the session. In other words, if a product is not ordered, then it should not appear in the receipt.  
# 3. A product must appear only once even if it has been ordered multiple times. In other words, if a product is ordered multiple times, then it should only have one entry in the receipt that describes the sum of all of the orders made for that product.
# 4. Products must appear in alphabetical order.

# In[11]:


# CODE CELL
def main():
    total = 0
    entered = input("Input {product_code},{quantity}: ")
    entered_code = entered[0: entered.index(",")]
    order_quantity = int(entered[entered.index(",") + 1:])
    name = get_property(entered_code, "name")
    subtotal = order_quantity * int(get_property(entered_code, "price"))
    total = total + subtotal
    with open("receipt.txt", "w") as order_list:
        order_list.write(f"""==
                        CODE\t\t\t\t\tNAME\t\t\t\tQUANTITY\t\tSUBTOTAL
                        {entered_code}\t\t\t{name}\t\t\t{order_quantity}\t\t\t{subtotal}
                        """)
    while entered != "/":
        entered = input("Input {product_code},{quantity}: ")
        if entered == "/":
            break
        else:
            entered_code = entered[0: entered.index(",")]
            order_quantity = int(entered[entered.index(",") + 1:])
            name = get_property(entered_code, "name")
            subtotal = order_quantity * int(get_property(entered_code, "price"))
            total = total + subtotal
            with open("receipt.txt", "a") as order_list:
                order_list.write(f"""
                            {entered_code}\t\t\t{name}\t\t\t{order_quantity}\t\t\t{subtotal}
                            """)
    with open("receipt.txt", "a") as receipt:
        receipt.write(f"""
                        Total:\t\t\t\t\t\t\t\t\t\t{total}
==""")                        

main()
# PROBLEM 3


# ## Problem 4: Final Instructions (28 points)
# 
# Paste the `products` dictionary and all three of your functions into a regular Python file called `[ID_NUM]_[LAST_NAME]_[FIRST_NAME]_HANDLINGFILES.py` (e.g., 199999_ILAGAN_JOSERAMON_HANDLINGFILES.py) and call the `main()` function once at the very bottom of the file.  
# 
# The program should run properly when it is run using the `python` command.  
# 
# Only Python files will be checked. Jupyter notebooks will not be checked.  

# In[ ]:




