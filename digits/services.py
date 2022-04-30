import numpy as np
from PIL import Image
from tensorflow import keras
from keras.preprocessing import image
from keras.models import load_model
from keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from django.conf import settings
from keras import backend as K
import os
import cv2

from keras.models import Sequential,Input,Model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

from tensorflow.keras.utils import to_categorical
from keras.models import model_from_json

def predict(img_path):
    jpgPath = savePngToJpg(img_path)

    img = image.load_img(jpgPath, target_size=(28, 28), color_mode='grayscale')
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = (255-x) / 255.

    model = None

    # SE CAMBIO A CARGAR MODELO POR JSON POR EFICIENCIA AL PREDECIR
    keras_path = settings.KERAS_MODEL_ROOT
    with open(keras_path + "model.json") as json_model:
        model = model_from_json(json_model.read())
        json_model.close()

        model.load_weights(keras_path + "model.weights")
        model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

    if (model == None):
        return -1


    # model = load_model(settings.KERAS_MODEL_PATH)
    # model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

    pred = model.predict(x);
    new_predict = np.argmax(np.round(pred),axis=1)
    print(new_predict)
    K.clear_session()
    return new_predict[0]


def savePngToJpg(image_path):
    png = Image.open(image_path)
    if (png.format == 'JPEG'):
        png.close()
        return image_path

    path, filename = os.path.split(os.path.abspath(image_path))
    finalPath = os.path.join(path, filename.replace('.png', '.jpg'))

    png.load()

    if len(png.split()) > 3:
        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3])  # 3 is the alpha channel

        background.save(finalPath, 'JPEG', quality=90)
    else:
        im = Image.open(image_path)
        rgb_im = im.convert('RGB')
        rgb_im.save(finalPath)

    png.close();
    return finalPath;


def train_model():
    from keras.datasets import mnist
    (train_X,train_Y), (test_X,test_Y) = mnist.load_data()

    classes = np.unique(train_Y)
    nClasses = len(classes)

    print(classes, nClasses)

    train_X = train_X.reshape(-1, 28,28, 1)
    test_X = test_X.reshape(-1, 28,28, 1)

    train_X = train_X.astype('float32')
    test_X = test_X.astype('float32')
    train_X = train_X / 255.
    test_X = test_X / 255.

    train_Y_one_hot = to_categorical(train_Y) # [0 0 0 0 0 1 0 0 0 0]
    test_Y_one_hot = to_categorical(test_Y)

    from sklearn.model_selection import train_test_split
    train_X,valid_X,train_label,valid_label = train_test_split(train_X, train_Y_one_hot, test_size=0.2, random_state=13)

    # batch_size = 128
    # num_classes = 10
    # epochs = 12

    batch_size = 64
    epochs = 20
    num_classes = 10

    # # PRIMERA VERSION
    # model = Sequential()
    # model.add(Conv2D(32, kernel_size=(3, 3),
    #                  activation='relu',
    #                  input_shape=(28,28,1)))
    # model.add(Conv2D(64, (3, 3), activation='relu'))
    # model.add(MaxPooling2D(pool_size=(2, 2)))
    # model.add(Dropout(0.25))
    # model.add(Flatten())
    # model.add(Dense(128, activation='relu'))
    # model.add(Dropout(0.5))
    # model.add(Dense(num_classes, activation='softmax'))


    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3),activation='linear',padding='same',input_shape=(28,28,1)))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D((2, 2),padding='same'))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), activation='linear',padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    model.add(Dropout(0.25))
    model.add(Conv2D(128, (3, 3), activation='linear',padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D(pool_size=(2, 2),padding='same'))
    model.add(Dropout(0.4))
    model.add(Flatten())
    model.add(Dense(128, activation='linear'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dropout(0.3))
    model.add(Dense(num_classes, activation='softmax'))

    model.summary()

    model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adam(),metrics=['accuracy'])

    train_dropout = model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

    test_eval = model.evaluate(test_X, test_Y_one_hot, verbose=1)

    print('Test loss:', test_eval[0])
    print('Test accuracy:', test_eval[1])

    accuracy = train_dropout.history['accuracy']
    val_accuracy = train_dropout.history['val_accuracy']
    loss = train_dropout.history['loss']
    val_loss = train_dropout.history['val_loss']
    print(accuracy)
    print(val_accuracy)

    predicted_classes = model.predict(test_X)
    predicted_classes = np.argmax(np.round(predicted_classes),axis=1)
    print(predicted_classes.shape, test_Y.shape)

    correct = np.where(predicted_classes==test_Y)[0]
    print("Found " + str(len(correct)) + " correct labels")

    incorrect = np.where(predicted_classes!=test_Y)[0]
    print ("Found " + str(len(incorrect)) + " incorrect labels ")

    from sklearn.metrics import classification_report
    target_names = ["Class {}".format(i) for i in range(num_classes)]
    print(classification_report(test_Y, predicted_classes, target_names=target_names))

    # SAVE MODEL
    keras_path = settings.KERAS_MODEL_ROOT
    model.save_weights(keras_path + "model.weights")
    with open(keras_path + "model.json", "w") as json_file:
        model_json = model.to_json()
        json_file.write(model_json)
    # model.save(settings.KERAS_MODEL_PATH)

