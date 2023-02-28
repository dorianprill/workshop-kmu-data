# this script carries out merge instructions for gta_v data as per
# https://www.kaggle.com/datasets/lucasokwudishu/gta-v-vehicle-dataset
# all tables have superfluous index columns, which are dropped on read

import numpy as np
import scipy as sp
import polars as pl

# (1) read in the 3 batch files and concatenate them, as all entries are distinct, drop index column
try:
    df = (pl.read_csv("resources/data/gta_v/gta_data_batch_1.csv", columns=range(1,35), sep=',')
        .extend(pl.read_csv("resources/data/gta_v/gta_data_batch_2.csv", columns=range(1,35), sep=','))
        .extend(pl.read_csv("resources/data/gta_v/gta_data_batch_3.csv", columns=range(1,35), sep=','))
    )
except (IOError, OSError) as e:
    print(f'Failed to read files {e}')
except OtherError as e:
    print(f'Other error {e}')


# check if there are duplicates
if df.shape != df.unique().shape:
    print(f'Warning: {df} has duplicates -> drop them manually')

# print(f'Vehicle batch entries are unique? {df.shape == df.unique().shape} (should be True)')


# (2) same thing as (1) with the upgrade cost data batches
try:
    dfcost = (pl.read_csv("resources/data/gta_v/gta_data_upgrade_cost_1.csv", columns=range(1,3))
        .extend(pl.read_csv("resources/data/gta_v/gta_data_upgrade_cost_2.csv", columns=range(1,3)))
    )
except (IOError, OSError) as e:
    print(f'Failed to read files {e}')
except OtherError as e:
    print(f'Other error {e}')


if dfcost.shape != dfcost.unique().shape:
    print(f'Warning: {dfcost} has duplicates -> drop them manually')

# (3) join(left) the two dataframes on the vehicle_url column
df = df.join(dfcost, on='vehicle_url', how='left')
del dfcost

# print null values per column
print('Null values per column (if any): ')
for col in df.get_columns():
    if col.is_null().sum() > 0:
        print(f'{col.name : <24} {col.is_null().sum()}')

# warning: since features are a arbitrary list of string, there may be null values i.e. no features 
print('Final DataFrame:')
print(df)

# (4) Save the new cleaned and joined data as a new file for convenience
df.write_csv("resources/data/gta_v/gta_v_data.csv")
# we can also use a non-human readable(but faster) format, e.g. parquet
df.write_parquet("resources/data/gta_v/gta_v_data.parquet")

