#----------------------------------------------------------------------------------------------------------------
#--
#Original Author:      Matt Tarpley                                  #
#Date Created:          10/5/2023                                    #
#Version:               1.00.00                                      #
#Date Last Modified:    10/10/2023                                    #
#Modified by:          Matthew Tarpley                               #
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
# 
#------------------------------------------------------------------------------------------------------------------>

#import functions
import read_write_file as rw
import Manipulation_Calculation_Functions as mcf

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
def display_title(): 
	print("=" * 60)
	print("        Baseball Team Manager")
	print()
	display_menu()
	print('POSITIONS')
	print('C, 1B, 2B, 3B, SS, LF, CF, RF, P')
	print("=" * 60)

def main():
	#tuple for positions/list of list for player
	positions = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF' , 'P')
#	players = [
#		['Joe', 'P', 10, 2, 0.2],
#		['Tom', 'SS', 11, 4, 0.364],
#		['Ben', '3B', 9, 3, 0.333],
#	]
	players = rw.read_player_data()
	display_title()
	menu_option = int(input("Menu option: "))

	#while loop to handle logic in program
	while menu_option != 7:

		#display lineup
		if menu_option == 1:

			mcf.display_lineup(players)
			menu_option = int(input("Menu option: "))
		#add player
		elif menu_option == 2:

			mcf.add_player(players, positions)
			rw.write_player_data(players)
			menu_option = int(input("Menu option: "))

		#delete player
		elif menu_option == 3:

			mcf.delete_player(players)
			rw.write_player_data(players)
			menu_option = int(input("Menu option: "))

		#move player
		elif menu_option == 4:

			mcf.move_player(players)
			rw.write_player_data(players)
			menu_option = int(input("Menu option: "))

		#edit player position
		elif menu_option == 5:

			mcf.change_position(players, positions)
			rw.write_player_data(players)
			menu_option = int(input("Menu option: "))

		#edit player stats
		elif menu_option == 6:

			mcf.edit_stats(players)
			rw.write_player_data(players)
			menu_option = int(input("Menu option: "))	

		else:
			print("Not a valid option. Please try again.")
			print()
			display_menu()
			print()
			menu_option = int(input("Menu option: "))
	print("Bye!")


if __name__=="__main__":
    main()