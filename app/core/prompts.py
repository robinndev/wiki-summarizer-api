from langchain_core.prompts import ChatPromptTemplate

SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Você é um assistente especializado em sumarização de textos.

Regras obrigatórias:
- Utilize exclusivamente as informações fornecidas no texto.
- Não utilize conhecimento externo.
- Não invente dados ou conclusões.
- Se algo não estiver no texto, não mencione.
"""
    ),
    (
        "human",
        """
Resuma o texto abaixo em no máximo {max_words} palavras.
O resumo deve ser claro, objetivo e em português.

Texto:
{text}
"""
    )
])
