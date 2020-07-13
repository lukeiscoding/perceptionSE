from keras import *
from keras.layers import *

def model():
    Leaky_Relu_activation = LeakyReLU(alpha=0.2)
    image = Input(shape=(128, 128, 1))
    conv_1 = Conv2D(16, kernel_size=(7, 7), padding='same', activation='relu', name='conv_1')(image)
    conv_1 = BatchNormalization()(conv_1)
    pool_1 = MaxPool2D(pool_size=2)(conv_1)
    conv_2 = Conv2D(32, kernel_size=(5, 5), padding='same', activation='relu', name='conv_2')(pool_1)
    conv_2 = BatchNormalization()(conv_2)
    pool_2 = MaxPool2D(pool_size=2)(conv_2)
    conv_3 = Conv2D(64, kernel_size=(5, 5), padding='same', activation='relu', name='conv_3')(pool_2)
    conv_3 = BatchNormalization()(conv_3)
    pool_3 = MaxPool2D(pool_size=2)(conv_3)
    conv_4 = Conv2D(128, kernel_size=(3, 3), padding='same', activation='relu', name='conv_4')(pool_3)
    conv_4 = BatchNormalization()(conv_4)
    pool_4 = MaxPool2D(pool_size=2)(conv_4)
    conv_5 = Conv2D(128, kernel_size=(3, 3), padding='same', activation='relu', name='conv_5')(pool_4)
    conv_5 = BatchNormalization()(conv_5)
    pool_5 = MaxPool2D(pool_size=2)(conv_5)
    conv_6 = Conv2D(128, kernel_size=(3, 3), padding='same', activation='relu', name='conv_6')(pool_5)
    conv_6 = BatchNormalization()(conv_6)
    pool_6 = MaxPool2D(pool_size=2)(conv_6)

    doub_6 = Deconv2D(128, kernel_size=(2, 2), strides=2, activation='relu', name='doub_6')(pool_6)
    conc_6 = Concatenate()([conv_6, doub_6])
    deco_6 = Conv2D(128, kernel_size=(3, 3), padding='same', activation=Leaky_Relu_activation, name='deco_6')(conc_6)
    deco_6 = BatchNormalization()(deco_6)
    doub_5 = Deconv2D(128, kernel_size=(2, 2), strides=2, activation='relu', name='doub_5')(deco_6)
    conc_5 = Concatenate()([conv_5, doub_5])
    deco_5 = Conv2D(128, kernel_size=(3, 3), padding='same', activation=Leaky_Relu_activation, name='deco_5')(conc_5)
    deco_5 = BatchNormalization()(deco_5)
    doub_4 = Deconv2D(128, kernel_size=(2, 2), strides=2, activation='relu', name='doub_4')(deco_5)
    conc_4 = Concatenate()([conv_4, doub_4])
    deco_4 = Conv2D(64, kernel_size=(3, 3), padding='same', activation=Leaky_Relu_activation, name='deco_4')(conc_4)
    deco_4 = BatchNormalization()(deco_4)
    doub_3 = Deconv2D(64, kernel_size=(2, 2), strides=2, activation='relu', name='doub_3')(deco_4)
    conc_3 = Concatenate()([conv_3, doub_3])
    deco_3 = Conv2D(32, kernel_size=(3, 3), padding='same', activation=Leaky_Relu_activation, name='deco_3')(conc_3)
    deco_3 = BatchNormalization()(deco_3)
    doub_2 = Deconv2D(32, kernel_size=(2, 2), strides=2, activation='relu', name='doub_2')(deco_3)
    conc_2 = Concatenate()([conv_2, doub_2])
    deco_2 = Conv2D(16, kernel_size=(3, 3), padding='same', activation=Leaky_Relu_activation, name='deco_2')(conc_2)
    deco_2 = BatchNormalization()(deco_2)
    doub_1 = Deconv2D(16, kernel_size=(2, 2), strides=2, activation='relu', name='doub_1')(deco_2)
    conc_1 = Concatenate()([conv_1, doub_1])
    deco_1 = Conv2D(1, kernel_size=(1, 1), padding='same', activation=Leaky_Relu_activation, name='deco_1')(conc_1)
    deco_1 = BatchNormalization()(deco_1)
    deco_0 = Conv2D(1, kernel_size=(1, 1), padding='same', activation='linear', name='deco_0')(deco_1)
    output = deco_0
    model = Model(input=image, output=output)
    return model