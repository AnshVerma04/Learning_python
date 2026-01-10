itemm ={"apple","banana","mango","watermelon","watermelon","apple"}

Uniqe_item = set()
for item in itemm:
    if item in Uniqe_item:
        print("Duplicate",items)
    else:
        Uniqe_item.add(item)