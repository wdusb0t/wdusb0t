import praw
import time
import os
import random

def bot_login():
	print("Loggin in...")
	r = praw.Reddit(username = "CMBDeletebot",
			password = "LigmaBalls",
			client_id = "sqngcD_LbkMnug",
			client_secret = "pdOZ5JrUVUTSU_sq9tWpsQx4u6I",
			user_agent = "Corrector and Reference Bot")
	print("Logged in!")

	return r


def run_bot(r, comments_replied_to, comment_count):

        try:
                print("Obtaining 10000 comments...")

                randomcomment = "null"
                        
                if randomcomment == "null":
                        for comment in r.subreddit('all').comments(limit=1):
                                randomcomment = comment.body

                for comment in r.subreddit('all').comments(limit=10000):

                        if "what happened?" in comment.body.lower() or comment.author == "BooCMB" or comment.author == "CommonMisspellingBot" and comment.id not in comments_replied_to and comment.author != r.user.me(): 
                                print("String by \"BooCMB\" or with \"what happened?\" found in comment " + comment.id)
                                comment.reply(randomcomment)
                                print("Replied to comment " + comment.id)
                                
                                comments_replied_to.append(comment.id)


                                with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")

                        
                        if "ligma" in comment.body.lower() and comment.id not in comments_replied_to and comment.author != r.user.me():
                                print("String with \"ligma\" found in comment " + comment.id)
                                comment.reply("Ligma Balls!")
                                print("Replied to comment " + comment.id)
                                
                                comments_replied_to.append(comment.id)


                                with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")

                        if "t series" in comment.body.lower() and comment.id not in comments_replied_to and comment.author != r.user.me():
                                print("String with \"t series\" found in comment " + comment.id)
                                comment.reply("Don't even mention that name.")
                                print("Replied to comment " + comment.id)
                                
                                comments_replied_to.append(comment.id)


                                with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")
                                




                        #if "fuck" in comment.body.lower() and len(comment.body) < 100 and comment.id not in comments_replied_to and comment.author != r.user.me():
                               # print("String with \"fuck\" found in comment " + comment.id)
                               # comment.reply("> " + comment.body.lower().replace("fuck", "heck").replace("shit", "heck").replace("\n", "\n> ") + "\n\n\nFTFY")
                               # print("Replied to comment " + comment.id)
                                
                               # comments_replied_to.append(comment.id)


                               # with open ("comments_replied_to.txt", "a") as f:
                               #         f.write(comment.id + "\n")

                        #if "shit" in comment.body.lower() and len(comment.body) < 100 and comment.id not in comments_replied_to and comment.author != r.user.me():
                               # print("String with \"shit\" found in comment " + comment.id)
                              #  comment.reply("> " + comment.body.lower().replace("fuck", "heck").replace("shit", "heck").replace("\n", "\n> ") + "\n\n\nFTFY")
                              #  print("Replied to comment " + comment.id)
                                
                               # comments_replied_to.append(comment.id)


                              #  with open ("comments_replied_to.txt", "a") as f:
                               #         f.write(comment.id + "\n")

                        if "f" == comment.body.lower() and comment.id not in comments_replied_to and comment.author != r.user.me():
                                print("String with \"F\" found in comment " + comment.id)
                                comment.reply("F")
                                print("Replied to comment " + comment.id)
                                
                                comments_replied_to.append(comment.id)


                                with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")

                        if comment.id not in comments_replied_to and comment.author == "BooBCMB":
                                print("String by \"BooBCMB\" found in comment " + comment.id)
                                comment.reply("Hey, BooBCMB, Most of them are actually pretty bad.  Also you should check your name, you may have unintentionally included something slightly profane in it.  \n\n Have a nice day!")
                                print("Replied to comment " + comment.id)
                                
                                comments_replied_to.append(comment.id)


                                with open ("comments_replied_to.txt", "a") as f:
                                        f.write(comment.id + "\n")




                print("Sleeping for 10 seconds...")
                #Sleep for 10 seconds...
                time.sleep(10)
        except:
                print("Error Occurred.")
                with open ("comments_replied_to.txt", "a") as f:
                        f.write(comment.id + "\n")
        return comment_count

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = list(filter(None, comments_replied_to))

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

comment_count = 1

while True:
	run_bot(r, comments_replied_to, comment_count)
