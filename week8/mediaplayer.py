
        
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
    
    def __str__(self):
        return self.title + " by " + self.artist 
    

    
class Playlist:
    
    def __init__(self):
        # Create an empty list.
        self.head = None
        self.tail = None
        self.count = 0
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def playFromBeginning(self):

        return f'{self.head.title} by: {self.head.artist}' 
        
    
    def insertAtBeginning(self, title, artist):
        new_node = Song(title, artist)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def search(self, value):
        temp = self.head
        isFound = False
        while temp is not None:
            if temp.title or temp.artist == value:
                isFound = True
                break
            temp = temp.next
        return isFound

    def insertAtEnd(self, title, artist):
        new_node = Song(title, artist)
        if self.isEmpty():
            self.insertAtBeginning(title, artist)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp
    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next = None
            temp.previous = None
                       
    def delete(self, title):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            if self.head.title == title:
                self.head = None
        else:
            temp = self.head
            while temp is not None:
                if temp.title == title:
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                self.deleteFromLast()
            else:
                temp.next = temp.previous.next
                temp.next.previous = temp.previous
                temp.next = None
                temp.previous = None
            
    def printPlayList(self):
        temp = self.head
        while temp is not None:
            print(temp.title + " by: " + temp.artist)
            temp = temp.next
            
    def printNowPlaying(self):
        temp = self.head
        print(temp.title + " by: " + temp.artist)
    
    def printNextSong(self):
        temp = self.head.next
        print(temp.title + " by: " + temp.artist)
        
    def printPrevSong(self):
        temp = self.head.prev
        print(temp.title + " by: " + temp.artist)

        
    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        

        

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
currentPlaylist = Playlist()

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

    currentPlaylist.__str__()
while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        input1 = input(f'Add New Title: ')
        input2 = input(f'And Artist Name: ')
        currentPlaylist.insertAtBeginning(input1, input2)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        input1 = input('REMOVE SONG: Enter Title: ')
        # remove song from playlist
        currentPlaylist.delete(input1)
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....")
        print(currentPlaylist.playFromBeginning())
             
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")
        print(currentPlaylist.printNextSong())                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")
        print(currentPlaylist.printPrevSong())  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ")
        print(currentPlaylist.printNowPlaying())   
    elif choice == 8:
        # Show the current song list order
        
        print("\nSong list:\n")
        print(currentPlaylist.printPlayList())
    elif choice == 0:
        print("Goodbye.")
        break

            
