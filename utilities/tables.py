#!/usr/bin/env python3

import pandas as pd
import os

def find_guage_diameter(props: str, material: str) -> None:
    """
    Accepts the table as a Dataframe object, property (props) and material.
    Returns the value of the material property and units assoicated with it.
    """
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/data/A-28.csv"
    df = pd.read_csv(path, header=0)
    column_title = df.columns[0]
    df.set_index(column_title, inplace=True)
    return float(df.at[props, material]) 