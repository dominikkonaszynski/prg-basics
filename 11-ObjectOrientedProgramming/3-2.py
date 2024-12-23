class Music():
    def __init__(self,artist,track_title,album,year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f"Performer: {self.artist} \nTitle:     {self.track_title} \nAlbum:     {self.album} \nYear:      {self.year}"
    
def main():
    piece1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
    piece2 = Music("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)
    print(piece1)
    print(piece2)
        
if __name__ == "__main__":
    main()