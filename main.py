import pandas as pd
import xlrd
import sys

def main(argv):
    """
    param {String} input_filename
    param {String} output_filename
    """
    
    input_filename = argv[1]
    output_filename = argv[2]
    # since we want to parse multiple sheets from the file, keep it around for later
    xls = pd.ExcelFile(input_filename)
    sheet1 = xls.parse('Sheet1')
    
    print sheet1.info()
    print sheet1
    

if __name__ == '__main__':
    main(sys.argv)
