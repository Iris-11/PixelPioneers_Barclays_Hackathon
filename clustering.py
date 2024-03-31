import numpy as np
import pandas as pd
import email


chunksize = 10000
for chunk in pd.read_csv('emails.csv', chunksize=chunksize):
    # process each chunk here
    print(chunk.head())
    break

