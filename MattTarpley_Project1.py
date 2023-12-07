#----------------------------------------------------------------------------------------------------------------
#--
#Original Author:      Matt Tarpley                                  #
#Date Created:          10/5/2023                                    #
#Version:               2.00.00                                      #
#Date Last Modified:    12/7/2023                                    #
#Modified by:          Matt Tarpley                               #
#Modification log:     
#					============================
#						mwt 10/3/23: created program
#							 worked on steps 1-4        
#						mwt 10/5/23:
#							 worked on step 5                 
#						mwt 10/6/23:
#							 began working on step 6 *left off on rearrange/change pos & stats function  
#                       mwt 10/10/23:
#							 finished rearrange/change pos & stats functionality
#							 created local git repo to track changes
#                            exported functions as module
#							 created csv to save player data
#                            set up GitHub remote repo, new branch for save player data changes
#                            pushed changes, merged with master
#						mwt 10/11/23
# 							created local branch 'handle-exeptions'
#							added error handling/cleaned up code and comments
#							merged w/ master and pushed to GitHub
#						
#					    mwt 12/4/23
# 							completed step 9 
#							created 3 tier folders
#							completed step 10
#							merged to master and pushed to GitHub
#
#						mwt 12/5/23
#							steps 14/15/16
#						
#						mwt 12/7/23
#							completed final steps, cleaned up code, pushed to github
#------------------------------------------------------------------------------------------------------------------>

#import functions
#import db.read_write_file as rw
import tkinter as tk
import db.DbAccess as db
import objects.DataHandler as handler
from ui.gui import TeamManagerGUI

#display menu
def display_menu():
	print("MENU OPTIONS")
	print("1 - Display Lineup")
	print("2 - Add Player")
	print("3 - Remove Player")
	print("4 - Move Player")
	print("5 - Edit Player Position")
	print("6 - Edit Player Stats")
	print("7 - Exit program")
	print()

#display title
def display_title(positions): 
	print("=" * 64)
	print("        Baseball Team Manager")
	print()
	handler.get_date()
	print()
	display_menu()
	print('POSITIONS')
	for p in positions:
		print(f"'{p}", end=' ')
	print()

#main function
def main():
	positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF' , 'P')
	#read data from sql
	lineup = db.get_lineup()

	root = tk.Tk()
	root.title("Matt Tarpley Baseball Team Manager")
	teamManager = TeamManagerGUI(root, lineup)
	#read data from file
	#players = rw.read_player_data()

	display_title(positions)
	print("=" * 64)
	menu_option = int(input("Menu option: "))

	#menu options
	while menu_option != 7:

		#display lineup
		if menu_option == 1:
			lineup = db.get_lineup()

			handler.display_lineup(lineup)
			menu_option = int(input("Menu option: "))
		#add player
		elif menu_option == 2:

			handler.add_player(lineup, positions)
			menu_option = int(input("Menu option: "))
		#delete player
		elif menu_option == 3:

			handler.delete_player(lineup)
			menu_option = int(input("Menu option: "))
		#move player
		elif menu_option == 4:

			handler.move_player(lineup)
			menu_option = int(input("Menu option: "))
		#edit player position
		elif menu_option == 5:

			handler.change_position(lineup, positions)
			menu_option = int(input("Menu option: "))
		#edit player stats
		elif menu_option == 6:

			handler.edit_stats(lineup)
			menu_option = int(input("Menu option: "))	
		else:
			print("Not a valid option. Please try again.")
			print()
			display_menu()
			print()
			menu_option = int(input("Menu option: "))
	print("Bye!")
	root.mainloop()
#exec program
if __name__=="__main__":
    main()