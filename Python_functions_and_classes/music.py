"""This is a simple class function that when executed, gives information about a music artist: artist's name, profile and favourite music
   Favourite here is relative as it's based on my own preference.
"""


import webbrowser

class Music():
    def __init__ (self, artist_name, artist_profile, favourite_song):
        self.artist = artist_name
        self.profile = artist_profile
        self.favourite = favourite_song  
    
    def open_favourite(self):
        webbrowser.open(self.favourite)
        
    def open_profile(self):
        webbrowser.open(self.profile)