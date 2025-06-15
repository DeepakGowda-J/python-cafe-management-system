class Restaurant:
    res_name='Python Kitchen'
    res_loc='Bangalore'
    res_owner='Deepak'
    res_UPI_ID= 'pythonkitchen@upi'
    res_payee_Name= 'Python Kitchen'
    transaction_histroy={}

    menu= menu = {
    "STARTERS": {
        "PANEER TIKKA": 180,
        "VEG MANCHURIAN": 150,
        "GOBI 65": 130,
        "HARA BHARA KABAB": 140,
        "CHICKEN TIKKA": 220,
        "TANDOORI CHICKEN": 250,
        "FISH FRY": 260,
        "MUTTON SEEKH KEBAB": 280,
        "SPRING ROLLS": 120,
        "MASALA PAPAD": 50
    },
    "VEG CURRY": {
        "PANEER BUTTER MASALA": 200,
        "PALAK PANEER": 190,
        "VEG KOLHAPURI": 170,
        "DAL TADKA": 130,
        "CHOLE MASALA": 140,
        "KADAI PANEER": 200,
        "BHINDI MASALA": 130,
        "MIX VEG CURRY": 160,
        "RAJMA MASALA": 140,
        "MALAI KOFTA": 210
    },
    "NON VEG CURRY": {
        "BUTTER CHICKEN": 250,
        "CHICKEN CURRY": 220,
        "MUTTON ROGAN JOSH": 290,
        "CHICKEN CHETTINAD": 240,
        "EGG CURRY": 150,
        "FISH CURRY": 260,
        "CHICKEN KORMA": 230,
        "PRAWN MASALA": 280,
        "KEEMA MUTTER": 250,
        "CHICKEN DO PYAZA": 220
    },
    "RICE BIRYANI": {
        "VEG BIRYANI": 180,
        "CHICKEN BIRYANI": 240,
        "MUTTON BIRYANI": 280,
        "JEERA RICE": 110,
        "PLAIN RICE": 90,
        "EGG FRIED RICE": 160,
        "CHICKEN FRIED RICE": 190,
        "PANEER PULAO": 170,
        "CURD RICE": 100,
        "LEMON RICE": 110
    },
    "JUICES": {
        "MANGO JUICE": 80,
        "ORANGE JUICE": 70,
        "WATERMELON JUICE": 60,
        "SWEET LASSI": 60,
        "MASALA CHAAS": 50
    },
    "DESSERTS": {
        "GULAB JAMUN": 50,
        "RASGULLA": 50,
        "KHEER": 70,
        "VANILLA ICE CREAM": 60,
        "CHOCOLATE SUNDAE": 90
    },
    "SNACKS": {
        "PANI PURI": 50,
        "BHEL PURI": 40,
        "DAHI PURI": 60,
        "PAV BHAJI": 90,
        "SAMOSA": 30,
        "ALOO TIKKI": 40,
        "VADA PAV": 25,
        "KACHORI": 30,
        "MIRCHI BAJJI": 35,
        "BREAD PAKODA": 45
    },
    "SOUTH INDIAN": {
        "MASALA DOSA": 80,
        "PLAIN DOSA": 60,
        "ONION UTTAPAM": 70,
        "IDLI": 40,
        "MEDU VADA": 45,
        "RAVA DOSA": 75,
        "PONGAL": 60,
        "UPMA": 50,
        "PESARATTU": 70,
        "TOMATO BATH": 55
    },
    "BREADS": {
        "BUTTER NAAN": 40,
        "GARLIC NAAN": 50,
        "TANDOORI ROTI": 20,
        "LACHHA PARATHA": 35,
        "PHULKA": 30,
        "STUFFED ALOO PARATHA": 60,
        "MISSI ROTI": 25,
        "KULCHA": 30,
        "ROOMALI ROTI": 25,
        "PURI": 40
    },
    "MILKSHAKES": {
        "JALEBI": 40,
        "MYSORE PAK": 50,
        "RASMALAI": 70,
        "CARROT HALWA": 80,
        "CHOCOLATE MILKSHAKE": 90,
        "STRAWBERRY MILKSHAKE": 90,
        "BANANA MILKSHAKE": 80,
        "BADAM MILK": 70,
        "ROSE FALOODA": 100,
        "KULFI (MALAI)": 60
    },
    "DRINKS": {
        "VIRGIN MOJITO": 120,
        "BLUE LAGOON": 130,
        "GREEN APPLE COOLER": 110,
        "LEMON ICED TEA": 100,
        "COLD COFFEE": 90,
        "THANDAI": 80,
        "JALJEERA": 50,
        "NIMBU SODA": 40,
        "BUTTERMILK": 40,
        "MINERAL WATER": 20
    }
}
    
    def __init__(self,name,phoneNu,email):
        self.name=name
        self.phoneNu=phoneNu
        self.email=email
        self.amount=0
        self.address={}
        self.cart={}

    @classmethod
    def get_res_info(cls):
        print(f' Restaurant  Name : {cls.res_name}\n Location : {cls.res_loc}\n Owner : {cls.res_owner}')

    @classmethod
    def get_menu_items(cls):
        print('Welcome! Take a look at our delicious menu')
        for i in cls.menu:
            print(f'{i}')
    @classmethod
    def calculate_Total_eranings(cls):
        amt=0
        for i in cls.transaction_histroy:
            amt+=cls.transaction_histroy[i]
        print(amt)
    
    @classmethod
    def udpate_menu(cls):
            qn=input('ADD or DELETE').upper()
            if qn=='ADD':
                menu_category=input('Enter The Category : ').upper()
                f_name=input('Enter The food Name : ').upper()
                cost=int(input('Enter The Cost : '))
                if f_name in cls.menu[menu_category]:
                    cls.menu[menu_category][f_name]=cost
                else:
                    cls.menu[menu_category][f_name]=cost
            elif qn=='DELETE':
                menu_category=input('Enter The Category : ').upper()
                f_name=input('Enter The food Name : ').upper()
                cls.menu[menu_category].pop(f_name)
            print(cls.menu[menu_category])
          
    def show_cart(self):
        print(f'Your Orders \n {self.cart}\n The Total amount : {self.amount}')

    def user_info(self):
        print(self.name,self.phoneNu,self.email,self.address)
    
    def change_address(self):
        palce=input('Enter The City')
        pincode=input('Enter The Pincode')
        self.address['PLACE']=palce
        self.address['PINCODE']=pincode
        
    def order(self):
        Restaurant.get_menu_items()
        Choice=input('Enter What Category of Food You Want To Oredr : ').upper()
        print('='*20)
        print(f'Menu Base On {Choice} Category')
        for i in Restaurant.menu[Choice]:
            print(f'{i} : {Restaurant.menu[Choice][i]}')
        print('='*20)
        no_order=int(input('Enter No of Food You Want To Order : '))
        for j in range(no_order):
            order_name=input('Enter Food name : ').upper()
            if order_name in Restaurant.menu[Choice]:
                print(f'{order_name} is Added')
                if order_name in self.cart:
                    self.cart[order_name + '*']=Restaurant.menu[Choice][order_name]
                    print(f'You Already Have {order_name} In Your Cart Quantity Will be Increased')
                else:
                    self.cart[order_name]=Restaurant.menu[Choice][order_name]
                    self.amount+=Restaurant.menu[Choice][order_name]   
            else:
                print(f'{order_name} Not There In Our menu')
        print('='*20)
        qn=input('Do You want Order More.. (Yes/No)').upper()
        if qn=='YES':
            self.get_menu_items()
            self.order()
        if qn=='NO':
            print("Thank you for dining with us — we look forward to serving you again!")
            print(f'NOTE\nYou Are Not Suppose To Cancel The Order Once The Payment Is Done')
            print('Proceed With payment')
            print('='*20)
            self.payment()
    

    def payment(self):
        if not self.address:
            palce=input('Enter The City : ')
            pincode=input('Enter The Pincode : ')
            print('='*20)
            self.address['Pincode']=pincode
            self.address['PLACE']=palce
        print(f'NOTE \nPay online and save 20%! Cash on Delivery adds ₹100 delivery fee')
        print('='*20)
        modeOf_payment=input('Please Enter Mode of Payment (UPI/CASH)').upper()
        if modeOf_payment=='CASH':
            print(f'Amount is {self.amount} and Delivery Fee ₹100 Total {self.amount+100} ')
            print('For any delivery updates, please contact our delivery partner MR.Tom at +91 8745625894')
            print('Your order will arrive within 30 minutes. Thank you for choosing us!')
            print('=*='*40)
            Restaurant.transaction_histroy[self.name]=self.amount+100
            self.cart={}
        elif modeOf_payment=='UPI':
            print(f'Amount is {self.amount} and Discount of 20% Total {self.amount - (self.amount*0.2)} ')
            print(f'Please pay {self.amount - (self.amount*0.2)} via Google Pay or PhonePe\nUPI ID: pythonkitchen@upi\nPayee Name: Python Kitchen')
            print('='*20)
            upi=input('Enter The UPI ; ')
            amount=int(input('Enter Your Amount : '))
            if amount==self.amount - (self.amount*0.2):
                print('Payment Succesfull ✅ ')
                print('For any delivery updates, please contact our delivery partner MR.Tom at +91 8745625894')
                print('Your order will arrive within 30 minutes. Thank you for choosing us!')
                print('=*='*40)
                Restaurant.transaction_histroy[self.name]=self.amount - (self.amount*0.2)
                self.cart={}
            else:
                print('You Entered Wrong Amount')
                self.payment()

tom=Restaurant('Tom',7483125345,'tom@gmail.com')
tom.order()
doe=Restaurant('Doe',8745469852,'doe@gmail.com')
doe.order()
Restaurant.get_res_info()
print(Restaurant.transaction_histroy)
Restaurant.calculate_Total_eranings()
