#! /usr/bin/bash

import json
from blog.models import Post

with open('post.json') as file:
    post_json = json.load(file)

for post in post_json:
    post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
    post.save()
