import webbrowser
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Scores").sheet1
#sheet.update_cell(2,2, "Hi")
print("Welcome to the Testing Portal")
print("======================================")
print("Instructions")
print("======================================")
print("1) Enter your Name, Class and Section carefully.\n2) Ensure that you have the question paper which will be provided by your teacher.\nDo not write anything in Roman numerals. Use only integers.\n4) Not following anyone of the instructions will lead to termination of your test or will result to wrong scores.")
ans_list = [11,12,13,14,15,16,17,18,19,20] # teacher will edit this answer list
insertRow = []
tot_prob = [] 
name = input("Enter your name: ")
insertRow.append(name)
class_n = int(input("Enter your class: "))
insertRow.append(class_n)
section = input("Enter your section: ")
insertRow.append(section)
q_n = len(ans_list)
for i in range(q_n):
  sheet.update_cell(1,4+i, "Problem {}".format(i+1))
  tot_prob.append(i+1)
i+=1
s = tot_prob[-1]
sheet.update_cell(1,3+s+1, "Score")
print("========================================")
print("Your test shall start in 10 seconds...")
time.sleep(10)
print("Enter your answers...")

response_list = []
for i in range(q_n):
  ans = int(input("Enter answer {}: ".format(i+1)))
  insertRow.append(ans)
  response_list.append(ans)


correct_list = [value for value in response_list if value in ans_list] 

marks = 5 #teacher will edit the marks alloted for each question; should be the same for all questions
score = len(correct_list)*5
insertRow.append(score)

sheet.insert_row(insertRow, 2) 

