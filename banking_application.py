import mysql.connector
import streamlit as s

mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='bank1')
a=mydb.cursor()
op=['signin','login']
options=s.selectbox('OPTION',op)
if options=='signin':
    cname=s.text_input('NAME')
    phno=s.number_input('PhNo',min_value=0)
    amount=s.number_input('Amount',min_value=1000)
    pin=s.number_input('CREATE A PIN', min_value=0)
    password=s.text_input('CREATE A PASSWORD',type="password")
    photo=s.file_uploader("UPLOAD YOUR PHOTO",type=['jpg','svg','pdf'])
    submit=s.button('Create a Account',type="primary")
    if submit:
        query="insert into customer (cname,phno,balance,pin,password,photo) values(%s,%s,%s,%s,%s,%s)"
        val=[cname,phno,amount,pin,password,photo.read()]
        a.execute(query,val)
        mydb.commit()
        s.success('Account Created Successfully')

elif options=='login':
    id=s.sidebar.number_input('enter your customer id:',min_value=0)
    password=s.sidebar.text_input('Enter your password:',type="password")
    login=s.sidebar.button('LOGIN',type="primary")
    if 'logged' not in s.session_state:
        s.session_state.logged=False
    if login:
        query=f'SELECT cid,password,balance FROM customer WHERE cid={id}'
        a.execute(query)
        details=a.fetchall()
        if details:
            if id==details[0][0]:
                if password==details[0][1]:
                    s.sidebar.success('Login successfully...')
                    s.session_state.logged=True
                else:
                    s.sidebar.error('Password is not matching...')
        else:
            s.sidebar.error('ID is not matching...')
if s.session_state.logged:
    radio=s.radio('Choose the options',['deposit','withdraw','balance'])
    if radio=='deposit':
        pin=s.number_input('Enter the pin',min_value=0)
        amt=s.number_input('Enter amount to deposit',min_value=0)
        if s.button('deposit'):
            query=f"SELECT pin FROM customer WHERE cid={id}"
            a.execute(query)
            d=a.fetchall()
            if pin==d[0][0]:
                query=f"update customer set balance=balance+{amt} where cid={id}"
                a.execute(query)
                mydb.commit()
                s.success('Amount Deposited Successfully')
        else:
            s.error('Pin is Not Matching')
    elif radio == 'withdraw':
        pin = s.number_input('Enter the pin', min_value=0)
        amt = s.number_input('Enter amount to deposit', min_value=0)
        if s.button('withdraw'):
            query = f"SELECT pin,balance FROM customer WHERE cid={id}"
            a.execute(query)
            d=a.fetchall()
            if pin==d[0][0]:
                if d[0][1]>0:
                    if amt<=d[0][1]:
                        query=f"update customer set balance=balance-{amt} where cid={id}"
                        a.execute(query)
                        mydb.commit()
                        s.success(f"amount got debited from your account...")
                    else:
                        s.error('INSUFFICIENT BALANCE')
                else:
                    s.error('ACCOUNT CONTAINS:0Rs')

    else:
        pin=s.number_input('Enter the pin',min_value=0)
        if s.button('Balance Check'):
            query=f"select pin,balance from customer where cid={id}"
            a.execute(query)
            d=a.fetchall()
            if pin==d[0][0]:
                s.success(f'Account Balance is :{d[0][1]} Rs')
            else:
                s.error('Pin is mis match')























