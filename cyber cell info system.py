
import pandas as pd
import pyttsx3
import os
import datetime
import csv
from random import randint
from matplotlib import pyplot as plt
import webbrowser
import datetime as dt
import subprocess

engine = pyttsx3.init()
engine.say('Welcome to Cyber Cell Information System')
engine.runAndWait()
 
t_date=datetime.date.today()
print("_____________________________________________________")
print("       WELCOME TO CYBER CELL INFORMATION SYSTEM      ")
print(" Devloped by: Varun Singh Rana","DATE:",t_date.day,"/",t_date.month,"/",t_date.year)
print("_____________________________________________________")

def menu():
    print("Enter 1:To File a Complaint")
    print("Enter 2:To Display Complaint Data")
    print("Enter 3:To Review Complaint")
    print("Enter 4:To Get Aware of Cyber Crime")
    print("Enter 5:To Exit")

menu()


def cfiling():
    id=str(randint(0,100000))
    cid=id
    st=randint("No_action_taken","Request_fulfilled")
    cname=input("Enter your Name :")
    idate=input("Enter the Date of Incident :")
    idetail=input("Enter Incident in Detail :")
    state=input("Enter Name of State :")
    dist=input("Enter Name of District :")
    city=input("Enter Name of city :")
    print(cname, idate, idetail, state, dist, city)
    input1=input("Enter Y/N to continue..")
    if input1=="Y" or input1=="y":
        print("Your complaint is.. ",cid)
        print("(please note down your complaint id)")
        print()
        print()
        print("Restarting System.....")
        print()
        menu()
        with open('Complaint.csv','a', newline='')as outfile:
            w=csv.writer(outfile)
            w.writerow([cid, cname, idate, idetail, state, dist, city, st])
            
            
    if input1=="N" or input1=="n":
        print('Stopping')
        #outfile.close()
        print()
        print()
        menu()

