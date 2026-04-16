# Forensic Data Lineage Audit (v7.2)

This document maps the dynamic components of the **Forensic Master Suite** to the raw research logs and notebook artifacts, providing a verifiable "Source of Truth" for the academic viva defense.

## 1. Metric Mapping

| Dashboard Module | Data Source File | Notebook Origin | Metric Type |
| :--- | :--- | :--- | :--- |
| **Capability Radar** | `outputs/research_logs.json` | `LSTM-delivery4.ipynb` / `CNN_delivery4.ipynb` | Capability Vector (0-1) |
| **Learning Vault** | `outputs/research_logs.json` | Training History (`history.history`) | Accuracy / Val_Accuracy |
| **Semantic Topology** | `outputs/research_logs.json` | `clustering_descriptive_analytics_delivery5.ipynb` | PCA-Reduced K-Means Coords |
| **Decision Matrix** | `outputs/research_logs.json` | Confusion Matrix Array | TP, FP, TN, FN |
| **Linguistic Audit** | `outputs/research_logs.json` | `exploredata-delivery3.ipynb` | Chi-Square Slang Frequency |
| **Efficiency Radar** | `outputs/research_logs.json` | Benchmarking Logs | Resource Efficiency Metrics |
| **Corpus Dynamics** | `outputs/research_logs.json` | `exploredata-delivery3.ipynb` | Tweet Length Histogram |
| **Predictor Banks** | `outputs/research_logs.json` | Feature Importance Logic | Top Lexical Predictors |

## 2. Model Architectures

### Architecture A: Bi-Directional LSTM
- **Layer 1**: SpatialDropout1D (0.4) - Context Regularization.
- **Layer 2**: Bi-Directional LSTM (100 units) - Temporal Sentiment capture.
- **Layer 3**: Dense (1 unit, Sigmoid) - Binary Probability outcome.
- **Optimizer**: Adam (lr=0.001).

### Architecture B: Convolutional Neural Network (CNN)
- **Layer 1**: Conv1D (128 filters, kernel=5) - Local feature extraction.
- **Layer 2**: GlobalMaxPooling1D - Spatial activation mapping.
- **Layer 3**: Dense (1 unit, Sigmoid) - Pattern-based sentiment probability.

## 3. Preprocessing Pipeline (Neural Sandbox)
The **Neural Sandbox** in the dashboard simulates the exact logic defined in `setup_project.py` and the delivery notebooks:
1. **Normalization**: Case-lowercase, regex punctuation removal.
2. **Reduction**: Porter Stemming implementation.
3. **Vectorization**: Index-based embedding mapping (Simulated).

## 4. Verification for Viva
- **Live Sync**: The green pulse in the dashboard indicates the JSON pulses are loaded correctly.
- **PDF Report**: Toggle the 'Generate Research Report' button to see the print-ready audit layout.
- **Forensic Trace**: Clicking any chart provides an interactive insight specific to that research area.
