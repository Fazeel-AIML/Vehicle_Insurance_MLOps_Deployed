# Vehicle Insurance Prediction

This project implements a machine learning model to predict vehicle insurance claims or premiums based on historical data. It includes a full pipeline for data preprocessing, model training, evaluation, and deployment, with a web service for real-time predictions. The project leverages Docker for containerization, DVC for data versioning, GitHub Actions for CI/CD, and AWS S3 for storing model artifacts.

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Project Overview

The Vehicle Insurance Prediction project aims to predict insurance outcomes (e.g., claim likelihood or premium amounts) using machine learning. Key features include:
- A machine learning pipeline for training and evaluating models on vehicle insurance data.
- A web service for serving predictions, with customizable styles and port configurations.
- CI/CD workflows using GitHub Actions for automated testing and deployment to AWS S3.
- Containerization with Docker for consistent development and deployment environments.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Docker (for containerized deployment)
- DVC (for data and model versioning)
- AWS CLI (for S3 uploads)
- Git (for version control)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Fazeel-AIML/Vehicle_Insurance_MLOps_Deployed
   cd Vehicle_Insurance_MLOps_Deployed
2. Python dependencies:
   ```bash
   pip install -r requirements.txt
3. Set up DVC
   ```bash
   dvc init
   dvc pull
To run:
  ```bash
  python main.py


---
