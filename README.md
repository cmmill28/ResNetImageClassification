# 2D Image Classification

## Requirements

- Python 3.8
- PyTorch
- Torchvision

## Train and Evaluate
- `cd ".\ResNetImageClassification"`
- `python train/main.py --image_dir dataset --model_dir models --epochs 10` - Train the model
- `python train/main.py --image_dir dataset --model_dir models --warmup_model_dir models --epochs 10` - Train the model from a checkpoint
- `python eval_image.py --image_dir ./run --model_dir ./models --output ./predictions.txt` - To evaluate images. See the output of `python eval_image.py --help` for arguments.
