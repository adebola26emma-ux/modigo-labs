def search_products(products, min_price=None, max_price=None, required_tags=None, sort_by="name"):
    # TODO: handle the mutable default argument problem for required_tags.
    # Filter products by min_price, max_price, and required_tags (all optional),
    # then return sorted product names according to sort_by.
    price_result = {}
    result = []
    for product in products:
        check = True
        name = product['name']
        price = product['price']
        tags = product['tags']
        if min_price is not None and price < min_price:
            check = False
        if max_price is not None and price > max_price:
            check = False
        if required_tags is not None:
            if required_tags - tags != set():
                check = False
        if check:
            price_result[price] = name
            result.append(name)
    if sort_by == 'name':
        return sorted(result)
    result = []
    price_result = dict(sorted(price_result.items()))
    for value in price_result.values():
        result.append(value)
    return result

products = [{'name': 'Mug', 'price': 10, 'tags': {'kitchen'}}, {'name': 'Lamp', 'price': 25, 'tags': {'lighting'}}]

print(search_products(products, min_price=15))
print(search_products(products, required_tags={'kitchen'}))
print(search_products(products, sort_by='price'))
print(search_products(products))