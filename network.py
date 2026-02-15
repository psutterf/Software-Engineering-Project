import socket


class LazerTagNetwork:
    
    def __init__(self, network_ip="127.0.0.1", send_port=7500, recieve_port=7501):
        self.network_ip = network_ip
        self.send_port = send_port
        self.recieve_port = recieve_port  #will be used in futrue sprints to get hit data 

        
        self.send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #create UDP socket for broadcasting

        self.send_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #enables socket for broadcasting


    def broadcast_id(self, equipment_id: int):
        message = str(equipment_id).encode()
        self.send_socket.sendto(message, (self.network_ip, self.send_port))

    def change_network(self, new_ip: str):
        self.network_ip = new_ip


# TODO: Delete later used for testing and implimentation example

def main():
    network = LazerTagNetwork()  #default network is local host and port 7500

    player_id = 12345 
    print(f"player tag : {player_id}")

    network.broadcast_id(player_id)  # open second terminal and run command "sudo tcpdump -i lo -n udp port 7500 -X" should see packet in Hex and decimal
    print("packet succefully sent")

    player_id = "message being sent wowowowowow"

    print(f"player tag : {player_id}")
    network.broadcast_id(player_id)
    print("packet succefully sent")

    print(f"Currently Using local host : {network.network_ip}")
    network.change_network("192.68.25.6")

    print(f"successfully changed network to {network.network_ip}")


if __name__ == "__main__":
    main()
        