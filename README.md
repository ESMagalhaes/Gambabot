# GambáBot

Pequeno chatbot usando Streamlit + LangChain + AWS Bedrock (via langchain_aws). Projeto de exemplo para trocar mensagens com um LLM hospedado no Amazon Bedrock e manter histórico de conversa em memória.

## Estrutura principal
- `chatbot_frontend.py` — app Streamlit (UI).
- `chatbot_backend.py` — funções que criam o LLM, memória e a cadeia de conversação.
- `requirements.txt` — lista de dependências (veja seção abaixo).

## Dependências
Instale em um virtualenv/conda:
- python >= 3.10
- streamlit
- boto3
- botocore
- langchain (ou a família de pacotes compatível que você usa: `langchain_classic`, `langchain_aws` conforme o seu código)
- langdetect (opcional, para detecção de idioma)
Exemplo:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate
pip install streamlit boto3 botocore langdetect
# instale os pacotes específicos que você usa:
pip install langchain_aws langchain_classic
```

Obs: Nomes de pacotes podem variar por versão. Ajuste conforme o que está instalado no seu ambiente.

## Configuração AWS
1. Configure suas credenciais AWS (perfil `default` ou altere no código):
```powershell
aws configure
```
2. Defina a região suportada pelo Bedrock:
```powershell
setx AWS_REGION us-east-1
```
ou use `AWS_DEFAULT_REGION`.

3. Se o modelo retornar ResourceNotFoundException (modelo EOL), liste modelos disponíveis:
```python
import boto3
client = boto3.client("bedrock")
print(client.list_models())
```
Escolha um `modelId:version` retornado e atualize `model=` em `chatbot_backend.py`.

## Como rodar
No diretório do projeto:
- Rodar UI Streamlit:
```powershell
cd "c:\Users\enzos\Documents\PastaBedrock"
streamlit run chatbot_frontend.py
```
- Testar backend como script:
```powershell
python chatbot_backend.py
```

## Problemas comuns e soluções rápidas

- ResourceNotFoundException (modelo EOL):
  - Substitua o `model=` por um ID válido (listar modelos com `boto3.client("bedrock").list_models()`).
  - Trate `botocore.exceptions.ClientError` para mensagens amigáveis.

- ImportError relacionados a `ConversationBufferMemory`:
  - Dependendo da versão do LangChain, a classe pode estar em `langchain.memory` ou outro pacote. Ajuste os imports para a versão instalada.

## Boas práticas
- Teste com um modelo ativo e permissões IAM corretas.
- Use variáveis de ambiente para perfis/region em produção.
- Remova vírgulas acidentais ao construir objetos (previne tuplas).

## Licença
Use conforme desejar. Sem garantia.

---
