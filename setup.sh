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

# Step 4: Check & pull Ollama models
models=("qwen2.5-coder" "gemma:2b")

for model in "${models[@]}"; do
    if ollama list | grep -q "$model"; then
        echo "✅ Model '$model' already pulled."
    else
        echo "⬇️ Pulling model '$model'..."
        ollama pull "$model"
    fi
done

echo "🎉 Setup completed successfully!"
