# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 16:01:35 2022

@author: archa
"""


import streamlit as st
import numpy as np
import pickle

emp_perf_model_path1 = open("model.pkl","rb")
emp_perf_model1=pickle.load(emp_perf_model_path1)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)

def main():
    st.title("Worker's Performance Rating Prediction App")
    st.markdown('Just Enter the following details and we will predict the performance rating of your Worker')
    a = st.slider("Age(years)",0,50)
    b = st.selectbox("Gender",('Female','Male'))
    if b == 'Female':
        b=0
    else:
        b=1
    c = st.selectbox("Nationality",('Canada','India','Pakisthan','USA'))
    if c == "Canada":
        c=0
    elif c == "India":
        c=1    
    elif c == "Pakisthan":
        c=2
    else:
        c=3
    d = st.selectbox("Site",('Site-1','Site-2','Site-3')) 
    if d == "Site-1":
         d=0
    elif d== "Site-2":
         d=1
    else:
         d=2 
    e = st.selectbox("Working_Hours",('Equal to 9hrs','Greater than 9hrs','Less than 9hrs'))
    if e == 'Equal to 9hrs':
    	e = 0
    elif e == 'Greater than 9hrs':
    	e = 1
    else:
        e = 2
    f = st.slider("Experience(years)",0,10)
    g = st.selectbox("Attendance",('Poor','Good'))
    if g == 'Good':
       g = 0
    else:
       g = 1  
    h = st.slider("Gas_Sensor",400,800)   
    i = st.selectbox("Noise-Sensor",('Good','Medium','Bad'))
    if i == 'Good':
        i = 0
    elif i == 'Medium':
        i = 1
    else:
        i = 2
    j = st.selectbox("Infrared_Sensor",('3 Âµm to 6 Âµm','0.75Âµm to 3 Âµm','> 6 Âµm'))
    if j == '3 Âµm to 6 Âµm':
        j = 0
    elif j == '0.75Âµm to 3 Âµm':
        j = 1 
    else:
        j = 2
    k = st.number_input("Skin_Response_Sensor") 
    l = st.number_input('Temperature')
    m = st.number_input("Respiratory_Rate(RR)")
    n = st.slider('Heart_Rate(HR)',80,180)
    o = st.selectbox("Work_Position",('Concrete','Curing','Excavation','FineAggregate','Machinery','Welding'))
    if o == 'Concrete':
        o = 0
    elif o == 'Curing':
        o = 1
    elif o == 'Excavation':
        o = 2
    elif o == 'FineAggregate':
        o = 3
    elif o == 'Machinery':
        o = 4  
    else:
        o = 5	             
    submit = st.button('Predict Rating')
    if submit: 
        prediction = emp_perf_model1.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]])
        prediction = int(prediction)
        if prediction == 0:
            st.success("Worker's performance is good")
        elif prediction == 1:
            st.warning("Worker's performance is average")
        else:
            st.error("Worker's performance is low")


if __name__ == '__main__':
    main()
