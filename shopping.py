users = {
     "user1": {
          "usertype":"user",
          "password":"1234567",
          "cart":[]
     },
     "user2": {
          "usertype":"user",
          "password":"1234567",
          "cart":[]
     },
     "admin":{
          "usertype":"admin",
          "password":"1234567"
     }
}

category={"1": "Footwear", "2": "Clothing","3": "Electronics"}
product1={"id":"1","name":"boot","catId":"1", "price":"800"}
product2={"id":"2","name":"sandal","catId":"1", "price":"300"}
product3={"id":"3","name":"tunic","catId":"2", "price":"1000"}
product4={"id":"4","name":"mobile","catId":"3", "price":"40000"}
products=[product1, product2, product3, product4]

name=""

def catlog():
     choice = input("\nSelect the categories from following \n 1. Footwears \n 2. Clothing \n 3. Electronic \n Enter your choice: ")
     print("\n Product from "+ category[str(choice)]+" are: \n\n")
     for index, item in enumerate(products):
          if(products[index]["catId"]== choice):
            print("-----------------------------")
            print("Product Id: "+(products[index]["id"]))
            print("Product Name: "+(products[index]["name"]))
            print("Product Price: "+(products[index]["price"]))
     print("-----------------------------")
     userMenu()

def viewCart():
    item=len(users[name]["cart"])
    if(item == 0):
       print("\n You have 0 item in cart \n")
    else: 
       print("\n You have "+ str(item) +" items in cart \n")
       for i in users[name]["cart"]:
           print("Category "+category[i["catId"]]+" | Product Name "+i["name"]+" Product Price "+i["price"])
    userMenu()

def addToCart():
    #  checkCatlog=input("\n Do you want to check catlog? (Y/N): ")
    #  if(checkCatlog == "Y"):
    #      catlog()
     pId = input("Enter the product id: ")
     quantity= input("Enter the quantity: ") 
     item=None
     for i in products: 
         if(i["id"]==pId):
             item=i
             print("Item to be added is"+ str(item))
             break
     j=int(quantity)
     while j!=0:
         users[name]["cart"].append(item)
         j = j-1
     print("The item added successfully")
     addMore=input("\n Do you want to add more product? (Y/N): ")
     if(addMore == "Y"):
         addToCart()
     else:
         userMenu()


def removeItem():
     pId = input("Enter the product id: ")
     quantity= input("Enter the quantity: ") 
     for i in products: 
         if(i["id"]==pId):
             print("Item to be removed is"+ str(i))
             break
     j=int(quantity)
     while j!=0:
         users[name]["cart"].remove(pId)
         j = j-1
     print("The item removed successfully")
     userMenu()

def checkout():
    item = users[name]["cart"]
    total = 0 
    for i in item:
       total=total+int(i["price"]) 
    paymentMode=input("Please select payment mode from following: \n 1. UPI \n 2. PayPal \n 3. Netbanking \n 4. Debit Card \n 5. Credit Card \n Enter choice: ")
      # Display a checkout message that is specific to the selected payment option.
    print("You will be shortly redirected to make a payment of Rs.", total)
    # Display a success message.
    print("Your payment has been successfully processed.")
    # print("Total is"+str(total))

def logout():
    global name
    name = ""
    print("\nyou have been logged out successfully")
    print("Visit us again soon!\n")
    return None



def userMenu():
     catlog()
     choice = input("\n\n Select from following option \n 1. View Cart \n 2. Add item to cart \n 3. Remove item from cart \n 4. Checkout \n  5. Logout \n Enter your choice: ")
     if(choice == "1"):
         viewCart()
     elif(choice == "2"):
        addToCart()
     elif(choice == "3"):
         removeItem()
     elif(choice == "4"):
        checkout()
     elif(choice == "5"):
         logout()



def userLogin():
     username = input("Enter username: ")
     password = input("Enter password: ")
     global name
     name =username

     if(users.get(username) is not None):
          if(users[username]["password"]==password):
               if(users[username]["usertype"]=="user"):
                 print("\n\nWelcome "+ username.upper()+"!!!\n\n")
                 userMenu()
          else:
               print("\nInvalid credentials\n")
          return username     
     else:
          print("\nInvalid credentials\n")
          return None


def signUp():
     username=input("Enter username: ")
     password=input("Enter password: ")
     retype=input("Enter confirm password: ")
     global name
     name =username
     if(password == retype):
          print("\n\nWelcome to Shopping App\n\n")
          users.update(
               { username:{
                    "usertype": "user",
                    "password": password,
                     "cart":[]}
               }
            )
          userMenu()
          return username
     else:
          print("Password and Confirm Password does not match")
          return None
     
def addCategory():
    print()
    id = input("\n Enter category id: ")
    name= input("Enter Category name: ")
    category.update({id:name})

def removeCategory():
    print()
    id = input("\n Enter category id: ")
    for i in products:
        if i["catID"] == id:
            print("removed", i, "from products", id)
            products.remove(i)

    del category[id]

def addProduct():
    print()
    id = input("\n Enter product id: ")
    name= input("Enter product name: ")
    catId = input("\n Enter product category id: ")
    price= input("Enter product price: ")


    # Create a new product dictionary.
    new_product = {
        "name": name,
        "id": id,
        "price": price,
        "catID": catId,
    }

    # Add the new product to the list of products.
    products.append(new_product)
    print("The product has been added successfully!")

def updateProduct():
    print()
    id = input("\n Enter product id: ")
    name= input("Enter product name: ")
    catId = input("\n Enter category id: ")
    price= input("Enter product price: ")

def removeProduct():
    print()
    id = input("\n Enter product id: ")
     
def adminMenu():
     catlog()
     choice = input("\n\n Select from following option \n 1. Add Category \n 2. Remove Category \n 3. Add Product \n 4. Update Product \n  5. Remove Product \n 6. Logout \n Enter your choice: ")
     if(choice == "1"):
         addCategory()
     elif(choice == "2"):
         removeCategory()
     elif(choice == "3"):
          addProduct()
     elif(choice == "4"):
         updateProduct()
     elif(choice == "5"):
         removeProduct
     elif(choice == "6"):
         logout()



def adminLogin():
     username = input("Enter username: ")
     password = input("Enter password: ")
     global name
     name =username

     if(users.get(username) is not None):
          if(users[username]["password"]==password):
               if(users[username]["usertype"]=="admin"):
                 print("\n\nWelcome "+ username.upper()+"!!!\n\n")
                 adminMenu()
          else:
               print("\nInvalid credentials\n")
          return username     
     else:
          print("\nInvalid credentials\n")
          return None

def start():
    print("\n\nWelcome to the Demo Marketplace\n\n")
    loginType=input("Enter the type of login \n 1. User Login \n 2. Signup \n 3. Admin Login \n Enter your choice: ")
    if(int(loginType) == 1):
         userLogin()
    elif (int(loginType)== 2):
         signUp()
    elif (int(loginType)== 3):
         adminLogin()
    else:
        print("Invalid choice")
start()