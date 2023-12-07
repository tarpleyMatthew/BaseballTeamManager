##Lineup class

from dataclasses import dataclass

@dataclass
class Lineup:
    def __init__(self):
        self.__lineup = []

    def add_player(self, player):
        self.__lineup.append(player)

    def remove_player(self, index): #NOT USED
        if 0 <= index < len(self.__lineup):
            del self.__lineup[index]
        else:
            print("Invalid index. Player not removed.")

    def move_player(self, current_index, new_index): #NOT USED
        if 0 <= current_index < len(self.__lineup) and 0 <= new_index <= len(self.__lineup):
            player = self.__lineup.pop(current_index)
            self.__lineup.insert(new_index, player)
        else:
            print("Invalid indices. Player not moved.")

    def get_player_at_index(self, index):
        if 0 <= index < len(self.__lineup):
            return self.__lineup[index]
        else:
            return None

    def edit_player_stats(self, index, at_bats, hits): #NOT USED
        if 0 <= index < len(self.__lineup):
            self.__lineup[index].at_bats = at_bats
            self.__lineup[index].hits = hits
        else:
            print("Invalid index. Player stats not edited.")

    def get_all_players(self):
        return self.__lineup

##  Iterator    
    def __iter__(self):
        for player in self.__lineup:
            yield player