"""
Purpose: Use Python to generate local data files in this folder.

To create data files,
   modify the code to import the dataset in the format you want.
   Uncomment those lines and run this script in the terminal with `python app_data.py`.

After creating the data files, you can comment out code you don't need to re-run.
In VS Code, you can select many lines, and use CTRL + / to comment out all of them.

CSV files can be easily reviewed in VS Code.

@imports seaborn as sns to load datasets into Pandas DataFrames (df)
@imports pandas as pd to write DataFrames (df) to Excel and CSV files

mtcars.csv was copied from the Shiny example at:
https://shinylive.io/py/examples/#read-local-csv


"""
import pathlib
import pandas as pd
import seaborn as sns

from util_logger import setup_logger

logger, logname = setup_logger(__name__)

# Get a path object representing this data folder.
data_folder = pathlib.Path(__file__).parent

url="https://github.com/mwaskom/seaborn-data/blob/master/tips.csv"
tips_df_df=pd.read_csv('https://github.com/mwaskom/seaborn-data/blob/master/iris.csv')

url="https://github.com/mwaskom/seaborn-data/blob/master/healthexp.csv"
healthexp_df=pd.read_csv('https://github.com/mwaskom/seaborn-data/blob/master/iris.csv')


# url="https://webpath/to/your/data.csv"
# df=pd.read_csv(url)
