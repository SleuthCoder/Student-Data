import csv
import pandas as pd
import plotly.express as px
with open("StudentData.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x = "student_id", y = "level")
    fig.show()
