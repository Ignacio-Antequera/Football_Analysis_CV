#!/bin/bash
#SBATCH -p dgx,dgx2,dios
#SBATCH --gres=gpu:1
#SBATCH --mem=30G
#SBATCH -c 16
#SBATCH -o /mnt/homeGPU/iantequera/My_Code/Football_Analysis_CV/slurm_outputs/%A.out
#SBATCH -e /mnt/homeGPU/iantequera/My_Code/Football_Analysis_CV/slurm_outputs/%A.err
#SBATCH --job-name football_analysis

# Verificar CUDA disponible
nvidia-smi
echo "CUDA_HOME: $CUDA_HOME"
ls -la /usr/local/cuda*/version.txt 2>/dev/null || echo "No CUDA version.txt found"

eval "$(conda shell.bash hook)"
conda activate /mnt/homeGPU/iantequera/My_Code/Football_Analysis_CV/.conda

# Verificar torch instalado
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"

python /mnt/homeGPU/iantequera/My_Code/Football_Analysis_CV/main.py