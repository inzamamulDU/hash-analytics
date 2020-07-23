import pandas as pd # pip install pandas
import csv
import os

def xlsx_to_csv(filename):
  # Open workbook using pandas
  wb = pd.ExcelFile(filename)
  filename = os.path.splitext(filename)[0] # Remove .xlsx part of the main file
  if not os.path.exists(filename):
      os.makedirs(filename)
  # to read all sheets
  for sheet_name in wb.sheet_names:
    #excel to pandas dataframe for write into csv
    sh = pd.DataFrame()
    #parse single sheet for write
    sh = wb.parse(sheet_name)
    # Create a file for each sheet
    with open(filename + '/' + str(sheet_name)+'.csv','wb') as f:
      #convert it to csv format
      sh.to_csv(f, index= False)
      print "Exported workbook '%s' " % (sheet_name)
      #close the file
      f.close()

      
xlsx_to_csv('dummy.xlsx')
print "-------------------------------------------------------"
print "processing finished Succesfully"

print "Created By Inzamamul Alam Munna"

print "Global Intern Hash Analytics From bangladesh"
