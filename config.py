class Config:
    # datas
    RAW_DATA_PATH = "./data/raw_article.json"
    PREPROCESSED_DATA_PATH = "./data/preprocessed_data.json"
    DUMMY_DATA_PATH = "./data/dummy_data.json"
    GPT_DATA_PATH = "./data/gpt_data.json"
    MODEL_GENERATE_DATA_NO_KSS_PATH = "./data/model_generate_data_no_kss.json"

    #seed
    SEED = 42

    # models
    BASE_MODEL_NAME = "Qwen/Qwen3-4B"
    TRAINED_MODEL_NAME = "Mindie/Qwen3-4b-kss-style-tuning"
    SENTENCE_MODEL = "google/embeddinggemma-300m"
    EVAL_MODEL = "google/gemma-3-4b-it"

    #loar config
    TASK_TYPE = "CAUSAL_LM"
    R = 16
    LORA_ALPHA = 32
    TARGET_MODULES = 'all-linear'

    # training
    LR = 1e-5
    BATCH_SIZE = 2
    EPOCHS = 5
    WARM_UP = 0.1
    GRADIENT_ACCUM = 2
