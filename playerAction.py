import tkinter as tk
from PIL import Image, ImageTk

class GameActionScreen:

    def __init__(self, red_players, green_players):

        self.window = tk.Tk()
        self.window.title("Game Action Screen")
        self.window.geometry("1200x850")
        self.window.minsize(1200, 850)     # stops user from resizing smaller to fit everything
        self.window.configure(bg="black")  # background color 

        self.window.update_idletasks()  #resizes window immediately; fixing issue where timer was clipped out

        self.base_icon_img = ImageTk.PhotoImage(
            Image.open("baseicon.jpg").resize((20,20))
        )
        
        self.red_score_labels = {}     
        self.green_score_labels = {}

        self.red_scores = {}           #stores players scores to be updated and summed later 
        self.green_scores = {}

        self.red_base_icons = {}
        self.green_base_icons = {}
        # -------------------
        #    Team Frame
        # -------------------

        top_frame = tk.Frame(self.window, bg="black")
        top_frame.pack(fill="x")  #--------------- > stretch horizontally 

        #team frames; two frames inside of top frame
        red_frame = tk.Frame(top_frame, bg="black")
        red_frame.pack(side="left", expand=True, fill="both", padx=20, pady=10)

        green_frame = tk.Frame(top_frame, bg="black")
        green_frame.pack(side="right", expand=True, fill="both", padx=20, pady=10)

        # Team titles; creates headers 
        tk.Label(
            red_frame,
            text="RED TEAM",
            fg="white",
            bg="black",
            font=("Arial", 24, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            green_frame,
            text="GREEN TEAM",
            fg="white",
            bg="black",
            font=("Arial", 24, "bold")
        ).pack(pady=(0, 10))

    
        red_players_frame = tk.Frame(red_frame, bg="black")
        red_players_frame.pack(fill="both", expand=True)

        green_players_frame = tk.Frame(green_frame, bg="black")
        green_players_frame.pack(fill="both", expand=True)

        # Make column name expand while score remains right-aligned 
        red_players_frame.columnconfigure(0, weight=1)
        red_players_frame.columnconfigure(1, weight=0)

        green_players_frame.columnconfigure(0, weight=1)
        green_players_frame.columnconfigure(1, weight=0)

        # Show red players
        for i, (pid, name) in enumerate(red_players):      #takes in a tuple of id and player name 

            self.red_scores[name] = 0  #initialize scores to 0 

            tk.Label(
                red_players_frame,
                text=name,
                fg="red",
                bg="black",
                font=("Arial", 18)
            ).grid(row=i, column=0, sticky="w", padx=10, pady=2)

            score_label = tk.Label(
                red_players_frame,
                text="0",
                fg="red",
                bg="black",
                font=("Arial", 18)
            )
            score_label.grid(row=i, column=1, sticky="e", padx=10, pady=2)

            icon_label = tk.Label(
                red_players_frame,
                bg="black"
            )
            icon_label.grid(row=i, column=2, padx=5)
            
            self.red_score_labels[name] = score_label
            self.red_base_icons[name] = icon_label

        # Show green players
        for i, (pid, name) in enumerate(green_players):

            self.green_scores[name] = 0

            tk.Label(
                green_players_frame,
                text=name,
                fg="lime",
                bg="black",
                font=("Arial", 18)
            ).grid(row=i, column=0, sticky="w", padx=10, pady=2)

            score_label = tk.Label(
                green_players_frame,
                text="0",
                fg="lime",
                bg="black",
                font=("Arial", 18)
            )
            score_label.grid(row=i, column=1, sticky="e", padx=10, pady=2)

            icon_label = tk.Label(
                green_players_frame,
                bg="black"
            )
            icon_label.grid(row=i, column=2, padx=5)
            self.green_score_labels[name] = score_label
            self.green_base_icons[name] = icon_label

        
        # total scores red team
        red_total_row = len(red_players) + 1   #calc row below last player entry

        tk.Label(
            red_players_frame,
            text="TOTAL",
            fg="white",
            bg="black",
            font=("Arial", 18, "bold")
        ).grid(row=red_total_row, column=0, sticky="w", padx=10, pady=(10,2))

        self.red_total_label = tk.Label(
            red_players_frame,
            text="0",
            fg="white",
            bg="black",
            font=("Arial", 18, "bold")
        )
        self.red_total_label.grid(row=red_total_row, column=1, sticky="e", padx=10)


        # total scores green team 
        green_total_row = len(green_players) + 1

        tk.Label(
            green_players_frame,
            text="TOTAL",
            fg="white",
            bg="black",
            font=("Arial", 18, "bold")
        ).grid(row=green_total_row, column=0, sticky="w", padx=10, pady=(10,2))

        self.green_total_label = tk.Label(
            green_players_frame,
            text="0",
            fg="white",
            bg="black",
            font=("Arial", 18, "bold")
        )
        self.green_total_label.grid(row=green_total_row, column=1, sticky="e", padx=10)

        # -------------------
        #     Game Log 
        # -------------------

        log_frame = tk.Frame(self.window, bg="#1e2f5e") #-------------> blue event box
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log = tk.Text(   # text widget 
            log_frame,
            bg="#1e2f5e",
            fg="white",
            font=("Arial", 14),
            height=8
        )
        self.log.pack(fill="both", expand=True)
        self.log.config(state="disabled") #-------> had issues where you could type in text box this disables it

        # -------------------
        #       Timer
        # -------------------

        self.timer_label = tk.Label(    # displays initial 5 min timer
            self.window,
            text="Time Remaining: 5:00",
            fg="white",
            bg="black",
            font=("Arial", 26)
        )
        self.timer_label.pack(anchor="e", padx=20, pady=10) #anchor e right-aligns timer
        self.time_left = 300     # 300 seconds = 5 min
        self.update_timer()      # calls to deincriment timer

    def update_timer(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.timer_label.config(
            text=f"Time Remaining: {minutes}:{seconds:02}"
        )

        if self.time_left > 0:
            self.time_left -= 1
            self.window.after(1000, self.update_timer)  # waits a second then calls function again 

    def give_base_icon(self, player_name):
        if player_name in self.red_base_icons: #check red team
            label = self.red_base_icons[player_name]
            label.config(image=self.base_icon_img)
            label.image = self.base_icon_img 
        
        elif player_name in self.green_base_icons: #check green team
            label = self.green_base_icons[player_name]
            label.config(image=self.base_icon_img)
            label.image = self.base_icon_img 
        
    def add_event(self, text):
        self.log.config(state="normal")       #toggles to enable editing temporarily 
        self.log.insert("end", text + "\n")
        self.log.see("end")
        self.log.config(state="disabled")    #adds text line and then toggles back off 
        if "hit the base" in text.lower():
            player_name = text.lower().replace("hit the base", "").strip()
            player_name = player_name.title() #for names that are capitalized
            self.give_base_icon(player_name)

# --------------
#      Test
# --------------
if __name__ == "__main__":

    red_players = [
        (1, "Jaybobjr"),
        (2, "Caderade"),
        (3, "P-Power")
    ]

    green_players = [
        (4, "Gart"),
        (5, "Opposition #1"),
        (6, "Opposition #2")
    ]

    screen = GameActionScreen(red_players, green_players)

    screen.add_event("Gart hit Jaybobjr")
    screen.add_event("P-dawg hit Opp #2")
    screen.add_event("Caderade hit the base")

    screen.window.mainloop()