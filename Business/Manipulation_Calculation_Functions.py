#### Manipulation and Calculation Functions ########
from datetime import date,datetime

#get date
def get_date():
    today = date.today()

    while True:
        print(f'CURRENT DATE:    {today}')
        date_input = input("GAME DATE (yyyy-mm-dd):    ")

        if not date_input.strip():
            print('No date entered')
            return  # Exit the function if no date is provided

        try:
            # Check if the input matches the 'yyyy-mm-dd' format
            game_date = datetime.strptime(date_input, '%Y-%m-%d').date()

            # Validate that the entered date is in the future
            if game_date <= today:
                print('Please enter a future date.')
                continue

            # Calculate the difference in days
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
def display_lineup(players):
	print('		Player		POS	AB	H	AVG')
	print('-' * 64)
	for i, (player_name, player_data) in enumerate(players.items(), start=1):
		print(f"{i}		{player_name}		{player_data['Position']}	{player_data['At Bats']}	{player_data['Hits']}	{player_data['Average']}")

#add player
def add_player(players, positions):
	name = input('Name:')

	while True:
		player_position = input('Position: ').upper()
		if player_position in positions:
			break
		else:
			print('Invalid position. Try again.')
			print('POSITIONS')
			for p in positions:
				print(f"'{p}", end=' ')
			continue
	
	at_bats, num_hits = get_at_bats_and_hits()
	average = calc_batting_average(num_hits, at_bats)

	new_player = {
        "Position": player_position,
        "At Bats": at_bats,
        "Hits": num_hits,
        "Average": average
    }

	players[name] = new_player
	print(f"{name} was added.")

#delete player
def delete_player(players):
	while True:
		try:
			index = int(input('Lineup number: '))
		except:
			print('invalid integer. Please try again.')
			continue

		player_names = list(players.keys())

		if index < 1 or index > len(player_names):
			print('There is no player in that lineup number try again.')
			continue
		else:
			selected_player = player_names[index - 1]

			print(f'{selected_player} was selected.')
			choice = input('Remove from lineup? y or n: ').upper()

			if choice == 'Y':
				print(f'{selected_player} was deleted.')
				players.pop(selected_player)
			elif choice == 'N':
				print('Please select different player.')
				continue
			else:
				print('Invalid choice please select different player.')
				continue
			break
#move player
def move_player(players):
    player_items = list(players.items())

    while True:
        try:
            index = int(input('Current lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue

        if index < 1 or index > len(player_items):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = player_items.pop(index - 1)
            print(f'{selected_player[0]} was selected.')

            try:
                new_index = int(input('New lineup number: '))
            except ValueError:
                print('Invalid input. Please enter a valid integer.')
                continue

            if new_index < 1 or new_index > len(player_items) + 1:
                print('Invalid lineup number. Please try again.')
                continue
            else:
                player_items.insert(new_index - 1, selected_player)

                reordered_players = dict(player_items)

                print(f'{selected_player[0]} was moved to position {new_index} in the lineup.')
                return reordered_players

#change player position
def change_position(players, positions):
    while True:
        try:
            player = int(input('Player lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue 
        
        player_names = list(players.keys())

        if player < 1 or player > len(player_names):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = player_names[player - 1]
            print(f'{selected_player} was selected.')
            print(f'Current position is {players[selected_player]["Position"]}')
            new_position = input('Enter new position: ').upper()

            if new_position in positions:
                players[selected_player]["Position"] = new_position
                print(f'{selected_player}\'s position has been changed to {new_position}.')
                break
            else:
                print('Invalid position. Try again.')
                print('POSITIONS')
                for p in positions:
                    print(f"'{p}", end=' ')
                continue

#edit player stats
def edit_stats(players):
    while True:
        try:
            player = int(input('Player lineup number: '))
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
            continue 
        
        player_names = list(players.keys())

        if player < 1 or player > len(player_names):
            print('There is no player in that lineup number. Please try again.')
            continue
        else:
            selected_player = player_names[player - 1]
            print(f'You selected {selected_player}, AB = {players[selected_player]["At Bats"]} H = {players[selected_player]["Hits"]}')
            print('Enter new stats')
            at_bats, num_hits = get_at_bats_and_hits()
            average = calc_batting_average(num_hits, at_bats)

            players[selected_player]["At Bats"] = at_bats
            players[selected_player]["Hits"] = num_hits
            players[selected_player]["Average"] = average

            print(f'{selected_player}\'s stats were updated.')
            break
