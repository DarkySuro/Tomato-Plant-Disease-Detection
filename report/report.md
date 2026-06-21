# TOMATO PLANT DISEASE DETECTION USING TRANSFER LEARNING AND DEEP LEARNING

## CHAPTER 1: INTRODUCTION

### 1.1 Background

Agriculture plays a significant role in the economy and food security of many countries. Plant diseases are one of the major causes of reduced crop productivity and economic losses. Traditional disease identification methods rely on manual inspection by agricultural experts, which can be time-consuming, expensive, and inaccessible in remote areas.

Recent advancements in Artificial Intelligence, Deep Learning, and Computer Vision have enabled automated plant disease detection systems capable of identifying diseases directly from leaf images. These systems can assist farmers in early disease diagnosis and timely intervention.

This project presents a Deep Learning-based Tomato Plant Disease Detection System using Transfer Learning with MobileNetV2.

### 1.2 Problem Statement

Manual identification of tomato plant diseases requires expert knowledge and is prone to human error. There is a need for an automated, accurate, and scalable solution capable of identifying tomato leaf diseases from images.

### 1.3 Objectives

* Develop an automated tomato disease detection system.
* Apply Transfer Learning using MobileNetV2.
* Classify tomato leaf images into 10 disease categories.
* Evaluate model performance using standard metrics.
* Deploy the trained model using Streamlit.

### 1.4 Scope of the Project

* Image-based disease classification.
* Tomato crop only.
* Multi-class disease classification.
* Web-based deployment.

### 1.5 Project Workflow

Dataset Collection → Data Analysis → Data Preprocessing → Data Augmentation → Transfer Learning → Fine-Tuning → Model Evaluation → Deployment

---

# CHAPTER 2: LITERATURE REVIEW

### 2.1 Introduction

Discuss previous research in:

* Plant Disease Detection
* Computer Vision in Agriculture
* Deep Learning Applications in Agriculture

### 2.2 Traditional Disease Detection Methods

* Visual Inspection
* Laboratory Analysis
* Limitations

### 2.3 Machine Learning Approaches

* SVM
* Decision Trees
* Random Forest

### 2.4 Deep Learning Approaches

* CNN
* ResNet
* Inception
* MobileNet

### 2.5 Research Gap

Existing systems often require large computational resources or lack real-time deployment capability.

### 2.6 Proposed Solution

Transfer Learning with MobileNetV2 combined with a lightweight deployment framework.

---

# CHAPTER 3: TECHNOLOGY STACK AND TOOLS

### 3.1 Hardware Requirements

Local System

* Intel Core i3 (3rd Generation)
* 8 GB DDR3 RAM
* NVIDIA GT 210 (1 GB)

Cloud Environment

* Google Colab GPU

### 3.2 Software Requirements

* Python 3.12
* Visual Studio Code
* Google Colab
* TensorFlow
* Keras
* Streamlit
* NumPy
* Matplotlib
* Scikit-Learn

### 3.3 Development Environment

Describe:

* UV Package Manager
* Virtual Environment Setup
* Dependency Management

---

# CHAPTER 4: DATASET DESCRIPTION AND EXPLORATORY DATA ANALYSIS

### 4.1 Dataset Source

PlantVillage Dataset

### 4.2 Dataset Overview

| Metric        | Value  |
| ------------- | ------ |
| Total Classes | 10     |
| Total Images  | 16011  |
| Dataset Size  | 247 MB |

### 4.3 Disease Categories

Explain all ten classes individually.

### 4.4 Class Distribution Analysis

Insert:

* Class Distribution Chart
* Dataset Summary Table

### 4.5 Sample Image Visualization

Insert:

* 3×3 or 5×2 image grid

### 4.6 Observations

Discuss:

* Class imbalance
* Largest and smallest classes
* Visual similarity between diseases

---

# CHAPTER 5: DATA PREPROCESSING

### 5.1 Dataset Splitting

| Dataset    | Images |
| ---------- | ------ |
| Train      | 11203  |
| Validation | 3198   |
| Test       | 1610   |

### 5.2 Data Augmentation

Implemented:

* Random Flip
* Random Rotation
* Random Zoom
* Random Translation

### 5.3 Image Resizing

224 × 224 × 3

### 5.4 Label Encoding

