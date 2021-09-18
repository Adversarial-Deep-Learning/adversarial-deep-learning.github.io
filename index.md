---
layout: default
title: Adversarial Deep Learning Website
nav_exclude: true
---
# Table of Contents

## Unit-1: Introduction

### 1. Introduction

1. Motivation  
2. Overview  
3. Outline of following chapters  

### 2. Brief Introduction to Deep Learning Concepts

1. Types of learning paradigms:
    - Supervised learning
    - Semi-supervised learning
    - Unsupervised learning

2. Artificial Neural Network
3. Convolutions and CNN
4. Recurrent Neural Networks
5. Encoder-Decoder
6. Auto-Encoders
7. Domain adaptation
8. Transformer

### 3. Background and Notation on Adversarial Deep Learning

1. History
2. Why do adversarial examples occur
    - High dimensionality
    - Insufficient data
    - Linearity of distribution
    - Robust and Non-Robust features
    - Overparameterization
3. Basic Notation
4. Taxonomy
5. Threat Model
    - Adversary’s goal
    - Adversary’s knowledge
        - White Box
        - Black Box
        - Grey Box
    - Victim models
6. Security Evaluation

### 4. Common Algorithms for Adversarial Testing of Deep Learning

1. Generation of Adversarial Examples
    - Box-Constrained L-BFGS
    - Fast Gradient Sign Method (FGSM)
    - Basic Iterative Method (BIM)
2. Evasion Black-Box Attacks
    - Houdini
    - Substitute Mode

## Unit-2: Adversarial Learning in Computer Vision

### 5. Attacking an Image Classifier

1. Evasion White-Box Attacks
    - Carlini and Wagner Attacks (C&W)
    - Deep Fool
    - Universal Attack
    - Ground Truth Attack
2. Evasion Black-Box Attacks
    - One-Pixel Attack
    - Upset and Angri
    - Zeroth Order Optimization (ZOO) based Attack
    - Query Efficient Black Box Attack
    - Adversarial Transformation Networks (ATNs)
    - Generative Adversarial Networks (GANs)
3. Poisoning Attacks
4. Attacks in the Real World
    - Cell-phone Camera Attack
    - Road Sign Attack
    - Cyberspace Attack
    - 3D Adversarial Object
    - Robotic Vision

### 6. Defending Against Adversarial Attacks

1. Recovering the True Labels of Adversarial Examples
    - Robust Optimization
        - Network Regularization
        - Adversarial Training
        - Provable Defenses
    - Gradient Masking/Obfuscation
        - Defensive Distillation
        - Shattered Gradients
        - Randomized Gradients
        - Exploding & Vanishing Gradients
2. Detecting and Rejecting Adversarial Example
    - Training-based Detection
    - Criteria-based Detection
        - Feature Squeezing
        - Artifacts
        - MagNet

## Unit-3: Adversarial Learning in Natural Language Processing

### Defense on NLP has just started last year so current existing papers are less than 10

1. Character-level
    - Typo correction
    - Robust encoding
    - Learning to Discriminate Perturbations
2. Word-level  

### 8. Attacking

### 9. Defense

## Unit-4: Exploring Further

### 10. Adversarial Attacks on Security

### 11. Adversarial Attacks on Interpretability

### 12. Adversarial Attacks on Privacy

### 13. Fairness and Adversarial Learning

1. The Concept of Fairness
    - Social Perspective
    - Probabilistic Perspective
2. Fairness by Adversarial Learning

### 14. Adversarial Attacks against Bayesian Learning

### 15. Adversarial Attacks against Reinforcement Learning

### 16. Adversarial Attacks against Quantum

### 17. Adversarial Attacks against Graph Learning

### 18. Adversarial Training for Improving Model Generalization

1. Domain Adaptation
2. Supervised and Semi-Supervised Classification
3. Regularization through Adversarial Learning
4. Why does adversarial training work?

### 19. Generative Adversarial Networks

### 20. A lawyer’s perspective on Adversaries and Adversarial Examples

---

## Week 3 — Privacy Attacks

- Stealing Machine Learning Models via Prediction APIs
- Model Reconstruction from Model Explanations
- Membership Inference Attacks Against Machine Learning Model

## Week 4 - Poisoning Attacks

- Poisoning Attacks against Support Vector Machines
- Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks
- Stronger Data Poisoning Attacks Break Data Sanitization Defenses
- Transferable Clean-Label Poisoning Attacks on Deep Neural Nets

## Week 5 - Evasion Attacks (Adversarial Examples)

- Explaining and Harnessing Adversarial Examples
- Towards Evaluating the Robustness of Neural Networks
- Why Do Adversarial Attacks Transfer? Explaining Transferability of Evasion and Poisoning Attacks

## Week 6 - Defense against Poisoning Attacks

- Certified Defenses for Data Poisoning Attacks
- Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels
- Robust Logistic Regression and Classification

## Week 7 - Advanced Adversarial Attacks

- Understanding Black-box Predictions via Influence Functions
- Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent
- Comprehensive Privacy Analysis of Deep Learning: Passive and Active White-box Inference
Attacks against Centralized and Federated Learning

## Week 8 - Privacy Defenses

- Machine Learning with Membership Privacy using Adversarial Regularization
- Privacy-preserving Prediction
- Deep Learning with Differential Privacy

## Week 9 - Defenses against Adversarial Examples

- Towards Deep Learning Models Resistant to Adversarial Attacks
- Certified Defenses against Adversarial Examples
- An abstract domain for certifying neural networks

## Week 10 - Advanced topics on Adversarial Examples

- Adversarially Robust Generalization Requires More Data
- Adversarial Examples Are Not Bugs, They Are Features
- Theoretically Principled Trade-off between Robustness and Accuracy