import pandas as pd
import time

import fb_auto
df = pd.read_csv('day.csv')

# Update column names to match the actual CSV structure
# Using 'Numeric' and 'Numeric-Suffix' columns for demonstration
title_column = 'Numeric'
suffix_column = 'Numeric-Suffix'

video_title = df[title_column].to_list()
video_suffix = df[suffix_column].to_list()
size = len(df)
count = 0 
for i in range(size):
    count+=1
    # Use fb_auto's fb_obj instead of directly using fb_obj
    message = f"Day {video_title[i]}: {video_suffix[i]} day of the challenge"
    fb_auto.fb_obj.put_object(parent_object='me', connection_name='feed', message=message)
    print(count, 'posted')
    time.sleep(10)
    
    