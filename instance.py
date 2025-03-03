from mastodon import Mastodon
#create a mastodon instance
mastodon=Mastodon(access_token="pyNjksdzBcvVpOnCKcbSDQ8qgaimX21sxzXv9P7LwjM",api_base_url="https://mastodon.social")

#retrieve all of the user posts id from mastodon API (Writen by Gabriel)
def user_posts(instance):
    user_posts=instance.account_statuses(instance.me())
    user_posts=[x['id'] for x in user_posts]
    return user_posts
#use status_post() function from mastodon API to post data (Writen by Matthew)
def post(content,instance):
    status=instance.status_post(content)
    return status['id']
#use status() function from mastodon API to retrieve data (Writen by Matthew)
def retrieve(id,instance):
    status=instance.status(id)
    return status['content']
#use status_delete function from mastodon API to delete data (Writen by Matthew)
def delete(id,instance):
    status=instance.status_delete(id)
    return status['content']
