items = ["apple","banana","orange","apple","mango"]

Uniqe_items = set()
for item in items:
    if item in Uniqe_items:
        print("Duplicate:", item)
    else:
        Uniqe_items.add(item)
