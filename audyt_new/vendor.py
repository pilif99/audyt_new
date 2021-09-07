
import pandas as pd
import glob
import os

class Vendor(pd.DataFrame):

    def __init__(self):

        super().__init__()
        self.zamien_na_self()

    def zamien_na_self(self):

        list_of_files = glob.glob(r"C:\Users\FLorenzLen\Downloads\*") # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)

        df = pd.read_excel(latest_file, skiprows = 1)
        df_dict = df.to_dict()
        self.append(super().__init__(df_dict))