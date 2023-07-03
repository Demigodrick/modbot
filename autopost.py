from pythorhead import Lemmy
from pythorhead.types import FeatureType
from dotenv import dotenv_values
from datetime import date
import os

config = dotenv_values(".env")

print(".env loaded")
 
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"] 
INSTANCE = config["INSTANCE"]
COMMUNITY = config["COMMUNITY"]

today = date.today()
today_format = today.strftime("%B %d, %Y")
lemmy = Lemmy(INSTANCE)
lemmy.log_in(USERNAME, PASSWORD)

def load_pinned_posts():
        #open save file with IDs of posts and unpin them.
        save = open("save.file","r")
        count = 0

        while True:
                count += 1
                line = save.readline()
                if not line:
                        break
                post_id = line.rstrip()        
                lemmy.post.feature(int(post_id), False, FeatureType.Community)
                print("Post " + post_id + " unpinned.")
        save.close()
        
        os.remove("save.file")
        open("save.file",'a').close()



def weekly_home_post():      
        #get community ID here based on name
        # UNCOMMENT THE NEXT LINE FOR TESTING AND COMMENT OUT ACTUAL INSTANCE
        #community_id = lemmy.discover_community(COMMUNITY)
        community_id = lemmy.discover_community("Home")
        
        #debug
        print("Creating Weekly Thread in Home", today_format)
        
        home_output = lemmy.post.create(community_id,name="Lemmy.zip Weekly Chat - " + today_format,body="Hey there, this is the weekly thread for all general topics and any questions. You can also join us on [Matrix](https://matrix.to/#/#lemmy.zip:matrix.org) for a chat!")

        post_id = home_output['post_view']['post']['id']

        #use .local for local pin or .community for community pin
        lemmy.post.feature(post_id, True, feature_type=FeatureType.Community)

        save = open("save.file","a")
        save.write(str(post_id)+"\n")
        save.close()

def weekly_gaming_post():

        #get community
        # UNCOMMENT THE NEXT LINE FOR TESTING AND COMMENT OUT ACTUAL INSTANCE
        #community_id = lemmy.discover_community(COMMUNITY)
        community_id = lemmy.discover_community("Gaming")
        
        #debug
        print("Creating Weekly Thread in Gaming", today_format)
        
        gaming_output = lemmy.post.create(community_id,name="What Are You Playing This Week? " + today_format + " edition",body="Hey there everybody! Weekly check-in time once again. So... What are you playing this week?")
        
        post_id = gaming_output['post_view']['post']['id']

        #use .local for local pin or .community for community pin
        lemmy.post.feature(post_id, True, feature_type=FeatureType.Community)

        save = open("save.file","a")
        save.write(str(post_id)+"\n")
        save.close()
