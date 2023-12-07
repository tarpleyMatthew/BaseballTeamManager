#### Manipulation and Calculation Functions ########
from datetime import date,datetime
from objects.Player import Player 
import db.DbAccess as db

#get date
def get_date():
    today = date.today()

    while True:
        print(f'CURRENT DATE:    {today}')
        date_input = input("GAME DATE (yyyy-mm-dd):    ")

        if not date_input.strip():
            print('No date entered')
            return 

        try:
            game_date = datetime.strptime(date_input, '%Y-%m-%d').date()

            if game_date <= today:
                print('Please enter a future date.')
                continue

            days_until_game = (game_date - today).days
            print(f'DAYS UNTIL GAME:    {days_until_game}')
            break

        except ValueError:
            print('Incorrect date format. Please enter the date in yyyy-mm-dd format.')
            continue


#get at bats & hits
def get_at_bats_and_hits():
	while True:
		try:
			at_bats = int(input("At bats: "))
			if at_bats < 0 or at_bats > 1000:
				print('Please enter a number between 0 and 1000.')
				continue
			break
		except:
			print('Invalid integer. Try again')
			continue
	while True:
		try:
			num_hits = int(input("Hits: "))
			if num_hits > at_bats or num_hits < 0:
				print('Please enter a number of hits that is\nat least 0 but less than at bats.')
				continue
			break
		except:
			print('Invalid integer. Try again')
			continue
	return at_bats, num_hits

#calculate batting average
def calc_batting_average(num_hits, at_bats):
	num_hits = float(num_hits)
	at_bats = float(at_bats)
	try:
		average = format(num_hits / at_bats, '.3f')
	except ZeroDivisionError:
		print('cannot divide by zero, average will be 0.')
	return average

#display lineup
def display_lineup(lineup):
    header = f"{'':<8}{'Player':<20}{'POS':<7}{'AB':<5}{'H':<3}{'AVG'}"
    print(header)
    print('-' * 46)
    
    for i, player in enumerate(lineup.get_all_players(), start=1):
        full_name = player.getFullName()
        position = player.position
        at_bats = player.atBats
        hits = player.hits
        average = player.getAverage()
        
        print(f"{i:<2}      {full_name:<20} {position:<7} {at_bats:<5} {hits:<3} {average}")


#add player
def add_player(lineup, positions):
    first_name = input('First name:')
    last_name = input('Last name:')

    while True:
        position = input('Position: ').upper()
        if position in positions:
            break
        else:
            print('Invalid position. Try again.')
            print('POSITIONS')
            for p in positions:
                print(f"'{p}", end=' ')
            continue
    
    at_bats, num_hits = get_at_bats_and_hits()
    bat_order = len(lineup.get_all_players()) + 1
    #average = calc_batting_average(num_hits, at_bats)

    player = Player(bat_order, first_name, last_name, position, at_bats, num_hits)
    db.add_player(player)

#    new_player = {
#        "Position": player.position,
#        "At Bats": player.atBats,
#        "Hits": player.hits,
#        "Average": player.getAverage()
#    }

#    players[player.getFullName()] = new_player
    print(f"{player.getFullName()} was added.")


#delete player
def delete_player(lineup):
    while True:
        try:
            index = int(input('Lineup number: '))
        except:
            print('Invalid integer. Please try again.')
            continue

        if index < 1 or index > len(lineup.get_all_players()):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = lineup.get_player_at_index(index - 1) 

            print(f'{selected_player.getFullName()} was selected.')
            choice = input('Remove from lineup? (Y or N): ').upper()

            if choice == 'Y':
                db.delete_player(index)
                print(f'{selected_player.getFullName()} was deleted.')
            elif choice == 'N':
                print('Please select a different player.')
                continue
            else:
                print('Invalid choice. Please select a different player.')
                continue
            break

#move player
def move_player(lineup):
    #player_items = list(players.items())

    while True:
        try:
            index = int(input('Current lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue

        if index < 1 or index > len(lineup.get_all_players()):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = lineup.get_player_at_index(index - 1)
            print(f'{selected_player.getFullName()} was selected.')

            try:
                new_index = int(input('New lineup number: '))
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
                continue

            if new_index < 1 or new_index > len(lineup.get_all_players()):
                print('Invalid lineup number. Please try again.')
                continue
            else:
                print(index,new_index)
                db.move_player(index, new_index)
                #.insert(new_index - 1, selected_player)
                #reordered_players = dict(player_items)

                print(f'{selected_player.getFullName()} was moved to position {new_index} in the lineup.')
                break

#change player position
def change_position(lineup, positions):
    while True:
        try:
            player = int(input('Player lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue 
        
        #player_names = list(players.keys())

        if player < 1 or player > len(lineup.get_all_players()):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = lineup.get_player_at_index(player - 1)
            print(f'{selected_player.getFullName()} was selected.')

            print(f'Current position is {selected_player.position}')
            new_position = input('Enter new position: ').upper()

            if new_position in positions:
                db.update_position(new_position, selected_player.batOrder)
               #players[selected_player]["Position"] = new_position
                print(f'{selected_player.getFullName()}\'s position has been changed to {new_position}.')
                break
            else:
                print('Invalid position. Try again.')
                print('POSITIONS')
                for p in positions:
                    print(f"'{p}", end=' ')
                continue

#edit player stats
def edit_stats(lineup):
    while True:
        try:
            player = int(input('Player lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue 
        
        #player_names = list(players.keys())

        if player < 1 or player > len(lineup.get_all_players()):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = lineup.get_player_at_index(player - 1)
            print(f'You selected {selected_player.getFullName()}, AB = {selected_player.atBats} H = {selected_player.hits}')
            print('Enter new stats')
            at_bats, num_hits = get_at_bats_and_hits()
            #average = calc_batting_average(num_hits, at_bats)

            #players[selected_player]["At Bats"] = at_bats
            #players[selected_player]["Hits"] = num_hits
            #players[selected_player]["Average"] = average

            db.update_stats(at_bats, num_hits, selected_player.batOrder)
            print(f'{selected_player.getFullName()}\'s stats were updated.')
            break
