import os
import time
import logging
from mastodon import Mastodon
from dotenv import load_dotenv
from functools import wraps

# Load environment variables
load_dotenv()

MASTODON_ACCESS_TOKEN = os.getenv( "MASTODON_ACCESS_TOKEN" )
MASTODON_API_BASE_URL = os.getenv( "MASTODON_API_BASE_URL" )

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a Mastodon instance
mastodon = Mastodon(access_token=MASTODON_ACCESS_TOKEN, api_base_url=MASTODON_API_BASE_URL)

# Writen by Ashish
# Decorator to handle rate-limiting and other retries
def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        retries = 3  # Number of retries before giving up
        for attempt in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error encountered: {e}")
                if "rate limit exceeded" in str(e).lower() and attempt < retries - 1:
                    logger.warning(f"Rate limit exceeded, retrying in 60 seconds... (Attempt {attempt + 1})")
                    time.sleep(60)  # Sleep for 60 seconds before retrying
                    continue
                logger.error("Max retries reached or non-rate-limited error occurred.")
                raise
    return wrapper

# Writen by Gabriel
# Retrieve all user posts from Mastodon
@handle_errors
def user_posts(instance):
    try:
        user_posts = instance.account_statuses(instance.me())
        user_posts = [x['id'] for x in user_posts]
        return user_posts
    except Exception as e:
        logger.error(f"Failed to retrieve user posts: {e}")
        raise

# Writen by Gabriel
# Post content to Mastodon
@handle_errors
def post(content, instance):
    try:
        status = instance.status_post(content)
        return status['id']
    except Exception as e:
        logger.error(f"Failed to post content: {e}")
        raise

# Writen by Matthew
# Retrieve a specific status by ID
@handle_errors
def retrieve(id, instance):
    try:
        status = instance.status(id)
        return status['content']
    except Exception as e:
        logger.error(f"Failed to retrieve status: {e}")
        raise

# Writen by Matthew
# Delete a specific status by ID
@handle_errors
def delete(id, instance):
    try:
        status = instance.status_delete(id)
        return status['content']
    except Exception as e:
        logger.error(f"Failed to delete status: {e}")
        raise
