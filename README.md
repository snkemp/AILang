# AILang
Training a neural network to design a programming language

# Finetuning

To finetune an off-the-shelf GPT model, you can run the following bash code:
```{bash}
#!/bin/bash
python -m torch.distributed.launch \
    --nproc_per_node <NUMBER_OF_LOCAL_GPUS> run_lm_finetuning.py \
    --model_type gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --train_data_file=../../data/train.comments.g4 \
    --output_dir=../../output \
    --num_train_epochs 1000
```

# Generation

To generate new text given a prompt and a path to a checkpoint:

```
python run_generation.py --model_type=gpt2 \
                         --model_name_or_path=../../output/checkpoint-2500 \
                         --length 800 --prompt "<YOUR PROMPT>"
```