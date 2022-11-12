class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_album()

    def build_album(self):
        self.photos = []
        for _ in range(self.pages):
            self.photos.append([])
        return self.photos

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = int(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for row in range(len(self.photos)):
            if len(self.photos[row]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {row + 1} slot {self.photos[row].index(label) + 1}"
        return "No more free slots"

    def display(self):
        display_album = []
        for row in range(len(self.photos)):
            row_list = []

            for picture in self.photos[row]:
                row_list.append(f"[]")

            display_album.append(f'{" ".join(row_list)}')

        return f'{11 * "-"}\n' + f'\n{11 * "-"}\n'.join(display_album) + f'\n{11 * "-"}'


album = PhotoAlbum(3)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# # print(album.display())
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
print(album.display())
