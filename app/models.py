from transformers import pipeline

def get_answer_from_model(question, context):
    generator = pipeline("text2text-generation", "t5-small")
    input_text = f"question: {question}, context: {context}"
    result = generator(input_text, max_length=100)
    return result[0]['generated_text']