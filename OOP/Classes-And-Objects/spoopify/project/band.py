from project.album import Album

class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []


    def add_album(self, album: Album):

        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):

        try:
            album = next(filter(lambda a: a.name == album_name,self.albums))
            if album.published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album)
            return f"Album {album.name} has been removed."
        except StopIteration:
            return f"Album {album_name} is not found."

    def details(self):
        info = f'Band {self.name}\n'
        info += '\n'.join([f'{album.details()}' for album in self.albums])
        return info


