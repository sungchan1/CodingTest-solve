from sys import stdin as s
# s =open("input.txt","r")
site_number, search_number= map(int, s.readline().split())
site_passwords = {}

for i in range(site_number):
    site, password = s.readline().split()
    site_passwords[site]= password

for i in range(search_number):
    print(site_passwords[s.readline().rstrip()])
    

