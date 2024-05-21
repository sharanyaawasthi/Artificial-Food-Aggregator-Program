import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

os.system('cls')
print('-'*101)
print('************************************** SANSKRITI SCHOOL, PUNE ***************************************')
print('************************************ INFORMATION PRACTICES (065) ************************************')
print()
print('\t\t\t\t   INVESTIGATORY PROJECT [2022-23]')
print()
print('*************************** RESTAURANT AGGREGATOR & FOOD DELIVERY SERVICE ***************************')
print()
print('\t\t\t\t\t    PREPARED BY ')
print('\t\t\t\t\t  Sharanya Awasthi')
print('\t\t\t\t\t Nandini Bahirgonde')
print('-'*101)
print()
print('\t\t\t\t\t WELCOME TO ESSENS')
print('***** A SERVICE TO EFFORTLESSLY CONNECT CUSTOMERS WITH THE FASTEST GROWING RESTAURANTS & CAFES! *****')
print()
print('FOR A PERSONALIZED EXPERIENCE -')
name = (input('What can we call you?\n'))
print()
print('Hello',name,'!')
print('Connect to various restaurants & cafes near you. We hope for a smooth experience!')
print('-'*101)
print('Press \'ENTER\' to continue')
input()
c = 'yes'
while c == 'yes':
    os.system('cls')
    print()
    print('\t\t\t\t\t      ~ HOME ~')
    print()
    print('1. About This Service')
    print('2. Order Now')
    print('3. Exit')
    print()
    ch = int(input('Kindly enter your choice [1-3] : '))
    if ch == 1:
        os.system('cls')
        print()
        print('\t\t\t\t ******** ABOUT THE SERVICE ********')
        print()
        print('The rapid growth of technology & Artificial Intelligence has been a boon during the COVID pandemic.\
              \nThese digital technologies have been successful in connecting the world & making the lives of people\
              \n\t\t\t\t\tmore & more comfortable.')
        print()
        print('ESSENS is an online restaurant aggregator & food delivery service created to make the process of\
              \nordering food & beverages smoother & much more effortless for the customers. Through this service,\
              \nthe customers can easily reach out to all the popular & renowned food chains, restaurants & cafes\
              \nwhile being at home!')
        print()
        print('ESSENS also provides various discounts & offers along with free gifts to make this experience more\
              \nenjoyable for the customers!')
        print()
        print('Press \'ENTER\' to go back to the homepage')
        input()
        
    elif ch == 2:
        FINALBILL_Items = []
        FINALBILL_Prices = []
        finaltotal = 0
        ch2 = 'Yes'
        while ch2 == 'Yes':
            os.system('cls')
            print()
            print('\t\t\t\t     ******* ORDER NOW *******')
            print('\t\t\t\t******* Restaurants & Cafes *******')
            print()
            print('Check out all the restaurants & cafes near you :')
            print()
            print('1. McDonald\'s')
            print('2. Coffee&Cakes')
            print('3. House Of Hongdae')
            print('4. Rainbow Ice-Cream Bar')
            print('5. The Shahi Punjabi Diner')
            print()
            print('6. Back To Home')
            print()
            ch1 = int(input('Kindly enter your choice of restaurant or cafe - [1-5] OR enter \'6\' to go back to the homepage : '))
            print()

            if ch1 == 1:
                os.system('cls')
                total1 = 0
                prices1 = []
                item1 = []
                burger = []
                print('-'*101)
                print()
                print('\t\t\t******************** MCDONALD\'S *******************')
                print('\t\t\t  **************** I\'m Lovin\' It ****************')
                print()
                print('We’re Passionate About Our Food. From adding more balanced options to our meals, to serving up fresh\
                       \nmeat & vegetable burgers that are cooked when you order, we’re always finding ways to show our\
                       \ncommitment to our customers and our food.')
                print('At McDonald’s, we take great care to ensure that what we serve every day is safe, quality food.\
                       \nFrom our chefs, to our dieticians and suppliers, McDonald’s food experts care deeply about the\
                       \nfood you eat.')
                print()
                print('And lastly when it comes to quality options, we’ve got you covered as always~')
                print()
                print('\t\t\t ********** SPECIAL OFFERS ON YOUR MEAL **********')
                print()
                print('1. Order worth 1000 INR or more & get free delivery to any address!')
                print('2. Get 25% off by ordering any \'3\' burgers at McDonald\'s.')
                print()
                print('-'*101)
                print()
                print('Press \'ENTER\' to continue')
                input()
                q1 = 'yes'
                while q1 == 'Yes' or q1 == 'yes' or q1 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t\t   ****** MCDONALD\'S MENU ******')
                    print() 
                    print('CHOOSE A BURGER -')
                    print('-'*101)
                    df1 = pd.read_csv(os.getcwd() + '\\McDonalds.csv', usecols = ['BURGERS','PRICE [BURGERS]'])
                    print(df1)
                    print('-'*101)
                    l1 = df1.loc[:,'PRICE [BURGERS]']
                    print()
                    n1 = int(input('Enter the burger of your choice [0-8] OR to skip, press \'9\' :\n'))
                    print()
                    if n1 == 9:
                        break
                    else:
                        y1 = df1.iloc[n1,1]
                        prices1.append(y1)
                        FINALBILL_Prices.append(y1)
                        z1 = df1.iloc[n1,0]
                        burger.append(z1)
                        item1.append(z1)
                        FINALBILL_Items.append(z1)
                        total1 = total1 + l1[n1]
                        print('Your Total price is',total1,'INR [Excluding GST]')
                        print('-'*101)
                    q1 = input('Would you like another Burger? [Yes/No]\n')         
                else:
                    pass
                
                q2 = 'yes'
                while q2 == 'Yes' or q2 == 'yes' or q2 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t\t   ****** MCDONALD\'S MENU ******')
                    print()
                    print('WOULD YOU LIKE TO ADD ON TO YOUR MEAL? -')
                    print('-'*101)
                    df1 = pd.read_csv(os.getcwd() + '\\McDonalds.csv', usecols = ['ADD Ons','PRICE [ADD ONs]'])
                    print(df1)
                    print('-'*101)
                    l2 = df1.loc[:,'PRICE [ADD ONs]']
                    print()
                    n2 = int(input('Enter your choice [0-8] OR to skip, press \'9\' :\n'))
                    print()
                    if n2 == 9:
                        break
                    else:
                        y2 = df1.iloc[n2,1]
                        prices1.append(y2)
                        FINALBILL_Prices.append(y2)
                        z2 = df1.iloc[n2,0]
                        item1.append(z2)
                        FINALBILL_Items.append(z2)
                        total1 = total1 + l2[n2]
                        print('Your Total price is',total1,'INR [Excluding GST]')
                        print('-'*101)
                    q2 = input('Would You like to add on more to your meal? [Yes/No]\n')
                else:
                    pass
            
                q3 = 'yes'
                while q3 == 'Yes' or q3 == 'yes' or q3 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t\t   ****** MCDONALD\'S MENU ******')
                    print()
                    print('WOULD YOU LIKE TO ORDER A DRINK? -')
                    print('-'*101)
                    df1 = pd.read_csv(os.getcwd() + '\\McDonalds.csv', usecols = ['DRINKS','PRICE [DRINKS]'])
                    print(df1)
                    print('-'*101)
                    l3 = df1.loc[:,'PRICE [DRINKS]']
                    print()
                    n3 = int(input('Enter your choice [0-8] OR to skip, press \'9\' :\n'))
                    print()
                    if n3 == 9:
                        break
                    else:
                        y3 = df1.iloc[n3,1]
                        prices1.append(y3)
                        FINALBILL_Prices.append(y3)
                        z3 = df1.iloc[n3,0]
                        item1.append(z3)
                        FINALBILL_Items.append(z3)
                        total1 = total1 + l3[n3]
                        print('Your Total price is',total1,'INR [Excluding GST]')
                        print('-'*101)
                    q3 = input('Would You like to have another drink? [Yes/No]\n')
                else:
                    pass

                q4 = 'yes'
                while q4 == 'Yes' or q4 == 'yes' or q4 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t\t   ****** MCDONALD\'S MENU ******')
                    print()
                    print('WOULD YOU LIKE TO ORDER A DESSERT? -')
                    print('-'*101)
                    df1 = pd.read_csv(os.getcwd() + '\\McDonalds.csv', usecols = ['DESSERT','PRICE [DESSERTS]'])
                    print(df1)
                    print('-'*101)
                    l4 = df1.loc[:,'PRICE [DESSERTS]']
                    print()
                    n4 = int(input('Enter your choice [0-8] OR to skip, press \'9\' :\n'))
                    print()
                    if n4 == 9:
                        break
                    else:
                        y4 = df1.iloc[n4,1]
                        prices1.append(y4)
                        FINALBILL_Prices.append(y4)
                        z4 = df1.iloc[n4,0]
                        item1.append(z4)
                        FINALBILL_Items.append(z4)
                        total1 = total1 + l4[n4]
                        print('Your Total price is',total1,'INR [Excluding GST]')
                        print('-'*101)
                    q4 = input('Would You like to have another dessert? [Yes/No]\n')
                else:
                    pass
            
                
                dic1 = {'Food Item' : item1, 'Price' : prices1}
                DF_final1 = pd.DataFrame(dic1)
                print()
                print('-'*101)
                os.system('cls')
                print('****************************************** MCDONALD\'S BILL ****************************************** ')
                print()
                print('-'*101)
                print('\t\t\t\t\t       ESSENS')
                print('-'*101)
                print('\t\t\t\t\t\tBILL')
                print('-'*101)
                print('\t\t\t\t\t       ORDER')
                print('-'*101)
                print()
                print(DF_final1)
                print()
                print('-'*101)
                print('\t\t\t\t\t     FINAL BILL')
                print('-'*101)
                print()
                print('Total Amount =',total1,'INR')
                print()
                if total1==1000 or total1>1000:
                    if len(burger)==3 or len(burger)>3:
                        discount1 = (25/100)*total1
                        total1 = total1 - discount1
                        gst_additional1 = (10/100)*total1
                        Ftotal1 = total1 + gst_additional1
                        finaltotal = finaltotal + Ftotal1
                        print('Special Discount Rate = 25% [Get 25% off by ordering any \'3\' burgers at McDonald\'s]')
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional1)
                        print()
                        print('GRAND TOTAL =',Ftotal1,'INR')
                    else:
                        gst_additional1 = (10/100)*total1
                        Ftotal1 = total1 + gst_additional1
                        finaltotal = finaltotal + Ftotal1
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional1)
                        print()
                        print('GRAND TOTAL =',Ftotal1,'INR')     
                elif total1<1000:
                    if len(burger)==3 or len(burger)>3:
                        discount1 = (25/100)*total1
                        total1 = total1 - discount1
                        total1 = total1 + 30
                        gst_additional1 = (10/100)*total1
                        Ftotal1 = total1 + gst_additional1
                        finaltotal = finaltotal + Ftotal1
                        print('Special Discount Rate = 25% [Get 25% off by ordering any \'3\' burgers at McDonald\'s]')
                        print('Delivery Cost = 30 INR')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional1)
                        print()
                        print('GRAND TOTAL =',Ftotal1,'INR')
                    else:
                        total1 = total1+30
                        gst_additional1 = (10/100)*total1
                        Ftotal1 = total1 + gst_additional1
                        finaltotal = finaltotal + Ftotal1
                        print('Delivery Cost = 30 INR')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional1)
                        print()
                        print('GRAND TOTAL =',Ftotal1,'INR') 
                print()
                print('-'*101)
                print()
                print('THANK YOU FOR YOUR ORDER! PLEASE VISIT AGAIN!')
                print()
                print('-'*101)
                more_restaurants = input('Do You Wish To Order From More Restaurants? :\n')
                if more_restaurants == 'Yes' or more_restaurants == 'yes' or more_restaurants == 'YES':
                    pass
                else:
                    break

            elif ch1 == 2:
                os.system('cls')
                total2 = 0
                prices2 = []
                item2 = []
                cake = []

                print('-'*101)
                print()
                print('\t\t************************** Coffee&Cakes *************************')
                print('\t\t  *********** To Always Satisfy Your Sweet Cravings ***********')
                print()
                print('\t\t        ~Treats That Make You Forget All Your Worries' )
                print('\t\t  Freshly Baked, Straight From The Oven & With Loads Of Love~')
                print()
                print('\t\t    *********** GETS SPECIAL OFFERS ON YOUR ORDERS **********')
                print()
                print('1. Order worth 1000 INR or more & get free delivery to any address!')
                print('2. Get 30% off by ordering any \'2\' cakes at Coffee&Cakes.')
                print()
                print('-'*101)
                print()
                print('Press \'ENTER\' to continue')
                input()
                
                q5 = 'yes'
                while q5 == 'Yes' or q5 == 'yes' or q5 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t\t   ****** Coffee&Cakes Menu ******')
                    print() 
                    print('Kindly select a freshly baked cake -')
                    print('-'*101)
                    df2 = pd.read_csv(os.getcwd() + '//Coffee&Cakes.csv', usecols = ['CAKES','PRICES [CAKES]'], encoding = 'ISO-8859-1')
                    print(df2)
                    print('-'*101)
                    l5 = df2.loc[:,'PRICES [CAKES]']
                    print()
                    n5 = int(input('Enter your choice [0-18] OR to skip, press \'19\' :\n'))
                    print()
                    if n5 == 19:
                        break
                    else:
                        y5 = df2.iloc[n5,1]
                        prices2.append(y5)
                        FINALBILL_Prices.append(y5)
                        z5 = df2.iloc[n5,0]
                        cake.append(z5)
                        item2.append(z5)
                        FINALBILL_Items.append(z5)
                        total2 = total2 + l5[n5]
                        print('Your Total price is',total2,'INR [Excluding GST]')
                        print('-'*101)
                    q5 = input('Want to try more of our delish cakes? [Yes/No]\n')
                else:
                    pass

                q6 = 'yes'
                while q6 == 'Yes' or q6 == 'yes' or q6 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t******************** Coffee&Cakes *******************')
                    print()
                    print('Check Out Our New Muffins & Cupcakes Range!')
                    print('-'*101)
                    df2 = pd.read_csv(os.getcwd() + '//Coffee&Cakes.csv', usecols = ['CUPCAKES & MUFFINS','PRICES [MUFFINS]'], encoding = 'ISO-8859-1')
                    print(df2)
                    print('-'*101)
                    l6 = df2.loc[:,'PRICES [MUFFINS]']
                    print()
                    n6 = int(input('Enter your choice [0-18] OR to skip, press \'19\' :\n'))
                    print()
                    if n6 == 19:
                        break
                    else:
                        y6 = df2.iloc[n6,1]
                        prices2.append(y6)
                        FINALBILL_Prices.append(y6)
                        z6 = df2.iloc[n6,0]
                        item2.append(z6)
                        FINALBILL_Items.append(z6)
                        total2 = total2 + l6[n6]
                        print('Your Total price is',total2,'INR [Excluding GST]')
                        print('-'*101)
                    q6 = input('Care for another one? [Yes/No]\n')
                else:
                    pass
            
                q7 = 'yes'
                while q7 == 'Yes' or q7 == 'yes' or q7 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t******************** Coffee&Cakes *******************')
                    print()
                    print('Select a coffee from our selection - ')
                    print('-'*101)
                    df2 = pd.read_csv(os.getcwd() + '//Coffee&Cakes.csv', usecols = ['COFFEE','PRICES [COFFEE]'], encoding = 'ISO-8859-1')
                    print(df2)
                    print('-'*101)
                    l7 = df2.loc[:,'PRICES [COFFEE]']
                    print()
                    n7 = int(input('Enter your choice [0-18] OR to skip, press \'19\' :\n'))
                    print()
                    if n7 == 19:
                        break
                    else:
                        y7 = df2.iloc[n7,1]
                        prices2.append(y7)
                        FINALBILL_Prices.append(y7)
                        z7 = df2.iloc[n7,0]
                        item2.append(z7)
                        FINALBILL_Items.append(z7)
                        total2 = total2 + l7[n7]
                        print('Your Total price is',total2,'INR [Excluding GST]')
                        print('-'*101)
                    q7 = input('There is no such thing as too much coffee...Order more? [Yes/No]\n')
                else:
                    pass

                dic2 = {'Food Item' : item2 , 'Price' : prices2}
                DF_final2 = pd.DataFrame(dic2)
                print()
                print('-'*101)
                os.system('cls')
                print('**************************************** COFFEE&CAKES BILL ****************************************** ')
                print()
                print('-'*101)
                print('\t\t\t\t\t       ESSENS')
                print('-'*101)
                print('\t\t\t\t\t\tBILL')
                print('-'*101)
                print('\t\t\t\t\t       ORDER')
                print('-'*101)
                print()
                print(DF_final2)
                print()
                print('-'*101)
                print('\t\t\t\t\t     FINAL BILL')
                print('-'*101)
                print()
                print('Total Amount =',total2,'INR')
                print()
                if total2==1000 or total2>1000:
                    if len(cake)==2 or len(cake)>2:
                        discount2 = (30/100)*total2
                        total2 = total2 - discount2
                        gst_additional2 = (10/100)*total2
                        Ftotal2 = total2 + gst_additional2
                        finaltotal = finaltotal + Ftotal2
                        print('Special Discount Rate = 30% [Get 30% off by ordering any \'2\' cakes at Coffee&Cakes]')
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional2)
                        print()
                        print('GRAND TOTAL =',Ftotal2,'INR')
                    else:
                        gst_additional2 = (10/100)*total2
                        Ftotal2 = total2 + gst_additional2
                        finaltotal = finaltotal + Ftotal2
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional2)
                        print()
                        print('GRAND TOTAL =',Ftotal2,'INR')     
                elif total2<1000:
                    if len(cake)==2 or len(cake)>2:
                        discount2 = (30/100)*total2
                        total2 = total2 - discount2
                        total2 = total2 + 15
                        gst_additional2 = (10/100)*total2
                        Ftotal2 = total2 + gst_additional2
                        finaltotal = finaltotal + Ftotal2
                        print('Special Discount Rate = 30% [Get 30% off by ordering any \'2\' cakes at Coffee&Cakes]')
                        print('Delivery Cost = 15 INR')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional2)
                        print()
                        print('GRAND TOTAL =',Ftotal2,'INR')
                    else:
                        total2 = total2+15
                        gst_additional2 = (10/100)*total2
                        Ftotal2 = total2 + gst_additional2
                        finaltotal = finaltotal + Ftotal2
                        print('Delivery Cost = 15 INR')
                        print('GST Rate = 10%')
                        print('GST Applied on Total Amount (In INR) =',gst_additional2)
                        print()
                        print('GRAND TOTAL =',Ftotal2,'INR') 
                print()
                print('-'*101)
                print()
                print('THANK YOU FOR YOUR ORDER! PLEASE VISIT AGAIN FOR MORE SWEET GOODS!')
                print()
                print('-'*101)
                more_restaurants = input('Do you wish to order from more restaurants? :\n')
                if more_restaurants == 'Yes' or more_restaurants == 'yes' or more_restaurants == 'YES':
                    pass
                else:
                    break

            elif ch1 == 3:
                os.system('cls')
                total3 = 0
                prices3 = []
                item3 = []
                korean_maincourse = []
                print('-'*101)
                print()
                print('\t\t      ******************** House Of Hongdae *******************')
                print('\t\t                  *********** [WELCOME] ***********')
                print()
                print('\t      ~Delicious Korean Treats From The Traditional Secret Recipes, Made With Love~')
                print()
                print('\'House Of Hongdae\' is known for it\'s flavourful & 100% organic meals which received great love and\
                       \nsupport from customers. We, since then have been keeping up that standard!')
                print('Our goal is to provide soulful & delicious korean food to everyone which would not only satisfy your\
                       \ntastebuds but will also give you comfort!')
                print()
                print('\t\t       ********* GETS SPECIAL OFFERS ON YOUR ORDERS **********')
                print()
                print('1. Order worth 1500 INR or more & get free delivery to any address!')
                print('2. Order any two main courses & get any 2 complimentary side dishes.')
                print()
                print('-'*101)
                print()
                print('Press \'ENTER\' to continue')
                input()
                FreeSideDishes_Prices = [0, 0]
                q8 = 'yes'
                while q8 == 'Yes' or q8 == 'yes' or q8 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* HOUSE OF HONGDAE\'s MENU *************')
                    print() 
                    print('APPETIZER -')
                    print('-'*101)
                    df3 = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['APPETIZERS','PRICES [APPETIZERS]'], encoding = 'ISO-8859-1')
                    print(df3)
                    print('-'*101)
                    l8 = df3.loc[:,'PRICES [APPETIZERS]']
                    print()
                    n8 = int(input('Enter your choice [0-12] OR to skip, press \'13\' :\n'))
                    print()
                    if n8 == 13:
                        break
                    else:
                        y8 = df3.iloc[n8,1]
                        prices3.append(y8)
                        FINALBILL_Prices.append(y8)
                        z8 = df3.iloc[n8,0]
                        item3.append(z8)
                        FINALBILL_Items.append(z8)
                        total3 = total3 + l8[n8]
                        print('Your Total price is',total3,'INR [Excluding GST]')
                        print('-'*101)
                    q8 = input('Do you wish to order another appetizer from our menu? [Yes/No]\n')
                else:
                    pass

                q9 = 'yes'
                while q9 == 'Yes' or q9 == 'yes' or q9 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* HOUSE OF HONGDAE\'s MENU *************')
                    print() 
                    print('MAIN COURSE -')
                    print('-'*101)
                    df3 = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['MAIN COURSE','PRICE [MAIN COURSE]'], encoding = 'ISO-8859-1')
                    print(df3)
                    print('-'*101)
                    l9 = df3.loc[:,'PRICE [MAIN COURSE]']
                    print()
                    n9 = int(input('Enter your choice [0-12] OR to skip, press \'13\' :\n'))
                    print()
                    if n9 == 13:
                        break
                    else:
                        y9 = df3.iloc[n9,1]
                        prices3.append(y9)
                        FINALBILL_Prices.append(y9)
                        z9 = df3.iloc[n9,0]
                        item3.append(z9)
                        korean_maincourse.append(z9)
                        FINALBILL_Items.append(z9)
                        total3 = total3 + l9[n9]
                        print('Your Total price is',total3,'INR [Excluding GST]')
                        print('-'*101)
                    q9 = input('Do you wish to order another main course from our menu? [Yes/No]\n')
                else:
                    pass
            
                q10 = 'yes'
                while q10 == 'Yes' or q10 == 'yes' or q10 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* HOUSE OF HONGDAE\'s MENU *************')
                    print() 
                    print('NOODLES[RAMYEON] - ')
                    print('-'*101)
                    df3 = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['NOODLES [RAMYEON]','PRICE [RAMYEON]'], encoding = 'ISO-8859-1')
                    print(df3)
                    print('-'*101)
                    l10 = df3.loc[:,'PRICE [RAMYEON]']
                    print()
                    n10 = int(input('Enter your choice [0-12] OR to skip, press \'13\' :\n'))
                    print()
                    if n10 == 13:
                        break
                    else:
                        y10 = df3.iloc[n10,1]
                        prices3.append(y10)
                        FINALBILL_Prices.append(y10)
                        z10 = df3.iloc[n10,0]
                        item3.append(z10)
                        FINALBILL_Items.append(z10)
                        total3 = total3 + l10[n10]
                        print('Your Total price is',total3,'INR [Excluding GST]')
                        print('-'*101)
                    q10 = input('Do you wish to order another serving of ramyeon from our menu? [Yes/No]\n')
                else:
                    pass

                q11 = 'yes'
                while q11 == 'Yes' or q11 == 'yes' or q11 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* HOUSE OF HONGDAE\'s MENU *************')
                    print() 
                    print('ADDITIONALS - ')
                    print('-'*101)
                    df3 = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['ADDITIONALS ','PRICE [ADDITIONALS]'], encoding = 'ISO-8859-1')
                    print(df3)
                    print('-'*101)
                    l11 = df3.loc[:,'PRICE [ADDITIONALS]']
                    print()
                    n11 = int(input('Enter your choice [0-12] OR to skip, press \'13\' :\n'))
                    print()
                    if n11 == 13:
                        break
                    else:
                        y11 = df3.iloc[n11,1]
                        prices3.append(y11)
                        FINALBILL_Prices.append(y11)
                        z11 = df3.iloc[n11,0]
                        item3.append(z11)
                        FINALBILL_Items.append(z11)
                        total3 = total3 + l11[n11]
                        print('Your Total price is',total3,'INR [Excluding GST]')
                        print('-'*101)
                    q11 = input('Do you want to add anything more to your korean meal? [Yes/No]\n')
                else:
                    pass

                dic3 = {'Food Item' : item3 , 'Price' : prices3}
                DF_final3 = pd.DataFrame(dic3)
                print()
                print('-'*101)
                os.system('cls')
                print('************************************* HOUSE OF HONGDAE\'S BILL *************************************** ')
                print()
                print('-'*101)
                print('\t\t\t\t\t       ESSENS')
                print('-'*101)
                print('\t\t\t\t\t\tBILL')
                print('-'*101)
                print('\t\t\t\t\t       ORDER')
                print('-'*101)
                print()
                print(DF_final3)
                print()
                print('-'*101)
                print('\t\t\t\t\t           BILL')
                print('-'*101)
                print()
                print('Total Amount =',total3,'INR')
                print()
                if total3==1500 or total3>1500:
                    if len(korean_maincourse)==2 or len(korean_maincourse)>2:
                        prices3 = prices3 + FreeSideDishes_Prices
                        FINALBILL_Prices = FINALBILL_Prices + FreeSideDishes_Prices
                        print('OFFER - Get complimentary Side Dishes for ordering any 2 Main Courses')
                        print()
                        print('Which \'2\' side dish would you like to have? It\'s from our side!')
                        print()
                        df_sidedish = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['ADDITIONALS '], encoding = 'ISO-8859-1')
                        print('-'*101)
                        print(df_sidedish)
                        print('-'*101)
                        
                        free_sidedish_choice1 = int(input('Enter your first choice [0-12] :\n'))
                        free_sidedish_itemname1 = df_sidedish.iloc[free_sidedish_choice1,0]
                        free_sidedish_choice2 = int(input('Enter your second choice [0-12] :\n'))
                        free_sidedish_itemname2 = df_sidedish.iloc[free_sidedish_choice2,0]
                        
                        item3.append(free_sidedish_itemname1)
                        item3.append(free_sidedish_itemname2)
                        FINALBILL_Items.append(free_sidedish_itemname1)
                        FINALBILL_Items.append(free_sidedish_itemname2)

                        dic_sidedishes = {'Food Item' : item3 , 'Price' : prices3}
                        DF_final_sidedishes = pd.DataFrame(dic_sidedishes)
                        os.system('cls')
                        print('****************************************** MODIFIED BILL ******************************************** ')
                        print()
                        print('-'*101)
                        print(DF_final_sidedishes)
                        print('-'*101)
                        print()
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1500 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        gst_additional3 = (10/100)*total3
                        print('GST Applied on Total Amount (In INR) =',gst_additional3)
                        Ftotal3 = total3 + gst_additional3
                        finaltotal = finaltotal + Ftotal3
                        print()
                        print('GRAND TOTAL =',Ftotal3,'INR')
                    else:
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 1500 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        gst_additional3 = (10/100)*total3
                        print('GST Applied on Total Amount (In INR) =',gst_additional3)
                        Ftotal3 = total3 + gst_additional3
                        finaltotal = finaltotal + Ftotal3
                        print()
                        print('GRAND TOTAL =',Ftotal3,'INR')
                        
                elif total3<1500:
                    if len(korean_maincourse)==2 or len(korean_maincourse)>2:
                        prices3 = prices3 + FreeSideDishes_Prices
                        FINALBILL_Prices = FINALBILL_Prices + FreeSideDishes_Prices
                        print('OFFER - Get complimentary Side Dishes for ordering any 2 Main Courses')
                        print()
                        print('Which \'2\' side dish would you like to have? It\'s from our side!')
                        print()
                        df_sidedish = pd.read_csv(os.getcwd() + '//House Of Hongdae.csv', usecols = ['ADDITIONALS '], encoding = 'ISO-8859-1')
                        print('-'*101)
                        print(df_sidedish)
                        print('-'*101)
                        
                        free_sidedish_choice1 = int(input('Enter your first choice [0-12] :\n'))
                        free_sidedish_itemname1 = df_sidedish.iloc[free_sidedish_choice1,0]
                        free_sidedish_choice2 = int(input('Enter your second choice [0-12] :\n'))
                        free_sidedish_itemname2 = df_sidedish.iloc[free_sidedish_choice2,0]
                        
                        item3.append(free_sidedish_itemname1)
                        item3.append(free_sidedish_itemname2)
                        FINALBILL_Items.append(free_sidedish_itemname1)
                        FINALBILL_Items.append(free_sidedish_itemname2)

                        dic_sidedishes = {'Food Item' : item3 , 'Price' : prices3}
                        DF_final_sidedishes = pd.DataFrame(dic_sidedishes)
                    
                        os.system('cls')
                        print('****************************************** MODIFIED BILL ******************************************** ')
                        print()
                        print('-'*101)
                        print(DF_final_sidedishes)
                        print('-'*101)
                        print()
                        print('Delivery Cost = 15 INR')
                        total3 = total3 + 15
                        print('GST Rate = 10%')
                        gst_additional3 = (10/100)*total3
                        print('GST Applied on Total Amount (In INR) =',gst_additional3)
                        Ftotal3 = total3 + gst_additional3
                        finaltotal = finaltotal + Ftotal3
                        print()
                        print('GRAND TOTAL =',Ftotal3,'INR')
                    else:
                        print('Delivery Cost = 15 INR')
                        total3 = total3 + 15
                        print('GST Rate = 10%')
                        gst_additional3 = (10/100)*total3
                        print('GST Applied on Total Amount (In INR) =',gst_additional3)
                        Ftotal3 = total3 + gst_additional3
                        finaltotal = finaltotal + Ftotal3
                        print()
                        print('GRAND TOTAL =',Ftotal3,'INR') 
                print()
                print('-'*101)
                print()
                print('THANK YOU FOR YOUR ORDER! PLEASE VISIT AGAIN!')
                print()
                print('-'*101)
                more_restaurants = input('Do You Wish To Order From More Restaurants? :\n')
                if more_restaurants == 'Yes' or more_restaurants == 'yes' or more_restaurants == 'YES':
                    pass
                else:
                    break

            elif ch1 == 4:
                c1 = 'Yes'
                while c1 == 'Yes':
                    os.system('cls')
                    total4 = 0
                    prices4 = []
                    item4 = []
                    k = []
                    print('-'*101)
                    print()
                    print('\t\t   ******************** Rainbow Ice-Cream Bar ********************')
                    print('\t\t      *************** For All Tastes & Desires ***************')
                    print()
                    print('\t     ~Beat the heat this summer & rock the winters with our explosive flavours~')
                    print()
                    print('Get to know more about us -')
                    print('1. About Our Packaging & Quality')
                    print('2. Popular Flavours Throughout the Years')
                    print('3. Order Now')
                    print()
                    icecream_shop_option = int(input('Choose an option [1-3] :\n'))
                    print()

                    if icecream_shop_option == 1:
                        os.system('cls')
                        print('-'*101)
                        print()
                        print('\t\t\t ********** Our Quality & Packaging **********')
                        print()
                        print('Rainbow Ice-Cream Bar was established in 2010 with the purpose of bringing a smile on everyone\'s faces\
                               \nwith its sweet and comforting ice-creams. Today, even after 12 years, RIC still holds those values!')
                        print()
                        print('Rainbow Ice-Creams are delicious, made from fresh milk & are available in a wide range of flavours')
                        print()
                        print('In terms of packaging, we send out 500g reusable tubs with strong seals, while delivering our\
                               \nice-creams. With the help of our insulated ice-cream boxes and delivery bags, we prevent our\
                               \nice-creams from melting over time so that they reach you in a perfect condition!')
                        print('WE HOPE TO IMPRESS YOU WITH OUR ICE-CREAM FLAVOURS AND QUALITY!')
                        print()
                        print('Press \'ENTER\' to go back')
                        input()

                    elif icecream_shop_option == 2:
                        os.system('cls')
                        print('-'*101)
                        print()
                        print('The following graph and table show the most bought ice-cream flavours from our shop :')
                        print()
                        icecream_flavours_csv = pd.read_csv(os.getcwd() + '//Ice-Cream Flavours.csv', usecols = ['ICE-CREAM FLAVOURS','TUBS SOLD SINCE 2010 [In Thousands]'], encoding = 'ISO-8859-1')
                        print(icecream_flavours_csv)
                        print()
                        icecream_flavours_csv.plot(kind ='bar', x = 'ICE-CREAM FLAVOURS', width = 0.5)
                        plt.title('Comparision Between Ice-Cream Flavours')
                        plt.xlabel('Ice-Cream Flavours')
                        plt.ylabel('Tubs Sold Since 2010 [In Thousands]')
                        plt.show()
                        print('Press \'ENTER\' to go back')
                        input()

                    elif icecream_shop_option == 3:
                        os.system('cls')
                        q12 = 'yes'
                        while q12 == 'Yes' or q12 == 'yes' or q12 == 'YES':
                            os.system('cls')
                            print('-'*101)
                            print()
                            print('\t\t  ******************** Rainbow Ice-Cream Bar\'s Menu ********************')
                            print() 
                            print('Choose an Ice-Cream Flavour -')
                            print('-'*101)
                            df4 = pd.read_csv(os.getcwd() + '//Ice Cream Bar.csv', usecols = ['ICECREAM','PRICE PER TUB'], encoding = 'ISO-8859-1')
                            print(df4)
                            print('-'*101)
                            l12 = df4.loc[:,'PRICE PER TUB']
                            print()
                            n12 = int(input('Enter your choice [0-15] OR to skip, press \'16\' :\n'))
                            print()
                            if n12 == 16:
                                break
                            else:
                                y12 = df4.iloc[n12,1]
                                prices4.append(y12)
                                FINALBILL_Prices.append(y12)
                                z12 = df4.iloc[n12,0]
                                item4.append(z12)
                                FINALBILL_Items.append(z12)
                                total4 = total4 + l12[n12]
                                print('Your Total price is',total4,'INR [Excluding GST]')
                                print('-'*101)
                            q12 = input('Order Another Flavour? [Yes/No]\n')
                        else:
                            pass

                        q13 = 'yes'
                        while q13 == 'Yes' or q13 == 'yes' or q13 == 'YES':
                            os.system('cls')
                            print('\t\t  ******************** Rainbow Ice-Cream Bar\'s Menu ********************')
                            print()
                            print('Choose From Our Popsicle Range - ')
                            print('-'*101)
                            df4 = pd.read_csv(os.getcwd() + '//Ice Cream Bar.csv', usecols = ['POPSICLE','PRICE [POPSICLE]'], encoding = 'ISO-8859-1')
                            print(df4)
                            print('-'*101)
                            l13 = df4.loc[:,'PRICE [POPSICLE]']
                            print()
                            n13 = int(input('Enter your choice [0-15] OR to skip, press \'16\' :\n'))
                            print()
                            if n13 == 16:
                                break
                            else:
                                y13 = df4.iloc[n13,1]
                                prices4.append(y13)
                                FINALBILL_Prices.append(y13)
                                z13 = df4.iloc[n13,0]
                                item4.append(z13)
                                FINALBILL_Items.append(z13)
                                total4 = total4 + l13[n13]
                                print('Your Total price is',total4,'INR [Excluding GST]')
                                print('-'*101)
                            q13 = input('Would You Like To Another Popsicle? [Yes/No]\n')
                        else:
                            pass

                        dic4 = {'Food Item' : item4, 'Price' : prices4}
                        DF_final4 = pd.DataFrame(dic4)
                        print()
                        print('-'*101)
                        os.system('cls')
                        print('************************************ RAINBOW ICE-CREAM\'S BILL ************************************ ')
                        print()
                        print('-'*101)
                        print('\t\t\t\t\t       ESSENS')
                        print('-'*101)
                        print('\t\t\t\t\t\tBILL')
                        print('-'*101)
                        print('\t\t\t\t\t       ORDER') 
                        print('-'*101)
                        print()
                        print(DF_final4)
                        print()
                        print('-'*101)
                        print('\t\t\t\t\t     FINAL BILL')
                        print('-'*101)
                        print()
                        print('Total Amount =',total4,'INR')
                        print()
                        if total4 == 300 or total4 > 300:
                            discount4 = (15/100)*total4
                            total4 = total4 - discount4
                            gst_additional4 = (10/100)*total4
                            Ftotal4 = total4 + gst_additional4
                            finaltotal = finaltotal + Ftotal4
                            print('Special Discount Rate = 15% [Get 15% off by ordering worth 300 INR or more]')
                            print('GST Rate = 10%')
                            print('GST Applied on Total Amount (In INR) =',gst_additional4)
                            print()
                            print('GRAND TOTAL =',Ftotal4,'INR')
                        else:
                            gst_additional4 = (10/100)*total4
                            Ftotal4 = total4 + gst_additional4
                            finaltotal = finaltotal + Ftotal4
                            print('GST Rate = 10%')
                            print('GST Applied on Total Amount (In INR) =',gst_additional4)
                            print()
                            print('GRAND TOTAL =',Ftotal4,'INR')     
                        print()
                        print('-'*101)
                        print()
                        print('THANK YOU FOR YOUR ORDER! PLEASE VISIT AGAIN!')
                        print()
                        print('-'*101)
                        break
                more_restaurants = input('Do You Wish To Order From More Restaurants? :\n')
                if more_restaurants == 'Yes' or more_restaurants == 'yes' or more_restaurants == 'YES':
                    pass
                else:
                    break

            elif ch1 == 5:
                os.system('cls')
                total5 = 0
                prices5 = []
                item5 = []
                appetizer = []
                print('-'*101)
                print()
                print('\t\t      ******************** The Shahi Punjabi Diner *******************')
                print('\t\t                   *********** [SWAAGAT] ***********')
                print()
                print('\t\t\t      ~Bringing The Essence Of Punjab Everywhere~')
                print()
                print('\t\t          ********* GETS SPECIAL OFFERS ON YOUR ORDERS **********')
                print()
                print('1. Order worth 2000 INR or more & get free delivery to any address!')
                print('2. Order any two appetizers & get any 1 for free.')
                print()
                print('-'*101)
                print()
                print('Press \'ENTER\' to continue')
                input()
                FreeAppetizer_Prices = [0]
                q14 = 'yes'
                while q14 == 'Yes' or q14 == 'yes' or q14 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* MENU *************')
                    print() 
                    print('SOUPS -')
                    print('-'*101)
                    df5 = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['SOUPS','PRICE PER BOWL'], encoding = 'ISO-8859-1')
                    print(df5)
                    print('-'*101)
                    l14 = df5.loc[:,'PRICE PER BOWL']
                    print()
                    n14 = int(input('Enter your choice [0-14] OR to skip, press \'15\' :\n'))
                    print()
                    if n14 == 15:
                        break
                    else:
                        y14 = df5.iloc[n14,1]
                        prices5.append(y14)
                        FINALBILL_Prices.append(y14)
                        z14 = df5.iloc[n14,0]
                        item5.append(z14)
                        FINALBILL_Items.append(z14)
                        total5 = total5 + l14[n14]
                        print('Your Total price is',total5,'INR [Excluding GST]')
                        print('-'*101)
                    q14 = input('Do you wish to order another soup from our menu? [Yes/No]\n')
                else:
                    pass

                q15 = 'yes'
                while q15 == 'Yes' or q15 == 'yes' or q15 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* MENU *************')
                    print() 
                    print('APPETIZERS-')
                    print('-'*101)
                    df5 = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['APPETIZERS','PRICE [APPETIZERS]'], encoding = 'ISO-8859-1')
                    print(df5)
                    print('-'*101)
                    l15 = df5.loc[:,'PRICE [APPETIZERS]']
                    print()
                    n15 = int(input('Enter your choice [0-14] OR to skip, press \'15\' :\n'))
                    print()
                    if n15 == 15:
                        break
                    else:
                        y15 = df5.iloc[n15,1]
                        prices5.append(y15)
                        FINALBILL_Prices.append(y15)
                        z15 = df5.iloc[n15,0]
                        item5.append(z15)
                        appetizer.append(z15)
                        FINALBILL_Items.append(z15)
                        total5 = total5 + l15[n15]
                        print('Your Total price is',total5,'INR [Excluding GST]')
                        print('-'*101)
                    q15 = input('Do you wish to order another appetizer from our menu? [Yes/No]\n')
                else:
                    pass
            
                q16 = 'yes'
                while q16 == 'Yes' or q16 == 'yes' or q16 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* MENU *************')
                    print() 
                    print('MAIN COURSE - ')
                    print('-'*101)
                    df5 = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['MAIN COURSE ','PRICE [MAIN COURSE]'], encoding = 'ISO-8859-1')
                    print(df5)
                    print('-'*101)
                    l16 = df5.loc[:,'PRICE [MAIN COURSE]']
                    print()
                    n16 = int(input('Enter your choice [0-14] OR to skip, press \'15\' :\n'))
                    print()
                    if n16 == 15:
                        break
                    else:
                        y16 = df5.iloc[n16,1]
                        prices5.append(y16)
                        FINALBILL_Prices.append(y16)
                        z16 = df5.iloc[n16,0]
                        item5.append(z16)
                        FINALBILL_Items.append(z16)
                        total5 = total5 + l16[n16]
                        print('Your Total price is',total5,'INR [Excluding GST]')
                        print('-'*101)
                    q16 = input('Do you wish to order another main course? [Yes/No]\n')
                else:
                    pass

                q17 = 'yes'
                while q17 == 'Yes' or q17 == 'yes' or q17 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* MENU *************')
                    print() 
                    print('BREAD/RICE - ')
                    print('-'*101)
                    df5 = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['BREAD/RICE','PRICE [BREAD/RICE]'], encoding = 'ISO-8859-1')
                    print(df5)
                    print('-'*101)
                    l17 = df5.loc[:,'PRICE [BREAD/RICE]']
                    print()
                    n17 = int(input('Enter your choice [0-14] OR to skip, press \'15\' :\n'))
                    print()
                    if n17 == 15:
                        break
                    else:
                        y17 = df5.iloc[n17,1]
                        prices5.append(y17)
                        FINALBILL_Prices.append(y17)
                        z17 = df5.iloc[n17,0]
                        item5.append(z17)
                        FINALBILL_Items.append(z17)
                        total5 = total5 + l17[n17]
                        print('Your Total price is',total5,'INR [Excluding GST]')
                        print('-'*101)
                    q17 = input('Do you wish to order more breads/rice? [Yes/No]\n')
                else:
                    pass

                q18 = 'yes'
                while q18 == 'Yes' or q18 == 'yes' or q18 == 'YES':
                    os.system('cls')
                    print('-'*101)
                    print()
                    print('\t\t\t ************* MENU *************')
                    print() 
                    print('ANY ADDITIONALS - ')
                    print('-'*101)
                    df5 = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['ADDITIONAL ','PRICE'], encoding = 'ISO-8859-1')
                    print(df5)
                    print('-'*101)
                    l18 = df5.loc[:,'PRICE']
                    print()
                    n18 = int(input('Enter your choice [0-14] OR to skip, press \'15\' :\n'))
                    print()
                    if n18 == 15:
                        break
                    else:
                        y18 = df5.iloc[n18,1]
                        prices5.append(y18)
                        FINALBILL_Prices.append(y18)
                        z18 = df5.iloc[n18,0]
                        item5.append(z18)
                        FINALBILL_Items.append(z17)
                        total5 = total5 + l18[n18]
                        print('Your Total price is',total5,'INR [Excluding GST]')
                        print('-'*101)
                    q18 = input('Do you want to add anything more? [Yes/No]\n')
                else:
                    pass

                dic5 = {'Food Item' : item5 , 'Price' : prices5}
                DF_final5 = pd.DataFrame(dic5)
                print()
                print('-'*101)
                os.system('cls')
                print('************************************* SHAHI PUNJABI DINER\'S BILL *************************************** ')
                print()
                print('-'*101)
                print('\t\t\t\t\t       ESSENS')
                print('-'*101)
                print('\t\t\t\t\t\tBILL')
                print('-'*101)
                print('\t\t\t\t\t       ORDER')
                print('-'*101)
                print()
                print(DF_final5)
                print()
                print('-'*101)
                print('\t\t\t\t\t           BILL')
                print('-'*101)
                print()
                print('Total Amount =',total5,'INR')
                print()
                if total5==2000 or total5>2000:
                    if len(appetizer)==2 or len(appetizer)>2:
                        prices5 = prices5 + FreeAppetizer_Prices
                        FINALBILL_Prices = FINALBILL_Prices + FreeAppetizer_Prices
                        print('OFFER - Order 2 appetizers and get 1 for free!')
                        print()
                        print('Which \'1\' appetizer would you like to have? It\'s from our side!')
                        print()
                        df_appetizer = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['APPETIZERS'], encoding = 'ISO-8859-1')
                        print('-'*101)
                        print(df_appetizer)
                        print('-'*101)
                        
                        free_appetizer_choice1 = int(input('Enter your choice of appetizer [0-12] :\n'))
                        free_appetizer_itemname1 = df_appetizer.iloc[free_appetizer_choice1,0]
                        
                        item5.append(free_appetizer_itemname1)
                        FINALBILL_Items.append(free_appetizer_itemname1)

                        dic_appetizer = {'Food Item' : item5 , 'Price' : prices5}
                        DF_final_appetizer = pd.DataFrame(dic_appetizer)
                        os.system('cls')
                        print('****************************************** MODIFIED BILL ******************************************** ')
                        print()
                        print('-'*101)
                        print(DF_final_appetizer)
                        print('-'*101)
                        print()
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 2000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        gst_additional5 = (10/100)*total5
                        print('GST Applied on Total Amount (In INR) =',gst_additional5)
                        Ftotal5 = total5 + gst_additional5
                        finaltotal = finaltotal + Ftotal5
                        print()
                        print('GRAND TOTAL =',Ftotal5,'INR')
                    else:
                        print('Delivery Cost = 0 INR [Free Delivery][Order worth 2000 INR or more & get free delivery to any address]')
                        print('GST Rate = 10%')
                        gst_additional5 = (10/100)*total5
                        print('GST Applied on Total Amount (In INR) =',gst_additional5)
                        Ftotal5 = total5 + gst_additional5
                        finaltotal = finaltotal + Ftotal5
                        print()
                        print('GRAND TOTAL =',Ftotal5,'INR')
                        
                elif total5<2000:
                    if len(appetizer)==2 or len(appetizer)>2:
                        prices5 = prices5 + FreeAppetizer_Prices
                        FINALBILL_Prices = FINALBILL_Prices + FreeAppetizer_Prices
                        print('OFFER - Order 2 appetizers and get 1 for free!')
                        print()
                        print('Which \'1\' appetizer would you like to have? It\'s from our side!')
                        print()
                        df_appetizer = pd.read_csv(os.getcwd() + '//The Shahi Punjabi Diner.csv', usecols = ['APPETIZERS'], encoding = 'ISO-8859-1')
                        print('-'*101)
                        print(df_appetizer)
                        print('-'*101)
                        
                        free_appetizer_choice1 = int(input('Enter your choice of appetizer [0-12] :\n'))
                        free_appetizer_itemname1 = df_appetizer.iloc[free_appetizer_choice1,0]
                        
                        item5.append(free_appetizer_itemname1)
                        FINALBILL_Items.append(free_appetizer_itemname1)

                        dic_appetizer = {'Food Item' : item5 , 'Price' : prices5}
                        DF_final_appetizer = pd.DataFrame(dic_appetizer)
                        os.system('cls')
                        print('****************************************** MODIFIED BILL ******************************************** ')
                        print()
                        print('-'*101)
                        print(DF_final_appetizer)
                        print('-'*101)
                        print()
                        print('Delivery Cost = 15 INR')
                        total5 = total5 + 15
                        print('GST Rate = 10%')
                        gst_additional5 = (10/100)*total5
                        print('GST Applied on Total Amount (In INR) =',gst_additional5)
                        Ftotal5 = total5 + gst_additional5
                        finaltotal = finaltotal + Ftotal5
                        print()
                        print('GRAND TOTAL =',Ftotal5,'INR')
                    else:
                        print('Delivery Cost = 15 INR')
                        total5 = total5 + 15
                        print('GST Rate = 10%')
                        gst_additional5 = (10/100)*total5
                        print('GST Applied on Total Amount (In INR) =',gst_additional5)
                        Ftotal5 = total5 + gst_additional5
                        finaltotal = finaltotal + Ftotal5
                        print()
                        print('GRAND TOTAL =',Ftotal5,'INR') 
                print()
                print('-'*101)
                print()
                print('THANK YOU FOR YOUR ORDER! PLEASE VISIT AGAIN!')
                print()
                print('-'*101)
                more_restaurants = input('Do You Wish To Order From More Restaurants? :\n')
                if more_restaurants == 'Yes' or more_restaurants == 'yes' or more_restaurants == 'YES':
                    pass
                else:
                    break

        dic_final = {'Food Item' : FINALBILL_Items , 'Price' : FINALBILL_Prices }
        finalbill = pd.DataFrame(dic_final)
        print()
        print('-'*101)
        os.system('cls')
        print('************************************* YOUR FINAL BILL *************************************** ')
        print()
        print('-'*101)
        print('\t\t\t\t\t       ESSENS')
        print('-'*101)
        print('\t\t\t\t\t\tBILL')
        print('-'*101)
        print('\t\t\t\t\t       ORDER')
        print('-'*101)
        print()
        print(finalbill)
        print()
        print('-'*101)
        print('\t\t\t\t\t           BILL')
        print('-'*101)
        print()
        print('Total Amount =', finaltotal, 'INR')
        print()
        print('-'*101)
        print()
        print('THANK YOU FOR YOUR ORDER!')
        print()
        print('-'*101)
        print()
        print('Press \'ENTER\' to go back to the homepage')
        input()
        finalbill.to_csv(os.getcwd() + '//Final Bill.csv')

    elif ch == 3:
        break

                
               
            
