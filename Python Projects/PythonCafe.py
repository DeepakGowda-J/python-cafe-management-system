menu = {
    'STARTERS':{
    'PIZZA':80,
    'PASTA':70,
    'BURGER':100,
    'GOBI MUNCHURI':60,
    'PANIPURI':40,
    'BELPURI':40,
    'BATATA VADA':75,
    'BAJJI':30,
    'ALOO BONDA':30,
    'MASAL VODA':35
    }
    ,
    'TIFFENS':{
    'IDLI':30,
    'DOSA':30,
    'MASALA DOSA':60,
    'SET DOSA':60,
    'JEERA RICE':50,
    'VEG PALAV':50
    },

    'LUNCH':{
    'RICE AND CURRY':80,
    'CHAPATHI':70,
    'FULL MEALS':200,
    'ROOTI AND CURRY':120,
    }
   
}

userOrders={}

print()
print('WELCOME TO PYTHON KITCHEN ')
print()
print('OUR MENU CART')
print()
for i in menu:
    print('Catagory : '+ i)
    print('='*6)
    for j in menu[i]:
        print(j+':'+str(menu[i][j]))
    print('-'*20)



catagory = input('Enter What Type of Food You Want ? : ').upper()


def foodCart(catagory):
    print('Your Food Items Along with Cost ')
    print('='*10)
    for i in menu[catagory]:
        print(i+' : '+ str(menu[catagory][i]))
    total_Price=0
    remove_amt=0
    order_No = int(input('Enter Number of Orders : '))
    for j in range(order_No):
        order= input('Enter Your Order : ').upper()
        if order in menu[catagory]:
            userOrders[order]=menu[catagory][order]
            print(f'Your order {order} is added to cart.')
            total_Price+=menu[catagory][order]
        else:
            print(f'Your Order {order} is Not Available')
            continue

    if total_Price>0:
        print('Order Completed')
        qn=input('Do You Want to Remove Any Order ? (Yes/No)').upper()
        if qn=='YES':
            delete_no = int(input('Enter the No of Order to be Removed : '))
            if order_No>=delete_no:
                for k in range(delete_no):
                    delOrder= input('Which Order You want Remove : ').upper()
                    if delOrder in userOrders:
                        userOrders.pop(delOrder)
                        remove_amt+= menu[catagory][delOrder]
                        print(f"Order {delOrder} is Removed")
                    else:
                        print(f'{delOrder} Not Present in Your Ordered List')
                        continue
            else:
                return 'Total Amount is '+ str(total_Price)
    print('YOUR ORDERS')
    for p in userOrders:
        print(f'{p} = {userOrders[p]}')


    return 'Total Amount is '+ str( total_Price-remove_amt )           

  


print(foodCart(catagory))
               


       

    
