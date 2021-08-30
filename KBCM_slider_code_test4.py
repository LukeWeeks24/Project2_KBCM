
import pandas as pd
import streamlit as st
import datetime
import re
import base64

df = pd.read_csv('time.csv')

def df_filter(message,df):

        slider_1, slider_2 = st.slider('%s' % (message),0,len(df)-1,[0,len(df)-1],1)

        while len(str(df.iloc[slider_1][1]).replace('.0','')) < 4:
            df.iloc[slider_1,1] = '0' + str(df.iloc[slider_1][1]).replace('.0','')
            
        while len(str(df.iloc[slider_2][1]).replace('.0','')) < 4:
            df.iloc[slider_2,1] = '0' + str(df.iloc[slider_1][1]).replace('.0','')

        start_time = datetime.datetime.strptime(str(df.iloc[slider_1][0]).replace('.0','') + str(df.iloc[slider_1][1]).replace('.0',''),'%H:%M:%S.%f')
        start_time = start_time.strftime('%H:%M:%S.%f')
        
        end_time = datetime.datetime.strptime(str(df.iloc[slider_2][0]).replace('.0','') + str(df.iloc[slider_2][1]).replace('.0',''),'%H:%M:%S.%f')
        end_time = end_time.strftime('%H:%M:%S.%f')

        st.info('Start: **%s** End: **%s**' % (start_date,end_date))
        
        filtered_df = df.iloc[slider_1:slider_2+1][:].reset_index(drop=True)

        return filtered_df




