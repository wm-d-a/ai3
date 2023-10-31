from transformers import AutoTokenizer, T5ForConditionalGeneration


def get_corrected_text(text):
    tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
    model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")
    input_text = text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=256)
    edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return edited_text


if __name__ == '__main__':
    print(get_corrected_text(
        'Fix grammatical errors in this sentence: When I grow up, I start to understand what he said is quite right.'))

