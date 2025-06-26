# Ollama Guide
## ✅ 1. Install

``` macOS (Intel or Apple Silicon)
brew install ollama
```

If you don't have Homebrew:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install Ollama:
```
brew install ollama
```

Linux
```
curl -fsSL https://ollama.com/install.sh | sh
```

Windows
```
Go to: https://ollama.com/download
Download and install the .msi package.
```

```
% ollama
Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command
Flags:
  -h, --help      help for ollama
  -v, --version   Show version information
```  

## ✅ 2. Start the Ollama service

Once installed, start the ollama background server:
```
ollama serve
```
Optionally, you can run it in background:
```
nohup ollama serve > ollama.log 2>&1 &
```
## ✅ 3. Pull and Run LLaMA 3
After starting the server:

```
ollama pull llama3
```
Test running it manually:
```
ollama run llama3

% ollama pull llama3
% ollama run llama3 
>>> What is elliptic curve cryptography
Elliptic curve cryptography (ECC) is a  ....
>>>
```

## ✅ Check Ollama is Running
```
ollama run llama3 <<< "Hello"
```

For a larger model, use 70b:
```
% ollama pull llama3:70b
% ollama run llama3:70b 
```

List our models:

```
% ollama list 
```

For the standard model, we have 8 billion parameters:

```
% ollama show llama3:latest 
  Model
    architecture        llama    
    parameters          8.0B     
    context length      8192     
    embedding length    4096     
    quantization        Q4_0   
Capabilities
    completion    
  Parameters
    num_keep    24                       
    stop        "<|start_header_id|>"    
    stop        "<|end_header_id|>"      
    stop        "<|eot_id|>"             
  License
    META LLAMA 3 COMMUNITY LICENSE AGREEMENT             
    Meta Llama 3 Version Release Date: April 18, 2024  
```

and for 70b we have 70.6 billion parameters:

```
% ollama show llama3:70b   
  Model
    architecture        llama    
    parameters          70.6B    
    context length      8192     
    embedding length    8192     
    quantization        Q4_0  
Capabilities
    completion    
  Parameters
    num_keep    24                       
    stop        "<|start_header_id|>"    
    stop        "<|end_header_id|>"      
    stop        "<|eot_id|>"             
  License
    META LLAMA 3 COMMUNITY LICENSE AGREEMENT             
    Meta Llama 3 Version Release Date: April 18, 2024   
```

⚠️ Add the path to ollama in shell config:

```
export PATH="$PATH:/usr/local/bin"
```
(Or wherever ollama is installed)

Add that line to your ~/.bashrc or ~/.zshrc and restart terminal.





| Model      | Command                       | Notes                           |
| ---------- | ----------------------------- | ------------------------------- |
| LLaMA 3    | `ollama pull llama3`          | Meta's latest, strong reasoning |
| Mistral    | `ollama pull mistral`         | Fast and compact, high quality  |
| Gemma      | `ollama pull gemma`           | From Google, for helpful output |
| Phi        | `ollama pull phi`             | Lightweight and concise         |
| Dolphin    | `ollama pull dolphin-mistral` | Instruction-tuned               |
| Code LLaMA | `ollama pull codellama`       | Great for coding tasks          |
