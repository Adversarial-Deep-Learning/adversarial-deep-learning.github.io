#!/bin/bash
mkdir adl_tutorials
cd adl_tutorials
git init
git remote add origin -f https://github.com/Adversarial-Deep-Learning/code-soup.git
git config core.sparseCheckout true 
git sparse-checkout set Tutorials
git pull origin main
echo "Done Cloning Code-Soup's tutorial"