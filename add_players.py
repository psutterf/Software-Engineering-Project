from db import fetch_player_by_id, insert_player

def main():

    print("Add two players to photon.players")
    for i in range(2):

        #check to make sure player ID is integer
        raw = input(f"Player ID #{i+1}: ").strip()
        if not raw.isdigit():
            print("Player ID must be an integer.")
            continue

        player_id = int(raw)
        row = fetch_player_by_id(player_id)

        #Check if row already exists and print the existing player
        if row:
            print(f"Found existing: id={row['id']} codename={row['codename']}")

        #Get codename and error check for empty strings
        codename = input("Codename: ").strip()
        if not codename:
            print("Codename cannot be empty.")
            continue

        insert_player(player_id, codename)
        print("Player Saved")

    print("Completed")

if __name__ == "__main__":
    main()
