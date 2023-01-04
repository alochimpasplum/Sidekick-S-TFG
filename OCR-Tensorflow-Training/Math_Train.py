import os
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Activation,Dropout,Conv2D, MaxPooling2D,BatchNormalization
from keras.optimizers import Adam, Adamax
from keras.metrics import categorical_crossentropy
from keras import regularizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model, load_model, Sequential


sdir: str = "./Datasets/handwritten_math_symbols"
classlist=os.listdir(sdir)
filepaths=[]
labels=[]
classes=[]
for klass in classlist:
    classpath=os.path.join(sdir, klass)
    if os.path.isdir(classpath):
        classes.append(klass)
        flist=os.listdir(classpath)
        for f in flist:
            fpath=os.path.join(classpath,f)
            if os.path.isfile(fpath):
                filepaths.append(fpath)
                labels.append(klass)
fseries=pd.Series(filepaths, name='filepaths')
Lseries=pd.Series (labels, name='labels')
df=pd.concat([fseries, Lseries], axis=1)
balance=df['labels'].value_counts()
print (balance) # dataset is reasonably balanced
train_split=.9
test_split=.05
dummy_split=test_split/(1-train_split)
train_df, dummy_df=train_test_split(df, train_size=train_split, shuffle=True, random_state = 123)
test_df, valid_df=train_test_split(dummy_df, train_size=dummy_split, shuffle=True, random_state=123)
def scalar(img):
    return img/127.5-1 # scale pixels between -1 and + 1
gen=ImageDataGenerator(preprocessing_function=scalar)
train_gen=gen.flow_from_dataframe(train_df, x_col= 'filepaths', y_col='labels', target_size=(128,128), class_mode='categorical',
                                  color_mode='rgb', shuffle=False)
test_gen=gen.flow_from_dataframe(test_df, x_col= 'filepaths', y_col='labels', target_size=(128,128), class_mode='categorical',
                                  color_mode='rgb', shuffle=False)
valid_gen=gen.flow_from_dataframe(valid_df, x_col= 'filepaths', y_col='labels', target_size=(128,128), class_mode='categorical',
                                  color_mode='rgb', shuffle=False)
base_model=tf.keras.applications.MobileNetV2( include_top=False, input_shape=(128,128,3), pooling='max', weights='imagenet')
x=base_model.output
x=keras.layers.BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001 )(x)
x = Dense(1024, kernel_regularizer = regularizers.l2(l = 0.016),activity_regularizer=regularizers.l1(0.006),
                bias_regularizer=regularizers.l1(0.006) ,activation='relu', kernel_initializer= tf.keras.initializers.GlorotUniform(seed=123))(x)
x=Dropout(rate=.3, seed=123)(x)
output=Dense(len(classes), activation='softmax',kernel_initializer=tf.keras.initializers.GlorotUniform(seed=123))(x)
model=Model(inputs=base_model.input, outputs=output)
model.compile(Adamax(lr=.001), loss='categorical_crossentropy', metrics=['accuracy'])
estop=tf.keras.callbacks.EarlyStopping( monitor="val_loss",  patience=4, verbose=1,restore_best_weights=True)
rlronp=tf.keras.callbacks.ReduceLROnPlateau(  monitor="val_loss",factor=0.5, patience=1, verbose=1)
history=model.fit(x=train_gen,  epochs=10, verbose=1, callbacks=[estop, rlronp],  validation_data=valid_gen,
               validation_steps=None,  shuffle=False,  initial_epoch=0)
model.save('model_math_symbols')