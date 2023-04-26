import tabula
import pandas as pd
import glob
import os
import PyPDF2


def extract_table():
 file_name = input('Enter the file name : ')
 reader = PyPDF2.PdfFileReader(file_name)
 num_pages = reader.getNumPages()
 file_name_csv = file_name.replace('.pdf','')
 output_folder_name = input('Enter the Output folder name : ')
 if not os.path.exists(f"{output_folder_name}"):
  os.makedirs(f'{output_folder_name}')
 for page_number in range(1,num_pages+1):   
  tables = tabula.read_pdf(file_name,pages=f'{page_number}',multiple_tables = True,lattice=True)
  if len([n for n in tables]) > 0:
   for i,df in enumerate(tables, start=1):
    error = ['Unnamed:', '.1']
    pattern = '|'.join(error)
    only_na= df.isna().all(axis='rows') # get all rows which contain only nas
    unnamed_col= only_na.index.str.contains(pattern) # get all rows which got a generic name Unnamed...
    unnamed_col&= only_na                                             
    df.drop(columns=only_na[unnamed_col].index, inplace = True) # now delete all columns which got no explicit name and only contain nas
    cols=df.columns[~df.columns.str.contains(pattern)]
    df2=df.iloc[:,:len(cols)]
    df2.columns = cols
    df2.to_csv(f"{output_folder_name}/{file_name_csv}_page_{page_number}_table_{i}.csv", index = False)

  

def merge_csv():
 foldername = input("ENTER THE input folder name: ")
 filename = input("ENTER THE FILENAME: ")
 files = f"{foldername}/{filename}*.csv"

 files = glob.glob(files)
 
 df = pd.concat(map(pd.read_csv, files), ignore_index = True)
 #outputfilename = filename.replace(".csv", "")
 outputfilename = input("ENTER THE OUTPUT FILENAME: ")
 output_folder_name = input("ENTER THE Output folder name: ")
 
 if not os.path.exists(f"{output_folder_name}"):
  os.makedirs(f"{output_folder_name}")
 
 df.to_csv(f'{output_folder_name}/{outputfilename}.csv',index = False)
 

if __name__ == '__main__' :
 
 while True:
  print("\n1:EXTRACT_TABLES_FROM_PDF\n2:MERGE_CSV_FILE")
  print("\n---------------------------------")
  cmd = input("\nPlease input command: ")
  
  if cmd.strip() == '1':
   extract_table()
   exit()
   
  elif cmd.strip() == '2':
   merge_csv()
   exit()
  
  else:
   exit()