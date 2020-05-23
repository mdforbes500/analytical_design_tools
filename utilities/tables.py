#!/usr/bin/env python3

import pandas as pd

def lookup_property(df: pd.DataFrame, props: str, material: str) -> None:
    """
    Accepts the table as a Dataframe object, property (props) and material.
    Returns the value of the material property and units assoicated with it.
    """
    return float(df.at[props, material]) 