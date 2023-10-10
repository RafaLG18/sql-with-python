#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:36:38 2023

@author: rafael
"""

import pandas as pd
import sqlite3 as sql

# create dataframe
data =pd.DataFrame({
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','David']
    })

# create database and save 
# the dataframe
conn=sql.connect('mydatabase.db')
# Use the to_sql method to save the DataFrame
data.to_sql('mytable',conn,if_exists='replace',index=False)

# close connection with database
conn.close()