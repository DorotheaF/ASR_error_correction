import json
import random

from unsloth import FastLanguageModel, FastModel
import torch
import os
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset

location = ""
# location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/"

with open(location + "data/train_files/all_train.json", "r") as file:
    prompts = json.load(file)

# data_files = {"train": "data/train_files/all_train.json"}
dataset = load_dataset("json", data_dir=location, data_files="data/train_files/all_train.json")

dataset = dataset.map(lambda x: {"text": x["text_reasoning"]})
dataset = dataset.shuffle(seed=42)


print("loaded dataset")

print(dataset)
print(dataset['train']['text'][0])

print(len(dataset))

model, tokenizer = FastModel.from_pretrained(
    # model_name = "unsloth/DeepSeek-R1-Distill-Llama-70B-bnb-4bit", #TODO
    model_name = "unsloth/DeepSeek-R1-Distill-Qwen-32B-unsloth-bnb-4bit",
    # model_name = "unsloth/DeepSeek-R1-Distill-Qwen-1.5B-unsloth-bnb-4bit",
    max_seq_length = 2048, # Choose any for long context!
    load_in_4bit = True,  # 4 bit quantization to reduce memory
    load_in_8bit = False, # [NEW!] A bit more accurate, uses 2x memory
    full_finetuning = False, # [NEW!] We have full finetuning now!
    token = os.getenv("HUGGING_FACE"), # use one if using gated models #TODO,
    device_map = "balanced"
)


# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0, # Supports any, but = 0 is optimized
    bias = "none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing = "unsloth", # True or "unsloth" for very long context

    random_state = 3407,
    max_seq_length = 2048, # Supports RoPE Scaling internally, so choose any!
    use_rslora = False,  # We support rank stabilized LoRA
    loftq_config = None, # And LoftQ
)



trainer = SFTTrainer(
    model = model,
    train_dataset = dataset['train'],
    tokenizer = tokenizer,
    args = SFTConfig(
        # max_seq_length = 2048,
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 10,
        # max_steps = 60,
        logging_steps = 1,
        output_dir = "outputs",
        optim = "adamw_8bit",
        seed = 3407,
        num_train_epochs=1,
    ),
)
trainer.train()

print("finished training")

FastLanguageModel.for_inference(model)

print("saving to ")
model.save_pretrained("finetuned_deepseek32_all_reasoning")

print("should have saved")

# tokenizer.save_pretrained("finetuned_trial_1_deepseek70")
# # Go to https://github.com/unslothai/unsloth/wiki for advanced tips like
# # (1) Saving to GGUF / merging to 16bit for vLLM
# # (2) Continued training from a saved LoRA adapter
# # (3) Adding an evaluation loop / OOMs
# # (4) Customized chat templates