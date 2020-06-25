import streamlit as st
import pandas as pd
import time

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from PIL import Image


st.write("""
# Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.table(df)


iris = load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

##calculate predicted values
values = []
for i in range(3):
    values.append(prediction_proba[0][i])

st.subheader('Confidence Bar')
bars = []
ind=0
for i in iris.target_names:
    st.write(i+'   ~ '+str(int(values[ind]*100))+' %')
    b = st.progress(0)
    bars.append(b)
    ind = ind + 1





predicted = iris.target_names[prediction][0]

disp_str ="""
## Predicted Iris Type : **"""+predicted+"""**
""" 
st.write(disp_str)
#st.write(prediction)



with st.spinner('Predicting'):
    prog_sec = 1.0
    for b_progress in range(100):
        time.sleep(prog_sec/100.0)
        for i in range(3):
            bars[i].progress(int((b_progress+1)*values[i]))
    image = Image.open(predicted+'.jpg')
    st.image(image, caption=predicted+' flower',use_column_width=True)

