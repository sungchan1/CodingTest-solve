# 내가 쓴 코드
def solution(phone_book):
    
    phone_book.sort()
    for number in range(len(phone_book) -1) : 
        if phone_book[number] == phone_book[number+1][:len(phone_book[number])] :
            return False


    return True


# 모범

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True