
#CODE FOR SCREEN

import tkinter as tk, threading
import tkinter.messagebox as MessageBox;
import mysql.connector as mysql
from PIL import Image,ImageTk 
import os
import mysql.connector as sqlcon 
import turtle
import time
import math
from tkinter import*
ss=Tk()
ss.title("SOLAR SYSTEM")

#SIZE OF WINDOW:
ss.maxsize(width=2000,height=1000)
ss.minsize(width=1950,height=1000)
#SCREEN COLOUR:
colour=Canvas(ss,bg='black')
colour.place(width=2000,height=1000)

#LABEL:
label1=Label(ss,text='𝓒.𝓢 𝓟𝓡𝓞𝓙𝓔𝓒𝓣',bg='black',fg="WHITE",font=("courier",70))
label1.place(x=650,y=360)
label2=Label(ss,text='𝔾𝕌𝕀𝔻𝔼𝔻 𝔹𝕐:',bg='black',fg='#F0FFF0',font=("courier",50))
label2.place(x=50,y=630)
label3=Label(ss,text='𝕊𝕌𝔹𝕄𝕀𝕋𝕋𝔼𝔻 𝔹𝕐:',bg='black',fg='#F0FFF0',font=("courier",50))
label3.place(x=1200,y=630)
label4=Label(ss,text='MR. SAMEER KUMAR',bg='black',fg='sky blue',font=('courier',40))
label4.place(x=50,y=730)
label5=Label(ss,text='(PGT Computer Science)',bg='black',fg='sky blue',font=('courier',40))
label5.place(x=40,y=800)
label6=Label(ss,text='𝒴𝒜𝒯𝐼𝒩,27',bg='black',fg='sky blue',font=('courier',45))
label6.place(x=1350,y=700)
label7=Label(ss,text='𝒴𝒰𝒱𝑅𝒜𝒥,28',bg='black',fg='sky blue',font=('courier',45))
label7.place(x=1350,y=800)
label8=Label(ss,text='jhgshdgys',bg='black',fg='sky blue',font=('courier',45))
label8.place(x=1350,y=900)
file1=PhotoImage(file="C:/Users/Admin/Desktop/JNVTAG-removebg-preview.png")
label9=Label(ss,image=file1,bg='black')
label9.place(x=600,y=80)
label10=Label(ss,text='(𝓚𝓐𝓤𝓛𝓐𝓝,𝓐𝓜𝓑𝓐𝓛𝓐)',bg='black',fg='DARK ORANGE',font=('courier',45))
label10.place(x=660,y=180)
label11=Label(ss,text='𝓣𝓞𝓟𝓘𝓒:𝓢𝓞𝓛𝓐𝓡 𝓢𝓨𝓢𝓣𝓔𝓜',bg='black',fg='red',font=('courier',70),width=20)
label11.place(x=400,y=460)
file2=PhotoImage(file="C:/Users/Admin/Desktop/YATIN YUVRAJ CS/JNV_LOGO2-removebg-preview.png")
label12=Label(ss,image=file2,bg='black')
label12.place(x=1500,y=100)
label13=Label(ss,image=file2,bg='black')
label13.place(x=130,y=100)
label14=Label(ss,text='2022-2023',bg='black',fg='white',font=('courier',40))
label14.place(x=770,y=280)

def tab():
#CREATING THE SCREEN:    
    win=turtle.Screen()
    win.bgpic('stars1.gif')
    win.bgcolor('black')
    win.setup(width=2000,height=1000)
    win.title('SOLAR SYSTEM')
    
#CREATING THE PEN:
    pen=turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    
#WRITING SOLAR SYSTEM:
    pen.color('red')
    pen.goto(-300,320)
    style=('courier',50,'bold')
    pen.write('OUR SOLAR SYTEM',font=style,align='right')
    win.addshape('img2.gif')
    m=turtle.Turtle()
    m.penup()
    m.goto(-220,360)
    m.pendown()
    m.shape('img2.gif')

    def tab1(a,b):
        import mysql.connector as sqlcon 
        mycon= sqlcon.connect(host="localhost", user="root", passwd="root") 

        if mycon.is_connected():     
            print("database connected successfully")    
        try:
            mycur=mycon.cursor() 
            qry="CREATE DATABASE solarsystem" 
            mycur.execute(qry) 
            print("Database created successfully")  
        except:
            print("Databse Already Created")



 
        mycon= sqlcon.connect(host="localhost", user="root", passwd="root", database="solarsystem",charset='utf8') 
 
        try:
            mycur=mycon.cursor() 
 
            mycur.execute("CREATE TABLE our_solar_system(planet_number int() primary key, planet_Name varchar(15), planet_colour  varchar(10), Period_of_revolution varchar(15), Period_of_rotation varchar(15), density float(4),  distance_from_the_sun varchar(15), planet_temprature float(5))")

            print("Table created successfully") 
        except:
            print("Table Created Already")



