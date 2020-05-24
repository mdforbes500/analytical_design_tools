#!/usr/bin/env python3

import pandas as pd
import os
import sys

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

def find_tensile_strength(material: str, units: str, d: float) -> None:
    """
    """
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "/data/10-4.csv"
    df = pd.read_csv(path, header=0)
    column_title = df.columns[0]
    df.set_index(column_title, inplace=True)
    #remove the columns for other unitsys
    if units == 'US Customary':
        df.drop(columns=["Diameter Range (mm)", "A (MPa-mm^m)"], inplace=True)
    elif units == 'Metric':
        df.drop(columns=["Diameter Range (in.)", "A (kpsi-in^m)"], inplace=True)
    else:
        raise Exception("Input Error: Units type must be either US Customary or Metric")
    #extract rows for series based on the material
    df = df.loc[material, :]
    #iterate through diameters until diameter falls into a range
    series = df['Diameter Range (in.)']
    if type(series) is not list:
        series = series.split("-")
        if d > float(series[0]) and d <= float(series[1]):
            A = float(df['A (kpsi-in^m)'])
            m = float(df['m'])
        else:
            raise Exception("No data available for guage of wire necessary.")
    else:
        bounds = []
        for index, entry in enumerate(series):
            bounds.append(entry)
            bounds[index] = bounds[index].split("-")
            if d > float(bounds[index][0]) and d <= float(bounds[index][1]):
            #then extract the A,m values for given entry
                A = float(df['A (kpsi-in^m)'].iloc[[index]])
                m = float(df['m'].iloc[[index]])
            else:
                raise Exception("No data available for guage of wire necessary.")
    #compute the tensile strength
    return A/d**m

def find_maximum_tensile_strength(material, minimum_tensile_strength, set_removed=False, **kwargs) -> None:
    """
    """
    pass