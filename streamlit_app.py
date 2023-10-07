import pickle 
import streamlit as st 
import numpy as np
from catboost import CatBoostRegressor
import sklearn

st.title("Inmobiliaria")

st.divider()

st.write("Seleccione el rango de datos:")

assess= st.slider("Assess",0,20)
bdrms= st.slider("Bdrms",0,50)
lotsize= st.slider("Lotsize",0,20)
sqrft= st.slider("sqrft",0, 10)
colonial=st.slider("colonial",0,1)

with open ("model.pkl",'rb') as doc:
    model= pickle.load(doc)


prediccion = model.predict(np.array([[assess, bdrms, lotsize, sqrft, colonial]]))
if st.button("Calcular:"):
    st.write(f"El valor es: {prediccion[0]}")