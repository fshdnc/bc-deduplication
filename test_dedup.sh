#!/bin/bash
#SBATCH --job-name=dedup
#SBATCH --account=project_2002085
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=10G
#SBATCH --partition=test
#SBATCH --output=/scratch/project_2002085/lihsin/dedup/stdout-%j.txt
#SBATCH --error=/scratch/project_2002085/lihsin/dedup/stderr-%j.txt


cd /scratch/project_2002085/lihsin/
export LD_LIBRARY_PATH=/scratch/project_2002085/lihsin/lib
./lib/onion dedup/all.txt > dedup/all-deduped.txt
