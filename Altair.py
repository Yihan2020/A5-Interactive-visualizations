import altair as alt
from vega_datasets import data
import pandas as pd

source = pd.read_csv("Altair.csv")

chart = alt.Chart(source).mark_bar().encode(
    x='Household',
    y='sum(Value)',
    color='Plug').properties(
    width=alt.Step(80))

chart.save('Altair.html')