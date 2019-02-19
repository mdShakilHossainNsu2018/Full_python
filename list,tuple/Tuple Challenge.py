# imelda = "more Mymme", "Imelda May", 2011, ((1, "one"), (2, "Two"), (3, "Three"), (4, "Four"))
# print(imelda)
# title, artist, year, details = imelda
#
# print(title)
# print(artist)
# print(year)
# for i in details:
#     track, title = i
#     print("\t number :{0} track: {1} ".format(track, title))

imelda = "more Mymme", "Imelda May", 2011, ([(1, "one"), (2, "Two"), (3, "Three"), (4, "Four")])
print(imelda)
imelda[3].append((5, "Five"))
title, artist, year, details = imelda
details.append((6, "Six"))
print(title)
print(artist)
print(year)
for i in details:
    track, title = i
    print("\t number :{0} track: {1} ".format(track, title))

