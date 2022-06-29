beer_count = range(99, 0, -1);

for beer in beer_count:
    if beer == 1:
        print(f"Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(f"Take one down and pass it around, {beer - 1} bottles of beer on the wall.")
