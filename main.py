import spreadsheet
from mast import get_catalog_info, cols
import csv
import os

def main():
    # keyLine = 13
    startIndex = 15 

    # insertIndex = 12

    spreadsheet.init_service()
    # spreadsheet.fetch_spreadsheet()

    outputPath = "./output.tsv"
    if (os.path.exists(outputPath)):
        os.remove(outputPath)
    
    output = open(outputPath, 'a')

    key = "\t".join(cols)
    output.write(key + "\n")

    fileLength = sum(1 for _ in open('table.tsv', 'r'))

    with open('table.tsv', 'r') as table:
        rd = csv.reader(table, delimiter='\t')


        key = []
        index = 0
        rd = csv.reader(table, delimiter='\t')
        for row in rd:
            index += 1
            if index > startIndex - 1:
                print("Writing TIC %s [%s/%s]" % (row[0], index - startIndex, fileLength))
                output.write("\t".join([str(i) for i in get_catalog_info(row[0])]) + "\n")

        output.close()

        #spreadsheet.insert_sheet(outputPath)
        print("Done!")
main()