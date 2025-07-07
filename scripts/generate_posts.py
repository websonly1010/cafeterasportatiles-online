import os
import openai

# Ajusta aquí el número de posts y la longitud deseada
NUM_POSTS = 5
WORDS_PER_POST = 200

openai.api_key = os.getenv("CHATGPT_API_KEY")

DOMAIN = "cafeterasportatiles.online"

def generate_post(title_prompt):
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"Eres un asistente que crea artículos de blog de formato Markdown, con título, subtítulos y texto."},
            {"role":"user","content": title_prompt}
        ],
        temperature=0.7,
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    os.makedirs("posts", exist_ok=True)
    for i in range(1, NUM_POSTS + 1):
        prompt = (
            f"Genera un artículo de aproximadamente {WORDS_PER_POST} palabras sobre '{DOMAIN}', "
            f"título descriptivo y subtítulos en Markdown. Guarda en archivo post_{i}.md"
        )
        content = generate_post(prompt)
        filename = f"posts/post_{i}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✔ Generated {filename}")
