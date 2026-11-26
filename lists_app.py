def add_item(items, item):
    items.append(item)

def remove_item(items, item):
    if item in items:
        items.remove(item)

def show_items(items):
    print(items)
    
def count_items(items):
    return len(items)

def clear_items(items):
    items.clear()S

sample = ["a", "b"]
add_item(sample, "c")
show_items(sample)
