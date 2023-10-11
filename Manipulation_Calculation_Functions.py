#### Manipulation and Calculation Functions ########

#get at bats & hits w/ validation
def get_at_bats_and_hits():
	while True:
		at_bats = int(input("At bats: "))
		if at_bats < 0 or at_bats > 1000:
			print('Please enter a number between 1 and 1000.')
			continue
		break
	while True:
		num_hits = int(input("Hits: "))
		if num_hits > at_bats or num_hits < 0:
			print('Please enter a number of hits that is\n more than 0 but less than the at bats.')
			continue
		break
	return at_bats, num_hits

#calc batting average
def calc_batting_average(num_hits, at_bats):
	average = round(num_hits / at_bats, 3)
	return average

#display lineup
def display_lineup(players):
	print('		Player		POS	AB	H	AVG')
	print('-' * 60)
	for i, player in enumerate(players, start=1):
		print(f"{i}		{player[0]}		{player[1]}	{player[2]}	{player[3]}	{player[4]}\n")

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
			print('C, 1B, 2B, 3B, SS, LF, CF, RF, P')
			continue
	
	at_bats, num_hits = get_at_bats_and_hits()
	average = calc_batting_average(num_hits, at_bats)

	new_player = [name, player_position, at_bats, num_hits, average]
	players.append(new_player)
	print(f"{name} was added.")

#delete player
def delete_player(players):
	while True:
		index = int(input('Lineup number: '))
		if index < 1 or index > len(players):
			print('There is no player in that lineup number try again.')
			continue
		else:
			index -= 1
			print(f'{players[index][0]} was selected.')
			choice = input('Remove from lineup? y or n: ').upper()

			if choice == 'Y':
				print(f'{players[index][0]} was deleted.')
				players.pop(index)
			elif choice == 'N':
				print('Please select different player.')
				continue
			else:
				print('Invalid choice please select different player.')
				continue
			break
#move player
def move_player(players):
	while True: 
		index = int(input('Current Lineup Number: '))
		if index < 1 or index > len(players):
			print('There is no player in that lineup number try again.')
			continue
		else:
			print(f'{players[index - 1][0]} was selected.')
			new_index = int(input('New lineup number: '))

			if new_index < 1 or new_index > len(players):
				print('Invalid lineup number please try again.')
				continue
			else:
				temp = players.pop(index - 1)
				players.insert(new_index - 1, temp)

			print(f'{players[index][0]} was moved.')
			break


#change player position
def change_position(players, positions):
	while True:
		player = int(input('Player lineup number: '))
		if player < 1 or player > len(players):
			print('There is no player in that lineup number try again.')
			continue
		else:
			print(f'{players[player - 1][0]} was selected.')
			print(f'Current position is {players[player - 1][1]}')
			new_position = input('Enter new position: ').upper()

			if new_position in positions:
				players[player - 1][1] = " " + new_position
				break
			else:
				print('Invalid position. Try again.')
				print('POSITIONS')
				print('C, 1B, 2B, 3B, SS, LF, CF, RF, P')
				continue
	print(f'{players[player - 1][0]}\'s position has been changed.')

#edit player stats
def edit_stats(players):
	while True:
		player = int(input('Player lineup number: '))
		if player < 1 or player > len(players):
			print('There is no player in that lineup number try again.')
			continue
		else:
			print(f'You selected{players[player - 1][0]}, AB = {players[player - 1][2]} H = {players[player - 1][3]}')
			print('Enter new stats')
			at_bats, num_hits = get_at_bats_and_hits()
			average = calc_batting_average(num_hits, at_bats)

			players[player - 1][2] = at_bats
			players[player - 1][3] = num_hits
			players[player - 1][-1] = average

			print(f'{players[player - 1][0]} was updated')
			break
