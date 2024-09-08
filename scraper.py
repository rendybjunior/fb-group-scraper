from facebook_scraper import get_posts
import json

options={
    "progress": False,
    "comments": False,
    "reactors": False,
    "allow_extra_requests": False,
    # "posts_per_page": 2
}

fields = [
    'post_url',
    'username',
    'time',
    'post_text',
    #'text', #combination of post and shared, if shared
    #'original_text', #only for translated
    'reaction_count',
    'likes',
    'comments',
    'shares',
    'image_low_quality',
    'video',
    'video_thumbnail',
    'is_live',
    'was_live',
    'shared_text',
    'shared_username',
    'shared_post_url',
]

posts = get_posts(group="KomunitasEvermos", cookies="cookies2.txt", pages=1, options=options)
with open('posts.json', 'w') as file:
    for post in posts:
        new_post = {}
        for field in fields:
            new_post[field] = post.get(field)
        new_post['time'] = post['time'].isoformat()
        json.dump(new_post, file)
        file.write('\n')
