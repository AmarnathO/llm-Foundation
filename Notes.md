**Setup Realted Notes**
- uv venev --python 3.12 : install specific version
- uv init : project initialization 
- source .venv/boin/actovate : activate venv
- uv python pin --glocal 3.12 : to set a version as global


**Git Setup** 
- git remote add origin https://github.com/YOUR_USERNAME/ollama-project.git : Adding remote repo 

- git branch -M main :  rename branch to main

- git remote set-url origin https://github.com/AmarnathO/llm-engineering.git  : Set teh name of Remote Repo as origin 


- git pull --no-rebase origin main
- git pull origin main --no-rebase 
--allow-unrelated-histories
- git push -u origin main


**Open Source LLM**
- llama from meta 
- mixtral from mistral
- deep seek from Deep Seek AI 
- qwen from Alibaba
- geema from google
- Phi from microsoft 


**Three Ways top use LLM**
-  **Chat Interface** : Eg :  chatgpt / Anthropic / gemani etc 

-  **Cloud API or LLM API** : Amazon bedrock / vertex from google / Azure ML / GroQ - Allow to run model on property hardware / Open Router 

-  **Direct Inference** : with Hugging face tranbsformer library / Ollama to run model locally 

##Flavours of LLM##
- **Base Model** : Predict the next token or word. Not very good at following instructions

- **Chat or instruct model** : Chat ways of model Model / System / Assistnt struchered 

- **Reasoning Model** : Reasoning model first think then answer

** The amount of reasoning model does is called as reasonnig budget or reasoning effort and there is technique called as budget forcing when we make a model to think more longer and do reasoning. The results are really amazing and there is a paper call as S1 that google put out - It's just add a word wait** 

**Context Window**
- max number of token that a model can have before it generate the next token 

**API Cost**
- in general subscription we have fixedmointhly cost 
- in API calls we have to pay for each API call that we made based on input and outout tokens - thsi also include the reasoning token utilised that has been done by model 

www.vellum.ai/llm/leaderboard : to see the model leading - context window and API cost specifically.


**TransFormer**
- These are Deep learning architecture that helps model to understand relation ship betwwen words in a sentense.

Sentences -> 
Tokenise - > Embedding + position information : convert token id into vector -> transformer layer (self attention) 
- > Output probablity - Calculate scores for possible next tokens - > generate output

**There are three important Transformer architecture patterns:**

- **Encoder-only** : Commonly used for text classification, sentiment analysis, named entity recognition, and semantic representations.
Eg : BERT


**Decoder** — Primarily used to generate text, one token at a time. Used for chatbots, code generation, writing, reasoning, and other generative AI applications.

Eg : llama , Gpt, Claude 

**Encoder–Decoder** — Used to transform one sequence into another, such as translating English into French.

Used for translation, summarization, and transforming input text into output text.

Eg : T5 and BART



#Prompt Caching#
- *Openai* :  Cache ht is only possible for exact prefix match within a prompt - For this we need to place static content like instructions and example at the begining of the prompty and then in teh en d that user variable part. ~ 40% Saving 

- Anthropic : You have to tell what you are caching and pay 25% more to prime the cache then you payt 10x less to reuse.

- gemani : Support both implicit and explicit caching 





