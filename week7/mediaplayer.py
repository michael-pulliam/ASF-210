
from tkinter.messagebox import NO


class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
    

    
class Playlist:
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def lter(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    
    def search(self, value):
        temp = self.head
        isFound = False
        while temp is not None:
            if temp.data == value:
                isFound = True
                break
            temp = temp.next
        return isFound
    
    def __init__(self):
        # Create an empty list.
        self.head = None
        self.tail = None
        self.count = 0
        
    # def iter(self):
    #     # Iterate through the list.
    #     current = self.head
    #     while current:
    #         val = (f'{current.title} by: {current.artist}')
    #         current = current.next
    #         yield val
            

        
    def addLast(self, title, artist) -> None:
        # Add a node at the end of the list
        new_node = Song(title, artist)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        
    def delete(self, title) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.title.lower() == title.lower():
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    # current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next       

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return f'{current.title} by: {current.artist}'
  


    def showPlaylist(self):
        for node in self.iter():
            print(str(node))   

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
currentPlaylist = Playlist()

# print(newSong.__getitem__(1))
def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

    currentPlaylist.showPlaylist()
    print(currentPlaylist.count)

while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
       
        input1 = input("Input Song Title: ")
        input2 = input("Input Song Artist Name: ")
        currentPlaylist.addLast(input1, input2)
        # Add song to playlist
        
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title
        input1 = input("Enter Title to Delete: ")
        currentPlaylist.delete(input1) 
        # remove song from playlist
        print("Song Removed from Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        print(currentPlaylist.__getitem__(0))        
    elif choice == 4:
        # Skip to the next song on the playlist
        currentSong = currentPlaylist.head
        print("Skipping....")  
        print("Now Playing....")  
        print(f'{currentSong.next.title} by: {currentSong.next.artist}')
        if currentSong.next == None:
            print("End Of Playlist...")
        else:
            currentPlaylist.head = currentPlaylist.head.next
        # Display song name that is now playing
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
    elif choice == 0:
        print("Goodbye.")
        break



# newSong.addFirst("You Should Know", "Vin Jay & Adkoh")
# newSong.addLast("Leedle Leedle Lee", "TrippyTheKid")

# newSong = Playlist()

# newSong.addFirst("You Should Know", "Vin Jay & Adkoh")



# print(newSong[0].title)
    # def setNextNode(self, node):
    #     self.next = node
    
    # def getNextNode(self):
    #     return self.next
    
    # def setPrevNode(self, node):
    #     self.prev = node
    
    # def getPrevNode(self):
    #     return self.prev            

