import numpy as np
from keras.preprocessing import image
from keras.models import load_model

from keras.utils.vis_utils import plot_model

model = load_model('modelV9.h5')
#model.summary()

def testfile():
    rslt = model.predict(img_pred)
    if rslt[0][0] == 1:
        prediction = "person"
    else:
        prediction = "noperson"

    print(prediction)


for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\LowLight\\noperson\\noperson (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("LowLight noperson finnish")


for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\LowLight\\person\\person (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("LowLight person finnish")

for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\MidLight\\noperson\\noperson (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("MidLight noperson finnish")

for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\MidLight\\person\\person (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("MidLight person finnish")

for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\HighLight\\noperson\\noperson (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("HighLight noperson finnish")

for i in range(1,6):
    integer = str(i)
    img_pred = image.load_img(
        'C:\\Users\\m_yer\\PycharmProjects\\untitled\\src\\data\\test\\Testindata\\HighLight\\person\\person (' + integer +').jpg',
        target_size=(64, 64))
    img_pred = image.img_to_array(img_pred)
    img_pred = np.expand_dims(img_pred, axis=0)
    testfile()
    #printing()

print("HighLight person finnish")

#plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
#rslt = model.predict(img_pred)


















