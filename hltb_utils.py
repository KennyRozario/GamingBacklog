from howlongtobeatpy import HowLongToBeat
import time
import logging

# Requires a file called games_list.txt consisting of a 
# game title per line. 
#
# This will create two files: hours.txt and scores.txt where
# each line maps to the line in games_list.txt for what the 
# filename suggests.
with open("games_list.txt", "r") as games_file:
    with open("hours.txt", "a") as hours_file:
        with open("scores.txt", "a") as scores_file:
            # cautionary rate-limt of 5 requests per second
            count = 5
            for line in games_file.readlines():
                if count == 0:
                    time.sleep(1)
                    count = 5

                game_title = line.title()
                logging.info(f"Searching for {game_title}")

                result = HowLongToBeat().search(game_title)[0]
                hours_file.write(f"{result.main_story}\n")
                scores_file.write(f"{result.review_score}\n")
                count -= 1
