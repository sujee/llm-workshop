# Run LLMs Locally

Running LLMs locally has pros and cons.

**Pros**

- All data remains locally.  Data is not transmitted via API.  This can be very important for sensitive data
- no per use or api use charges
- More control

**Cons**

- **Size**: Running models locally can be challenging; large state of the art models will need significant resources (CPU, memory, GPU)
- **CPU vs. GPU**: LLMs benefit greatly from GPUs (Graphics Processing Units) due to their parallel processing capabilities. A powerful CPU might suffice for smaller models, but a dedicated GPU is highly recommended for larger ones.
- **RAM**: LLMs need substantial RAM (Random Access Memory). The amount required depends on the model size. 16GB or more is generally a good starting point.

## 1 - Run Using UI Clients

There are plenty of UI clients that will let you download and run models locally.

Few favorites:

- [LM Studio](https://lmstudio.ai/) - very easy to use, free to use.
- [Jan.ai](https://jan.ai/) - 100% open source

Download one of the UI clients.

Experiment with some of the models. 

Few pointers:

- you would need a GPU to effectively run large models
- start with smaller models that run well on CPU

**models**

| Model        | Size                     | Description                                                                                                                                  |
|--------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Llama 3.2 1B | Q8 : 1.32 GB             | A tiny and speedy Llama model from Meta, optimized for multilingual dialogue use cases.                                                      |
| Llama 3.2 3B | Q8 : 3.42 GB             | The new and small Llama model from Meta, optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks. |
| Phi 3.1 mini | 2 - 4 GB                 | Small model from Microsoft that runs well on CPU                                                                                             |
| Gemma 2      | 2B : 2.7 GB <br><br> 9B : 9.8 GB | Open source model from Google that offers pretty good performance across all tasks                                                           |                                                                                                         |


## 2 - Run using `Ollama`

[Ollama](https://ollama.com/) is command line client that supports many models

Follow the download installations instructions from the website, and install for your platform

Once you have it installed, follow the quick guide : https://github.com/ollama/ollama/blob/main/README.md#quickstart

### 2.1 - Use Ollama CLI

```bash
ollama run llama3.2:1b
```

Now you can chat with the model

> Write a haiku about cats

> Write python code to read a JSON file

### 2.2 - Use web service

Make sure ollama is running on a terminal

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

To see better formated output, we can use `jq` (Download from [here](https://jqlang.github.io/jq/))


```bash
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2:1b",
  "prompt": "Why is the sky blue?",
  "stream": false
}'  | jq
```

### 2.3 - Using Ollama python API

Code: [ollama_1_intro.ipynb](ollama_1_intro.ipynb)

## 3 - Run Using `llama-cpp`

[llama-cpp](https://github.com/ggerganov/llama.cpp) is another way of running models.

How ever the installation can be a little tricky.

Here are basic instructions for a Ubuntu linux system

```bash
sudo apt install -y build-essential

git clone https://github.com/ggerganov/llama.cpp

cd llama.cpp

make -j
```

Run

```bash
./main --color -m ./models/llama-2-7b-chat.Q5_K_S.gguf  \
  -p "What is the largest city in the world?"

```

