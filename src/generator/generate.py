from transformers import pipeline

# Use a model fine-tuned for QA or instruction-following generation
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question, context):
    prompt = f"question: {question} context: {context}"
    response = qa_pipeline(prompt, max_new_tokens=100)
    # Flan-T5 returns generated text in 'generated_text' or just string depending on version
    answer = response[0]['generated_text'] if 'generated_text' in response[0] else response[0]['summary_text'] if 'summary_text' in response[0] else response[0]
    return answer.strip()
