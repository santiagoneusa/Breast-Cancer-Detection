from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import numpy as np
from PIL import Image
import tensorflow as tf

MODEL_PATH = os.path.join(settings.BASE_DIR, 'model', 'modelo_aug_cancer_mama_vgg16.keras')
model = tf.keras.models.load_model(MODEL_PATH)
TF_ENABLE_ONEDNN_OPTS=0

MODEL_INFO = {
    'accuracy': 0.95,
    'precision': 0.94,
    'recall': 0.96,
    'data_used': "+8,000 mammogram images",
    'model_type': "Convolutional Neural Network",
    'classes': ["Benign", "Malignant"]
}

def home(request):
    return render(request, 'home.html', {'model_info': MODEL_INFO})

def ai_model(request):
    template_data = {'prediction': None, 'confidence': None, 'error': None}
    
    if request.method == 'POST' and request.FILES['image']:
        try:
            uploaded_file = request.FILES['image']
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)
            
            img = Image.open(file_path)
            img = img.resize((224, 224))
            img_array = np.array(img)
            img_array = img_array / 255.0
            img_array = np.expand_dims(img_array, axis=0)
            
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions[0])
            confidence = np.max(predictions[0]) * 100
            
            template_data['prediction'] = MODEL_INFO['classes'][predicted_class]
            template_data['confidence'] = f"{confidence:.2f}%"
            template_data['image_url'] = settings.MEDIA_URL + filename
            
        except Exception as e:
            template_data['error'] = f"Error processing image: {str(e)}"
    
    return render(request, 'ai_model.html', {'template_data': template_data})