def displaydata():
        print('Enter 1: to see state graph')
        print('Enter 2: to go back')
        print('Enter 3: Exit')
        ch2=int(input("Enter the Choice -"))
        if ch2==1:
            df=pd.read_csv(r"Complaint.csv")
            #state_data=df["State"].unique()
            state_data=['delhi','west bengal','Uttarakhand','uttar pradesh','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Maharashtra','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Andaman and Nicobar Islands','Dadra & Nagar Haveli and Daman & Diu','Chandigarh','Jammu and Kashmir','Lakshadweep','Ladakh','Puducherry']
            dl=wb=uk=up=ap=ar=am=bh=ch=go=gj=hr=hp=jh=kn=ke=mp=mh=ma=mg=mi=ng=od=pj=mh=rj=sk=tn=tg=tr=ai=dd=cg=jk=lw=ld=pu=0
            for i in range(df.shape[0]):
                if df.iat[i,4]=='delhi':
                    dl=dl+1
                if df.iat[i,4]=='west bengal':
                    wb=wb+1
                if df.iat[i,4]=='Uttarakhand':
                    uk=uk+1
                if df.iat[i,4]=='uttar pradesh':
                    up=up+1
                if df.iat[i,4]=='Andhra Pradesh':
                    ap=ap+1
                if df.iat[i,4]=='Arunachal Pradesh':
                    ar=ar+1
                if df.iat[i,4]=='Assam':
                    am=am+1
                if df.iat[i,4]=='Bihar':
                    bh=bh+1
                if df.iat[i,4]=='Chhattisgarh':
                    ch=ch+1
                if df.iat[i,4]=='Goa':
                    go=go+1
                if df.iat[i,4]=='Gujarat':
                    gj=gj+1
                if df.iat[i,4]=='Haryana':
                    hr=hr+1
                if df.iat[i,4]=='Himachal Pradesh':
                    hp=hp+1
                if df.iat[i,4]=='Jharkhand':
                    jh=jh+1
                if df.iat[i,4]=='Karnataka':
                    kn=kn+1
                if df.iat[i,4]=='Kerala':
                    ke=ke+1
                if df.iat[i,4]=='Madhya Pradesh':
                    mp=mp+1
                if df.iat[i,4]=='Maharashtra':
                    mh=mh+1
                if df.iat[i,4]=='Manipur':
                    ma=ma+1
                if df.iat[i,4]=='Meghalaya':
                    mg=mg+1
                if df.iat[i,4]=='Mizoram':
                    mi=mi+1
                if df.iat[i,4]=='Nagaland':
                    ng=ng+1
                if df.iat[i,4]=='Odisha':
                    od=od+1
                if df.iat[i,4]=='Punjab':
                    pj=pj+1
                if df.iat[i,4]=='Maharashtra':
                    mh=mh+1
                if df.iat[i,4]=='Rajasthan':
                    rj=rj+1
                if df.iat[i,4]=='Sikkim':
                    sk=sk+1
                if df.iat[i,4]=='Tamil Nadu':
                    tn=tn+1
                if df.iat[i,4]=='Telangana':
                    tg=tg+1
                if df.iat[i,4]=='Tripura':
                    tr=tr+1
                if df.iat[i,4]=='Andaman and Nicobar Islands':
                    ai=ai+1
                if df.iat[i,4]=='Dadra & Nagar Haveli and Daman & Diu':
                    dd=dd+1
                if df.iat[i,4]=='Chandigarh':
                    cg=cg+1
                if df.iat[i,4]=='Jammu and Kashmir':
                    jk=jk+1
                if df.iat[i,4]=='Lakshadweep':
                    lw=lw+1
                if df.iat[i,4]=='Ladakh':
                    ld=ld+1
                if df.iat[i,4]=='Puducherry':
                    pu=pu+1

             
            
            cid=[dl,wb,uk,up,ap,ar,am,bh,ch,go,gj,hr,hp,jh,kn,ke,mp,mh,ma,mg,mi,ng,od,pj,mh,rj,sk,tn,tg,tr,ai,dd,cg,jk,lw,ld,pu]
            explode=(0.1,0,0,0,0)
            plt.pie(cid, labels=state_data, autopct='%1.1f%%', startangle=50)
            #plt.legend(cid, labels=state_data, loc='center left', bbox_to_anchor=(-0.1, 1.),fontsize=8)
            plt.title("state data")
            plt.show()
        if ch2==2:
            menu()
            print()
        if ch2==3:
            exit()
            
    
def crview():
    ci=input('Enter Complaint ID:')
    df=pd.read_csv(r'Complaint.csv',header=None)
    #df2=df.to_string(index=False)
    df1=df[df[0]==ci]
    print('Your Complaint Details :')
    blankIndex=[' '] * len(df1)
    df1.index=blankIndex
    print(df1)
    

def crimeawareness():
    print("Enter 1:To see Cyber Crime Awareness PDF File")
    print("Enter 2:To Known more")
    print("Enter 3:To Go Back")
    print("Enter 4:To EXIT")
    ch3=int(input("Enter the Choice -"))
    if ch3==1:
        path = 'Cyber Crime Awareness.pdf'
        subprocess.Popen([path], shell=True)
        menu()
        print()
    if ch3==2:
        url="https://cybercrime.gov.in/Webform/CyberAware.aspx"
        webbrowser.open(url)
        menu()
        print()
    if ch3==3:
        menu()
        print()
    if ch3==4:
        exit()

while True:
    ch=int(input("->Select Any Option From Above:"))
    if ch>0 and ch<6:
        print("You Selected..",ch)
    else:
        print("Invalid Option Selected")
    if(ch==1):
        cfiling()
    elif(ch==2):
        displaydata()
    elif(ch==3):
        crview()
    elif(ch==4):
        crimeawareness()
    elif(ch==5):
        print("Thank you for your time")
        break
        

