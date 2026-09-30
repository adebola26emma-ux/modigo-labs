def filter_and_group(catalog, required_tags, excluded_tags):
    # TODO: filter `catalog` by required_tags (must have all) and excluded_tags
    # (must have none), then group matching product names by category
    result = {}
    for item in catalog:
        name = item['name']
        category = item['category']
        tags = item['tags']
        check = True
        for tag in required_tags:
            if tag not in tags:
                check = False
        for tag in excluded_tags:
            if tag in tags:
                check = False
        if check: #All requirements satisfied
            if category not in result:
                result[category] = []
            result[category].append(name)
    return result

catalog = [{'name': 'Laptop', 'category': 'Electronics', 'tags': {'portable', 'new'}}, {'name': 'Desk', 'category': 'Furniture', 'tags': {'wooden'}}]

print(filter_and_group(catalog, {'portable'}, set()))
print(filter_and_group(catalog, set(), {'wooden'}))
print(filter_and_group(catalog, set(), set()))
print(filter_and_group(catalog, {'used'}, set()))
print(filter_and_group(catalog, {'wooden'}, set()))
