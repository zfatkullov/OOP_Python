class Playlist:
    def __init__(self,name):
        self.name = name
        self._tracks = []

    def _check_track(self, track):
        if not isinstance(track, str):
            raise TypeError
        if not track.strip():
            raise ValueError

    def add(self, track):
        self._check_track(track)
        self._tracks.append(track)

    def __len__(self):
        return len(self._tracks)

    def __getitem__(self, item):
        return self._tracks[item]

    def __setitem__(self, key, value):
        self._check_track(value)
        self._tracks[key] = value

    def __delitem__(self, key):
        del self._tracks[key]

    def __contains__(self, item):
        return item in self._tracks

    def __iter__(self):
        return iter(self._tracks)

    def __repr__(self):
        return f'Playlist({self.name!r}, tracks={len(self._tracks)})'

p = Playlist("Rock")
p.add("Song A"); p.add("Song B"); p.add("Song C")
print(len(p))         # 3
print(p[0], p[-1])    # Song A Song C
print(p[1:3])         # ['Song B', 'Song C']
print("Song B" in p)  # True
p[0] = "Song X"
del p[1]
for t in p:
    print(t)          # Song X, Song C
print(p)              # Playlist('Rock', tracks=2)