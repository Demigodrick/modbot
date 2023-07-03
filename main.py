from autopost import load_pinned_posts, weekly_home_post, weekly_gaming_post


#define which posts to run
if __name__ == "__main__":
    load_pinned_posts() #keep this first
    weekly_home_post()
    weekly_gaming_post()
