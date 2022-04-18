import numpy as np
import pandas as pd

# datetime utilities
from datetime import timedelta, datetime

import matplotlib.pyplot as plt
import seaborn as sns

# no yelling in the library
import warnings
warnings.filterwarnings("ignore")

import acquire as get


def prepare_store_data():
    df = get.get_store_item_demand_data()
    
    # Convert date column to datetime format.
    df.sale_date = pd.to_datetime(df.sale_date)
    
    # Set the index to be the datetime variable.
    df = df.set_index('sale_date').sort_index()
    
    # 4. Add a 'month' and 'day of week' column to your dataframe.
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def prepare_opsd_data(): 
    df = get.get_opsd_data()
    
    # convert date column to datetime format.
    df.Date = pd.to_datetime(df.Date)
    
    # set the index to be the datetime variable
    df = df.set_index('Date').sort_index()
    
    # add a month and a year column to your dataframe
    df['month'] = df.index.month
    df['year'] = df.index.year
    
    # Fill any missing values.
    df = df.fillna('0')
    
    return df