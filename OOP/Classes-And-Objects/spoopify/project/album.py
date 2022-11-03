from project.song import Song



class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name:str):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda s: s.name == song_name,self.songs))
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}."
        except StopIteration:
            return "Song is not in the album."


    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f'Album {self.name}\n'
        result += '\n'.join([f'== {song.get_info()}' for song in self.songs])
        result += '\n'
        return result
