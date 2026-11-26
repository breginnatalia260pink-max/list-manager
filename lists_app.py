def add_item(items, item):
    items.append(item)

def remove_item(items, item):
    if item in items:
        items.remove(item)

def show_items(items):
    print(items)