#MySQL Databse connection 

        import mysql.connector as sqlcon 
     
        mycon= sqlcon.connect(host="localhost", user="root", passwd="root", database="solarsystem") 

        if mycon.is_connected():     
            print("Connected to MYSQL database successfully") 
            mycur= mycon.cursor()




        def insert():
            planet_number=e_planet_number.get();
            planet_name=e_planet_name.get();
            planet_colour=e_planet_colour.get();
            Period_of_revolution =e_Period_of_revolution.get();
            Period_of_rotation =e_Period_of_rotation.get();
            density =e_density.get(); 
            distance_from_the_sun =e_distance_from_the_sun.get();
            planet_temprature =e_planet_temprature.get();
    
    
    
            if( planet_number=="" or planet_name==""or planet_colour=="" or Period_of_revolution =="" or Period_of_rotation=="" or
            density ==""or distance_from_the_sun =="" or  planet_temprature=="" ):
                MessageBox.showinfo("Insert Status","All Fields are required")
            else:
                con=mysql.connect(host="localhost",user="root",password="root",database="solarsystem")
                cursor=con.cursor()
        
                cursor.execute("INSERT INTO our_solar_system (planet_number,planet_name,planet_colour,Period_of_revolution,Period_of_rotation,density,distance_from_the_sun,planet_temprature)VALUES ('"+ planet_number +"','"+ planet_name +"','"+ planet_colour +"','"+ Period_of_revolution +"','"+Period_of_rotation+"','"+ density +"','"+ distance_from_the_sun +"','" +planet_temprature+"')")
                cursor.execute("commit");
        
                e_planet_number.delete(0,'end')
                e_planet_name.delete(0,'end')
                e_planet_colour.delete(0,'end')
                e_Period_of_revolution.delete(0,'end')
                e_Period_of_rotation.delete(0,'end')
                e_density.delete(0,'end')
                e_distance_from_the_sun.delete(0,'end')
                e_planet_temprature.delete(0,'end')
       
        

        
        
                MessageBox.showinfo("Data sucessesfully inserted");
                con.close();
        
        def delete():
    
    
            if(e_planet_number.get()==""):
                        MessageBox.showinfo("Delete Status","ID is compulsory for delete")
            else:
                con=mysql.connect(host="localhost",user="root",password="root",database="solarsystem")
                cursor=con.cursor()
                cursor.execute("delete from our_solar_system where planet_number='"+ e_planet_number.get() +"'")
                cursor.execute("commit")
        
                e_planet_number.delete(0,'end')
                e_planet_name.delete(0,'end')
                e_planet_colour.delete(0,'end')
                e_Period_of_revolution.delete(0,'end')
                e_Period_of_rotation.delete(0,'end')
                e_density.delete(0,'end')
                e_distance_from_the_sun.delete(0,'end')
                e_planet_temprature.delete(0,'end')
        
        

        
        
                MessageBox.showinfo("Data succsesfully removed");
                con.close();



        def update():
    
    
            planet_name=e_planet_name.get();
            planet_colour=e_planet_colour.get();
            Period_of_revolution =e_Period_of_revolution.get();
            Period_of_rotation =e_Period_of_rotation.get();
            density =e_density.get(); 
            distance_from_the_sun=e_distance_from_the_sun.get();
            planet_temprature =e_planet_temprature.get();
            planet_number=e_planet_number.get();
    
    
    
            if( planet_number=="" or planet_name=="" or Period_of_revolution =="" or Period_of_rotation=="" ):
                MessageBox.showinfo("Update Status","All Fields are required")
            else:
                con=mysql.connect(host="localhost",user="root",password="root",database="solarsystem")
                cursor=con.cursor()
                query=("UPDATE our_solar_system SET planet_name=%s,planet_colour=%s,Period_of_revolution=%s,Period_of_rotation=%s,density=%s,distance_from_the_sun=%s,planet_temprature=%s where planet_number=%s")
                record=(planet_name ,planet_colour, Period_of_revolution, Period_of_rotation, density , distance_from_the_sun,  planet_temprature,planet_number)
                cursor.execute(query,record)
        
                cursor.execute("commit");
        
                e_planet_number.delete(0,'end')
                e_planet_name.delete(0,'end')
                e_planet_colour.delete(0,'end')
                e_Period_of_revolution.delete(0,'end')
                e_Period_of_rotation.delete(0,'end')
                e_density.delete(0,'end')
                e_distance_from_the_sun.delete(0,'end')
                e_planet_temprature.delete(0,'end')
        
       
                MessageBox.showinfo("Data succesesfully updated");
                con.close();        

        def get():
    
    
    
            planet_number=e_planet_number.get();
            if (e_planet_number.get()==""):
                MessageBox.showinfo("Fetch Status","ID is compulsory for getting output")

   
        
            else:
                con=mysql.connect(host="localhost",user="root",password="root",database="solarsystem")
                cursor=con.cursor()
                cursor.execute("select * from our_solar_system where planet_number='"+ planet_number +"'")
                rows=cursor.fetchall()
        
                for row in rows:
                    e_planet_name.insert(0,row[1])
                    e_planet_colour.insert(0,row[2])
                    e_Period_of_revolution.insert(0,row[3])
                    e_Period_of_rotation.insert(0,row[4])
                    e_density.insert(0,row[5])
                    e_distance_from_the_sun.insert(0,row[6])
                    e_planet_temprature.insert(0,row[7])
            
            
            
        
        
                    con.close();

        def clear():
            e_planet_number.delete(0,'end')
            e_planet_name.delete(0,'end')
            e_planet_colour.delete(0,'end')
            e_Period_of_revolution.delete(0,'end')
            e_Period_of_rotation.delete(0,'end')
            e_density.delete(0,'end')
            e_distance_from_the_sun.delete(0,'end')
            e_planet_temprature.delete(0,'end')
        def exit():
            d=MessageBox.askyesno("Exit Status","Do You Want to Exit")
            if d:
                root.destroy()
        root=Tk()
        root.geometry("2200x2200")
        root.title("solar system ")
        colour=Canvas(root,bg='skyblue')
        colour.place(width=2200,height=2200)

        Main_Title= Label(root,text='DATA ENTRY ',font=('bold',50),bg="skyblue").place(x=260,y=10)



        a = Label(root,text='𝓟𝓛𝓐𝓝𝓔𝓣 𝓝𝓞. :',font=('bold',25),bg="cyan")
        a.place(x=20,y=140)


        name = Label(root,text=' 𝓟𝓛𝓐𝓝𝓔𝓣 𝓝𝓐𝓜𝓔: ',font=('bold',25),bg="cyan")
        name.place(x=20,y=200)

        b = Label(root,text='𝓟𝓛𝓐𝓝𝓔𝓣 𝓒𝓞𝓛𝓞𝓤𝓡:',font=('bold',25),bg="cyan")
        b.place(x=20,y=260)

        c = Label(root,text='𝓟𝓔𝓡𝓘𝓞𝓓 𝓞𝓕 𝓡𝓔𝓥𝓞𝓛𝓤𝓣𝓘𝓞𝓝:',font=('bold',25),bg="cyan")
        c.place(x=20,y=325)
        c1=Label(root,text='(IN DAYS\YEARS)',font=('bold',15),bg="cyan").place(x=20,y=365)

        e= Label(root,text='𝓟𝓔𝓡𝓘𝓞𝓓 𝓞𝓕 𝓡𝓞𝓣𝓐𝓣𝓘𝓞𝓝:',font=('bold',25),bg='cyan').place(x=20,y=425)
        e1=Label(root,text='(IN DAYS\HOURS)',font=('bold',15),bg="cyan").place(x=20,y=470)
        f = Label(root,text='𝓓𝓔𝓝𝓢𝓘𝓣𝓨:',font=('bold',25),bg="cyan").place(x=20,y=520)
        f1=Label(root,text='(IN g/cm^3)',font=('bold',15),bg="cyan").place(x=20,y=560)


        g  = Label(root,text='𝓓𝓘𝓢𝓣𝓐𝓝𝓒𝓔 𝓕𝓡𝓞𝓜 𝓣𝓗𝓔 𝓢𝓤𝓝:',font=('bold',25),bg="cyan").place(x=20,y=610)

        i=Label(root,text='( IN km)',font=('bold',15),bg="cyan").place(x=20,y=650)
        h= Label(root,text='𝓟𝓛𝓐𝓝𝓔𝓣 𝓣𝓔𝓜𝓟𝓡𝓐𝓣𝓤𝓡𝓔:',font=('bold',25),bg="cyan").place(x=20,y=700)
        h1=Label(root,text='(IN CELCIUS DEGREE)',font=('bold',15),bg="cyan").place(x=20,y=740)
        i = Label(root,text='SOME PLANET NUMBER FOR',font=('bold',30),bg="cyan")
        i.place(x=1200,y=140)
        J = Label(root,text='INFORMATION:',font=('bold',25),bg="cyan")
        J.place(x=1200,y=120)
        K = Label(root,text='MERCURY : 1',font=('bold',25),bg="cyan")
        K.place(x=1200,y=100)
        L = Label(root,text='𝓟𝓛𝓐𝓝𝓔𝓣 𝓝𝓞. :',font=('bold',25),bg="cyan")
        L.place(x=1200,y=140)





        e_pathlabel = Entry(root)
        e_pathlabel1 = Entry(root)

        e_planet_number = Entry(root,font=("italic",25))
        e_planet_number.place(x=460,y=140)

        e_planet_name= Entry(root,font=("italic",25))
        e_planet_name.place(x=460,y=200)

        e_planet_colour = Entry(root, font=("italic",25))
        e_planet_colour.place(x=460,y=260)

        e_Period_of_revolution = Entry(root, font=("italic",25))
        e_Period_of_revolution.place(x=460,y=325)


        e_Period_of_rotation = Entry(root, font=("italic",25))
        e_Period_of_rotation.place(x=460,y=425)

        e_density = Entry(root, font=("italic",25))
        e_density.place(x=460,y=520)

        e_distance_from_the_sun = Entry(root, font=("italic",25))
        e_distance_from_the_sun.place(x=460,y=610)

        e_planet_temprature= Entry(root, font=("italic",25))
        e_planet_temprature.place(x=460,y=700)








        insert=Button(root,text="INPUT",font=("italic",25),width=13,bg="yellow",command=insert)
        insert.place(x=20,y=840)

        btn=Button(root,text="SHOW RECORD",font=("italic",25),width=15,bg="light green",command=get)
        btn.place(x=900,y=140)

        btn=Button(root,text="CLEAR",font=("italic",25),width=13,bg="light green",command=clear)
        btn.place(x=900,y=240)
        
        btn=Button(root,text="DELETE",font=("italic",25),width=13,bg="light green",command=delete)
        btn.place(x=900,y=340)

        btn=Button(root,text="UPDATE",font=("italic",25),width=13,bg="light green",command=update)
        btn.place(x=900,y=440)

        insert=Button(root,text="EXIT",font=("italic",25),width=13,bg="yellow",command=exit)
        insert.place(x=620,y=840)
        


    

    
    def sun(a,b):
        sc=Toplevel()
        colour1=Canvas(sc,bg='cadetblue')
        colour1.place(width=2000,height=1000)
        sc.maxsize(width=2000,height=1000)
        sc.minsize(width=1800,height=1000)
        label15=Label(sc,text='..*.SUN.*..',bg='black',fg='white',font=('courier',50))
        label15.place(x=800,y=0)
        file5=PhotoImage(file="sun.png")
        label16=Label(sc,image=file5)
        label16.place(x=1300,y=100)
