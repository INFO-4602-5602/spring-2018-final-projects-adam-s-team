file = open('ask_academia.csv', 'r')
subreddit_1_lines = file.readlines()[1:]

file = open('ask_historians.csv', 'r')
subreddit_2_lines = file.readlines()[1:]

file = open('ask_men.csv', 'r')
subreddit_3_lines = file.readlines()[1:]

file = open('ask_science.csv', 'r')
subreddit_4_lines = file.readlines()[1:]

file = open('ask_socialscience.csv', 'r')
subreddit_5_lines = file.readlines()[1:]

file = open('ask_women.csv', 'r')
subreddit_6_lines = file.readlines()[1:]

subreddit_lines = [subreddit_1_lines, subreddit_2_lines, subreddit_3_lines, subreddit_4_lines, subreddit_5_lines, subreddit_6_lines]

max_karma = 51
for i in range(max_karma):

	out_file = open('../' + str(i) + '.csv', 'w')
	out_file.write('subreddit,above,below\n')

	above = 0
	below = 0
	for line in subreddit_1_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Academia,' + str(above) + ',' + str(below) + '\n')

	above = 0
	below = 0
	for line in subreddit_2_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Historians,' + str(above) + ',' + str(below) + '\n')

	above = 0
	below = 0
	for line in subreddit_3_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Men,' + str(above) + ',' + str(below) + '\n')

	above = 0
	below = 0
	for line in subreddit_4_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Science,' + str(above) + ',' + str(below) + '\n')

	above = 0
	below = 0
	for line in subreddit_5_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Social_Science,' + str(above) + ',' + str(below) + '\n')

	above = 0
	below = 0
	for line in subreddit_6_lines:
		line = line.replace(' ', '').replace('\n', '').split(',')
		karma_value = int(line[3])
		if karma_value >= i:
			above = above + 1
		else:
			below = below + 1

	out_file.write('Ask_Women,' + str(above) + ',' + str(below) + '\n')

	out_file.close()