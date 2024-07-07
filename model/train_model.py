from transformers import MarianMTModel, MarianTokenizer 
import torch 

# Load the pre-trained MarianMT model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-es'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Save the model and tokenizer
model.save_pretrained('./model')
tokenizer.save_pretrained('./model')
