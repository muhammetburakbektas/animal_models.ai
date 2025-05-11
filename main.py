
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import gradio as gr

# Görüntü boyutu ve eğitim parametreleri
img_height, img_width = 100, 100
batch_size = 32
epochs = 10

# Veri yolu
data_dir = 'data/raw-img'

# Eğitim ve doğrulama verilerini yükle
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_gen = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    shuffle=True
)

# Basit bir CNN modeli
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    layers.MaxPooling2D(2, 2),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(train_gen.num_classes, activation='softmax')
])

# Modeli derle
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Modeli eğit
model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=epochs
)

# Eğitilen modeli kaydet
model.save('animal_classifier_model.h5')
print("Model başarıyla kaydedildi.")

# Modeli yeniden yükle
model = load_model('animal_classifier_model.h5')

# Sınıf adlarını al
class_names = list(train_gen.class_indices.keys())

# Tahmin fonksiyonu
def predict_image(img_path):
    img = image.load_img(img_path, target_size=(100, 100))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    return predicted_class

# Gradio ile web arayüzü
def classify_image_gradio(img):
    img.save("temp.jpg")  # geçici olarak kaydet
    result = predict_image("temp.jpg")
    return f"Bu görsel sınıfı: {result}"

interface = gr.Interface(
    fn=classify_image_gradio,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Hayvan Sınıflandırıcı",
    description="Bir görsel yükleyin, sistem hangi hayvana ait olduğunu tahmin etsin."
)

interface.launch()
