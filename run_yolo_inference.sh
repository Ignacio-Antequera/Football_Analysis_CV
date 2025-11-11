#!/bin/bash
#SBATCH -p dios
#SBATCH --gres=gpu:1
#SBATCH --mem=30G
#SBATCH -c 16
#SBATCH -o /mnt/homeGPU/iantequera/Football_Analysis_CV/slurm_outputs/%A.out
#SBATCH -e /mnt/homeGPU/iantequera/Football_Analysis_CV/slurm_outputs/%A.err
#SBATCH --job-name yolo_inference

eval "$(conda shell.bash hook)"
conda activate /home/iantequera/Football_Analysis_CV/.conda
python /home/iantequera/Football_Analysis_CV/yolo_inference.py
