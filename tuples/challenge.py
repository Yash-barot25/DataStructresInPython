album = "More mayhm", "imelda more", 2011, (
    (1, "how are you"), (2, "doing well"), (3, "what about youself"), (4, "thanks"))

albumname, name, year, albums = album
print(albumname)
print(name)
print(year)
print(albums)
print(album[3])
track1, track2, track3, track4 = albums
print("Track number {}, name {}".format(track1[0], track1[1]))
print("Track number {}, name {}".format(track2[0], track2[1]))
print("Track number {}, name {}".format(track3[0], track3[1]))
print("Track number {}, name {}".format(track4[0], track4[1]))

album = "More mayhm", "imelda more", 2011, (
    [(1, "how are you"), (2, "doing well"), (3, "what about youself"), (4, "thanks")])

albumname, name, year, albums = album
print(albumname)
print(name)
print(year)
print(albums)
print(album[3])
albums.append((23, "last one"))
track1, track2, track3, track4, track5 = albums
print("Track number {}, name {}".format(track1[0], track1[1]))
print("Track number {}, name {}".format(track2[0], track2[1]))
print("Track number {}, name {}".format(track3[0], track3[1]))
print("Track number {}, name {}".format(track4[0], track4[1]))
print("Track number {}, name {}".format(track5[0], track5[1]))
