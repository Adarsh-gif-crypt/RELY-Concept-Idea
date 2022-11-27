import streamlit as st
import time
import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
import os
import flag as fl


st.set_page_config(layout='wide')

titlespacer0, title, titlespacer1 = st.columns((6,5,2))
title.title('RELY')

st.markdown("""**RELY** or **_Reassuring Life for Elderly Adults
with blockchain enabled Pervasive Healthcare systems_** is a conceptual framework 
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.""")


divs0, div, divs1 = st.columns((6,6,2))
div.header('Access Control')


st.markdown("""### Which data should be collected? """)
cb1,cb2,cb3,cb4,cb5,cb6 = st.columns(6)
cb11,cb22,cb33,cb44,cb55,cb66 = st.columns(6)
heartrate = cb1.checkbox('Heartrate')
bp = cb2.checkbox('Blood Pressure')
oxm = cb3.checkbox('Oxygen Level')
temp = cb4.checkbox('Temperature')
sl = cb5.checkbox('Glucose Level')
ww = cb6.checkbox('Hydration Level')
usg1 = cb11.checkbox('Telivision Activity')
usg2 = cb22.checkbox('Smartphone Activity')
usg3 = cb33.checkbox('Smartwatch Activity')
usg4 = cb44.checkbox('Luminous Objects Activity')
usg5 = cb55.checkbox('Pulse Oximenter')
usg6 = cb66.checkbox('Sleeping Patterns')

data = pd.DataFrame()

st.markdown('<br><br><br>',unsafe_allow_html=True)

st.markdown("""### The data should be shared with? """)
cb12,cb13,cb14,cb15 = st.columns(4)
kin = cb12.checkbox('Next of Kin (Children/Spouse)')
med = cb13.checkbox('Medical Professionals')
des = cb14.checkbox('Any other')
com = cb15.checkbox('Company',help='The company only collects the granted data for research purposes. Uncheck this box if you do not wish to share this information with the company')

emailkin = ''
emailmed = ''
emaildes = ''
emailcom = ''

emailhelptext = 'Emails are usually in the form of xyz@abc.com. If you do not know the email of your kin, please contact them immediately'
rolehelptext = 'Positions such as General Physician, Cardiologist, Pediatricians etc. Please contact your doctor or associated medical professional for position details.'
qualhelptext = 'No person other than a doctor having qualification recognized by Medical Council of India and registered with Medical Council of India/State Medical Council(s) is allowed to practice Modern System of Medicine or Surgery. A person obtaining qualification in any other system of Medicine is not allowed to practice. Modern System of Medicine in any form. Please contact your doctor or associated medical professional for the rquired information'

if kin:
    namekin = cb12.text_input('Enter Name',key=00)
    agekin = cb12.text_input('Enter Age',key=00)
    emailkin = cb12.text_input('Enter Email',key=00,placeholder='something@something.com',help=emailhelptext)

if med:
    namemed = cb13.text_input('Enter Name',key=1)
    rolemed = cb13.text_input('Enter Position',key=1,help=rolehelptext)
    idmed = cb13.text_input('Qualification ID',key=1,help=qualhelptext)
    emailmed = cb13.text_input('Medical Professional Email ID',key=1,help=emailhelptext)

# st.write(emailkin) test1

if des:
    namedes = cb14.text_input('Enter Name',key=2)
    agedes = cb14.text_input('Enter Age',key=2)
    emaildes = cb14.text_input('Enter Email',key=2,help=emailhelptext)

if com:
    emailcom = 'companyemail@companyext.com'


sender_email = 'as8969@srmist.edu.in'




if st.button('Initiate Collection of Data'):
    time.sleep(10)
    data = pd.read_excel('Book1.xlsx')
    #st.write(data)

#uniqk = ''

    
def random_unique_key():
    len=8
    random.shuffle(characters)
    unique_key=[]
    for i in range(len):
        unique_key.append(random.choice(characters))
    random.shuffle(unique_key)
    #print("".join(unique_key))
    return "".join(unique_key)
        
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()[]{}~`")
uniqk = random_unique_key()

st.markdown("""#### To access the data, please click on the button below <br><br>""",unsafe_allow_html=True)
if st.button('Access Data'):


    time.sleep(5)
    to = [emailkin,emaildes,emailmed,emailcom]
    password = input('Email Password for Confirmation: ')
    to = emailkin
    bcc1 = emaildes
    bcc2 = emailmed
    rcpt = [bcc1] + [bcc2] + [to]
    #rcpt = to

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test 8"
    message["From"] = sender_email
    message["To"] = to

    text = 'Your Unique Key is:-{0} \n Please do not share this key with anyone.'.format(uniqk)


    part1 = MIMEText(text, "plain")


    message.attach(part1)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, rcpt, message.as_string()
        )

        #time.sleep(2)
        
        

        
        stream = os.popen('node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDczMTlFNWY1RjlBQ2IwZUU3MjQyRjExNjNEMjlDNTFmMWI0MjQzQjAiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NTUxODk0NDM2MTEsIm5hbWUiOiJSRUxZIn0.xdrXhRbQAI4wuL2aqrhBfcXNZG7-SuL7lId9QO9knCE Book1.xlsx')
        output = stream.read()
        
        #uniqk1 = st.text_input('Enter your Unique Key',help ='Please check your email for the unique key')
        uniqk1 = input('Enter Unique Key: ')


        if uniqk==uniqk1:   
                st.write(output)
                st.write('Copy this CID to access the secured file')
        
        if uniqk1 is None:
            st.write('Please type in your unique key:')

        anomalies = fl.find_anomaly('Book1.xlsx','Anomaly1')

        if anomalies is not None:
            