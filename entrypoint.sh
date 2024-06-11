      
#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve LLAMA2 model..."
ollama pull llama2
echo "🟢 Done!"

# Signal to the 'app' container that the model is ready
# touch /ready  # Create a file named 'ready'

# Wait for Ollama process to finish.
wait $pid
