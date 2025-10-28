from tkinter import *
from PIL import Image, ImageTk 
from tkinter import messagebox
import random,os,tempfile,smtplib
#FUNCTIONLITY PART:

def clear():
       bathsoapEntry.delete(0,END)
       facecreamEntry.delete(0,END)
       shampooEntry.delete(0,END)
       hairsprayEntry.delete(0,END)
       bodylotionEntry.delete(0,END)
       facewashEntry.delete(0,END)

       riceEntry.delete(0,END)
       oilEntry.delete(0,END)
       wheatEntry.delete(0,END)
       sugarEntry.delete(0,END)
       daalEntry.delete(0,END)
       teaEntry.delete(0,END)

       cokeEntry.delete(0,END)
       fantaEntry.delete(0,END)
       spriteEntry.delete(0,END)
       limcaEntry.delete(0,END)
       pepsiEntry.delete(0,END)
       majaEntry.delete(0,END)

       bathsoapEntry.insert(0,0)
       facecreamEntry.insert(0,0)
       shampooEntry.insert(0,0)
       hairsprayEntry.insert(0,0)
       bodylotionEntry.insert(0,0)
       facewashEntry.insert(0,0) 

       riceEntry.insert(0,0)
       oilEntry.insert(0,0)
       wheatEntry.insert(0,0)
       sugarEntry.insert(0,0)
       daalEntry.insert(0,0)
       teaEntry.insert(0,0)

       cokeEntry.insert(0,0)
       fantaEntry.insert(0,0)
       spriteEntry.insert(0,0)
       limcaEntry.insert(0,0)
       pepsiEntry.insert(0,0)
       majaEntry.insert(0,0)
            

       cosmeticpriceEntry.delete(0,END)
       grocerypriceEntry.delete(0,END)
       drinkspriceEntry.delete(0,END)

       cosmetictaxEntry.delete(0,END)
       grocerytaxEntry.delete(0,END)
       drinkstaxEntry.delete(0,END)

       nameEntry.delete(0,END)
       phoneEntry.delete(0,END)
       billnumberEntry.delete(0,END)

       textarea.delete(1.0,END)




def send_email():
    def send_gmail():
       try:
          ob=smtplib.SMTP('smtp.gmail.com',587)
          ob.starttls()
          ob.login(senderEntry.get(),passwordEntry.get())
          message=email_textarea.get(1.0,END)
          ob.sendermail(senderEntry.get(),recieverEntry.get(),message)
          ob.quit()
          messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
          root1.destroy()
       except:
             messagebox.showerror('Error','Something went wrong ,Please try again',parent=root1)
             


    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send Mail') 
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        # ---------------- SENDER FRAME ----------------
        senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'),
                                 bd=6, bg='gray20', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email",
                            font=('arial', 14, 'bold'), bg='gray20', fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'),
                            bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text='Password',
                              font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'),
                              bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        # ---------------- RECIPIENT FRAME ----------------
        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'),
                                    bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverlabel = Label(recipientFrame, text='Email Address',
                              font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverlabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'),
                              bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text='Message',
                             font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)

        email_textarea.delete(1.0,END)

        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
       
        fd, file_path = tempfile.mkstemp(suffix='.txt')
        with os.fdopen(fd, 'w') as f:
            f.write(textarea.get(1.0, END))
        os.startfile(file_path, 'print')
      



def search_bill():
      for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
              f=open(f'bill/{i}','r')
              textarea.delete(1.0,END)
              for data in f:
                    textarea.insert(END,data)
              f.close() 
              break
      else:
            messagebox.showerror('Error','Invalid Bill Number')             
            


if not os.path.exists('bills'):
       os.mkdir('bills')



def save_bill():
      global billnumber
      result=messagebox.askyesno('Confire','Do you want to save the bill?')
      if result:
             bill_content=textarea.get(1.0,END)
             file=open(f'bills/{billnumber}.txt','w')
             file.write(bill_content)
             file.close()
            
             messagebox.showinfo('Sucess',f'bill number{billnumber} is saved successfully')
             billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)
