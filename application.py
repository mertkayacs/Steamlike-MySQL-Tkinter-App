import tkinter as tk
from tkinter import *
from tkcalendar import Calendar, DateEntry
import datetime
from PIL import ImageTk, Image

global db
global entered_query
global text_box
global adminmail
global adminpassword
global adminid
global pickedUser
global pickedgame
global bandate
global devmail
global devpassword
global devid
global revenue
global devusername

global title
global ram
global graphiccard
global reqos
global platform
global discount
global series
global price

global pickedgamefordev

global newdevmail
global newdevpassword
global newdevusername
global achievementname
global achievementpoint
global modname

global usermail
global userpassword
global userid
global cardinfo

global newusermail
global newuserpassword
global newuserusername

global pickedgameforusr
global pickedmodforusr

global useridnum

global creditinput

global hoursplayed
global pickedgamediscountedprice

global pickedusrfriend
global pickedfriend

class windowclass():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.user_button = tk.Button(master, text="User Page", command=self.userdbdevWindow)        
        self.dev_button = tk.Button(master, text="Dev Page", command=self.devdbdevWindow)
        self.admin_button = tk.Button(master, text="Admin Page", command=self.admindbdevWindow)
        self.steam_dev_button = tk.Button(master, text="SteamDb Dev Page", command=self.steamdbdevWindow)

        self.img = ImageTk.PhotoImage(Image.open("steama.jpg"))
        self.imagepanel = Label(master, image = self.img)

        self.imagepanel.place(x = 50,
        y = 0,height=100,width = 150)

        self.user_button.place(x = 50,
        y = 105,height=40,width = 150)

        self.dev_button.place(x = 50,
        y = 145,height=40,width = 150)

        self.admin_button.place(x = 50,
        y = 185,height=40,width = 150)

        self.steam_dev_button.place(x = 50,
        y = 225,height=40,width = 150)
   
    def userdbdevWindow(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x200")
        toplevel.title("User Validation Page")
        app = User_Validation_Window(toplevel)   

    def devdbdevWindow(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x200")
        toplevel.title("Developer Validation Page")
        app = Developer_Validation_Window(toplevel)   

    def admindbdevWindow(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x200")
        toplevel.title("Admin Validation Page")
        app = Admin_Validation_Window(toplevel)   

    def steamdbdevWindow(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("800x600")
        toplevel.title("Query Entering Page")
        app = Steamdbdev_Window(toplevel)

    def command(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x350")
        app = Demo2(toplevel)


class User_Validation_Window:
    
    def __init__(self, master):
        global usermail
        global userpassword
        global userid
        global cardinfo

        usermail = tk.StringVar()  
        userpassword = tk.StringVar()  

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.mail_box = tk.Entry(self.frame , textvariable=usermail )
        self.password_box = tk.Entry(self.frame ,show = "*", textvariable=userpassword )
        self.submitbutton = tk.Button(self.frame, text = 'Login', width = 25, command = self.getusrData)
        self.signupbutton = tk.Button(self.frame, text = 'Signup', width = 25, command = self.signupDev)
        self.mail_label = tk.Label(self.frame,text = "Mail Address : ")
        self.pass_label = tk.Label(self.frame,text = "Password : ")

        self.mail_label.place(x = 0,
        y = 55)

        self.pass_label.place(x = 0,
        y = 115)

        self.mail_box.place(x = 100,
        y = 40,
        width=240,
        height=40)
        
        self.password_box.place(x = 100,
        y = 100,
        width=240,
        height=40)
        
        self.signupbutton.place(x = 200,
        y = 150,
        width=80,
        height=40)

        self.submitbutton.place(x = 100,
        y = 150,
        width=80,
        height=40)

        self.frame.pack()
        #root.after(1000, Main)
        #root.mainloop()
    def signupDev(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x260")
        toplevel.title("User Signup Page")
        app = User_Signup_Window(toplevel)   

    def getusrData(self):
        global db
        global usermail
        global userpassword
        global devid
        global userid
        global usercardinfo

        logintodb("","")
        if(usermail == ""):
            return
        devid = -1
        mail_str = usermail.get()
        password_str = userpassword.get()
        if(mail_str == ""):
            return
        print("here")
        query = "Select username,cardinfo from gamer2 where (email = \"" + mail_str + "\") and " + "(password = \""+ password_str + "\")"
        print(query)

        cur = db.cursor()
        try: 
            
            cur.execute(query) 
            #db.commit()
            myresult = cur.fetchall()
            userid = myresult[0][0]
            usercardinfo = myresult[0][1]


        except: 
            db.rollback() 
            print("Error occured") 
            return

        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x170")
        toplevel.title("User Page")
        app = User_Window(toplevel)   


class User_Window:
    def __init__(self, master):
        global userbalance
        global usermail
        global userpassword
        global userid
        global usercardinfo
        game_name = tk.StringVar()  
        entered_query = tk.StringVar()  
        entered_query = tk.StringVar()  
        self.getuserid()
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.getbalance()   
        print("here")
        usernamestr = str(userid)
        #font= fonte qualquer, bold
        self.usernametxt = tk.Label(self.frame,text = "Your Username :",font=("Arial Bold", 10))
        self.usernamefordev = tk.Label(self.frame,text = usernamestr)
        self.addgamebutton = tk.Button(self.frame, text = 'Store', width = 25, command = self.storePage)
        self.mygamesbutton = tk.Button(self.frame, text = 'My Games', width = 25, command = self.myGamesPage)
        self.friendsbutton = tk.Button(self.frame, text = 'Friends', width = 25, command = self.myFriendsPage)
        self.addcreditbutton = tk.Button(self.frame, text = 'Add Credit', width = 25, command = self.addcredit)

        self.usernametxt.place(x = 7,
        y = 25,height=30,width = 150)


        self.usernamefordev.place(x = 137,
        y = 25,height=30,width = 150)

        self.addgamebutton.place(x = 25,
        y = 80,height=60,width = 80)

        self.mygamesbutton.place(x = 115,
        y = 80,height=60,width = 100)

        self.addcreditbutton.place(x = 265,
        y = 25,height=30,width = 80)

        self.friendsbutton.place(x = 230,
        y = 80,height=60,width = 100)


        self.frame.pack()


    def getuserid(self):

        global useridnum
        global usermail
        global userbalance
        global db
        logintodb("","")

        queryforuseridnum = "Select id from gamer1 where (email = \""+usermail.get()+"\");"
        useridnum = 0
        print(queryforuseridnum)
        cur = db.cursor()

        try: 
            cur.execute(queryforuseridnum) 
            myresult = cur.fetchall()
            index = 0
            useridnum = int(myresult[0][0])
            #db.commit()         

        except: 
            db.rollback() 
            print("Error occured") 

    def addcredit(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("200x170")
        toplevel.title("Credit Adding Page")
        app = Credit_Window(toplevel)   

    def getbalance(self):
        print("here")
        global usermail
        global userpassword
        global userid
        global usercardinfo
        global userbalance
        global db
        logintodb("","")
        cur = db.cursor()
        query = "SELECT balance from gamer3 where cardinfo = \""+usercardinfo+"\""
        print(query)
        try: 
            cur.execute(query) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                userbalance = float(myresult[0][0])
                print(userbalance)
            return

        except: 
            db.rollback() 



    def myFriendsPage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("470x500")
        toplevel.title("Friends Page")
        app = Friends_Window(toplevel)           

    def storePage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("900x700")
        toplevel.title("Store Page")
        app = Store_Window(toplevel)   

    def addgamePage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("400x380")
        toplevel.title("Game Adding Page")
        app = Add_Game_Window(toplevel)   

    def myGamesPage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("600x550")
        toplevel.title("My Games Page")
        app = User_My_Games_Window(toplevel)   

class Friends_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    
        self.alluserslabel = tk.Label(self.frame,text = "All Users (No Friends)")
        self.allusers_box = tk.Listbox(self.frame)
        self.allusers_box.bind('<<ListboxSelect>>',self.CurUsrSelect)
        self.addUsersListbox()
        self.addfriendbutton = tk.Button(self.frame, text = 'Add Selected User as Friend', width = 25, command = self.addFriend)
        self.addFamilysharebutton = tk.Button(self.frame, text = 'Add Selected Friend to FamilyShare', width = 25, command = self.addFamilyShare)
        self.friendslabel = tk.Label(self.frame,text = "My Friends")
        self.friendslist_box = tk.Listbox(self.frame)
        self.friendslist_box.bind('<<ListboxSelect>>',self.CurFrdSelect)
        self.addFriendsListbox()

        self.addfriendbutton.place(x = 5,
        y =460,height=30,width = 200)

        self.addFamilysharebutton.place(x = 225,
        y =460,height=30,width = 200)

        self.alluserslabel.place(x = 0,
        y =0,height=30,width = 200)

        self.friendslabel.place(x = 220,
        y =0,height=30,width = 200)

        self.allusers_box.place(x = 0,
        y =40,height=400,width = 200)

        self.friendslist_box.place(x = 220,
        y =40,height=400,width = 200)

        self.frame.pack()

    def addFriend(self):
        print("")

    def addFamilyShare(self):
        print("")

    def addUsersListbox(self):
        global userid
        global useridnum
        global db
        global pickedusrfriend
        global pickedfriend        
        #query = "select username from gamer2 where username != \"" + userid+"\""
        #cur.execute(queryfor1) 
        #myresult = cur.fetchall()
        #index = 0


    def addFriendsListbox(self):
        global userid
        global useridnum
        global db
        global pickedusrfriend
        global pickedfriend
        logintodb("","")

        self.allusers_box.delete(0,'end')
        cur = db.cursor()

        #query = "select username from gamer2 where username != \"" + userid+"\""
        queryfor1 = "select gamerid2 from isfriendswith where gamerid1 = "+str(useridnum)

        print(queryfor1)
        #print(queryfor2)

        try: 
            #NOT FRIEND CHECK
            cur.execute(queryfor1) 
            myresult = cur.fetchall()
            index = 0
            
            friends1 = []
            for item in myresult:
                print(item[0])
                userstr = str(item[0])
                queryfor2 = "select email from gamer1 where id = "+ userstr
                cur.execute(queryfor2) 
                myresult2 = cur.fetchall()
                for item2 in myresult2:
                    print(item2[0])
                    queryfor3 = "select username from gamer2 where email = \""+ str(item2[0]) + "\""
                    cur.execute(queryfor3) 
                    myresult3 = cur.fetchall()  
                    print(myresult3[0][0])           
                    friends1.append(str(myresult3[0][0]))

            index = 0
            for element in friends1:
                self.friendslist_box.insert(index,str(element))     
                index = index+1           
            #db.commit()         


        except: 
            db.rollback() 
            print("Error occured")        

    def CurUsrSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedusrfriend
        pickedusrfriend = picked
        print("-"+picked+"-")

    def CurFrdSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedfriend
        pickedfriend = picked
        print("-"+picked+"-")


class User_My_Games_Window:
    def __init__(self, master):
        global hoursplayed
        global rating
        hoursplayed = tk.StringVar()
        rating = tk.StringVar()
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    

        self.gameslabel = tk.Label(self.frame,text = "Games Bought By Me")
        self.gamesforusr = tk.Listbox(self.frame)
        self.gamesforusr.bind('<<ListboxSelect>>',self.CurSelect)
        self.addGamestoGamesListbox()

        self.modlabel = tk.Label(self.frame,text = "Mod For Selected Game")
        self.modforusr = tk.Listbox(self.frame)
        self.modforusr.bind('<<ListboxSelect>>',self.CurModSelect)
        self.addGamestoModsListbox()


        self.installmod = tk.Button(self.frame, text = 'Install Selected Mod', width = 25, command = self.installmodforuser)
        self.uninstallmod = tk.Button(self.frame, text = 'Uninstall Selected Mod', width = 25, command = self.uninstallmodforuser)
        self.showmods = tk.Button(self.frame, text = 'Show All Installed Mods', width = 25, command = self.showmodsforuser)
        self.playgamebutton = tk.Button(self.frame, text = 'Play The Selected Game', width = 25, command = self.playgame)
        self.giveratingbutton = tk.Button(self.frame, text = 'Rating for Selected Game', width = 25, command = self.giverating)
        self.playedhoursbox = tk.Entry(self.frame , textvariable=hoursplayed )

        self.playedhourslabel = tk.Label(self.frame,text = "Hours To Play")

        self.ratingbox = tk.Entry(self.frame , textvariable=rating )

        self.ratinglabel = tk.Label(self.frame,text = "Rating for Selected Game")


        self.installmod.place(x = 350,
        y =90,height=40,width = 200)

        self.uninstallmod.place(x = 350,
        y =130,height=40,width = 200)

        self.showmods.place(x = 350,
        y =175,height=40,width = 200)


        self.gameslabel.place(x = 30,
        y =0,height=40,width = 200)

        self.gamesforusr.place(x = 0,
        y =30,height=500,width = 300)

        self.modlabel.place(x = 380,
        y =0,height=40,width = 200)

        self.modforusr.place(x = 330,
        y =30,height=40,width = 300)

        self.playedhourslabel.place(x = 350,
        y =230,height=40,width = 200)

        self.playedhoursbox.place(x = 350,
        y =270,height=40,width = 200)

        self.playgamebutton.place(x = 350,
        y =315,height=40,width = 200)

        self.ratinglabel.place(x = 350,
        y =385,height=40,width = 200)

        self.ratingbox.place(x = 350,
        y =420,height=40,width = 200)

        self.giveratingbutton.place(x = 350,
        y =460,height=40,width = 200)


        self.frame.pack()


    def showmodsforuser(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("400x200")
        toplevel.title("Mods for User Page")
        app = User_Mods_Window(toplevel)   

    def CurSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedgameforusr
        pickedgameforusr = picked
        self.addGamestoModsListbox()
        print(picked)

    def CurModSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedmodforusr
        pickedmodforusr = picked
        print(picked)

    def installmodforuser(self):

        global useridnum
        global usermail
        global userpassword
        global userid
        global usercardinfo
        global userbalance
        global db
        global pickedgameforusr
        global pickedmodforusr
        logintodb("","")
        #self.modforusr.delete(0,'end')
        cur = db.cursor()

        try: 

            query = "INSERT INTO installs values ("+str(useridnum)+",\""+ str(pickedgameforusr)+"\"," +"\""+ str(pickedmodforusr) +"\");"
            print(query)
            cur.execute(query) 
            db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 

    def uninstallmodforuser(self):

        global usermail
        global userpassword
        global userid
        global useridnum
        global usercardinfo
        global userbalance
        global db
        global pickedgameforusr
        global pickedmodforusr
        logintodb("","")
        #self.modforusr.delete(0,'end')
        cur = db.cursor()
        query = "delete FROM installs where gamertitle = \"" + pickedgameforusr + "\"" + " and gamerid = "+str(useridnum)
        print(query)

        try: 

            cur.execute(query) 
            db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 


    def giverating(self):
        
        global rating        
        global hoursplayed
        global pickedgameforusr
        global useridnum
        logintodb("","")
        #self.modforusr.delete(0,'end')
        cur = db.cursor()

        #HAS AND GAME1
        #IF GAME1 RATING = 0 JUST ADD IF ELSE AVG
        query = "UPDATE HAS SET RATING = "+str(rating.get()) + " where gamerid = " + str(useridnum) +" and game_title = \""+str(pickedgameforusr) +"\""
        querytogetcurrentrating = "select rating from game1 where title = \"" + str(pickedgameforusr) +"\""


        #try: 

        print(query)
        cur.execute(query) 
                
        print(querytogetcurrentrating) 
        cur.execute(querytogetcurrentrating)            
        myresult = cur.fetchall()
        currentrating =  int(myresult[0][0])
        ratingnow = 0
        if(currentrating == 0):
            ratingnow = int(rating.get()) + currentrating 
        else:
            ratingnow = int(rating.get()) + currentrating 
            ratingnow = ratingnow/2  
        queryforgame1 = "UPDATE game1 SET RATING = "+str(ratingnow) + " where title = \""+str(pickedgameforusr) +"\""    
        cur.execute(queryforgame1)           
        print(queryforgame1) 
        db.commit()     
        return    
        #except: 
        #    db.rollback() 
        #    print("Error occured") 



    def playgame(self):
        
        global hoursplayed
        global pickedgameforusr
        global useridnum
        logintodb("","")
        #self.modforusr.delete(0,'end')
        cur = db.cursor()

        query = "select playtime from has where gamerid = " + str(useridnum) + " and " + " game_title = " + "\"" + str(pickedgameforusr) + "\""

        try: 

            print(query)
            cur.execute(query) 
            myresult = cur.fetchall()
            playtimebefore =  int(myresult[0][0])  
            playtime = playtimebefore + int(hoursplayed.get())
            updatequery = "update has set playtime = " + str(playtime) + " where gamerid = " + str(useridnum) + " and " + " game_title = " + "\"" + str(pickedgameforusr) + "\""
            cur.execute(updatequery)   
            print(updatequery)      
            db.commit()            
            return

            #db.commit()         
        except: 
            db.rollback() 
            print("Error occured") 



    def addGamestoModsListbox(self):
        global usermail
        global userpassword
        global userid
        global usercardinfo
        global userbalance
        global db
        global pickedgameforusr
        global pickedmodforusr
        logintodb("","")
        self.modforusr.delete(0,'end')
        cur = db.cursor()

        try: 

            query = "Select modname from mod_name where gametitle = \""+ str(pickedgameforusr)+"\""
            print(query)
            cur.execute(query) 
            myresult = cur.fetchall()
            index = 0
            for item in myresult:
                modnamestr = str(item)
                modnamestr = modnamestr[2:-3]
                self.modforusr.insert(index,modnamestr)
                index = index+1
            #db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 



    def addGamestoGamesListbox(self):
        global usermail
        global userpassword
        global userid
        global useridnum
        global usercardinfo
        global userbalance
        global db
        logintodb("","")


        queryforuseridnum = "Select id from gamer1 where (email = \""+usermail.get()+"\");"
        useridnum = 0
        print(queryforuseridnum)
        cur = db.cursor()

        try: 
            cur.execute(queryforuseridnum) 
            myresult = cur.fetchall()
            index = 0
            useridnum = int(myresult[0][0])

            query = "Select game_title from has where gamerid = "+ str(useridnum)
            print(query)
            cur.execute(query) 
            myresult = cur.fetchall()
            for item in myresult:
                gamenamestr = str(item)
                gamenamestr = gamenamestr[2:-3]
                self.gamesforusr.insert(index,gamenamestr)
                index = index+1
            #db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 


class Credit_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    
        global creditinput
        creditinput = tk.StringVar()

        self.credit_label = tk.Label(self.frame,text = "Desired Amount to add to Balance")
        self.credit_box = tk.Entry(self.frame , textvariable=creditinput )
        self.addbutton  = tk.Button(self.frame, text = 'Add to Account', width = 25, command = self.addcredit)
        
        
        self.credit_label.place(x = -25,
        y = 0,height=30,width = 250)

        self.credit_box.place(x = 20,
        y = 50,height=30,width = 150)

        self.addbutton.place(x = 20,
        y = 100,height=30,width = 150)


        self.frame.pack()
    
    def addcredit(self):
        global creditinput
        global usermail
        global userpassword
        global useridnum
        global usercardinfo
        global userbalance
        global db
        global pickedgameforusr
        global pickedmodforusr
        logintodb("","")
        cur = db.cursor()

        current_credit = 0
        creditstr = str(creditinput.get())
        firstqueryforbalance = "select balance from gamer3 where cardinfo = \"" + usercardinfo +"\""

        try: 

            print(firstqueryforbalance)
            cur.execute(firstqueryforbalance) 

            myresult = cur.fetchall()
            current_balance = myresult[0][0]
            current_credit = float(current_balance) + float(creditstr)
            query = "UPDATE gamer3 SET balance = " + str(current_credit) + " where cardinfo = \"" + usercardinfo +"\""
            print(query)
            cur.execute(query) 
            db.commit()      
            self.master.withdraw()   
            return

        except: 
            db.rollback() 
            print("Error occured")         


class User_Mods_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    
        self.modsforuser = tk.Listbox(self.frame)
        self.addGamestoAllModsListbox()
        self.modsforuser.place(x = 0,
        y =0,height=200,width = 400)

        self.frame.pack()

    def addGamestoAllModsListbox(self):
        global usermail
        global userpassword
        global useridnum
        global usercardinfo
        global userbalance
        global db
        global pickedgameforusr
        global pickedmodforusr
        logintodb("","")
        self.modsforuser.delete(0,'end')
        cur = db.cursor()

        try: 

            query = "Select gamertitle,modname from installs where gamerid = " + str(useridnum)
            print(query)
            cur.execute(query) 
            myresult = cur.fetchall()
            index = 0
            for item in myresult:
                modnamestr = "      "+str(item[0]) + " : " + str(item[1])
                modnamestr = modnamestr[2:-3]
                self.modsforuser.insert(index,modnamestr)
                index = index+1
            #db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 


class Store_Window:
    def __init__(self, master):
        self.getbalance()
        global userbalance
        revenuestr = str(userbalance) + " $"
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    
        
        self.revenuetxt= tk.Label(self.frame,text = "Credit Before Buy :",font=("Arial Bold", 10))
        self.revenueforusr = tk.Label(self.frame,text = revenuestr)
        self.buybutton = tk.Button(self.frame, text = 'Buy the Selected Game', width = 25, command = self.buygame)

        self.gameslabel = tk.Label(self.frame,text = "Not Bought Games")
        self.gameslist = tk.Listbox(self.frame)
        self.gameslist.bind('<<ListboxSelect>>',self.CurSelect)

        #self.priceslabel = tk.Label(self.frame,text = "Not Bought Games")
        #self.priceslist = tk.Listbox(self.frame)

        self.addgamestore()

        self.gameslist.place(x = 0,
        y = 0,height=700,width = 600)

        #self.priceslist.place(x = 200,
        #y = 0,height=500,width = 100)
        self.buybutton.place(x = 625,
        y = 65,height=40,width = 200)

        self.revenuetxt.place(x = 525,
        y = 10,height=30,width = 350)

        self.revenueforusr.place(x = 755,
        y = 5,height=40,width = 100)

        self.frame.pack()



    def buygame(self):
        self.getbalance()
        global usermail
        global userpassword
        global userid
        global usercardinfo
        global userbalance
        global useridnum
        global db
        global pickedgameforusr
        global pickedgamediscountedprice


        if(float(userbalance) < float(pickedgamediscountedprice)):
            print("NOT ENOUGH MONEY")
            return

        leftmoney = float(userbalance) - float(pickedgamediscountedprice)
        querytoadjustbalance =  "Update gamer3 SET balance = "+str(leftmoney) +" where cardinfo = "+"\"" + usercardinfo + "\""

        logintodb("","")

        cur = db.cursor()
        query = "Insert into has values("
        query = query + str(useridnum) + ","
        query = query +"\""+ str(pickedgameforusr) + "\","
        query = query + "0,0);"



        print(query)
        print(querytoadjustbalance)
        try: 
            cur.execute(query) 
            cur.execute(querytoadjustbalance) 
            db.commit()
            return

        except: 
            db.rollback() 



    def getbalance(self):
        print("here")
        global usermail
        global userpassword
        global userid
        global usercardinfo
        global userbalance
        global db
        logintodb("","")
        cur = db.cursor()
        query = "SELECT balance from gamer3 where cardinfo = \""+usercardinfo+"\""
        print(query)
        try: 
            cur.execute(query) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                userbalance = float(myresult[0][0])
                #print(userbalance)
            return

        except: 
            db.rollback() 

    def CurSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedgameforusr
        global pickedgamediscountedprice
        
        firstindex = picked.find("|")
        firstindex = firstindex-2
        pickedgameforusr = picked[0:firstindex]

        lastindex = picked.rindex(":")
        lastindex = lastindex + 2
        pickedgamediscountedprice = picked[lastindex:]

        print("-"+pickedgamediscountedprice+"-")        
        print("-"+pickedgameforusr+"-")

    def addgamestore(self):
        global useridnum
        global db

        logintodb("","")
        queryforhas = "Select game_title from has where gamerid = "+str(useridnum)
        queryforall = "Select title,price from game1"
        cur = db.cursor()
        savequery = queryforhas

        #try: 
        cur.execute(savequery) 
        myresult = cur.fetchall()
        index = 0
        bought_games = []
        for item in myresult:
            bought_games.append(item[0])
        #print(bought_games)


        cur.execute(queryforall) 
        myresult = cur.fetchall()
        all_games = []
        for item in myresult:
            all_games.append(item[0])
        #print(all_games)

        list_difference = []
        for item in all_games:
            if item not in bought_games:
                list_difference.append(item)

        list_difference_for_price = []
        list_difference_for_discount = []
        list_discountedprices = []
        for item in list_difference:
            queryforprice = "select price,discount from game1 where title = \"" + str(item) + "\""
            print(queryforprice)
            cur.execute(queryforprice) 
            myresult = cur.fetchall()
            list_difference_for_price.append(str(myresult[0][0]))  
            list_difference_for_discount.append(str(myresult[0][1])) 
            price = float(myresult[0][0])
            print(myresult[0][1])
            discount =float(myresult[0][1])
            discountedprice = price - ((price * discount)/100)
            list_discountedprices.append(str(discountedprice))
        #print(list_difference_for_price)   

        #priceslist
        #gameslist
        index = 0
        
        for item in list_difference:
            stringtoadd = item + "  |  price : " + list_difference_for_price[index] +" | discount : "+ list_difference_for_discount[index]  + " | discounted price : " +list_discountedprices[index]
            print(stringtoadd)
            self.gameslist.insert(index,stringtoadd)
            index = index+1

class User_Signup_Window:

    def __init__(self, master):
        global db
        global usermail
        global userpassword
        global devid
        global userid
        global usercardinfo
        global newusermail
        global newuserpassword
        global newuserusername

        newusermail = tk.StringVar()  
        newuserpassword = tk.StringVar()  
        newuserusername = tk.StringVar()
        usercardinfo = tk.StringVar()



        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.mail_box = tk.Entry(self.frame , textvariable=newusermail )
        self.password_box = tk.Entry(self.frame ,show = "*", textvariable=newuserpassword )
        self.signupbutton = tk.Button(self.frame, text = 'Signup', width = 25, command = self.signupnewuser)
        self.mail_label = tk.Label(self.frame,text = "Mail Address : ")
        self.pass_label = tk.Label(self.frame,text = "Password : ")
        self.username_box = tk.Entry(self.frame , textvariable=newuserusername )
        self.username_label = tk.Label(self.frame,text = "Username : ")
        self.cardinfo_box = tk.Entry(self.frame , textvariable=usercardinfo )
        self.cardinfo_label = tk.Label(self.frame,text = "Card Digits : ")


        self.username_label.place(x = 0,
        y = 0)

        self.username_box.place(x = 100,
        y = 0,
        width=240,
        height=40)


        self.mail_label.place(x = 0,
        y = 55)

        self.pass_label.place(x = 0,
        y = 110)

        self.mail_box.place(x = 100,
        y = 50,
        width=240,
        height=40)
        
        self.password_box.place(x = 100,
        y = 100,
        width=240,
        height=40)
        
        self.cardinfo_label.place(x = 0,
        y = 165)

        self.cardinfo_box.place(x = 100,
        y = 160,
        width=240,
        height=40)


        self.signupbutton.place(x = 100,
        y = 210,
        width=80,
        height=40)



        self.frame.pack()


    def signupnewuser(self):
        global newusermail
        global newuserpassword
        global newuserusername
        global usercardinfo
        global db
        logintodb("","")
        cur = db.cursor()
        if(newuserpassword.get() == "" or newusermail.get() == "" or newuserusername.get() == "" or usercardinfo.get() == ""):
            print("EMPTY VALUE!")
            return
        queryfordevid = "select count(*) from gamer1"
        queryforinsert1 = "INSERT INTO gamer1 VALUES("
        queryforinsert2 = "INSERT INTO gamer2 VALUES("
        queryforinsert3 = "INSERT INTO gamer3 VALUES("
        #print(query)
        try: 
            cur.execute(queryfordevid) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                newuserid = int(myresult[0][0]) + 91
                queryforinsert1 = queryforinsert1 + str(newuserid) + ","
                queryforinsert1 = queryforinsert1 +"\""+ str(newusermail.get()) + "\");"
                
                queryforinsert2 = queryforinsert2 + "\"" + newusermail.get() +"\","
                queryforinsert2 = queryforinsert2 + "\"" + newuserusername.get() +"\","
                queryforinsert2 = queryforinsert2 + "\"" + newuserpassword.get() +"\","
                queryforinsert2 = queryforinsert2 + "\"" + usercardinfo.get() +"\");"

                queryforinsert3 = queryforinsert3 + "\"" + usercardinfo.get() +"\","
                queryforinsert3 = queryforinsert3 + "0);"


                print(queryforinsert1)
                print(queryforinsert2)
                print(queryforinsert3)

                cur.execute(queryforinsert1) 
                cur.execute(queryforinsert2) 
                cur.execute(queryforinsert3) 
                db.commit()
                #devusername = myresult[0][1]
                self.master.withdraw()
            return

        except: 
            db.rollback() 

    

class Developer_Validation_Window:
    
    def __init__(self, master):
        global devmail
        global devpassword
        global devid
        devid = -1

        devmail = tk.StringVar()  
        devpassword = tk.StringVar()  

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.mail_box = tk.Entry(self.frame , textvariable=devmail )
        self.password_box = tk.Entry(self.frame ,show = "*", textvariable=devpassword )
        self.submitbutton = tk.Button(self.frame, text = 'Login', width = 25, command = self.getdevData)
        self.signupbutton = tk.Button(self.frame, text = 'Signup', width = 25, command = self.signupDev)
        self.mail_label = tk.Label(self.frame,text = "Mail Address : ")
        self.pass_label = tk.Label(self.frame,text = "Password : ")

        self.mail_label.place(x = 0,
        y = 55)

        self.pass_label.place(x = 0,
        y = 115)

        self.mail_box.place(x = 100,
        y = 40,
        width=240,
        height=40)
        
        self.password_box.place(x = 100,
        y = 100,
        width=240,
        height=40)
        
        self.signupbutton.place(x = 200,
        y = 150,
        width=80,
        height=40)

        self.submitbutton.place(x = 100,
        y = 150,
        width=80,
        height=40)

        self.frame.pack()
        #root.after(1000, Main)
        #root.mainloop()
    def signupDev(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("350x220")
        toplevel.title("Dev Signup Page")
        app = Dev_Signup_Window(toplevel)   

    def getdevData(self):
        global db
        global devmail
        global devpassword
        global devid
        logintodb("","")
        if(devmail == ""):
            return
        devid = -1
        mail_str = devmail.get()
        password_str = devpassword.get()
        if(mail_str == ""):
            return
        query = "Select * from developer2 where (email = \"" + mail_str + "\") and " + "(password = \""+ password_str + "\")"
        print(query)
        cur = db.cursor()
        savequery = query
        devidtemp = -1

        try: 
            cur.execute(savequery) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                query2 = "Select * from developer1 where (email = \"" + mail_str + "\")"
                cur.execute(query2) 
                myresult2 = cur.fetchall()
                devidtemp = myresult2[0]
            devid = devidtemp
            db.commit()

            #change to -1
            if(devid != -1):
                self.master.withdraw()
                toplevel = tk.Toplevel(self.master)
                toplevel.geometry("350x170")
                toplevel.title("Developer Page")
                app = Dev_Window(toplevel)   

        except: 
            db.rollback() 
            print("Error occured") 



class Dev_Signup_Window:
    def __init__(self, master):
        global newdevmail
        global newdevpassword
        global newdevusername
        devid = -1

        newdevmail = tk.StringVar()  
        newdevpassword = tk.StringVar()  
        newdevusername = tk.StringVar()

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.mail_box = tk.Entry(self.frame , textvariable=newdevmail )
        self.password_box = tk.Entry(self.frame ,show = "*", textvariable=newdevpassword )
        self.signupbutton = tk.Button(self.frame, text = 'Signup', width = 25, command = self.signupnewDev)
        self.mail_label = tk.Label(self.frame,text = "Mail Address : ")
        self.pass_label = tk.Label(self.frame,text = "Password : ")
        self.username_box = tk.Entry(self.frame , textvariable=newdevusername )
        self.username_label = tk.Label(self.frame,text = "Username : ")


        self.username_label.place(x = 0,
        y = 0)

        self.username_box.place(x = 100,
        y = 0,
        width=240,
        height=40)


        self.mail_label.place(x = 0,
        y = 55)

        self.pass_label.place(x = 0,
        y = 115)

        self.mail_box.place(x = 100,
        y = 50,
        width=240,
        height=40)
        
        self.password_box.place(x = 100,
        y = 100,
        width=240,
        height=40)
        
        self.signupbutton.place(x = 100,
        y = 150,
        width=80,
        height=40)

        self.frame.pack()


    def signupnewDev(self):
        global db
        global newdevmail
        global newdevpassword
        global newdevusername
        logintodb("","")
        cur = db.cursor()
        if(newdevpassword.get() == "" or newdevmail.get() == "" or newdevusername.get() == ""):
            print("EMPTY VALUE!")
            return
        queryfordevid = "select count(*) from developer1"
        queryforinsert1 = "INSERT INTO developer1 VALUES("
        queryforinsert2 = "INSERT INTO developer2 VALUES("
        #print(query)
        try: 
            cur.execute(queryfordevid) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                newuserid = int(myresult[0][0]) + 91
                queryforinsert1 = queryforinsert1 + str(newuserid) + ","
                queryforinsert1 = queryforinsert1 +"\""+ str(newdevmail.get()) + "\");"
                
                queryforinsert2 = queryforinsert2 + "\"" + newdevmail.get() +"\","
                queryforinsert2 = queryforinsert2 + "\"" + newdevusername.get() +"\","
                queryforinsert2 = queryforinsert2 + "\"" + newdevpassword.get() +"\","
                queryforinsert2 = queryforinsert2 + "0);"

                cur.execute(queryforinsert1) 
                cur.execute(queryforinsert2) 
                db.commit()
                #devusername = myresult[0][1]
                print(queryforinsert1)
                print(queryforinsert2)
                self.master.withdraw()
            return

        except: 
            db.rollback() 


class Dev_Window:
    def __init__(self, master):
        global revenue
        global devusername

        game_name = tk.StringVar()  
        entered_query = tk.StringVar()  
        entered_query = tk.StringVar()  
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.getrev()   
        revenuestr = str(revenue) + " $"
        usernamestr = str(devusername)
        #font= fonte qualquer, bold
        self.revenuetxt= tk.Label(self.frame,text = "Your Revenue  :",font=("Arial Bold", 10))
        self.usernametxt = tk.Label(self.frame,text = "Your Username :",font=("Arial Bold", 10))
        self.revenuefordev = tk.Label(self.frame,text = revenuestr)
        self.usernamefordev = tk.Label(self.frame,text = usernamestr)
        self.addgamebutton = tk.Button(self.frame, text = 'Add Game', width = 25, command = self.addgamePage)
        self.mygamesbutton = tk.Button(self.frame, text = 'My Games', width = 25, command = self.myGamesPage)


        self.usernametxt.place(x = 7,
        y = 0,height=30,width = 150)

        self.revenuetxt.place(x = 5,
        y = 30,height=30,width = 150)

        self.usernamefordev.place(x = 137,
        y = 0,height=30,width = 150)

        self.revenuefordev.place(x = 160,
        y = 25,height=40,width = 100)

        self.addgamebutton.place(x = 25,
        y = 80,height=60,width = 80)

        self.mygamesbutton.place(x = 130,
        y = 80,height=60,width = 100)

        self.gameentry = tk.Entry(self.frame) 

        self.frame.pack()



    def getrev(self):
        global devmail
        global devusername
        global revenue
        global db
        logintodb("","")
        cur = db.cursor()
        query = "SELECT revenue,username from developer2 where email = \""+str(devmail.get())+"\""
        print(query)
        try: 
            cur.execute(query) 
            #db.commit()
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                revenue = int(myresult[0][0])
                devusername = myresult[0][1]
                print(revenue)
            return

        except: 
            db.rollback() 



    def addgamePage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("400x380")
        toplevel.title("Game Adding Page")
        app = Add_Game_Window(toplevel)   

    def myGamesPage(self):
        toplevel = tk.Toplevel(self.master)
        toplevel.geometry("600x450")
        toplevel.title("My Games Page")
        app = My_Games_Window(toplevel)   

class My_Games_Window:
    def __init__(self, master):
        global achievementname
        global achievementpoint
        global modname
        achievementname = tk.StringVar()  
        achievementpoint = tk.IntVar()  
        modname = tk.StringVar()  

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    

        self.gameslabel = tk.Label(self.frame,text = "Games Developed by Me")
        self.gamesfordev = tk.Listbox(self.frame)
        self.gamesfordev.bind('<<ListboxSelect>>',self.CurSelect)
        self.addGamestoGamesListbox()

        self.achname_box = tk.Entry(self.frame , textvariable=achievementname )
        self.achpoint_box = tk.Entry(self.frame , textvariable=achievementpoint )
        self.mod_box = tk.Entry(self.frame , textvariable=modname )

        self.addAchievementButton = tk.Button(self.frame, text = 'Add Achievement For Selected Game', width = 25, command = self.addAchievement)
        self.addModButton = tk.Button(self.frame, text = 'Add Mod For Selected Game', width = 25, command = self.addMod)
        self.AchievementLabelDetails = tk.Label(self.frame,text="Achievement Name                                     Achievement Point")
        self.ModLabelDetails = tk.Label(self.frame,text="Mod Name")


        self.mod_box.place(x = 220,
        y = 300,height=35,width = 200)

        self.achname_box.place(x = 220,
        y = 90,height=35,width = 200)

        self.achpoint_box.place(x = 490,
        y = 90,height=35,width = 100)


        self.ModLabelDetails.place(x = 220,
        y = 255,height=35,width = 200)

        self.AchievementLabelDetails.place(x = 230,
        y = 45,height=35,width = 400)

        self.addAchievementButton.place(x = 220,
        y = 150,height=35,width = 200)

        self.addModButton.place(x = 220,
        y = 360,height=35,width = 200)

        self.gameslabel.place(x = 30,
        y = 0,height=35,width = 150)

        self.gamesfordev.place(x = 0,
        y = 40,height=400,width = 200)

        self.frame.pack()

    def addAchievement(self):
        global pickedgamefordev
        global achievementname
        global achievementpoint

        if(achievementname.get() == ""):
            return
        

        logintodb("","")
        queryforachievement1 = "Insert into achievement1 values("
        queryforachievement1 = queryforachievement1 + "\"" + pickedgamefordev + "\","
        queryforachievement1 = queryforachievement1 + "\"" + achievementname.get() + "\");"
        
        queryforachievement2 = "Insert into achievement2 values("
        queryforachievement2 = queryforachievement2 + "\"" +achievementname.get() + "\","
        queryforachievement2 = queryforachievement2 + str(achievementpoint.get())+");"

        print(queryforachievement1)
        print(queryforachievement2)
        cur = db.cursor()

        try: 
            cur.execute(queryforachievement1) 
            cur.execute(queryforachievement2) 
            #myresult = cur.fetchall()
            db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 



    def addMod(self):
        global pickedgamefordev
        global modname
        global devid
        if(modname.get() == ""):
            return

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        timestr = "" + str(year) + "-"+str(month)+ "-" + str(day) + " "+str(hour)+":"+str(minute)+":"+str(second)

        logintodb("","")
        queryformod1 = "Insert into mod_name values("
        queryformod1 = queryformod1 + "\"" + pickedgamefordev + "\","
        queryformod1 = queryformod1 + "\"" + modname.get() + "\","
        queryformod1 = queryformod1 + str(devid[0]) + ","
        queryformod1 = queryformod1 + "\"" + timestr + "\");"

        print(queryformod1)
        cur = db.cursor()
        try: 
            cur.execute(queryformod1) 
            #myresult = cur.fetchall()
            db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 


    def addGamestoGamesListbox(self):
        global devid
        global db
        idfordev = devid[0]

        logintodb("","")
        query = "Select title from game1 where developer_id ="+str(idfordev)
        print(query)
        cur = db.cursor()
        savequery = query

        try: 
            cur.execute(savequery) 
            myresult = cur.fetchall()
            index = 0
            for item in myresult:
                gamenamestr = str(item)
                gamenamestr = gamenamestr[2:-3]
                self.gamesfordev.insert(index,gamenamestr)
                index = index+1
            #db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 


    def CurSelect(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedgamefordev
        pickedgamefordev = picked
        print(picked)

class Add_Game_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    

        global title
        global ram
        global graphiccard
        global reqos
        global platform
        global discount
        global series
        global price



        title = tk.StringVar()  
        ram = tk.StringVar()  
        graphiccard = tk.StringVar()  
        reqos = tk.StringVar()  
        platform = tk.StringVar()  
        discount = tk.IntVar()  
        series = tk.StringVar()  
        price = tk.IntVar()  

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        
        self.title_box = tk.Entry(self.frame , textvariable=title )
        self.titlelabel = tk.Label(self.frame,text = "Game Title :")

        self.ram_box = tk.Entry(self.frame , textvariable=ram )
        self.ramlabel = tk.Label(self.frame,text = "Required Ram:")

        self.graphic_box = tk.Entry(self.frame , textvariable=graphiccard )
        self.graphiclabel = tk.Label(self.frame,text = "Required Graphics Card :")

        self.os_box = tk.Entry(self.frame , textvariable=reqos )
        self.oslabel = tk.Label(self.frame,text = "Required OS :")

        self.discount_box = tk.Entry(self.frame , textvariable=discount )
        self.discountlabel = tk.Label(self.frame,text = "Discount Rate % :")
        
        self.series_box = tk.Entry(self.frame , textvariable=series )
        self.serieslabel = tk.Label(self.frame,text = "Game Series :")

        self.price_box = tk.Entry(self.frame , textvariable=price )
        self.pricelabel = tk.Label(self.frame,text = "Price :")
        
        self.platform_box = tk.Entry(self.frame , textvariable=platform )
        self.platformlabel = tk.Label(self.frame,text = "Platform :")

        self.submitbutton = tk.Button(self.frame, text = 'Add This Game', width = 25, command = self.addGameToDb)

        self.title_box.place(x = 140,
        y = 10,height=30,width = 250)
        self.titlelabel.place(x = 0,
        y = 10,height=30,width = 130)
        

        self.ram_box.place(x = 140,
        y = 50,height=30,width = 250)
        self.ramlabel.place(x = 0,
        y = 50,height=30,width = 130)

        self.graphic_box.place(x = 140,
        y = 90,height=30,width = 250)
        self.graphiclabel.place(x = 0,
        y = 90,height=30,width = 130)

        self.os_box.place(x = 140,
        y = 130,height=30,width = 250)
        self.oslabel.place(x = 0,
        y = 130,height=30,width = 130)

        self.platform_box.place(x = 140,
        y = 170,height=30,width = 250)
        self.platformlabel.place(x = 0,
        y = 170,height=30,width = 130)

        self.series_box.place(x = 140,
        y = 210,height=30,width = 250)
        self.serieslabel.place(x = 0,
        y = 210,height=30,width = 130)

        self.discount_box.place(x = 140,
        y = 250,height=30,width = 250)
        self.discountlabel.place(x = 0,
        y = 250,height=30,width = 130)

        self.price_box.place(x = 140,
        y = 290,height=30,width = 250)
        self.pricelabel.place(x = 0,
        y = 290,height=30,width = 130)
        
        self.submitbutton.place(x = 150,
        y = 330,height=30,width = 100)
        

        self.frame.pack()



    def addGameToDb(self):

        global db
        global title
        global ram
        global graphiccard
        global reqos
        global platform
        global discount
        global series
        global price
        global devid

        logintodb("","")

        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        second = now.second
        timestr = "" + str(year) + "-"+str(month)+ "-" + str(day) + " "+str(hour)+":"+str(minute)+":"+str(second)
        print(timestr)

        query = "INSERT INTO GAME1 VALUES ("
        query = query +"\""+title.get()  +"\","
        query = query + str(0) + ","
        query = query + str(0)
        query = query +",\""+ram.get()  +"\","
        query = query +"\""+graphiccard.get()  +"\","
        query = query +"\""+reqos.get()  +"\","
        query = query +"\""+platform.get()  +"\","
        query = query + str(devid[0]) + ","
        query = query + str(discount.get()) + ","
        query = query +"\""+series.get()  +"\","
        query = query +"\""+timestr  +"\","
        query = query + str(price.get())
        query = query + ");"


        print(query)
        cur = db.cursor()
        savequery = query

        try: 
            cur.execute(savequery) 
            #myresult = cur.fetchall()
            db.commit()         


        except: 
            db.rollback() 
            print("Error occured") 



class Admin_Window:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)    
        self.userlabel = tk.Label(self.frame,text = "All Users")
        self.gameslabel = tk.Label(self.frame,text = "Games for selected user")
        self.banlabel = tk.Label(self.frame,text = "Selected user is banned.")
        
        self.users_list = tk.Listbox(self.frame)
        self.users_list.bind('<<ListboxSelect>>',self.CurSelet)

        self.gamesforuser = tk.Listbox(self.frame)
        self.gamesforuser.bind('<<ListboxSelect>>',self.CurSelet2)

        self.permabanbutton = tk.Button(self.frame, text = 'Perma Ban User', width = 55, command = self.PermaBanUser)
        self.datebanbutton = tk.Button(self.frame, text = 'Ban User For Selected Date', width = 55, command = self.BanUserDate)

        now = datetime.datetime.now()
        self.calendar = DateEntry(self.frame,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=now.year, month=now.month, day=now.day)
                
        self.permabanbutton.place(x = 500,
        y = 125,height=30,width = 170)

        self.datebanbutton.place(x = 500,
        y = 165,height=30,width = 170)
        #self.banlabel.configure(visible = False)

        self.calendar.place(x = 500,
        y = 45,height=60,width = 100)

        self.userlabel.place(x = 40,
        y = 10)

        self.gameslabel.place(x = 230,
        y = 10)

        self.getUsers(self.users_list)
        self.users_list.place(x = 10,
        y = 35,height = 250,width = 120)

        self.gamesforuser.place(x = 150,
        y = 35,height = 250,width = 300)

        self.calendar.bind("<<DateEntrySelected>>", self.print_sel)
        self.frame.pack()

    def banlabelvisible(self):
        self.banlabel.place(x = 460,
        y = 10,height=30,width = 200)

        self.banlabel.configure(foreground="red")
    
    def BanUserDate(self):
        global bandate
        global pickedUser
        global pickedgame
        global adminid
        global db
        logintodb("","")
        cur = db.cursor()
        
        queryforgamerid = "select id from gamer1,gamer2 where gamer1.email = gamer2.email and username = \""+pickedUser+"\""
        #print(queryforgamerid)
        #print(savequery)
        if(pickedUser == ""):
            return
        try: 
            cur.execute(queryforgamerid) 
            myresult = cur.fetchall()
            currentgamerid = str(myresult[0])
            print("ok")
            currentgamerid = currentgamerid[1:-2]
            print("ok")
            #currentgamerid = int(currentgamerid)

            queryfordateban = "Insert into bans values("+str(adminid)+","+str(currentgamerid)+",\""+str(pickedgame)+"\",\""+str(bandate)+" 00:00:00\""+");"
            print(queryfordateban)
            cur.execute(queryfordateban) 
            db.commit()
            #cur.fetchall()
            self.banlabelvisible()


        except: 
            db.rollback() 
            print("Error occured") 


    def PermaBanUser(self):
        global bandate
        global pickedUser
        global pickedgame
        global adminid
        global db
        logintodb("","")
        cur = db.cursor()
        
        queryforgamerid = "select id from gamer1,gamer2 where gamer1.email = gamer2.email and username = \""+pickedUser+"\""
        #print(queryforgamerid)
        #print(savequery)
        if(pickedUser == ""):
            return
        try: 
            cur.execute(queryforgamerid) 
            myresult = cur.fetchall()
            currentgamerid = str(myresult[0])
            currentgamerid = currentgamerid[1:-2]
            #currentgamerid = int(currentgamerid)
            print("ok")
            queryforpermaban = "Insert into bans values("+str(adminid)+","+str(currentgamerid)+",\"permanent-ban\","+"\"9999-01-01 00:00:00\""+");"
            print(queryforpermaban)
            cur.execute(queryforpermaban) 
            db.commit()
            #cur.fetchall()
            self.banlabelvisible()


        except: 
            db.rollback() 
            print("Error occured") 


    def print_sel(self,event):
        global bandate
        bandate = str(self.calendar.get_date())
        print(self.calendar.get_date())

    def CurSelet(self,event):
        #userselect
        global pickedUser
        widget = event.widget
        selection=widget.curselection()
        if(len(selection) == 0):
            return
        picked = widget.get(selection[0])
        pickedUser = picked
        self.getGamesForUser(picked,self.gamesforuser)

    def CurSelet2(self,event):
        #gameselect
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        global pickedgame
        pickedgame = picked
        print(picked)

    def getGamesForUser(self,picked,gamesforuserlist):
        global db
        logintodb("","")
        global pickedUser
        pickedUserstr = str(pickedUser)
        cur = db.cursor()
        savequery = "SELECT game_title FROM Game1,has,Gamer1,Gamer2 where (gamerid=id) and (gamer1.email=gamer2.email) and (username = \""+pickedUserstr+"\") and (has.game_title = game1.title)"
        #print(savequery)

        try: 
            cur.execute(savequery) 
            myresult = cur.fetchall()
            #print(myresult)
            gamesforuserlist.delete(0,'end')
            index = 0
            for element in myresult:
                gametitlestr = str(element)
                gametitlestr = gametitlestr[2:-3]
                gamesforuserlist.insert(index,gametitlestr)
                index = index + 1
                print(self.calendar.get_date())

        except: 
            db.rollback() 
            print("Error occured") 


    def getUsers(self,users_list):

        global db
        logintodb("","")
        cur = db.cursor()
        savequery = "SELECT username FROM GAMER2"
        adminidtemp = -1

        try: 
            cur.execute(savequery) 
            myresult = cur.fetchall()
            print(myresult)
            index = 0
            for element in myresult:
                usernamestr = str(element)
                usernamestr = usernamestr[2:-3]
                users_list.insert(index,usernamestr)
                index = index + 1

        except: 
            db.rollback() 
            print("Error occured") 

class Admin_Validation_Window:
    
    def __init__(self, master):
        global entered_query
        global adminmail
        global adminpassword
        mail = tk.StringVar()  
        password = tk.StringVar()  
        adminmail = mail
        adminpassword = password

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.mail_box = tk.Entry(self.frame , textvariable=mail )
        self.password_box = tk.Entry(self.frame ,show = "*", textvariable=password )
        self.submitbutton = tk.Button(self.frame, text = 'Login', width = 25, command = self.getAdminData)
        self.mail_label = tk.Label(self.frame,text = "Mail Address : ")
        self.pass_label = tk.Label(self.frame,text = "Password : ")

        self.mail_label.place(x = 0,
        y = 55)

        self.pass_label.place(x = 0,
        y = 115)

        self.mail_box.place(x = 100,
        y = 40,
        width=240,
        height=40)
        
        self.password_box.place(x = 100,
        y = 100,
        width=240,
        height=40)
        

        self.submitbutton.place(x = 150,
        y = 150,
        width=80,
        height=40)

        self.frame.pack()
        #root.after(1000, Main)
        #root.mainloop()
    def getAdminData(self):
        global adminmail
        global adminpassword
        mail_str = adminmail.get()
        password_str = adminpassword.get()
        if(mail_str == ""):
            return
        query = "Select * from admin2 where (email = \"" + mail_str + "\") and " + "(password = \""+ password_str + "\")"
        print(query)
        cur = db.cursor()
        savequery = query
        adminidtemp = -1

        try: 
            cur.execute(savequery) 
            myresult = cur.fetchall()
            if(len(myresult) != 0):
                query2 = "Select * from admin1 where (email = \"" + mail_str + "\")"
                cur.execute(query2) 
                myresult2 = cur.fetchall()
                adminidtemp = myresult2[0][0]
            global adminid
            adminid = adminidtemp
            print(adminid)

            #change to -1
            if(adminid != -1):
                self.master.withdraw()
                toplevel = tk.Toplevel(self.master)
                toplevel.geometry("700x300")
                toplevel.title("Admin Page")
                app = Admin_Window(toplevel)   

        except: 
            db.rollback() 
            print("Error occured") 

class Steamdbdev_Window:

    def __init__(self, master):
        global entered_query
        entered_query = tk.StringVar()  

        self.master = master
        self.frame = tk.Frame(self.master,height = 1000,width = 1000)
        self.entry_box = tk.Entry(self.frame , textvariable=entered_query )
        self.submitbutton = tk.Button(self.frame, text = 'Submit Query', width = 25, command = self.getQueryResponse)
        self.text_output = tk.Listbox(self.frame)
        global text_box
        text_box  = self.text_output
        self.entry_box.place(x = 150,
        y = 10,
        width=500,
        height=60)
        
        self.submitbutton.place(x = 350,
        y = 100,
        width=80,
        height=40)

        self.text_output.place(x = 0,
        y = 160,
        width=800,
        height=600)

        self.frame.pack()
        #root.after(1000, Main)
        #root.mainloop()

    def close_windows(self):
        self.master.destroy()

    def getQueryResponse(self):
        global entered_query
        global text_box
        text_box.delete(0,'end')
        given_query = str(entered_query.get())
        cur = db.cursor()
        savequery = given_query
      
        try: 
            cur.execute(savequery) 
            myresult = cur.fetchall() 
            column_names = cur.column_names
            game_list2 = []
            column_names_str = "  |  "
            for element in column_names:
                column_names_str = column_names_str + element + "  |  "
            text_box.insert(0,column_names_str)
            num = 1
            for x in myresult: 
                print(x)
                result_text = "  |  "
                for element in x:
                    result_text = result_text + str(element) + "  |  "
                text_box.insert(num,result_text)
                num = num+1
            print("Query Excecuted successfully") 
            #game_data = game_list2
            
            #return game_list2
            return
          
        except: 
            db.rollback() 
            print("Error occured") 
        return
    

class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()
    def close_windows(self):
        self.master.destroy()


def logintodb(user, passw): 
      
    global db
    import mysql.connector

    db = mysql.connector.connect(
    host="localhost",
     user="root",
     password=os.environ.get("STEAMDB_PASSWORD", ""),
     db="steamdb"
    )

    
logintodb("","")
root = tk.Tk()
root.title("STEAM")
root.geometry("250x300")
cls = windowclass(root)
root.mainloop()
