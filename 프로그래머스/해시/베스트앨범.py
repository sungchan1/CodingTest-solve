def solution(genres, plays):
    
    
    album = dict()
    number = 0
    limit = 2
    answer = list()


    for genre, playtime in zip(genres,plays):
        if genre in album :
            album[genre][0] += playtime 
            album[genre][1].append( [number , playtime] )
        else :
            album[genre] = [playtime , [[number, playtime]]]
        number += 1
        
    for key, value in album.items():
        value[1] = sorted(value[1], key=lambda x: (-x[1], x[0] )  )
    
    # album_sorted = sorted(album.values(), key=lambda x: (-x[1], x[0]))

    best_album = sorted ( album.values(), key=lambda x: (-x[0]))
    for best_songs in best_album:
        number = 0
        for song in best_songs[1]:
            if number == limit :
                break
            else :
                answer.append(song[0])
            number +=1
    
    return answer




import numpy as np

class TOP :
    def __init__(self):
        self.songs = list()
        self.songs_sorted = list()
        self.totalPlays = 0

    
    def input(self,id, playTimes):
        self.totalPlays += playTimes
        self.songs.append([id, playTimes])
        self.songs_sorted = sorted(self.songs, key=lambda x: (-x[1], x[0]))
    
        
        
        

    
# def solution(genres, plays):
    
#     set_genres = list(set(genres))
#     answer = [ 1 for x in range(len(set_genres))]
#     dict_genres = { genre : TOP() for genre in set_genres}
    
#     for i in range(len(genres)):
#         dict_genres[genres[i]].input(i, plays[i])   
    

#     playtiems_array=  [top.totalPlays for top  in dict_genres.values()]
#     playtiems_array.sort()
#     playtiems_array.reverse()
    
#     for top in dict_genres.values() :
#         if len(top.songs_sorted) > 1:
#             answer[playtiems_array.index(top.totalPlays)] = [top.songs_sorted[0][0], top.songs_sorted[1][0]]
#         else :
#             answer[playtiems_array.index(top.totalPlays)] = [top.songs_sorted[0][0]]
            
            
            
#     answer2 = np.array(answer).flatten().tolist()
#     print(answer2)

#     return answer2