def bill_area():
    if nameEntry.get()==''or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()==''and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs'and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
         messagebox.showerror('Error','No Products are Selected')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,'\t\t**WELCOME CUSTOMER**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        if bathsoapEntry.get()!='0':
              textarea.insert(END,f'\nBath Soap \t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')

        if hairsprayEntry.get()!='0':
              textarea.insert(END,f'\nHair Spray \t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')

        if facecreamEntry.get()!='0':
               textarea.insert(END,f'\nFace Cream \t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')    

        if facewashEntry.get()!='0':
              textarea.insert(END,f'\nFace Wash \t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')

        if shampooEntry.get()!='0':
              textarea.insert(END,f'\nShampoo \t\t\t{shampooEntry.get()}\t\t\t{ shampooprice} Rs')      
         
        if bodylotionEntry.get()!='0':
              textarea.insert(END,f'\nBody Lotion \t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')   
        
        if riceEntry.get()!='0':
              textarea.insert(END,f'\nRice \t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        
        if oilEntry.get()!='0':
              textarea.insert(END,f'\nOil \t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        
        if wheatEntry.get()!='0':
               textarea.insert(END,f'\nWheat \t\t\t{oilEntry.get()}\t\t\t{wheatprice} Rs')

        if sugarEntry.get()!='0':
               textarea.insert(END,f'\nSugar \t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')  

        if daalEntry.get()!='0':
               textarea.insert(END,f'\nDaal \t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')          

        if teaEntry.get()!='0':
               textarea.insert(END,f'\nTea \t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')                 

        if cokeEntry.get()!='0':
               textarea.insert(END,f'\nCoke \t\t\t{cokeEntry.get()}\t\t\t{ cokeprice} Rs')    

        if fantaEntry.get()!='0':
               textarea.insert(END,f'\nFanta \t\t\t{fantaEntry.get()}\t\t\t{ fantaprice} Rs')

        if spriteEntry.get()!='0':
               textarea.insert(END,f'\nSprite \t\t\t{spriteEntry.get()}\t\t\t{ spriteprice} Rs')   

        if limcaEntry.get()!='0':
               textarea.insert(END,f'\nLimca \t\t\t{limcaEntry.get()}\t\t\t{ limcaprice} Rs')   

        if pepsiEntry.get()!='0':
               textarea.insert(END,f'\nPepsi \t\t\t{pepsiEntry.get()}\t\t\t{ pepsiprice} Rs')

        if majaEntry.get()!='0':
               textarea.insert(END,f'\nMaja \t\t\t{majaEntry.get()}\t\t\t{ majaprice} Rs')                      
 
        textarea.insert(END,'\n=======================================================')

        if cosmeticpriceEntry.get()!='0.0 Rs':  
              textarea.insert(END,f'\nCosmatic Tax\t\t\t\t{cosmetictaxEntry.get()}')     

        if grocerypriceEntry.get()!='0.0 Rs':  
              textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}') 

        if drinkspriceEntry.get()!='0.0 Rs':  
               textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}') 

        textarea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill}')  

        textarea.insert(END,'\n=======================================================')     
        
        save_bill()





def total():
    global soapprice,hairsprayprice,facecreamprice,facecreamprice,facewashprice,shampooprice, bodylotionprice
    global riceprice,oilprice,wheatprice,sugarprice,daalprice,teaprice
    global cokeprice,fantaprice,spriteprice, limcaprice,pepsiprice,majaprice
    global totalbill

    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    shampooprice=int(shampooEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+shampooprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice}Rs')
    cosmtictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,str(cosmtictax)+'Rs')

   #grocery price calculation
    riceprice=int(riceEntry.get())*30
    oilprice=int(oilEntry.get())*100
    wheatprice=int(wheatEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    daalprice=int(daalEntry.get())*140
    teaprice=int(teaEntry.get())*80

    totalgroceryprice = riceprice+oilprice+wheatprice+sugarprice+daalprice+teaprice
    grocerypriceEntry.delete(0,E)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'Rs')

    cokeprice=int(cokeEntry.get())*50
    fantaprice=int(fantaEntry.get())*20
    spriteprice=int(spriteEntry.get())*30
    limcaprice=int(limcaEntry.get())*20
    pepsiprice=int(pepsiEntry.get())*45
    majaprice=int(majaEntry.get())*90
   
    totaldrinksprice=cokeprice+fantaprice+spriteprice+limcaprice+pepsiprice+majaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,str(totaldrinksprice)+'Rs')
    drinkstax=totalcosmeticprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinkstax)+'Rs')                     
    
    totalbill = totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmtictax+grocerytax+drinkstax
    
