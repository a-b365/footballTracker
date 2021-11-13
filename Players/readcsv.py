import csv

from Players.models import PlayerData


with open("players.csv") as f:

	csv_reader=csv.reader(f,delimiter=',')
	line_count=0

	for row in csv_reader:

		if line_count==0:

			line_count+=1

		else:


			p=PlayerData(player_name=str(row[0]),player_position=str(row[1]),age=row[2],player_height=row[3],player_weight=row[4],player_nationality_id=row[5])

			p.save()

			line_count+=1

	print(f'Processed {line_count} lines.')



	