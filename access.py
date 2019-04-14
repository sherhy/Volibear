import shelve

with shelve.open("champions") as db:
    for key, val in db.items():
        print(key, val)
