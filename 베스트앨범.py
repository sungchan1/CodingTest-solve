class TOP :
    def __init__(self):
        self.first_id = -1
        self.first_plays = -1 
        self.second_id = -2
        self.second_plays = -2
        self.result = [self.first_id, self.second_id]
    
    def input(self,id, playTimes):
        if playTimes > self.first_plays :
            self.first_id = id
            self.first_plays = playTimes
                
        elif playTimes > self.econd_plays:
            self.second_id = id
            self.second_plays = playTimes
            self.result = [self.first_id, self.second_id]
            
    
    
def solution(genres, plays):
    
    set_genres = list(set(genres))
    answer = []
    dict_genres = { genre : TOP() for genre in set_genres}
    
    for i in range(len(genres)):
        dict_genres[genres[i]].input(i, plays[i])   
    
    
    print( dict_genres.values())
    playtiems_array=  sort([top.first_plays for top  in dict_genres.values()])
        
    
    for top in dict_genres.values() :

        if top.second_id != -2 :
            answer[playtiems_array.index(top.first_plays)] = top.result[0]
        
        else :
            answer[playtiems_array.index(top.first_plays)] = top.result[0]
        
        

    return answer