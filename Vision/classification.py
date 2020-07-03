import tensorflow as tf
import time
from tensorflow.keras.applications.vgg19 import VGG19,preprocess_input,decode_predictions
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from PIL import Image



import streamlit as st

st.write("""
# VGG19 Classification
""")
st.write("## Based on : Very Deep Convolutional Networks for Large-Scale Image Recognition")

vggstruct = Image.open('vgg19.jpg')
st.image(vggstruct, caption='VGG19 architecture',use_column_width=True)


#preprocess input data
def preprocess(img_path):
    image = img_path.resize((224,224))
    image = img_to_array(image)
    image = image.reshape((1,image.shape[0],image.shape[1],image.shape[2]))
    image = preprocess_input(image)
    return image

# hyperparameter
i_path = 'pen.jpg'
num_classes = 1

uploaded_file = st.file_uploader("Choose Picture", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Picture',use_column_width=True)



    # predictions
    image = preprocess(image)

    #load VGG19 model
    with st.spinner('Loading VGG19 Model'):
        model = VGG19()
    with st.spinner('Predicting Object'):
        i_pred = model.predict(image)
        label = decode_predictions(i_pred,top=num_classes)

    
    with st.spinner('Confidence'):
        # process output
        confidence = round(label[0][0][2],3)
        st.write(confidence)
        bar = st.progress(0)
        prog_sec = 1.0
        for b_progress in range(100):
            time.sleep(prog_sec/100.0)
            bar.progress( int((b_progress+1)*confidence) )
        
        confidence = round(confidence*100,2)
        output = "# "+label[0][0][1] + " with " + str(confidence) + " % confidence"
        st.write(output)