#GUI:
root=Tk() 
root.title('Retail Billing System')
root.geometry('1270x685')
root.configure(bg="#e6f0fa")
icon_path = r"C:\Users\HP\OneDrive\Desktop\intership\icon.png"
img = Image.open(icon_path)
img = img.resize((32,329), Image.LANCZOS) 
icon_image = ImageTk.PhotoImage(img)
root.iconphoto(False, icon_image)


headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='#1e3d59',fg='white',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='white',bd=8,relief=GROOVE,bg='#4a6fa5')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(    customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root,bg="#e6f0fa")
productsFrame.pack(pady=10)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='white',bd=8,relief=GROOVE,bg='#4a6fa5')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='face cream',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='face wash',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

shampooLabel=Label(cosmeticsFrame,text='Shampoo',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
shampooLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')


shampooEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
shampooEntry.grid(row=3,column=1,pady=9,padx=10,)
shampooEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair spray',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
hairsprayLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=4,column=1,pady=9,padx=10,)
hairsprayEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Bodylotion',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10,)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='white',bd=8,relief=GROOVE,bg='#4a6fa5')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10,)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10,)
oilEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
wheatLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=2,column=1,pady=9,padx=10,)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
sugarLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=1,pady=9,padx=10,)
sugarEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
daalLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=4,column=1,pady=9,padx=10,)
daalEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10,)
teaEntry.insert(0,0)

colddrinksFrame=LabelFrame(productsFrame,text='Cold drinks',font=('times new roman',15,'bold'),fg='white',bd=8,relief=GROOVE,bg='#4a6fa5')
colddrinksFrame.grid(row=0,column=2)

cokeLabel=Label(colddrinksFrame,text='Coke',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
cokeLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cokeEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cokeEntry.grid(row=0,column=1,pady=9,padx=10,)
cokeEntry.insert(0,0)

fantaLabel=Label(colddrinksFrame,text='Fanta',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
fantaLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

fantaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fantaEntry.grid(row=1,column=1,pady=9,padx=10,)
fantaEntry.insert(0,0)

spriteLabel=Label(colddrinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,)
spriteEntry.insert(0,0)

limcaLabel=Label(colddrinksFrame,text='Limca',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
limcaLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

limcaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
limcaEntry.grid(row=3,column=1,pady=9,padx=10,)
limcaEntry.insert(0,0)

pepsiLabel=Label(colddrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
pepsiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=4,column=1,pady=9,padx=10,)
pepsiEntry.insert(0,0)

majaLabel=Label(colddrinksFrame,text='Maja',font=('times new roman',15,'bold'),bg='#4a6fa5',fg='white')
majaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

majaEntry=Entry(colddrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
majaEntry.grid(row=5,column=1,pady=9,padx=10,)
majaEntry.insert(0,0)

billFrame=Frame(productsFrame,bd=8,relief=GROOVE,bg='#e6f0fa')
billFrame.grid(row=0,column=3,padx=10)

billareaLabel=Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7 ,bg='#1e3d59',fg='white',relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

textarea=Text(billFrame,height=18,width=55,yscrollcommand=scrollbar.set,bg='white',fg='black')
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill menu',font=('times new roman',15,'bold'),fg='white',bd=8,relief=GROOVE,bg='#4a6fa5')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic price',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10,)

grocerypriceLabel=Label(billmenuFrame,text='Grocery price',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10,)

drinkspriceLabel=Label(billmenuFrame,text='Cold drink price',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10,)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic tax',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10,)

grocerytaxLabel=Label(billmenuFrame,text='Grocery tax',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10,)

drinkstaxLabel=Label(billmenuFrame,text='Cold drink tax',font=('times new roman',14,'bold'),bg='#4a6fa5',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10,)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='#4a6fa5',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='#4a6fa5',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='#4a6fa5',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='#4a6fa5',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='#4a6fa5',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)







root.mainloop()





























