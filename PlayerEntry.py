import tkinter as tk #importing tkinter to use as gui 

class PlayerEntry: #player entry class
    def __init__(self): #runs when class player entry is called

        #create window 
        self.window = tk.Tk() #makes window 
        self.window.geometry("1200x800") #window size
        self.window.columnconfigure(0, weight=1)
        
        #entry terminal text (ET)
        self.window.title("Entry Terminal") #title of window
        
        #black background
        self.window.configure(bg='black')
        
        #edit current game text
        self.ETlabel = tk.Label(self.window, text="Edit Current Game", font=('Times New Roman', 18, 'bold'), fg="white", bg="black") #window text, font, size, boldness
        self.ETlabel.grid(row=0, column=0, pady=5) #dist between label and window 
        
        #create box to hold RGteams
        self.holdTeamsRG = tk.Frame(self.window, bg="black", width=500, height=700) #creates a fream thatll hold everthing 
        self.holdTeamsRG.grid(row=1, column=0) #expand is if theres extraa room in the widget give it to this one 

        self.RGteams() #call RGteams to run everything below
        self.gameMode() 
        self.fButtons()
        self.DelandIns()
        
        self.window.mainloop() #gets the screen to show (must be below everything)
        
    def RGteams(self):
        #red and green team background color
        self.redLabel1 = tk.Frame(self.holdTeamsRG, background='#3b0009') #labels for grids
        self.greenLabel2 = tk.Frame(self.holdTeamsRG, background='#114024')

        #define a grid
        self.holdTeamsRG.columnconfigure(0, weight=1) #first column and its width
        self.holdTeamsRG.columnconfigure(1, weight=1) #second column and its width
        self.holdTeamsRG.rowconfigure(0, weight = 1) #one big row (which has the 2 columns)
  
        #place a widget
        self.redLabel1.grid(row = 0, column=0, sticky= 'nsew')
        self.greenLabel2.grid(row = 0, column=1, sticky= 'nsew')
        
        #red and green team title text (and text box border) 
        self.RTitle = tk.Label(self.redLabel1, text="RED TEAM", font=('Times New Roman', 15), bg="#3b0009", fg="white", borderwidth=1, relief="raised")
        self.RTitle.grid(row=0, column=0, columnspan=4, pady=10)
        self.GTitle = tk.Label(self.greenLabel2, text="GREEN TEAM", font=('Times New Roman', 15), bg="#114024", fg="white", borderwidth=1, relief="raised")
        self.GTitle.grid(row=0, column=0, columnspan=4, pady=10)
        
        for c in range(4):
            self.redLabel1.columnconfigure(c, weight=1)
            self.greenLabel2.columnconfigure(c, weight=1)
        
        #red widgets green team 2 columns that go to 19 
        for i in range(20):
            #button on left red
            Rbtn = tk.Button(self.redLabel1, width=2)
            Rbtn.grid(row=i+1, column=0,padx=2, pady=2)
            
            #button number
            RbtnTxt = tk.Label(self.redLabel1, text=str(i+0), fg="white", bg="#3b0009")
            RbtnTxt.grid(row=i+1, column=1,padx=2, pady=2, sticky='w')
            
            #two entry columns
            entryTextR1 = tk.Entry(self.redLabel1, width=30) #first one
            entryTextR1.grid(row=i+1, column=2,padx=2, pady=2, sticky='nsew')
            entryTextR2 = tk.Entry(self.redLabel1, width=32)
            entryTextR2.grid(row=i+1, column=3,padx=2, pady=2, sticky='nsew') #second 1
        
        #green widgets green team 2 columns that go to 19 
        for i in range(20):
            #button on left green
            Gbtn = tk.Button(self.greenLabel2, width=2)
            Gbtn.grid(row=i+1, column=0,padx=2, pady=2)
            
            #button number
            GbtnTxt = tk.Label(self.greenLabel2, text=str(i+0), fg="white", bg="#114024")
            GbtnTxt.grid(row=i+1, column=1,padx=2, pady=2, sticky='w')
            
            #two entry columns
            entryTextG1 = tk.Entry(self.greenLabel2, width=32) #first one
            entryTextG1.grid(row=i+1, column=2,padx=2, pady=2, sticky='nsew')
            entryTextG2 = tk.Entry(self.greenLabel2, width=32)
            entryTextG2.grid(row=i+1, column=3,padx=2, pady=2, sticky='nsew') #second one
    
    #game mode text under red and green team (seperate from the RGteams but touching it like blocks together)
    def gameMode(self):
        self.GMFrame = tk.Frame(self.window, background="#777777") #frame for grids
        self.GMFrame.grid(row=2, column=0, pady=0)
        #self.GMFrame.pack()
        self.GMLabel = tk.Label(self.GMFrame, background="#777777", text="Game Mode: Standard public mode", fg="white", font=('Times New Roman', 10)) #text in frame thats under Red and green
        self.GMLabel.pack(padx=2,pady=1)
    
    #all f buttons
    def fButtons(self):
        #frame that holds buttons
        self.fButtonFrame = tk.Frame(self.window, background="black")
        self.fButtonFrame.grid(row=3, column=0, pady=5)
        
        #make columns spread 
        for c in range(8):
            self.fButtonFrame.columnconfigure(c, weight=1)
        
        #make the buttons
        self.f1 = tk.Button(self.fButtonFrame, text="F1\nEdit\nGame", width=8, height=3, justify="center")
        self.f1.grid(row=0, column=0, padx=4)
        
        self.f2 = tk.Button(self.fButtonFrame, text="F2\nGame\nParameters", width=8, height=3)
        self.f2.grid(row=0, column=1, padx=4)
        
        self.f3 = tk.Button(self.fButtonFrame, text="F3\nStart\nGame", width=8, height=3)
        self.f3.grid(row=0, column=2, padx=4)
        
        self.f5 = tk.Button(self.fButtonFrame, text="F5\nPreEntered\nGames", width=8, height=3)
        self.f5.grid(row=0, column=3, padx=4)
        
        self.f7 = tk.Button(self.fButtonFrame, text="F7", width=8, height=3)
        self.f7.grid(row=0, column=4, padx=4)
        
        self.f8 = tk.Button(self.fButtonFrame, text="F8\nView\nGame", width=8, height=3)
        self.f8.grid(row=0, column=5, padx=4)
        
        self.f10 = tk.Button(self.fButtonFrame, text="F10\nFlick\nSync", width=8, height=3)
        self.f10.grid(row=0, column=6, padx=4)
        
        self.f12 = tk.Button(self.fButtonFrame, text="F12\nClear\nGame", width=8, height=3)
        self.f12.grid(row=0, column=7, padx=4)
        
    ##text under fs stuff on the very bottom of the widnow screen
    def DelandIns(self):
        self.DIFrame = tk.Frame(self.window, background="#ACACAC") #frame for grids
        self.DIFrame.grid(row=4, column=0, sticky="ew")
        self.DILabel = tk.Label(self.DIFrame, background="#ACACAC", text="<Del> to Delete Player, <Ins> to Manually Insert, or edit codename", fg="black", font=('Times New Roman', 10)) #text in frame thats under Red and green
        self.DILabel.pack(pady=1)

