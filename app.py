from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Set up Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Your Google Sheet Name").sheet1  # or use .worksheet("Sheet1")

@app.route("/")
def index():
    data = sheet.get_all_records()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
