import torch
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

MODEL_NAME = "Qwen/Qwen2.5-Coder-7B-Instruct"
PATH_FONTES = "./fontes"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, 
    quantization_config=bnb_config, 
    device_map="auto",
    use_cache=True
)

def executar_agente(role, tarefa, contexto="", max_tokens=512):
    """Função única e otimizada para todos os agentes."""
    prompt = f"<|im_start|>system\n{role}. Seja técnico, direto e ignore informalidades.<|im_end|>\n"
    prompt += f"<|im_start|>user\n{contexto}\nTAREFA: {tarefa}<|im_end|>\n<|im_start|>assistant\n"
    
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    
    with torch.no_grad():
        out = model.generate(
            **inputs, 
            max_new_tokens=max_tokens, 
            temperature=0.1,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(out[0], skip_special_tokens=True).split("assistant")[-1].strip()

ticket_sujo = """
Bom dia equipe, espero que estejam bem. Estava aqui tomando meu café e tentando rodar 
o sistema na tela index.html, mas percebi que quando clico no botão de abrir modal, 
simplesmente nada acontece. Isso é terrível pois temos o deploy amanhã e o cliente 
está cobrando. Podem ver isso com prioridade máxima? Obrigado!
"""

print("Filtrando ruido do ticket...")
resumo = executar_agente(
    "Analista de Triagem", 
    "Extraia apenas o arquivo e o erro técnico deste relato.",
    ticket_sujo, 64
)
print(f"-> Foco técnico: {resumo}")

print("\nAnalisando fontes...")

arquivos_texto = "\n".join([f"[{f}]: {open(os.path.join(PATH_FONTES, f)).read()}" for f in os.listdir(PATH_FONTES)])

diagnostico = executar_agente(
    "Especialista em Debugging", 
    "Com base nos fontes, aponte a falha exata.",
    f"ERRO: {resumo}\nFONTES:\n{arquivos_texto}", 300
)
print(f"-> Causa Raiz: {diagnostico}")

opcao = input("\n[?] Deseja aplicar a correção automaticamente? (s/n): ").lower()

if opcao == 's':
    print("\nGerando Patch de correção...")

    correcao = executar_agente(
        "Senior Developer", 
        "Reescreva o arquivo afetado corrigindo o erro. Retorne APENAS o código puro.",
        f"DIAGNÓSTICO: {diagnostico}\nCÓDIGO ATUAL:\n{arquivos_texto}", 1024
    )
    
    path_fixed = os.path.join(PATH_FONTES, "index_fixed.html")
    with open(path_fixed, "w") as f:

        f.write(correcao.replace("```html", "").replace("```", ""))
    
    print(f"Fonte de teste: {path_fixed}")
