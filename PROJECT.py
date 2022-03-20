import random
import mysql.connector as ms
mydb = ms.connect(host="localhost", user="root", passwd="1234")
if mydb.is_connected():
    print("success!")
else:
    print("error")

mycursor = mydb.cursor()
mycursor.execute("create database if not exists BMS;")
mycursor.execute("USE BMS;")
def createtable():
    db = ms.connect(
        host="localhost",
        user="root",
        password="1234",
        database="BMS")
    mycursor = db.cursor()
    table ="CREATE TABLE if not exists accounts(id int not null primary key, name varchar(50) not null,username varchar(20) not null, password varchar(15) not null, balance float not null, age int not null, gender  char(1) not null, mobile bigint not null, street  TEXT, district  varchar(30) not null,pin_code int not null, state  varchar(20) not null, country varchar(20) not null, nominee  varchar(50) not null);"
    mycursor.execute(table)
    print("Table is created")
createtable()
ctr = 0
bank = 1
while bank == 1:
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print("WELCOME TO BANK OF KALOS")
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('Press 1 for Online Banking')
    print('Press 2 for Registering a New Bank Account')
    print('Press 3 for Cancel your Bank Account')
    print('Press 4 for Account Holder Help Services')
    print('Press 5 for Exit')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    choice = int(input("Option : "))
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    if choice == 1:
        def welcome_message():
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            print('WELCOME TO BANK OF KALOS')
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        def login():
            while True:
                un = input("Enter your username : ")
                p = (input("Enter your password :"))
                print('====================================')
                value = (un, p)
                query = """select * from accounts where username=%s and password=%s """
                mycursor.execute(query, value)
                data_login = mycursor.fetchall()
                if len(data_login) != 0:
                    globals()['ctr'] = 1
                    break
                else:
                    print('LOGIN UNSUCCESSFUL')
                    print("USERNAME OR PASSWORD IS WRONG")
                    print('====================================')
            return data_login
        def interface():
            welcome_message()
            b = login()
            if globals()['ctr'] == 1:
                i = b[0][0]
                name = b[0][2]
                print("LOGIN SUCCESSFUL")
                print('====================================')
                c = 1
                while c == 1:
                    print('Press 1 for Depositing money')
                    print('Press 2 for Withdrawing money')
                    print('Enter 3 for Updating Full Account Details')
                    print("Press 4 for View Account Details")
                    print('Press 5 for Checking balance')
                    print('Press 6 for Logging out')
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    ch = int(input("Enter your option :- "))
                    if ch == 1:
                        money_deposit = int(input('Amount to be deposited : '))
                        print('======================================')
                        mycursor.execute('update accounts set balance=balance+%s where id=%s', (money_deposit, i))
                        mydb.commit()
                        q = 'select balance from accounts where id=%s and username=%s'
                        mycursor.execute(q, (i, name))
                        a = mycursor.fetchall()
                        a = a[:]
                        for x in a:
                            print("Updated Balance : ", x)
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch == 2:
                        money_withdrawn = int(input('Amount to be withdrawn :- '))
                        print('====================================')
                        mycursor.execute('update accounts set balance=balance-%s where id=%s', (money_withdrawn, i))
                        mydb.commit()
                        q = 'select balance from accounts where id=%s and username=%s'
                        mycursor.execute(q, (i, name))
                        a = mycursor.fetchall()
                        a = a[:]
                        for x in a:
                            print("Updated Balance : ", x)
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch == 3:
                        print('Press 1 for Changing Password')
                        print('Enter 2 for Changing Mobile No.')
                        print('Press 3 for Changing Street')
                        print('Press 4 for Changing District ')
                        print('Press 5 for Changing Pin Code')
                        print('Press 6 for Changing State')
                        print('Press 7 for Changing Nominee')
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        ch1 = int(input("Enter your option :- "))
                        if ch1 == 1:
                            new_password = input('Enter New Password :- ')
                            print('====================================')
                            mycursor.execute('update accounts set password=%s where id=%s', (new_password, i))
                            mydb.commit()
                            q = 'select password from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated Password : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 2:
                            new_mobile_no = int(input('Enter New Mobile No. :- '))
                            print('====================================')
                            mycursor.execute('update accounts set mobile = %s where id=%s', (new_mobile_no, i))
                            mydb.commit()
                            q = 'select mobile from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated Mobile No. : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 3:
                            new_street = input('Enter New Street Address :- ')
                            print('====================================')
                            mycursor.execute('update accounts set street = %s where id=%s', (new_street, i))
                            mydb.commit()
                            q = 'select street from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated Street Address : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 4:
                            new_district = input('Enter New District Name :- ')
                            print('====================================')
                            mycursor.execute('update accounts set district = %s where id=%s', (new_district, i))
                            mydb.commit()
                            q = 'select district from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated District Name : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 5:
                            new_pin_code = int(input('Enter New Pin Code :- '))
                            print('====================================')
                            mycursor.execute('update accounts set pin_code = %s where id=%s', (new_pin_code, i))
                            mydb.commit()
                            q = 'select pin_code from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated Pin Code : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 6:
                            new_state = input('Enter New State :- ')
                            print('====================================')
                            mycursor.execute('update accounts set state = %s where id=%s', (new_state, i))
                            mydb.commit()
                            q = 'select state from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated State : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        elif ch1 == 7:
                            new_nominee = input('Enter New Nominee :- ')
                            print('====================================')
                            mycursor.execute('update accounts set nominee = %s where id=%s', (new_nominee, i))
                            mydb.commit()
                            q = 'select nominee from accounts where id=%s and username=%s'
                            mycursor.execute(q, (i, name))
                            a = mycursor.fetchall()
                            a = a[:]
                            for x in a:
                                print("Updated Nominee : ", x)
                                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        else:
                            print('Wrong Option')
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch == 4:
                        q = 'select * from accounts where id=%s and username=%s'
                        mycursor.execute(q, (i, name))
                        a = mycursor.fetchall()
                        for x in a:
                            print("Account Number: ", x[0])
                            print('-----------------------------------')
                            print("Account Holder's Name: ': ", x[1])
                            print('-----------------------------------')
                            print("Account Holder's Username': ", x[2])
                            print('-----------------------------------')
                            print("Account Balance: ", x[4])
                            print('-----------------------------------')
                            print("Account Holder Age: ", x[5])
                            print('-----------------------------------')
                            print("Account Holder's Gender: ", x[6])
                            print('-----------------------------------')
                            print("Account Holder's Number: ", x[7])
                            print('-----------------------------------')
                            print("Account Holder's street address: ", x[8])
                            print('-----------------------------------')
                            print("Account Holder's district address: ", x[9])
                            print('-----------------------------------')
                            print("Account Holder's pin code address: ", x[10])
                            print('-----------------------------------')
                            print("Account Holder's state: ", x[11])
                            print('-----------------------------------')
                            print("Account Holder's country: ", x[12])
                            print('-----------------------------------')
                            print("Account Holder's Nominee: ", x[13])
                            print('-----------------------------------')
                    elif ch == 5:
                        q = 'select balance from accounts where id=%s and username=%s'
                        mycursor.execute(q, (i, name))
                        a = mycursor.fetchall()
                        a = a[:]
                        for x in a:
                            print("Balance :- ", x)
                            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                    elif ch == 6:
                        c = 0
                    else:
                        print("Wrong Option ")
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        interface()
    elif choice == 2:
        print('FILL THESE DETAILS TO CREATE YOUR ACCOUNT')
        idea = random.randint(1, 100)
        name = input("Enter your name : ")
        username = input('Enter your username : ')
        pas = input('Enter your password : ')
        balance = float(input('Enter your balance : '))
        age = int(input('Enter your age : '))
        gender = input('Enter your gender (M/F) : ')
        mob = int(input('Enter Mobile no. : '))
        street = input('Enter your street name: ')
        district = input('Enter your District: ')
        pin_code = int(input('Enter your pin code: '))
        state = input('Enter State: ')
        country = input('Enter your Country: ')
        nominee = input(
            "Enter Nominee Name (In case after Death the Account Credentials has to be handed Over): ")
        print('====================================')
        query = 'insert into accounts values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        value = (idea, name, username, pas, balance, age, gender, mob, street, district, pin_code, state, country, nominee)
        mycursor.execute(query, value)
        mydb.commit()
    elif choice == 3:
        un = input("Enter your username :- ")
        p = (input("Enter your password :-"))
        print('''====================================''')
        value = (un, p)
        query = "select * from accounts where username=%s and password=%s "
        mycursor.execute(query, value)
        data_login = mycursor.fetchall()
        mycursor.execute('delete from accounts where id=%s and username=%s', (data_login[0][0], data_login[0][2]))
        mydb.commit()
        print("Account Closed")
        print('====================================')
    elif choice == 4:
        print('TOLL FREE NO. - 9798197981 ')
        print('====================================')
    elif choice == 5:
        bank = 0
    else:
        print('Wrong Option')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

