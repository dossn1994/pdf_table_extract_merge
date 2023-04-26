Pdf Table Extract and Merge Csv..Python Console:

1.Make sure Python and Java is installed and path variable is set.
2.Packages to be installed before running the python script:
  *Tabule - input command(pip install tabula-py)
  *Pypdf2 - input command(pip install PyPDF2==2.12.1)
  *Pandas - input command(pip install pandas)
  *Glob   - input command(pip install glob2)
  
  Install all the packages in cmd using command prompt.
 
 #After the script is executed it will show two options:
 1.EXTRACT_TABLES_FROM_PDF
 2.2:MERGE_CSV_FILE
 
#To extract tables give the input as 1.

#then it will ask for pdf filename which is to be extracted.
#Then give the folder name as input.if the given folder name is already present the csv files will be extracted in that folder.if not the folder will 
be created newly and files will be extracted to that folder.

note:the pdf file and python script should be in the same directory.

====================================================================================
#To merge csv give the input as 2.

#It will ask for the folder name where the file exist which is to be merged.
#then it will ask for the file name.
#then it will also ask for the output folder name where the output file will moved.

Note:to merge csv the csv file should have similar name.it should match to an extent.

eg: if the input filename is given as csv_file.
it will merge names like csv_file... csv_file1,csv_file2 etc.

the datatype and column count should be the same to merge. 

=========================================================================================================================================================================