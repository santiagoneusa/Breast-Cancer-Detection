<div align="center">

# Breast Cancer Detection with CNN

</div>

## Overview
This project implements a Convolutional Neural Network (CNN) based on pre-trained architectures such as VGG16, ResNet, and MobileNet, using transfer learning and fine-tuning techniques. The model was trained on a dataset of breast ultrasound images to classify lesions as benign or malignant.

## Model Evaluation
The model was evaluated using clinically relevant metrics:

| Metric |	Achieved Value | 
|--------|----------------|
| Precision |	94% | 
| Recall |	96% | 
| F1-Score |	95% | 
| Accuracy |	95% | 
| AUC ROC |	0.99 | 

Additionally, ROC curves, confusion matrices, and classification reports were generated to validate the model's performance.

## Requirements

Follow these steps to set up the application locally:

### 1. Clone the Repository

Clone the project repository to your local machine:

    git clone https://github.com/santiagoneusa/Breast-Cancer-Detection.git
    

### 2. Set Up a Virtual Environment (Optional but Recommended)
    - Using Python:
        python -m venv venvname
        
    - Using Conda:
        conda create --name venvname
        
Replace the `venvname` with a proper name of the virtual environment, such as `CancerDetection`.

### 3. Install the Dependencies

Navigate to the project directory and install all required Python packages:

    pip install -r requirements.txt
    
### 4. Navigate to the Project Directory
    cd Breast-Cancer-Detection

### 5. Apply Migrations
    python manage.py migrate

### 5. Run the Development Server
    python manage.py runserver

Once the server is running, open the provided URL (typically http://127.0.0.1:8000/) in your browser to access the application.

## Contributors

- **Juan Manuel Gómez**
- **Santiago Neusa**