from flask import Flask
from config import db_uri
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

def get_sheet():
    # define the scope
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    # add credentials to the account
    creds = ServiceAccountCredentials.from_json_keyfile_name('add_json_file_here.json', scope)

    # authorize the clientsheet 
    client = gspread.authorize(creds)
    # get the instance of the Spreadsheet
    sheet = client.open('commentary data')

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)
    return sheet_instance
    
def get_missing() -> pd.DataFrame:
    sheet = get_sheet()
    records_data = sheet.get_all_records()
    return pd.DataFrame.from_dict(records_data)

def update_sheet(df: pd.DataFrame):
    sheet.insert_rows(df.values.tolist())
    
@app.route("/form", methods=["GET", "POST"])
def form():
    pass

