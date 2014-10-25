import pandas as pd
import xlrd

already_found = set()

def ifStringThenFilterByPrefix(x):
     if type(x) is unicode:
          if x[0:5] == '     ' and x[6] != ' ':
               if x not in already_found:
                   already_found.add(x)
                   print x
                   return True
     return False

def main():
    # since we want to parse multiple sheets from the file, keep it around for later
    xls = pd.ExcelFile('data/GDPbyInd_VA_NAICS_1947-1997.xls')
    _skip_rows = range(1, 94) + range(184, 370)
    already_found = set()
    sheet1 = xls.parse('1947-87_02NAICS_VA', header=0, index_col=1, skiprows=_skip_rows)
    top_level_industries = set()
    for entry in list(sheet1.index):
        if type(entry) is unicode:
          if entry[0:5] == '     ' and entry[6] != ' ':
               top_level_industries.add(entry)
               
    top_level_industries_data = sheet1.reindex_axis(top_level_industries, axis=0)
    print top_level_industries_data
    
    return top_level_industries_data


if __name__ == '__main__':
    main()
