######## Functions to read and write data to seperate file #################
import csv
FILENAME = "player_data.csv"

#read data from file
def read_player_data():
    players = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            players.append(row)
    return players

#write player data
def write_player_data(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(players)

