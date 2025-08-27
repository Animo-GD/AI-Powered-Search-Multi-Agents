#!/bin/bash
set -e  

# Step 1: Create venv if not exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
else
    echo "✅ Virtual environment already exists."
fi

# Step 2: Activate venv
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Step 3: Install dependencies
echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🎉 Setup completed successfully!"
