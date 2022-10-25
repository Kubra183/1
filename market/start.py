from Products import Product



List_products = [Product(1,"apple",2,"Fruit"),
              Product(2,"orange",4,"Fruit"),
              Product(3,"banana",5,"Fruit"),
              Product(4,"pear",1,"Fruit"),
              Product(5,"mango",2,"Fruit"),
              Product(6,"chili",3,"Vegetables"),
              Product(7,"corn",6,"Vegetables"),
              Product(8,"onion",3,"Vegetables"),
              Product(9,"tomato",1,"Vegetables"),
              Product(10,"garlic",3,"Vegetables")]


print("Add products to cart by entering numbers press '0' to buy\n\n")
i=1
for products in List_products:
    print(str(i)+"-"+products.name,str(products.price)+"$")
    i+=1

List_Cart =[]
Cart = 0
while True:

    while True:
        try:
            choose=int(input("Please enter a product number: "))
            break
        except:
            print("Wrong input please try again")
            continue

    if choose==0:
        break
    elif choose<=len(List_products):
        Producdt_id=choose
        Cart+=List_products[Producdt_id-1].price
        print(List_products[Producdt_id-1].name+" Added!"+"\nCategory:"+List_products[Producdt_id-1].category+" Cost:"+str(Cart))
        List_Cart.append(List_products[Producdt_id-1].name)
    else:
        print("Wrong number please try again\n")

print("Your Cast: \n")
for procs in List_Cart:
    print(procs)        
print("####Total Cost: "+str(Cart))

             