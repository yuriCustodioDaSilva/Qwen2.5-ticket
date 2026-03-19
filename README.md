# Sistema de Diagnóstico e Recuperação Autônoma de Código (SDRA)

Este repositório apresenta uma implementação de agentes de inteligência artificial projetados para automatizar a triagem e a correção de falhas em ambientes de desenvolvimento de software.

## Objetivos do Sistema
O SDRA visa eliminar o gargalo humano entre o recebimento de um ticket de suporte e a aplicação do patch técnico. O sistema processa descrições em linguagem natural, identifica a causa raiz no código-fonte e propõe correções automáticas, reduzindo o **Tempo Médio de Reparo (MTTR)** de horas para segundos.

## Arquitetura Técnica e Diferenciais

### 1. Modelo Base: Qwen2.5-Coder-7B-Instruct
Escolhi o **Qwen2.5-Coder** por ser leve, multilingual, extremamente eficiente e otimizado para tarefas que exigem raciocínio lógico e sintaxe de código precisa.

### 2. Especialização via Fine-tuning (LoRA)
Utilizamos a técnica **LoRA (Low-Rank Adaptation)** para especializar o modelo no domínio da nossa empresa. 
*   **Vantagem:** Em vez de treinar bilhões de parâmetros, "congelamos" o modelo base e treinamos apenas uma camada de adaptação de baixo posto. 
*   **Resultado:** Um treinamento rápido, barato e que gera arquivos leves (checkpoints), permitindo versionar a inteligência da IA (v1.0, v1.1) conforme o nosso framework evolui.

### 3. Conhecimento Vivo com RAG (Retrieval-Augmented Generation)
O **RAG** permite que a IA consulte nossa base de conhecimentos, documentações e históricos de soluções antes de responder. 
*   **Impacto:** Reduz drasticamente as "alucinações", garantindo que as sugestões de correção sejam baseadas em fatos e padrões já aprovados pela nossa engenharia.

### 4. Eficiência Operacional (Auto-tuning e Quantização)
Aplicamos técnicas de **Auto-tuning** para extrair a performance máxima do hardware disponível. Através da **Quantização**, reduzimos a pegada de memória do modelo para que ele rode com alta velocidade em GPUs de baixo custo, mantendo a precisão necessária para o ambiente de produção.

## Open Source
Por utilizarmos um modelo **Open Source**, garantimos que 100% dos dados de clientes e códigos proprietários permaneçam dentro do nosso firewall. 
*   **Privacidade:** Compliance total com a LGPD.
*   **Ativo Estratégico:** Teremos uma IA especialista no nosso **próprio framework** e no mercado de **agronegócio**, capaz de gerar documentação e tirar dúvidas técnicas da equipe interna de forma autônoma.

## Impacto na Operação Empresarial
A automação do ciclo de vida do bug gera ganhos em três frentes principais:
1.  **Triagem Técnica Imediata**: Conversão de reclamações informais em dados estruturados (Arquivo, Tipo de Bug, Severidade).
2.  **Escalabilidade Infinita**: Capacidade de processar centenas de tickets simultaneamente sem aumentar o headcount.
3.  **Foco em Inovação**: Desenvolvedores deixam de atuar em "bugs de sintaxe" e focam em arquitetura e novas funcionalidades de alto valor.

## Projeção de Viabilidade Financeira (Cloud GPU)

A operação deste sistema é otimizada para provedores de GPU por demanda, permitindo uma execução de baixo custo.


| Provedor | Hardware Recomendado | Custo Estimado (Hora) | Throughput Esperado |
| :--- | :--- | :--- | :--- |
| **Vast.ai** | NVIDIA RTX 3060 / 4060 Ti | $0.06 - $0.15 | 80 - 110 tokens/s |
| **RunPod** | NVIDIA RTX 4090 | $0.34 - $0.45 | 180 - 240 tokens/s |

**Custo por ciclo**: Uma análise completa, ou seja Triagem + Diagnóstico + Patch. Consome aproximadamente 3.000 tokens. Em uma RTX 4090, isso representa um custo computacional **APROXIMADO** de **$0.002 USD** por correção.

## Referências Técnicas
* [Análise de Hardware para Deep Learning](https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/)
* [Aritmética de Inferência em Transformers](https://kipp.ly/transformer-inference-arithmetic/)
* [Modelo base Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)

## Demonstração de Execução

Abaixo, um registro do fluxo de processamento do `index.py`, demonstrando a triagem, o diagnóstico e a geração do patch:

![Resultado da Execução do index.py](image.png)