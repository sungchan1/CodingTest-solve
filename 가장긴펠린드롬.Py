# def checkPalindrome(buffer_stack, substring) :
#     if not buffer_stack:
#         return False 
#     if len(buffer_stack+substring) %2 == 0 and buffer_stack[::-1] == substring:
#         return True
#     elif len(buffer_stack+substring) %2 != 0 and buffer_stack[::-1] == substring[1:]:
#         return True
#     else:
#         return False
# def DFS(buffer_stack, substring):
#     # 끝까지 왔을 떄
#     if not substring :
#         return -1
#     # Palindrome 일때
#     if checkPalindrome(buffer_stack, substring) :
#         currentLen = len(buffer_stack+substring)
#     elif checkPalindrome(buffer_stack, substring[:len(buffer_stack)+1]) :
#         currentLen = len(buffer_stack) * 2 + 1
#     elif checkPalindrome(buffer_stack, substring[:len(buffer_stack)]) :
#         currentLen = len(buffer_stack) * 2
#     else :
#         currentLen = 1
#     pushed_stack = buffer_stack+substring[0]
#     poped_substring = substring[1:]
#     # print("---------",buffer_stack, " ",  substring, " ", currentLen)
#     # 가능성 체크
#     if ''.join(reversed(pushed_stack)) in poped_substring:
#         return max(currentLen,DFS(pushed_stack, poped_substring))
#     else :
#         return max(currentLen,DFS(substring[0], poped_substring))
# def solution(s):
#     answer = DFS(s[0], s[1:])
#     return answer


def solution(s):
    max_len=0
    for i in range (len(s)):
        for j in range(len(s)-1,i-1,-1):
            new_str = s[i:j+1]
            if max_len >= len(new_str):
                break
            if new_str == new_str[::-1]:
                max_len = max(max_len,len(new_str))

    return max_len