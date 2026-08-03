# PROJECT DIARY

## Project Title:

**Tomato Plant Disease Detection Using Transfer Learning and Deep Learning**

---

## Date: 09-06-2026

---

### Task 1: Project Environment Setup

#### Description

Initialized the project environment and configured all required development tools.

#### Technical Details

* Installed UV package manager.
* Created a virtual environment using Python 3.12.
* Configured Visual Studio Code workspace.
* Installed tensorflow-cpu, pandas, numpy, matplotlib, pillow and jupyter dependencies.
* Verified TensorFlow installation.

#### Challenges

* Pylance reported missing module errors initially.
* Notebook dependency was required for proper environment recognition.

#### Actions Taken

* Installed notebook package.
* Reconfigured Python interpreter in VS Code.

#### Result

* Development environment successfully configured.

#### Learning

* Learned environment management using UV.
* Understood dependency isolation and project reproducibility.

---

## Date: 09-06-2026

---

### Task 2: Project Planning and Requirement Analysis

#### Description

Defined project scope, objectives, workflow, and technology stack.

#### Technical Details

* Selected PlantVillage dataset.
* Chose MobileNetV2 as the base model.
* Selected Streamlit for deployment.
* Designed project architecture and folder structure.

#### Challenges

* Deciding between single-crop and multi-crop classification.

#### Actions Taken

* Evaluated dataset complexity.
* Selected Tomato-only disease classification approach.

#### Result

* Final project scope established.

#### Learning

* Learned how project requirements influence model design decisions.

---

## Date: 10-06-2026

---

### Task 3: Dataset Acquisition

#### Description

Collected and organized the PlantVillage Tomato Dataset.

#### Technical Details

* Downloaded PlantVillage dataset.
* Extracted dataset files.
* Verified image integrity and class folders.

#### Dataset Statistics

* Total Classes: 10
* Total Images: 16,011
* Dataset Size: 247 MB

#### Challenges

* Understanding dataset organization.

#### Actions Taken

* Examined directory structure and class distribution.

#### Result

* Dataset successfully acquired and verified.

#### Learning

* Learned the importance of dataset quality before training.

---

## Date: 11-06-2026

---

### Task 4: Exploratory Data Analysis (EDA)

#### Description

Performed initial analysis of dataset characteristics.

#### Technical Details

* Counted images in each class.
* Generated class-wise statistics.
* Calculated dataset summary metrics.

#### Dataset Summary

* Total Classes: 10
* Total Images: 16,011
* Largest Class: Tomato Yellow Leaf Curl Virus (3208 Images)
* Smallest Class: Tomato Mosaic Virus (373 Images)
* Average Images per Class: 1601.1

#### Challenges

* Long class names affecting chart readability.

#### Actions Taken

* Created structured DataFrame summaries.
* Improved chart labeling.

#### Result

* Dataset distribution successfully analyzed.

#### Learning

* Learned how class imbalance can affect model performance.

---

## Date: 11-06-2026

---

### Task 5: Dataset Visualization

#### Description

Visualized class distribution and sample images.

#### Technical Details

* Created class distribution charts.
* Displayed sample images from each class.
* Examined visual characteristics of diseases.

#### Challenges

* Learning Matplotlib visualization techniques.

#### Actions Taken

* Developed image visualization utilities.

#### Result

* Better understanding of disease patterns.

#### Learning

* Learned image data exploration techniques.

---

## Date: 12-06-2026

---

### Task 6: Dataset Splitting

#### Description

Prepared train, validation, and test datasets.

#### Technical Details

Dataset split:

| Dataset    | Images |
| ---------- | ------ |
| Train      | 11,203 |
| Validation | 3,198  |
| Test       | 1,610  |

#### Challenges

* Maintaining class balance across splits.

#### Actions Taken

* Automated dataset splitting process.

#### Result

* Training-ready dataset generated.

#### Learning

* Learned the purpose of train, validation, and test sets.

---

## Date: 14-06-2026
____________________

### Task 2: Google Colab Configuration

#### Description

Configured Google Colab for cloud-based model training because the local system had limited hardware resources for deep learning training.

#### Technical Details

