import facebook_scraper as fs
import time
import random
import logging
import json

# with open('./mbasic_header.json', 'r') as file:
#     fs._scraper.mbasic_headers = json.load(file)

fs.enable_logging(logging.INFO)
page_start = 6
page_number = 5
post_per_page = 100

for i in range(page_start, page_start + page_number + 1):
    fs.write_posts_to_csv(
        base_url="https://mbasic.facebook.com",
        group='x', # The method uses get_posts internally so you can use the same arguments and they will be passed along
        cookies='cookies2.txt',
        page_limit=post_per_page,
        timeout=60,
        options={
            'progress': False,
            'comments': False,
            'reactors': False,
            'allow_extra_requests': False,
            # 'whitelist_methods': [
            #     'extract_post_url',
            #     'extract_text',
            #     'extract_time',
            #     'extract_image_lq',
            #     'extract_likes',
            #     'extract_comments',
            #     'extract_shares',
            #     'extract_username',
            #     'extract_video',
            #     'extract_video_thumbnail',
            #     'extract_is_live',
            #     'extract_share_information',
            # ]
        },
        filename=f'./data/messages_{i}.csv', # Will throw an error if the file already exists
        resume_file='next_page.txt', # Will save a link to the next page in this file after fetching it and use it when starting.
        matching='.+', # A regex can be used to filter all the posts matching a certain pattern (here, we accept anything)
        not_matching='^Warning', # And likewise those that don't fit a pattern (here, we filter out all posts starting with "Warning")
        # keys=[
        #     'post_url',
        #     'username',
        #     'time',
        #     'post_text',
        #     #'text', #combination of post and shared, if shared
        #     #'original_text', #only for translated
        #     'reaction_count',
        #     'likes',
        #     'comments',
        #     'shares',
        #     'image_lowquality',
        #     'video',
        #     'video_thumbnail',
        #     'is_live',
        #     'was_live',
        #     'shared_text',
        #     'shared_username',
        #     'shared_post_url',
        # ], # List of the keys that should be saved for each post, will save all keys if not set
        format='csv', # Output file format, can be csv or json, defaults to csv
        days_limit=3650 # Number of days for the oldest post to fetch, defaults to 3650
    )
    print(f'Done page {i}...')
    time.sleep(random.randint(2, 5))

