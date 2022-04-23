import streamlit as st
import  numpy as np
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Price Predictor')
# Laptop company
company = st.selectbox('Brand',np.sort(df['Company'].unique()))
# Type of laptop
type = st.selectbox('Type',np.sort(df['TypeName'].unique()))
# Laptop Ram
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])
# weight
weight=st.number_input('Weight of the laptop')
#TouchScreen
touchscreen = st.selectbox('Touchscreen',['Yes','No'])
# IPs Display
ipsdisplay = st.selectbox('IPS Display',['No','Yes'])
# screen size
screen_size = st.number_input('Screen_size')
#Resolution
resolution=st.selectbox('Screen Resolution',
                        ['1920x1080','1366x768','1600x900',
                         '3840x2160','3200x1800','2880x1800',
                         '2560x1600','2560x1440','2340x1440'])
#CPU
cpu = st.selectbox('CPU Brand',df['Cpu_brand'].unique())
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(in GB)',[0,128,256,512,1024,2048])
gpu = st.selectbox('GPU Brand',df['Gpu_brand'].unique())
os=st.selectbox('OS',df['OpSys'].unique())

if st.button('Predict Price'):
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0

    if ipsdisplay== 'Yes':
        ipsdisplay = 1
    else:
        ipsdisplay = 0
    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res**2) + (y_res**2))**0.5 / screen_size
    query = np.array([company,type,ram,os,weight,touchscreen,ipsdisplay,ppi,cpu,hdd,ssd,gpu])
    query=query.reshape(1,12)

    st.title(int(np.exp(pipe.predict(query)[0])))