- Used Google Colab for training the deep learning model.
- Enabled GPU runtime.
- Verified GPU availability.
- Mounted Google Drive.
- Uploaded dataset/model files to Google Drive.
- Used Google Drive paths for saving trained models and outputs.

#### Hardware Reason

Local system specifications:

- Processor: Intel i3 3rd Generation
- RAM: 8 GB DDR3
- GPU: NVIDIA Zotac GT 210, 1 GB

Due to limited GPU support for modern TensorFlow training, Google Colab was selected for efficient model training.

#### Colab Setup Steps

- Opened Google Colab notebook.
- Changed runtime type to GPU.
- Verified TensorFlow and GPU availability.
- Mounted Google Drive using:

```python
from google.colab import drive
drive.mount('/content/drive')
```

#### Challenges

- Initial GPU was not detected.
- Dataset needed to be properly uploaded and extracted in Colab.
- Paths had to be managed carefully between Google Drive and Colab runtime.

#### Actions Taken

- Enabled GPU from Runtime settings.
- Verified GPU availability using TensorFlow.
- Uploaded dataset to Google Drive.
- Extracted dataset inside Colab runtime.
- Saved trained model files directly to Google Drive.

#### Result

Google Colab was successfully configured for model training using GPU acceleration.

#### Learning

- Learned how to use cloud-based GPU resources.
- Understood why local hardware may not be suitable for deep learning training.
- Learned Google Drive mounting and file path management in Colab.
- Learned how to save trained models persistently from Colab.

---

## Date: 14-06-2026

---

### Task 7: Data Augmentation Pipeline

#### Description

Implemented image augmentation techniques.

#### Technical Details

Applied:

* Random Flip
* Random Rotation
* Random Zoom
* Random Translation

#### Challenges

* Selecting augmentation parameters.

#### Actions Taken

* Tested various augmentation combinations.

#### Result

* Improved dataset variability.

#### Learning

* Learned how augmentation improves generalization.

---

## Date: 15-06-2026

---

### Task 8: Transfer Learning Research

#### Description

Studied transfer learning concepts before implementation.

#### Technical Details

* Learned ImageNet pretraining.
* Studied feature extraction.
* Studied fine-tuning strategies.
* Compared CNN architectures.

#### Challenges

* Understanding feature extraction vs fine-tuning.

#### Actions Taken

* Conducted detailed theoretical analysis.

#### Result

* Clear understanding of transfer learning workflow.

#### Learning

* Learned how pretrained models transfer knowledge to new tasks.

---

## Date: 16-06-2026

---

### Task 9: Model Architecture Development

#### Description

Built the disease classification model.

#### Technical Details

Base Model:

* MobileNetV2
* Input Shape: 224×224×3
* ImageNet Weights
* include_top=False

Classification Head:

* GlobalAveragePooling2D
* Dense(128)
* Dropout
* Dense(10)

Model Parameters:

* Total Parameters: 2,423,242
* Trainable Parameters: 165,258
* Non-Trainable Parameters: 2,257,984

#### Challenges

* Selecting suitable architecture.

#### Actions Taken

* Evaluated lightweight transfer learning models.

#### Result

* Final model architecture completed.

#### Learning

* Learned model design using pretrained networks.

---

## Date: 16-06-2026

---

### Task 10: Training Configuration

#### Description

Configured training pipeline.

#### Technical Details

* Loss Function: Categorical Crossentropy
* Batch Size: 32
* Epochs: 16
* Optimizer: Adam

Callbacks:

* ModelCheckpoint
* EarlyStopping
* ReduceLROnPlateau

#### Challenges

* Selecting appropriate callbacks.

#### Actions Taken

* Implemented training monitoring strategies.

#### Result

* Robust training configuration established.

#### Learning

* Learned callback-based training optimization.

---

## Date: 16-06-2026

---

### Task 11: Feature Extraction Training

#### Description

Trained the classifier head while keeping MobileNetV2 frozen.

#### Technical Details

* MobileNetV2 frozen.
* Classification layers trained.

#### Results

Final Validation Accuracy:

* 85.52%

#### Challenges

* Monitoring overfitting.

#### Actions Taken

* Used validation monitoring and checkpoints.

#### Result