screen = PlayerEntry()

#=====================================================================JAYDENS NOTES=====================================================================#
#do tk. to see everything that i could possibly use from tk
#create window 
#window = tk.Tk()
#window.geometry("1200x800") #window size
#window.title("Entry Terminal") #title of window
#label = tk.Label(window, text="Edit Current Game", font=('Arial', 18, 'bold')) #window text, font, size, boldness
#label.pack(padx=10, pady=10) #dist between label and window 
#textbox = tk.Text(window, height=3, font=('Arial', 16)) #adds text box for typing
#textbox.pack() #padding for text when typing
#entryText = tk.Entry(window, font=('Arial', 15)) #adds entry/password type text box for typing
#entryText.pack(padx=10, pady=10)
#button = tk.Button(window, text="click Me", font=('arial', 18)) #button
#button.pack(padx=10, pady=10)
#buttonFrame = tk.Frame(window)
#buttonFrame.columnconfigure(0, weight=1) #buttons to stretch 
#buttonFrame.columnconfigure(1, weight=1)
#buttonFrame.columnconfigure(2, weight=1)
#btn1 = tk.Button(buttonFrame, text="1", font=('Arial', 18)) #actual button thats inside button frame 
#btn1.grid(row=0, column=0, sticky=tk.W+tk.E) #first button first row frist colum (basically stretches button accros whole row using stick)
#buttonFrame.pack(fill='x') #strecth into x dimention
#anotherbtn = tk.Button(window, text="Test") #test button
#anotherbtn.place(x=200, y=200, height=100, width=100) #can place btn anywhere
#anotherbtn.pack(padx=10, pady=10)
#window.mainloop() #gets the screen to show (must be below everything)

