import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


minha_chave = os.getenv("OPENAI_API_KEY") or "sua_chave_aqui"
client = OpenAI(api_key=minha_chave)

@app.route('/', methods=['GET', 'POST'])
def index():
    classificacao = None
    resposta = None
    texto_original = None
    
    if request.method == 'POST':
        texto_original = request.form.get('email_texto')
        
        if texto_original:
            try:
                
                prompt = f"Analise o email: '{texto_original}'. Responda exatamente neste formato: CATEGORIA: [Produtivo ou Improdutivo] | RESPOSTA: [Sugestão de resposta]."
                
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Você é um assistente de triagem bancária."},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                resultado = response.choices[0].message.content
                
                if "|" in resultado:
                    partes = resultado.split('|')
                    classificacao = partes[0].replace("CATEGORIA:", "").strip()
                    resposta = partes[1].replace("RESPOSTA:", "").strip()
                else:
                    classificacao = "Análise Concluída"
                    resposta = resultado

            except Exception as e:
                classificacao = "Erro"
                resposta = f"Erro na API: {str(e)}"

    return render_template('index.html', classificacao=classificacao, resposta=resposta, texto=texto_original)

if __name__ == '__main__':
  
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
