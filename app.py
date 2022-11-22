# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:03:07 2022

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
    st.title('Worker Performance Rating Prediction App')
    st.markdown('Just Enter the following details and we will predict the performance rating of your Worker')
    a = st.slider("Age(years)",0,50)
    b = st.selectbox("Gender",('Female','Male'))
    if b == 'Female':
        b=0
    else:
        b=1
    c = st.selectbox("Nationality",("Bangladesh", "China","Japan","Malaysia","Pakistan","Philippines","Sri Lanka"))
    if c == "Bangladesh":
        c=0
    elif c == "China":
        c=1    
    elif c == "Japan":
        c=2
    elif c == "Malaysia":
        c=3
    elif c == "Pakistan":
        c=4
    elif c == "Philippines":
        c=5
    else:
        c=6
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
    ##g = st.selectbox("Attendance",('Abscent','Present'))
    ##if g == 'Abscent':
     ##   g = 0
   ## else:
       ## g = 1  
    h = st.selectbox("Noise_Detection",('Yes','No'))
    if h == 'No':
        h = 0
    else:
        h = 1      
    i = st.selectbox("Infrared_Sensor",('Yes','No'))
    if i == 'No':
        i = 0
    else:
        i = 1
    j = st.selectbox("Gas_Sensor",('Yes','No'))
    if j == 'No':
        j = 0
    else:
        j = 1   
    k = st.selectbox("Galvanic_Skin_Response_Sensor",('Yes','No'))
    if k == 'No':
        k = 0
    else:
        k = 1  
    l = st.number_input('Temperature')
    m = st.slider("Respiratory_Rate(RR)",0,30)
    n = st.slider('Heart_Rate(HR)',80,160)
    o = st.selectbox("Work_Position",('Adjusting Bricks','Crushing','Curing','Cutting Bricks','Cutting Re-bar','Drilling','Excavation','Fetching Mortar','Lashing Rope','Moving Bricks','Moving Stones','Placing Rebar','Re-bar','Welding','Wiring'))
    if o == 'Adjusting Bricks':
        o = 0
    elif o == 'Crushing':
        o = 1
    elif o == 'Curing':
        o = 2
    elif o == 'Cutting bricks':
        o = 3
    elif o == 'Cutting Re-bar':
        o = 4  
    elif o == 'Drilling':
        o = 5
    elif o == 'Excavation':
        o = 6
    elif o == 'Fetching Mortar':
        o = 7
    elif o == 'Lashing Rope':
        o = 8
    elif o == 'Moving Stones':
        o = 9
    elif o == 'Placing Rebar':
        o = 10
    elif o == 'Re-bar':
        o = 11
    elif o == 'Welding':
        o = 12
    else:
        o = 13	
    p = st.selectbox("Over_time",('Yes','No'))
    if p == 'No':
        p = 0
    else:
        p = 1               
    submit = st.button('Predict Rating')
    if submit: 
        prediction = emp_perf_model1.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]])
        prediction = int(prediction)
        if prediction == 0:
            st.warning("Worker's performance is average")
        elif prediction == 1:
            st.success("Employee's performance is good")
        else:
            st.error("Employee's performance is low")


if __name__ == '__main__':
    main()
