def all_unique_tags(posts):
    tags = []
    for post in posts:
        for tag in post['tags']:
            tags.append(tag)
    return set(tags)

print(all_unique_tags([{'title': 'A', 'tags': ['python', 'web']}, {'title': 'B', 'tags': ['web', 'css']}]))
