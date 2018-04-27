import praw
import pickle
from time import sleep
from time import time
from collections import defaultdict
from sys import argv

def get_opts(argv):
	opts = {}
	while argv:
		if argv[0][0] == '-':
			opts[argv[0]] = argv[1]
		argv = argv[1:]
	return opts


def pickle_out(filename, object_to_dump):
    with open(filename, 'wb') as pickleFile:
        pickle.dump(object_to_dump, pickleFile)
        pickleFile.close()


def scrape(num_iterations, sleep_time, num_iterations_to_update, subreddit):
    reddit = praw.Reddit(client_id='zE2MnpS9TOYsrA',
                         client_secret='LORNbmvqBtMRzoiniQK8dNLYRso',
                         user_agent='prob models')

    posts = {}
    posts_to_check = defaultdict(list)

    for iteration in range(num_iterations):
        user_count = reddit.subreddit(subreddit).active_user_count
        time_of_check = time()
        for submission in reddit.subreddit(subreddit).new(limit=999):
            id = submission.id
            if id not in posts:
                if time_of_check - submission.created_utc < sleep_time - 1:   #only posts created after the last sleep_time
                    # print(time_of_check-submission.created_utc, submission.title)
                    posts[id] = [submission.title, submission.score, submission.created_utc, user_count, -1]
                    posts_to_check[iteration+num_iterations_to_update].append(id)

        for id in posts_to_check[iteration]:
            post = reddit.submission(id=id)
            posts[id][4] = post.score  # 4 is the final score of the post

        print('iteration: ',iteration,', num posts collected: ',len(posts))
        pickle_out(subreddit+'_posts', posts)

        sleep(sleep_time)

    #then we check the last set of new posts
    for iteration in range(num_iterations, num_iterations+num_iterations_to_update):
        for id in posts_to_check[iteration]:
            post = reddit.submission(id=id)
            posts[id][4] = post.score  # 4 is the final score of the post

        print('iteration: ',iteration,', collecting final karma')
        pickle_out(subreddit+'_posts', posts)
        if iteration == num_iterations+num_iterations_to_update -1:	#we have finished updating
        	break
        sleep(sleep_time)

####################################
my_args = get_opts(argv)

scrape(num_iterations=336, sleep_time=3600, num_iterations_to_update=24, subreddit=my_args['-subreddit'])