#INFORMATION ABOUT SUN:        
        write=Label(sc,
                    text='''Our Sun is a 4.5 billion-year-old star a hot glowing ball of hydrogen and helium
at the center of our solar system.The Sun is about 93 million miles (150 million
from Earth, and without its energy,life as we know it could not exist here on
our home planet.The Sun is the star at the center of the Solar System It is a
nearly perfect ball of hot plasma, heated to incandescence by nuclear fusion
reactions in its core. The Sun radiates this energy mainly as light,ultravio-
let,and infrared radiation,and is the most important source of energy for life
on Earth.\n⇒Surface temperature:\n⇒Mass:1.989 ×10^30kg
⇒Distance to Earth:149.6 million km\n⇒Age:4.603 billion years
⇒Radius: 696,340 km
⇒Density: 1.41 g/cm³''',font=('courier',20),bg='cadetblue',relief= 'solid')
        
        write.place(x=0,y=100)                    
#BACK AND UPDATE BUTTON:
        btn2=Button(sc,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
        btn2.place(x=80,y=800)
        def back1():
            sc.destroy()
            
        btn3=Button(sc,text='BACK',command=back1,bg='black',fg='red',font=('courier',30))
        btn3.place(x=1600,y=800)
        
        sc.mainloop()
        
    def mercury(a,b):
        sc1=Toplevel()
        colour2=Canvas(sc1,bg='cadetblue')
        colour2.place(width=2000,height=1000)
        sc1.maxsize(width=2000,height=1000)
        sc1.minsize(width=1800,height=1000)
        label17=Label(sc1,text='MERCURY',bg='black',fg='white',font=('courier',50))
        label17.place(x=800,y=0)
#INFORMATION ABOUT MERCURY:        
        info=Label(sc1,text='INFORMATION ABOUT MERCURY:',font=('courier',50),bg='cadetblue',fg='darkblue')
        info.place(x=0,y=100)
        write_1=Label(sc1,text='''Mercury is the fastest planet in our solar system – traveling through space at
nearly 29 miles(47 kilometers) per second.The closer a planetb is to the Sun,
the faster it travels.Mercury is the smallest planet in the Solar System and
the closest to the Sun.Its orbit around the Sun takes 87.97 Earth days, the
shortest of all the Sun's planets.Mercury rotates in a way that is unique in
the Solar System.
⇒Distance from Sun: 58 million km
⇒Orbital period: 88 days
⇒Radius: 2,439.7 km
⇒Surface area: 74.8 million km²
⇒Mass: 3.285 × 10^23 kg (0.055 M⊕)
⇒Length of day: 58d 15h 30m''',font=('courier',20),bg='cadetblue',relief='solid')
        write_1.place(x=20,y=180)
        file6=PhotoImage(file="mercury.png")
        label18=Label(sc1,image=file6)
        label18.place(x=1300,y=100)
#BACK AND UPDATE BUTTON:        
        btn4=Button(sc1,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
        btn4.place(x=80,y=800)
        def back2():
            sc1.destroy()
            
        btn5=Button(sc1,text='BACK',command=back2,bg='black',fg='red',font=('courier',30))
        btn5.place(x=1600,y=800)
        sc1.mainloop()
         
    def venus(a,b):
        sc2=Toplevel()
        colour3=Canvas(sc2,bg='cadetblue')
        colour3.place(width=2000,height=1000)
        sc2.maxsize(width=2000,height=1000)
        sc2.minsize(width=1800,height=1000)
        label19=Label(sc2,text='VENUS',bg='black',fg='white',font=('courier',50))
        label19.place(x=800,y=0)
#INFORMATION ABOUT VENUS:
        info1=Label(sc2,text='INFORMATION ABOUT VENUS:',bg='cadetblue',font=('courier',50),fg='darkorange'
                    ).place(x=10,y=100)
        write_2=Label(sc2,text='''Venus is the second planet from the Sun and is Earth's closest planetary neighbor.
It's one of the four inner, terrestrial (or rocky) planets, and it's often called
Earth's twin because it's similar in size and density.These are not identical twi-
ns, however – there are radical differences between the two worlds.It is sometimes
called Earth's "sister" or "twin" planet as it is almost as large and has a similar
composition. As an interior planet to Earth, Venus appears in Earth's sky never
far from the Sun, either as morning star or evening star.It is smalll and rocky.
⇒Distance from Sun: 108.2 million km
⇒Radius: 6,051.8 km
⇒Orbital period: 225 days
⇒Mass: 4.867 × 10^24 kg (0.815 M⊕)
⇒Surface area: 460.2 million km²
⇒Density: 5.24 g/cm³''',font=('courier',20),bg='cadetblue',relief='solid').place(x=10,y=180)
        file7=PhotoImage(file="venus.png")
        label20=Label(sc2,image=file7)
        label20.place(x=1350,y=100)
#BACK AND UPDATE BUTTON:
        btn6=Button(sc2,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
        btn6.place(x=80,y=800)
        def back3():
            sc2.destroy()
            
        btn7=Button(sc2,text='BACK',command=back3,bg='black',fg='red',font=('courier',30))
        btn7.place(x=1600,y=800)
        sc2.mainloop()
        
    def earth(a,b):
        sc3=Toplevel()
        colour4=Canvas(sc3,bg='cadetblue')
        colour4.place(width=2000,height=1000)
        sc3.maxsize(width=2000,height=1000)
        sc3.minsize(width=1800,height=1000)
        label21=Label(sc3,text='EARTH',bg='black',fg='white',font=('courier',50))
        label21.place(x=800,y=0)
#INFORMATION ABOUT EARTH:
        info2=Label(sc3,text='INFORMATION ABOUT EARTH:',bg='cadetblue',fg='red',font=('courier',50)).place(x=10,y=100)
        write_3=Label(sc3,text='''Earth is only the fifth largest planet in the solar system, it is the only
world in our solar system with liquid water on the surface. Just slightly
larger than nearby Venus, Earth is the biggest of the four planets closest
to the Sun, all of which are made of rock and metal.Earth is the third
planet from the Sun and the only astronomical object known to harbor life.
While large volumes of water can be found throughout the Solar System,only
Earth sustains liquid surface water. About 71% of Earth's surface is made
up of the ocean, dwarfing Earth's polar ice, lakes, and  rivers.
⇒Radius: 6,371 km
⇒Mass: 5.972 × 10^24 kg
⇒Age: 4.543 billion years
⇒Distance from Sun: 149.6 million km
⇒Gravity: 9.807 m/s²
⇒Surface area: 510.1 million km²
⇒Population: 783.66 crores (2021)''',bg='cadetblue',font=('courier',20),relief='solid').place(x=10,y=180)
        file8=PhotoImage(file="earth.png")
        label22=Label(sc3,image=file8)
        label22.place(x=1250,y=100)
#BACK AND UPDATE BUTTON:        
        btn8=Button(sc3,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
        btn8.place(x=80,y=800)
        def back4():
            sc3.destroy()
            
        btn9=Button(sc3,text='BACK',command=back4,bg='black',fg='red',font=('courier',30))
        btn9.place(x=1600,y=800)
        sc3.mainloop()
    def mars(a,b):
         sc4=Toplevel()
         colour5=Canvas(sc4,bg='cadetblue')
         colour5.place(width=2000,height=1000)
         sc4.maxsize(width=2000,height=1000)
         sc4.minsize(width=1800,height=1000)
         label23=Label(sc4,text='MARS',bg='black',fg='white',font=('courier',50))
         label23.place(x=800,y=0)
#INFORMATION ABOUT MARS:
         info3=Label(sc4,text='⡷⠂𝙄𝙉𝙁𝙊𝙍𝙈𝘼𝙏𝙄𝙊𝙉 𝘼𝘽𝙊𝙐𝙏 𝙈𝘼𝙍𝙎⠐⢾➤',bg='cadetblue',fg='peach puff',
                     font=('courier',50)).place(x=0,y=100)
         write_4=Label(sc4,text='''Mars is the fourth planet from the Sun – a dusty, cold, desert world with
a very thin atmosphere. Mars is also a dynamic planet with seasons,polar
ice caps,canyons, extinct volcanoes, and evidence that it was even more
active in the pasthe second-smallest planet in the Solar System, only
being larger than Mercury. In the English language,\t\t\t 
Mars is named for the Roman god of war.
⇒Distance from Sun: 227.9 million km
⇒Orbital period: 687 days
⇒Radius: 3,389.5 km
⇒Mass: 6.39 × 10^23 kg (0.107 M⊕)
⇒Gravity: 3.721 m/s²''',bg='cadetblue',font=('courier',20),relief='solid').place(x=20,y=180)
         file9=PhotoImage(file="mars.png")
         label24=Label(sc4,image=file9)
         label24.place(x=1200,y=100)
#BACK AND UPDATE BUTTON:         
         btn10=Button(sc4,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
         btn10.place(x=80,y=800)
         
         def back5():
             sc4.destroy()
            
         btn12=Button(sc4,text='BACK',command=back5,bg='black',fg='red',font=('courier',30))
         btn12.place(x=1600,y=800)
         sc4.mainloop()

    def jupiter(a,b):
         sc5=Toplevel()
         colour6=Canvas(sc5,bg='cadetblue')
         colour6.place(width=2000,height=1000)
         sc5.maxsize(width=2000,height=1000)
         sc5.minsize(width=1800,height=1000)
         label25=Label(sc5,text='JUPITER',bg='black',fg='white',font=('courier',50))
         label25.place(x=800,y=0)
#INFORMATION ABOUT JUPITER:
         info4=Label(sc5,text='𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 𝐀𝐁𝐎𝐔𝐓 𝐉𝐔𝐏𝐈𝐓𝐄𝐑:',bg='cadetblue',fg='cyan',
                     font=('courier',50)).place(x=20,y=100)
         write_5=Label(sc5,text='''Jupiter is the fifth planet from our Sun and is, by far, the largest\t
planet in the solar system – more than twice as massive as all the other
planets combined. Jupiter's stripes and swirls are actually cold, windy
clouds of ammonia and water, floating in an atmosphere of hydrogen and
helium.It is a gas giant with a mass more than two and a half times\t
that of all the other planets in the Solar System combined, but slight-
ly less than one-thousandth the mass of the Sun.\t\t\t
⇒Distance from Sun: 778.5 million km
⇒Radius: 69,911 km
⇒Orbital period: 12 years
⇒Mass: 1.898 × 10^27 kg (317.8 M⊕)
⇒Surface area: 61.42 billion km²
⇒Coordinates: RA 0h 1m 37s|Dec-1°16′1″''',bg='cadetblue',
                       font=('courier',20),relief='solid').place(x=20,y=180)
         file10=PhotoImage(file="jupiter.png")
         label26=Label(sc5,image=file10)
         label26.place(x=1200,y=100)
#BACK AND UPDATE BUTTON:
         btn13=Button(sc5,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
         btn13.place(x=80,y=800)
         
         def back6():
             sc5.destroy()
            
         btn14=Button(sc5,text='BACK',command=back6,bg='black',fg='red',font=('courier',30))
         btn14.place(x=1600,y=800)
         sc5.mainloop()
   
    def saturn(a,b):
         sc6=Toplevel()
         colour7=Canvas(sc6,bg='cadetblue')
         colour7.place(width=2000,height=1000)
         sc6.maxsize(width=2000,height=1000)
         sc6.minsize(width=1800,height=1000)
         label27=Label(sc6,text='SATURN',bg='black',fg='white',font=('courier',50))
         label27.place(x=800,y=0)
#INFORMATION ABOUT SATURN:
         info5=Label(sc6 ,text='𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡 𝗔𝗕𝗢𝗨𝗧 𝗦𝗔𝗧𝗨𝗥𝗡:',font=('courier',60),bg='cadetblue',
                     fg='#DCDC14').place(x=20,y=100)
         write_6=Label(sc6,text='''Saturn is the sixth planet from the Sun and the second-largest planet in our
solar system. Like fellow gas giant Jupiter, Saturn is a massive ball made
mostly of hydrogen and helium. Saturn is not the only planet to have rings,
but none are as spectacular or as complex as Saturn's. Saturn also has doz-
ens of moons. after Jupiter. It is a gas giant with an average radius of
about nine and a half times that of Earth. It has only one-eighth the ave-
rage density of Earth; however, with its larger volume, Saturn is over 95
times more massive.\t\t\t\t\t\t\t
⇒Distance from Sun: 1.434 billion km
⇒Orbital period: 29 years
⇒Radius: 58,232 km
⇒Mass: 5.683 × 10^26 kg (95.16 M⊕)
⇒Surface area: 42.7 billion km²
⇒Age: 4.503 billion years''',
                       bg='cadetblue',font=('courier',20),relief='solid').place(x=20,y=180)
         file11=PhotoImage(file="saturn.png")
         label28=Label(sc6,image=file11)
         label28.place(x=1300,y=100)
#BACK AND UPDATE BUTTON:
         btn15=Button(sc6,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
         btn15.place(x=80,y=800)
         
         def back7():
             sc6.destroy()
            
         btn14=Button(sc6,text='BACK',command=back7,bg='black',fg='red',font=('courier',30))
         btn14.place(x=1600,y=800)
         sc6.mainloop()

    def uranus(a,b):
         sc6=Toplevel()
         colour7=Canvas(sc6,bg='cadetblue')
         colour7.place(width=2000,height=1000)
         sc6.maxsize(width=2000,height=1000)
         sc6.minsize(width=1800,height=1000)
         label27=Label(sc6,text='URANUS',bg='black',fg='white',font=('courier',50)).place(x=800,y=0)
#INFORMATION ABOUT URANUS:
         info6=Label(sc6,text='𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 𝐀𝐁𝐎𝐔𝐓 𝐔𝐑𝐀𝐍𝐔𝐒⇉',bg='cadetblue',fg='red',font=('courier',50)).place(x=20,y=100)
         write_7=Label(sc6,text='''Uranus is the seventh planet from the Sun, and has the third-largest diameter
in our solar system. It was the first planet found with the aid of a telescope,
Uranus was discovered in 1781 by astronomer William Herschel, although he\t
originally thought it was either a comet or a star.Its name is a reference to
the Greek god of the sky, Uranus, who, according to Greek mythology,was the
great-grandfather of Ares, grandfather of Zeus and father of Cronus.It has the
third-largest planetary radius and fourth-largest planetary mass in the Solar
System.\t\t\t\t\t\t\t\t\t
⇒Distance from Sun: 2.871 billion km
⇒Orbital period: 84 years
⇒Radius: 25,362 km
⇒Surface area: 8.083 billion km²
⇒Mass: 8.681 × 10^25 kg (14.54 M⊕)
⇒Length of day: 0d 17h 14m''',bg='cadetblue',
                       font=('courier',20),relief='solid').place(x=20,y=180)   
         file11=PhotoImage(file="uranus.png")
         label28=Label(sc6,image=file11)
         label28.place(x=1310,y=150)
#BACK AND UPDATE BUTTON:
         btn15=Button(sc6,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
         btn15.place(x=80,y=800)
         
         def back7():
             sc6.destroy()
            
         btn14=Button(sc6,text='BACK',command=back7,bg='black',fg='red',font=('courier',30))
         btn14.place(x=1600,y=800)
         sc6.mainloop()
    def neptune(a,b):
         sc6=Toplevel()
         colour7=Canvas(sc6,bg='cadetblue')
         colour7.place(width=2000,height=1000)
         sc6.maxsize(width=2000,height=1000)
         sc6.minsize(width=1800,height=1000)
         label27=Label(sc6,text='NEPTUNE',bg='black',fg='white',font=('courier',50))
         label27.place(x=800,y=0)
#INFORMATION ABOUT NEPTUNE:
         info7=Label(sc6,text='''𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍 𝐀𝐁𝐎𝐔𝐓 𝐍𝐄𝐏𝐓𝐔𝐍𝐄:''',bg='cadetblue',fg='brown',
                     font=('courier',50)).place(x=0,y=100)
         write_8=Label(sc6,text='''More than 30 times as far from the Sun as Earth, Neptune is the only planet in our
solar system not visible to the naked eye and the first predicted by mathematics
before its discovery.In 2011 Neptune completed its first 165-year orbit since its
discovery in 1846.It is the fourth-largest planet in the Solar System by diameter,
the third-most- massive planet, and the densest giant planet. It is 17 times the
mass of Earth, and slightly more massive than its near-twin Uranus.\t\t
⇒Orbital period: 165 years
⇒Distance from Sun: 4.495 billion km
⇒Radius: 24,622 km
⇒Discovered: 23 September 1846
⇒Surface area: 7.618 billion km²
⇒Mass: 1.024 × 10^26 kg (17.15 M⊕)''',bg='cadetblue',font=('courier',20),relief='solid').place(x=20,y=180)
      
         file11=PhotoImage(file="neptune.png")
         label28=Label(sc6,image=file11)
         label28.place(x=1400,y=100)
#BACK AND UPDATE BUTTON:
         btn15=Button(sc6,text='UPDATE',command=tab,bg='black',fg='red',font=('courier',30))
         btn15.place(x=80,y=800)
         
         def back7():
             sc6.destroy()
            
         btn14=Button(sc6,text='BACK',command=back7,bg='black',fg='red',font=('courier',30))
         btn14.place(x=1600,y=800)
         sc6.mainloop()    
               
#CREATING THE SUN:
    SUN=turtle.Turtle()
    SUN.shape('circle')
    SUN.shapesize(stretch_len=5,stretch_wid=5)
    SUN.color('yellow')
    SUN.penup()
    SUN.goto(300,0)
    SUN.onclick(sun)
    pen.color('red')
    pen.goto(310,-70)
    style=('courier',10,'bold')
    pen.write('SUN',font=style,align='right')
    

#CREATING MERCURY
    MERCURY=turtle.Turtle()
    MERCURY.shape('circle')
    MERCURY.shapesize(stretch_len=1,stretch_wid=1)
    MERCURY.color('gray50')
    MERCURY.penup()
    MERCURY.goto(300,-70)
    MERCURY.pensize(2)
    MERCURY.pendown()
    MERCURY.onclick(mercury)
    pen.color('cadetblue')
    pen.goto(300,-90)
    style=('courier',10,'bold')
    pen.write('MERCURY',font=style,align='right')
   
#CREATING VENUS
    VENUS=turtle.Turtle()
    VENUS.shape('circle')
    VENUS.shapesize(stretch_len=1.4,stretch_wid=1.4)
    VENUS.color('white')
    VENUS.penup()
    VENUS.goto(300,-100)
    VENUS.pensize(2)
    VENUS.pendown()
    pen.color('SKYBLUE')
    pen.goto(330,-130)
    style=('courier',10,'bold')
    pen.write('VENUS',font=style,align='right')
    VENUS.onclick(venus)

#CREATING EARTH
    EARTH=turtle.Turtle()
    EARTH.shape('circle')
    EARTH.shapesize(stretch_len=1.7,stretch_wid=1.7)
    EARTH.color('blue')
    EARTH.penup()
    EARTH.goto(305,-140)
    EARTH.pensize(2)
    EARTH.pendown()
    pen.color('green')
    pen.goto(330,-160)
    style=('courier',10,'bold')
    pen.write('EARTH',font=style,align='right')
    EARTH.onclick(earth)
    
#CREATING MARS:
    MARS=turtle.Turtle()
    MARS.shape('circle')
    MARS.shapesize(stretch_len=1.3,stretch_wid=1.3)
    MARS.color('red')
    MARS.penup()
    MARS.goto(310,-180)
    MARS.pensize(2)
    MARS.pendown()
    pen.color('white')
    pen.goto(330,-200)
    style=('courier',10,'bold')
    pen.write('MARS',font=style,align='right')
    MARS.onclick(mars)

#CREATING JUPITER:
    JUPITER=turtle.Turtle()
    JUPITER.shape('circle')
    JUPITER.shapesize(stretch_len=3,stretch_wid=3)
    JUPITER.color('beige')
    JUPITER.penup()
    JUPITER.goto(310,-245)
    JUPITER.pensize(2)
    JUPITER.pendown()
    pen.color('pink')
    pen.goto(330,-270)
    style=('courier',10,'bold')
    pen.write('JUPITER',font=style,align='right')
    JUPITER.onclick(jupiter)

#CREATING SATURN:
    SATURN=turtle.Turtle()
    SATURN.shape('circle')
    SATURN.shapesize(stretch_len=2.5,stretch_wid=2.5)
    SATURN.color('brown')
    SATURN.penup()
    SATURN.goto(315,-308)
    SATURN.pensize(2)
    SATURN.pendown()
    pen.color('yellow')
    pen.goto(330,-330)
    style=('courier',10,'bold')
    pen.write('SATURN',font=style,align='right')
    SATURN.onclick(saturn)
#CREATING SATURN_RING:
    SATURN_RING=turtle.Turtle()
    SATURN_RING.hideturtle()
    SATURN_RING.color('white')
    SATURN_RING.penup()
    SATURN_RING.goto(315,-340)
    SATURN_RING.pensize(2)
    SATURN_RING.pendown()
    SATURN_RING.circle(32)
    
#CREATING URANUS:
    URANUS=turtle.Turtle()
    URANUS.shape('circle')
    URANUS.shapesize(stretch_len=1.4,stretch_wid=1.4)
    URANUS.color('violet')
    URANUS.penup()
    URANUS.goto(315,-370)
    URANUS.pensize(2)
    URANUS.pendown()
    pen.color('red')
    pen.goto(330,-400)
    style=('courier',10,'bold')
    pen.write('URANUS',font=style,align='right')
    URANUS.onclick(uranus)
    
#CREATING NEPTUNE:
    NEPTUNE=turtle.Turtle()
    NEPTUNE.shape('circle')
    NEPTUNE.shapesize(stretch_len=1,stretch_wid=1)
    NEPTUNE.color('sky blue')
    NEPTUNE.penup()
    NEPTUNE.goto(320,-410)
    NEPTUNE.pensize(2)
    NEPTUNE.pendown()
    pen.goto(330,-440)
    pen.color('brown')
    style=('courier',10,'bold')
    pen.write('NEPTUNE',font=style,align='right')
    NEPTUNE.onclick(neptune)

#CREATING UPDATE BUTTON:
    UPDATE=turtle.Turtle()
    UPDATE.shape('circle')
    UPDATE.shapesize(stretch_len=5,stretch_wid=5)
    UPDATE.color('sky blue')
    UPDATE.penup()
    UPDATE.goto(-300,-410)
    UPDATE.pensize(2)
    UPDATE.pendown()
    UPDATE.onclick(tab1)
    
   
    
    
     
#SETTING THE ANIMATION SPEED:
    win.tracer(15)

#FUNCTIONS:
    def orbits():
        MERCURY.fd(2.9)
        MERCURY.lt(2.4)
        VENUS.fd(1.6)
        VENUS.lt(0.9)
        EARTH.fd(3.4)
        EARTH.lt(1.4)
        MARS.fd(3.7)
        MARS.lt(1.2)
        JUPITER.fd(3.8)
        JUPITER.lt(0.9)
        SATURN.fd(4.2)
        SATURN.lt(0.8)
        URANUS.fd(5.8)
        URANUS.lt(0.9)
        NEPTUNE.fd(5)
        NEPTUNE.lt(0.7)
           
#MAIN LOOP:
    SATURN_RING.circle(30)
    while True:
        orbits()
        SATURN_RING.clear()
        SATURN_RING.goto(SATURN.xcor()-1,SATURN.ycor()-32)
        SATURN_RING.circle(30)
        win.update()
    win.mainloop()
#CREATING START BUTTON:       
file3=PhotoImage(file='start.png')    
btn1=Button(ss,image=file3,command=tab,bg='black',fg='red',font=('courier',30))
btn1.place(x=800,y=600)

ss.mainloop()
             