Categorical Encoding

### 5.5 Data Pipeline

Explain image_dataset_from_directory()

---

# CHAPTER 6: TRANSFER LEARNING

### 6.1 Introduction to Transfer Learning

Explain:

* Pretrained Models
* ImageNet
* Knowledge Transfer

### 6.2 Why Transfer Learning

Advantages:

* Faster Training
* Better Accuracy
* Reduced Computational Cost

### 6.3 Feature Extraction

Explain:

* Frozen Layers
* Trainable Layers

### 6.4 Fine-Tuning

Explain:

* Unfreezing Layers
* Low Learning Rate Strategy

---

# CHAPTER 7: MODEL ARCHITECTURE

### 7.1 MobileNetV2 Overview

Architecture overview.

### 7.2 Base Model Configuration

Input Shape:

224×224×3

Weights:

ImageNet

include_top=False

### 7.3 Classification Head

* GlobalAveragePooling2D
* Dense(128)
* Dropout
* Dense(10)

### 7.4 Model Summary

Insert model summary screenshot/table.

### 7.5 Parameter Analysis

| Parameter Type | Count     |
| -------------- | --------- |
| Trainable      | 165,258   |
| Non-Trainable  | 2,257,984 |
| Total          | 2,423,242 |

---

# CHAPTER 8: MODEL TRAINING

### 8.1 Training Configuration

Batch Size:

32

Epochs:

15

Loss Function:

Categorical Crossentropy

Optimizer:

Adam

### 8.2 Callbacks

#### Model Checkpoint

Purpose and implementation.

#### Early Stopping

Purpose and implementation.

#### ReduceLROnPlateau

Purpose and implementation.

### 8.3 Feature Extraction Training Results

Insert:

* Training Accuracy Graph
* Validation Accuracy Graph
* Training Loss Graph
* Validation Loss Graph

### 8.4 Training Observations

Discuss learning behavior.

---

# CHAPTER 9: MODEL EVALUATION

### 9.1 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

### 9.2 Baseline Model Results

Accuracy:

91.55%

Loss:

0.2574

### 9.3 Fine-Tuned Model Results

Accuracy:

92.36%

Loss:

0.2283

### 9.4 Classification Report

Insert full classification report table.

### 9.5 Confusion Matrix

Insert confusion matrix image.

### 9.6 Comparative Analysis

Compare:

* Feature Extraction Model
* Fine-Tuned Model

### 9.7 Key Findings

Discuss:

* Mosaic Virus improvement
* Target Spot improvement
* Healthy class improvement

---

# CHAPTER 10: STREAMLIT DEPLOYMENT

### 10.1 Deployment Architecture

Image Upload → Preprocessing → Model Prediction → Result Display

### 10.2 Application Features

* Upload Image
* Disease Prediction
* Confidence Score
* Disease Information

### 10.3 Application Interface

Insert screenshots.

### 10.4 Debugging Process

Discuss:

* Late Blight prediction issue
* Double preprocessing problem
* Resolution process

### 10.5 Final Application

Explain working pipeline.

---

# CHAPTER 11: RESULTS AND DISCUSSION

### 11.1 Overall Performance

Discuss final accuracy.

### 11.2 Strengths

* High Accuracy
* Fast Inference
* Lightweight Architecture

### 11.3 Limitations

* Tomato-only dataset
* Controlled image conditions

### 11.4 Real-World Applicability

Agricultural advisory systems.

---

# CHAPTER 12: CONCLUSION AND FUTURE WORK

### 12.1 Conclusion

Summarize complete project.

Mention:

* Transfer Learning effectiveness
* Fine-Tuning benefits
* Final accuracy

### 12.2 Future Scope

* Multi-crop detection
* Disease severity estimation
* Treatment recommendation system
* Mobile application deployment
* Cloud API integration

---

# REFERENCES

Include references for:

* PlantVillage Dataset
* MobileNetV2 Paper
* TensorFlow Documentation
* Streamlit Documentation
* Transfer Learning Research Papers

---

# APPENDICES

## Appendix A

Training Code

## Appendix B

Streamlit Application Code

## Appendix C

Classification Report

## Appendix D

Confusion Matrix

## Appendix E

Project Diary

## Appendix F

GitHub Repository Link
