class Music():
    def __init__(self,artist,track_title,album,year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year
    
    def __str__(self):
        return f"Performer: {self.artist} \n Title"