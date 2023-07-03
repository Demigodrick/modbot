from pythorhead import Lemmy
from dotenv import dotenv_values
from datetime import date
from pythorhead.types import FeatureType


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

regex = r'(\"id\":\s\d+)'

def weekly_home_post():      
        #get community ID here based on name
        # UNCOMMENT THE NEXT LINE FOR TESTING AND COMMENT OUT ACTUAL INSTANCE
        community_id = lemmy.discover_community(COMMUNITY)
        #community_id = lemmy.discover_community("Home")
        
        #debug
        print("Creating Weekly Thread in Home", today_format)
        
        lemmy.post.create(community_id,name="Lemmy.zip Weekly Chat - " + today_format,body="Hey there, this is the weekly thread for all general topics and any questions. You can also join us on [Matrix](https://matrix.to/#/#lemmy.zip:matrix.org) for a chat!")

def weekly_gaming_post():

        #get community
        # UNCOMMENT THE NEXT LINE FOR TESTING AND COMMENT OUT ACTUAL INSTANCE
        community_id = lemmy.discover_community(COMMUNITY)
        #community_id = lemmy.discover_community("Gaming")
        
        #debug
        print("Creating Weekly Thread in Gaming", today_format)
        
        output = lemmy.post.create(community_id,name="What Are You Playing This Week? " + today_format + " edition",body="Hey there everybody! Weekly check-in time once again. So... What are you playing this week?")
        
        post_id = output['post_view']['post']['id']

        lemmy.post.feature(post_id, True, feature_type=FeatureType.Local)

