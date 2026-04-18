# LoRA-based Instruction Tuning with Knowledge Preservation

👉 **Model**: https://huggingface.co/Mindie/Qwen3-4b-kss-style-tuning
👉 **Code**: https://github.com/byeongmin1/qwen3-4b-lora-instruction-tuning

---

## 📌 Overview

This project investigates whether **LoRA-based instruction tuning** can improve task-specific performance while preserving the base model’s general knowledge.

We design an end-to-end pipeline including:

* data generation
* data filtering and evaluation
* instruction tuning (LoRA)
* knowledge retention evaluation (MMLU)

---

## 🎯 Objective

* Improve instruction-following capability (structured summarization)
* Analyze knowledge retention after fine-tuning
* Validate whether LoRA reduces catastrophic forgetting

---

## 🧠 Key Results

* The fine-tuned model successfully performs structured summarization tasks
* **No significant degradation** in general knowledge performance observed

### 📊 MMLU Evaluation (Logit-based)

We evaluate knowledge retention using logit-based comparison:

* Sample size: 20 questions per subject

| Model      | Avg Logit (Correct Answer) |
| ---------- | -------------------------- |
| Base Model | (0.7254)                     |
| LoRA Model | (0.7245)                     |

* Δ (Base -LoRA): **(0.009)**

**Result:**
The difference is negligible, indicating that general knowledge is preserved.

---

## 🏗️ Pipeline

### 1. Data Generation

* Source: Articles
* Task: Generate structured summaries (KSS-style format)

---

### 2. Data Filtering & Evaluation

#### (1) Format Validation

* Rule-based algorithm checks format consistency
* Invalid samples are regenerated

#### (2) Semantic Filtering

* Similarity between article and summary is measured
* Ensures semantic alignment

#### (3) Quality Sampling

* Top 10% (high similarity)
* Bottom 10% (low similarity)
* Random 10% (middle)

LLM model evaluation performed across all groups.

---

### 3. Model Training

* **Method**: LoRA fine-tuning

* **Objective**: Structured summarization (instruction following)

* **Training Strategy**:
  A contrastive instruction setup was applied:

  * *Use KSS-style summaries*
  * *Do not use KSS-style summaries*

This allows the model to learn both format generation and format suppression.

---

### 4. Evaluation

#### Instruction Following

* Evaluated on structured summarization tasks

#### Knowledge Retention (MMLU)

* Logit-based evaluation (not generation-based)
* Base vs fine-tuned model comparison

---

## 📊 Dataset

To construct a balanced dataset, both long-form and short-form texts were used.

* Articles → main training data (long-form)
* GPT-generated data → short-form supplementation

---

### 1. Article-based Data

* **Article → Generated Structured Summary (KSS-style)**

  * Main dataset used for training
  * Generated through filtering pipeline
  * 👉 https://huggingface.co/datasets/Mindie/Summary_article_KSS_style_dataset

* **Article → Generated Summary (Not structured)**

  * Generated without instruction
  * Used for *“Do not use KSS-style”* training

---

### 2. GPT-generated Data

* **GPT-generated Structured Summary**

  * Provides short structured examples

* **GPT-generated Summary (Not structured)**

  * Provides short unstructured examples

---

### Note

* Only KSS-style article–summary pairs are stored

* Other data types are used during training and filtering

* GPT data is generated:

  * with format instruction → structured
  * without instruction → unstructured

---

## 🤖 Model

* **Base Model**: Qwen3-4B
* **Fine-tuned Model**: https://huggingface.co/Mindie/Qwen3-4b-kss-style-tuning
* **Method**: LoRA (PEFT)
* **Similarity Model**: google/embeddinggemma-300m
* **Quality Evaluation Model**: google/gemma-3-4b-it

---

## 🔁 Reproducibility

This repository provides:

* Data generation pipeline
* Filtering & evaluation code
* Dummy/sample dataset

You can reproduce:

* format validation
* filtering pipeline
* similarity scoring
* LLM model evaluating data quality

---

## 🚀 Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Mindie/Qwen3-4b-kss-style-tuning"
)

tokenizer = AutoTokenizer.from_pretrained(
    "Mindie/Qwen3-4b-kss-style-tuning"
)
```

---

## ⚠️ Limitations

* MMLU evaluation uses sampled subset
* Full dataset not publicly released
* Results depend on training configuration

---

## 🚀 Future Work

* Full-scale MMLU evaluation
* Comparison with full fine-tuning
* Data quality vs performance analysis

---

## 🛠️ Tech Stack

* Python
* Hugging Face Transformers
* LoRA (PEFT)

---

## 📂 Repository Structure

```
project/
  config
  codes/
  data/
```

---

## 🧩 Key Insight

LoRA enables effective instruction tuning while preserving general knowledge,
but this behavior depends on data quality and training design.
