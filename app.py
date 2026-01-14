import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

load_dotenv()

api_key_env = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    classificacao = None
    resposta = None
    texto_original = None

    if request.method == 'POST':
        texto_original = request.form.get('email_texto')
        
        if texto_original:
            
            prompt = f"Analise este email: '{texto_original}'. Responda estritamente no formato: CATEGORIA: [Produtivo ou Improdutivo] | RESPOSTA: [Sua sugestão]."
            
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "Você é um assistente bancário eficiente."},
                          {"role": "user", "content": prompt}]
            )
            
            resultado = response.choices[0].message.content
            
            classificacao = resultado.split('|')[0].replace("CATEGORIA:", "").strip()
            resposta = resultado.split('|')[1].replace("RESPOSTA:", "").strip()

    return render_template('index.html', classificacao=classificacao, resposta=resposta, texto=texto_original)

if __name__ == '__main__':
    app.run(debug=True)
