
from eden import Eden
from vendor import Vendor
import pandas as pd, pandas

class Audyt_New:

    def __init__(self, marka):

        df1 = Vendor()
        df2 = Eden(288, marka = marka, czyaudyt = True)

        df1['EAN'] = pd.to_numeric(df1['EAN'], errors='coerce')
        
        try:
            df2['g_EANCode'] = pd.to_numeric(df2['g_EANCode'])
        except:
            pass
        
        print(df1.dtypes)
        print(df2.dtypes)

        df2 = pandas.merge(df2, df1[['EAN', 'ASIN']], how = 'left', left_on = 'g_EANCode', right_on = 'EAN')

        df2 = df2.drop(columns = ['EAN'])

        writer = pd.ExcelWriter('Audyt_' + marka + '.xlsx', engine = 'xlsxwriter')

        df1.to_excel(writer, sheet_name = 'Vendor', index = False)
        df2.to_excel(writer, sheet_name = 'Eden', index = False)

        writer.save()

if __name__ == '__main__':

    a = Audyt_New('airoh')