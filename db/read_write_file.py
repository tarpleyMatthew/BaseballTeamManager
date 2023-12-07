######## Functions to read and write data to seperate file #################

import csv
FILENAME = "Database/player_data.csv"
DICT_KEYS = ['Name', 'Position', 'At Bats', 'Hits', 'Average']

#read data from file
def read_player_data():
    players = []


    try:
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                players.append(row)

        player_dict = {row[0]: dict(zip(DICT_KEYS[1:], row[1:])) for row in players}
        return player_dict
    except FileNotFoundError:
        print('Team data file could not be found.\nA new file will be created.')
        return player_dict
    except OSError:
        print('File found - error reading file.\nA new file will be created.')
        return player_dict
    except:
        print('An unexpected error occured.\nA new file will be created.')
        return player_dict

#write player data
def write_player_data(players):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=DICT_KEYS)

        for player_name, player_data in players.items():
            writer.writerow({
                'Name': player_name,
                'Position': player_data['Position'],
                'At Bats': player_data['At Bats'],
                'Hits': player_data['Hits'],
                'Average': player_data['Average']
            })    

