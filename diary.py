from datetime import date

today = date.today()
date_str = today.strftime('%B %d %Y')

entry = input('what\'s on your mind today dude?\r')

diary_file = open('diary.txt','a')
diary_file.write(date_str + '\n' + entry + '\n')
diary_file.close()

input('\nalright, this program will now terminate')