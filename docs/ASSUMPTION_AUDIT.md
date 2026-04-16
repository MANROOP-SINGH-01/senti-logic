# Viva Defense: Assumption Audit

This document justifies the technical decisions made during the Social Media Sentiment Analysis project. Use this as a reference during interrogation.

## 1. Why Sentiment140?
- **Justification**: Scale (1.6M records) is required to train the 400,000 dense weights in the GloVe embedding layer. Small datasets do not provide enough variance for LSTM context retention.

## 2. Why LSTM over Naive Bayes?
- **Justification**: Naive Bayes (Bag-of-Words) assumes word independence. It ignores the sequence. LSTM (Long Short-Term Memory) captures the "Distance Context." In sentiment, "Not happy" is the opposite of "Happy." LSTM understands the 'Not' modifies 'Happy'.

## 3. Why the 20% Test Split?
- **Justification**: Standard academic practice for large-scale datasets (320,000 test tweets) provides high statistical confidence that the accuracy reported is not due to overfitting on a small set.

## 4. Why Snowball Stemming?
- **Justification**: Snowball is faster and more aggressive than Porter stemming. For Twitter language where suffixes are often mangled, reducing words to their roots is essential to combat the "Sparsity Problem."

## 5. Why K-Means for Unsupervised?
- **Justification**: Used as an exploratory tool to confirm if the 1.6M records naturally cluster into sentiment groups without labels. K=2 was chosen via the elbow method to test the simplest polar divide.

## 6. What if the Accuracy is capped?
- **Defense**: Accuracy (~78.9%) is limited by the "Ambient Noise" of Twitter. Human inter-annotator agreement on sentiment is often only ~80-85%. Achieving 79% on automated classification suggests the model is approaching human-level performance limits for this noisy domain.

## 7. Handling Sarcasm
- **Admission**: The current architecture is "Semantically Shallow." Sarcasm detection requires world-knowledge context. We acknowledge this as a boundary of the research.
