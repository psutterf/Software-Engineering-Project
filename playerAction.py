import tkinter as tk
from PIL import Image, ImageTk
import threading
from network import LazerTagNetwork

class GameActionScreen:

    def __init__(self, red_players, green_players):

        print("GameActionScreen __init__ called")

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

        # create network object
        self.network = LazerTagNetwork()
        self.network.send_start_code()           # traffic generator needs to be running before game starts so that it can recieve code 

        
        self.running = True

        # lookup tables for players 
        self.player_lookup = {}
        self.player_team = {}

        for player in red_players:
            hardware_id = str(player["hardware_id"])
            self.player_lookup[hardware_id] = player["name"]
            self.player_team[hardware_id] = "red"

        for player in green_players:
            hardware_id = str(player["hardware_id"])
            self.player_lookup[hardware_id] = player["name"]
            self.player_team[hardware_id] = "green"


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
        for i, player in enumerate(red_players):
            name = player["name"]      

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
        for i, player in enumerate(green_players):
            name = player["name"]


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

        self.timer_label = tk.Label(    # displays initial 6 min timer
            self.window,
            text="Time Remaining: 6:00",
            fg="white",
            bg="black",
            font=("Arial", 26)
        )
        self.timer_label.pack(anchor="e", padx=20, pady=10) #anchor e right-aligns timer
        self.time_left = 360     # 360 seconds = 6 min
        self.update_timer()      # calls to deincriment timer


        print("created")


        # start listener thread
        self.listener_thread = threading.Thread(target=self.listen_for_packets, daemon=True)
        self.listener_thread.start()

    def update_timer(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60

        self.timer_label.config(
            text=f"Time Remaining: {minutes}:{seconds:02}"
        )

        if self.time_left > 0:
            self.time_left -= 1
            self.window.after(1000, self.update_timer)  # waits a second then calls function again 
        else:
            self.running = False
            self.network.send_end_code()
            self.add_event("Game ended")

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

    def listen_for_packets(self):
        while self.running:
            try:
                data, addr = self.network.receive_data()
                self.window.after(0, self.handle_packet, data)
            except Exception as e:
                print("Receive error:", e)
                break

    def handle_packet(self, message):
        event_text = self.parse_event(message)
        if event_text:
            self.add_event(event_text)

        self.network.send_ack()  # sends a response back to traffic generator so it continues 

        if "hit teammate" in event_text.lower(): #friendly fire needs a second response 
            self.network.send_ack()

    def parse_event(self, message):
        message = message.strip()

        if ":" not in message:
            return f"Unknown message: {message}"

        attacker_id, target_id = message.split(":", 1)

        attacker_name = self.player_lookup.get(attacker_id, f"Unknown({attacker_id})")
        attacker_team = self.player_team.get(attacker_id, "unknown")

        # base hit
        if target_id == "43" or target_id == "53":
            self.update_score(attacker_name, 100)
            self.give_base_icon(attacker_name)
            return f"{attacker_name} hit the base"

        target_name = self.player_lookup.get(target_id, f"Unknown({target_id})")
        target_team = self.player_team.get(target_id, "unknown")

        # friendly fire
        if attacker_team == target_team and attacker_team != "unknown":
            self.update_score(attacker_name, -10)
            self.update_score(target_name, -10)
            return f"{attacker_name} hit teammate {target_name}"

        # enemy hit
        self.update_score(attacker_name, 10)
        return f"{attacker_name} hit {target_name}"

    def update_score(self, player_name, points):
        if player_name in self.red_scores:
            self.red_scores[player_name] += points
            self.red_score_labels[player_name].config(text=str(self.red_scores[player_name]))
            self.red_total_label.config(text=str(sum(self.red_scores.values())))

        elif player_name in self.green_scores:
            self.green_scores[player_name] += points
            self.green_score_labels[player_name].config(text=str(self.green_scores[player_name]))
            self.green_total_label.config(text=str(sum(self.green_scores.values())))


# --------------
#      Test
# --------------
if __name__ == "__main__":

    red_players = [
        {"pid": 1, "name": "Jaybobjr", "hardware_id": 11, "team": "red"},
        {"pid": 2, "name": "Caderade", "hardware_id": 13, "team": "red"},
        {"pid": 3, "name": "P-Power", "hardware_id": 15, "team": "red"}
    ]

    green_players = [
        {"pid": 4, "name": "Gart", "hardware_id": 20, "team": "green"},
        {"pid": 5, "name": "Opposition #1", "hardware_id": 22, "team": "green"},
        {"pid": 6, "name": "Opposition #2", "hardware_id": 24, "team": "green"}
    ]

    screen = GameActionScreen(red_players, green_players)

    screen.window.mainloop()