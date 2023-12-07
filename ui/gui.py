## GUI TO UPDATE AND FIND PLAYERS###

import tkinter as tk
from tkinter.messagebox import showerror
import db.DbAccess as db
from objects.Player import Player
from objects.Lineup import Lineup

class TeamManagerGUI:
    def __init__(self, root, lineup):
        self.root = root

        #create frame
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(padx=10, pady=10)

        #labels and loop to create grid based on labels
        labels = ["Player ID:", "First Name:", "Last Name:", "Position:", "At Bats:", "Hits:"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(self.entry_frame, text=label_text)
            label.grid(row=i, column=0, sticky='w')

            entry = tk.Entry(self.entry_frame)
            entry.grid(row=i, column=1, padx=5, pady=3)
            self.entries[label_text] = entry

        #find player button
        self.find_button = tk.Button(self.entry_frame, text="Find Player", command=lambda: self.find_player(lineup))
        self.find_button.grid(row=0, column=2, padx=5, pady=3, rowspan=len(labels))

        #average ** had to do as label to show value
        self.result_label = tk.Label(self.entry_frame, text="")
        self.result_label.grid(row=len(labels), column=1, padx=5, pady=3, sticky='w')

        #save changes/ close buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(padx=10, pady=5)

        self.save_button = tk.Button(self.button_frame, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=0, column=0, padx=5)

        self.close_button = tk.Button(self.button_frame, text="Close", command=root.destroy)
        self.close_button.grid(row=0, column=1, padx=5)

        #load default player
        self.current_player = lineup.get_player_at_index(0)
        self.current_player.playerID = 1
        self.update_entry_fields()

    #find player
    def find_player(self, lineup):
        player_id = self.entries["Player ID:"].get()

        if player_id.strip():
            try:
                player_id = int(player_id) 

                all_players = lineup.get_all_players()
                if player_id < 0 or player_id >= len(all_players):
                    showerror(title='Error', message="Please enter a valid Player ID.")
                    self.clear_entry_fields()
                else:
                    self.current_player = lineup.get_player_at_index(player_id - 1)
                    self.current_player.playerID = player_id
                    self.update_entry_fields()

            except ValueError:
                showerror(title='Error', message="Please enter a valid Player ID (an integer).")
                self.clear_entry_fields()
        else:
            print("Please enter a Player ID.")

    #Clear fields
    def clear_entry_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.result_label.config(text="")

    #update fields
    def update_entry_fields(self):
        average = self.current_player.getAverage()
        
        self.entries["Player ID:"].delete(0, tk.END)
        self.entries["Player ID:"].insert(0, str(self.current_player.playerID))

        self.entries["First Name:"].delete(0, tk.END)
        self.entries["First Name:"].insert(0, self.current_player.firstName)

        self.entries["Last Name:"].delete(0, tk.END)
        self.entries["Last Name:"].insert(0, self.current_player.lastName)

        self.entries["Position:"].delete(0, tk.END)
        self.entries["Position:"].insert(0, self.current_player.position)

        self.entries["At Bats:"].delete(0, tk.END)
        self.entries["At Bats:"].insert(0, self.current_player.atBats)

        self.entries["Hits:"].delete(0, tk.END)
        self.entries["Hits:"].insert(0, self.current_player.hits)

        self.result_label.config(text=str(average))

    #update player data
    def save_changes(self):
        self.current_player.firstName = self.entries["First Name:"].get()
        self.current_player.lastName = self.entries["Last Name:"].get()
        self.current_player.position = self.entries["Position:"].get()
        self.current_player.atBats = int(self.entries["At Bats:"].get())
        self.current_player.hits = int(self.entries["Hits:"].get())

        db.update_player(self.current_player) #call to db