* Strong baseline model generated.

#### Learning

* Learned feature extraction training workflow.

---

## Date: 16-06-2026

---

### Task 12: Baseline Model Evaluation

#### Description

Evaluated feature extraction model.

#### Results

* Test Accuracy: 90.87%
* Test Loss: 0.2574

#### Additional Analysis

* Classification Report
* Confusion Matrix
* Precision
* Recall
* F1-Score

#### Challenges

* Understanding class-wise performance.

#### Actions Taken

* Detailed confusion matrix analysis.
* Detailed classification_report analysis.

#### Result

* Identified weak classes.

#### Learning

* Learned model evaluation methodology.

---

## Date: 17-06-2026

---

### Task 13: Fine-Tuning MobileNetV2

#### Description

Improved performance by unfreezing upper layers.

#### Technical Details

* Unfroze upper MobileNetV2 layers.
* Reduced learning rate.
* Re-trained model.

#### Challenges

* Preventing catastrophic forgetting.

#### Actions Taken

* Used very small learning rate.

#### Result

* Improved model performance.

#### Learning

* Learned advanced transfer learning techniques.

---

## Date: 18-06-2026

---

### Task 14: Fine-Tuned Model Evaluation

#### Description

Evaluated the fine-tuned model.

#### Results

| Metric        | Value  |
| ------------- | ------ |
| Test Accuracy | 92.36% |
| Test Loss     | 0.2283 |

#### Major Improvement

Tomato Mosaic Virus:

* Recall improved from 52.6% to 100%

#### Challenges

* Analyzing class-wise trade-offs.

#### Actions Taken

* Compared baseline and fine-tuned models.

#### Result

* Fine-tuned model selected as final model.

#### Learning

* Learned performance comparison techniques.

---

## Date: 18-06-2026

---

### Task 15: Model Export and Serialization

#### Description

Prepared model for deployment.

#### Technical Details

Saved:

* final_tomato_disease_model.keras
* class_names.json

#### Challenges

* Maintaining class mapping consistency.

#### Actions Taken

* Exported class labels separately.

#### Result

* Deployment-ready model created.

#### Learning

* Learned model deployment preparation.

---

## Date: 19-06-2026

---

### Task 16: Streamlit Application Development

#### Description

Developed a web-based prediction application.

#### Features

* Image Upload
* Disease Prediction
* Confidence Score
* Top Predictions
* Disease Information

#### Challenges

* Integrating TensorFlow model with Streamlit.

#### Actions Taken

* Built modular prediction pipeline.

#### Result

* Functional disease detection application.

#### Learning

* Learned ML application deployment workflow.

---

## Date: 19-06-2026

---

### Task 17: Application Debugging and Testing

#### Description

Resolved prediction inconsistencies.

#### Major Issue

Application consistently predicted Late Blight.

#### Root Cause

Double preprocessing of images.

#### Actions Taken

* Removed duplicate MobileNetV2 preprocessing.
* Corrected image pipeline.

#### Result

* Prediction accuracy restored.

#### Learning

* Learned real-world deployment debugging techniques.

---

## Date: 20-06-2026

---

### Task 18: Project Documentation

#### Description

Prepared complete project documentation.

#### Documents Created

* Project Diary
* README.md
* Training Documentation
* Evaluation Reports
* Deployment Guide

#### Result

* Project documentation completed.

#### Learning

* Learned software project documentation standards.

---

## Date: 20-06-2026

---

### Task 19: Final Project Completion

#### Description

Completed development, evaluation, and deployment phases.

#### Final Deliverables

* Trained Deep Learning Model
* Streamlit Web Application
* Project Report
* Presentation Slides
* GitHub Repository
* Project Documentation

#### Final Outcome

Successfully developed a Deep Learning-based Tomato Plant Disease Detection System using MobileNetV2 Transfer Learning with a final test accuracy of 92.36%.

#### Key Learning Summary

* Transfer Learning
* Deep Learning Fundamentals
* Computer Vision
* TensorFlow & Keras
* Model Evaluation
* Streamlit Deployment
* Project Documentation
* Debugging and Problem Solving
* End-to-End Machine Learning Workflow

--------------------------------------------------------------------------------
