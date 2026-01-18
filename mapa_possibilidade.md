# 📦 Ferramentais Universais — Catálogo Conceitual

Este documento lista **ferramentas universais amplamente utilizadas na internet**, que não pertencem a um domínio específico (educação, conteúdo, negócios, etc.), mas que são recorrentes em praticamente qualquer sistema, produto digital, automação ou agente inteligente.

O objetivo **não é implementar tudo agora**, mas **mapear possibilidades reais**, evitando retrabalho e decisões improvisadas no futuro.

---

## 🧱 Critérios de Inclusão

Uma ferramenta entra neste catálogo se atender a pelo menos **dois critérios**:

- Resolve um problema recorrente em múltiplos domínios  
- É comum em produtos SaaS, APIs ou automações reais  
- Evita reescrita constante de lógica  
- É reutilizável por diferentes agentes  
- Não depende de contexto de negócio específico  

---

## 1️⃣ Manipulação de Tempo & Datas

Ferramentas relacionadas ao tempo são universais e transversais.

Possibilidades:
- Conversão entre formatos de data
- Diferença entre datas
- Cálculo de janelas temporais (últimos 7, 30, 90 dias)
- Conversão de timezone
- Timestamp ↔ formato humano
- Validação de datas
- Detecção de datas futuras/passadas

Usado em:
- logs
- auditoria
- relatórios
- histórico de agentes
- planejamento
- métricas

Camada sugerida: **Camada 1 — Tools Fundamentais**

---

## 2️⃣ Estruturação & Serialização de Dados

Ferramentas para organizar, transformar e apresentar dados.

Possibilidades:
- Dict → Markdown
- Listas → tabelas lógicas
- Markdown → estrutura de dados
- Normalização de chaves
- Flatten / expand de estruturas
- Padronização de output textual

Usado em:
- APIs
- relatórios
- exportação de resultados
- agentes explicadores
- produtos educacionais

Camada sugerida: **Camada 1 — Tools Fundamentais**

---

## 3️⃣ Sanitização & Segurança Básica de Entrada

Ferramentas invisíveis, mas críticas para qualquer sistema exposto.

Possibilidades:
- Remoção de HTML/scripts
- Limitação de tamanho de entrada
- Normalização de whitespace
- Mascaramento de dados sensíveis (CPF, e-mail, telefone)
- Detecção de input vazio ou inválido

Usado em:
- formulários
- APIs
- agentes públicos
- sistemas com input humano

Camada sugerida: **Camada 1 — Tools Fundamentais**

---

## 4️⃣ Utilitários de Web (nível leve)

Sem scraping pesado, apenas manipulação básica de URLs e links.

Possibilidades:
- Validação de URL
- Extração de domínio
- Normalização de links
- Detecção de tipo de link
- Análise textual de confiabilidade básica

Usado em:
- pesquisa
- análise de fontes
- conteúdo
- automações

Camada sugerida: **Camada 1 ou Camada 2**

---

## 5️⃣ Avaliação & Scoring Genérico

Ferramentas neutras de avaliação, sem domínio específico.

Possibilidades:
- Score numérico simples (0–100)
- Classificação por faixas
- Comparação de versões
- Ranking básico
- Priorização de itens

Usado em:
- diagnóstico
- tomada de decisão
- planejamento
- agentes meta

Camada sugerida: **Camada 2 — Pesquisa & Inteligência**

---

## 6️⃣ Detecção de Padrões Textuais (leve)

Ferramentas simples de análise estrutural de texto.

Possibilidades:
- Detecção de perguntas
- Detecção de listas
- Detecção de instruções
- Identificação de repetição
- Classificação textual (narrativo, técnico, instrucional)

Usado em:
- conteúdo
- educação
- diagnóstico
- normalização de entrada

Camada sugerida: **Camada 5 — Criativas & Conteúdo**

---

## 7️⃣ Logging Lógico (não técnico)

Registro de ações e decisões em linguagem humana.

Possibilidades:
- Registro de tool utilizada
- Resumo da ação executada
- Resultado gerado
- Direção sugerida

Usado em:
- auditoria cognitiva
- explicabilidade
- memória futura
- revisão de decisões

Camada sugerida: **Pré-Camada 8 — Evolução Técnica**

---

## 8️⃣ Exportação Universal de Resultados

Ferramentas para entrega final de informação.

Possibilidades:
- Geração de relatório textual
- Resumo executivo
- Checklist final
- Plano estruturado para humanos

Usado em:
- produtos digitais
- APIs
- SaaS
- uso real por pessoas

Camada sugerida: **Camada 5 ou Camada 7**

---

## 🚦 O que NÃO entra neste catálogo (por enquanto)

Para manter sanidade arquitetural:

- Scraping pesado
- Banco de dados
- Cache
- Autenticação
- Memória de longo prazo
- Integrações externas

Esses elementos pertencem a **produto**, não a **tool base**.

---

## 🧠 Observação Final

Este catálogo não é uma lista de tarefas.

Ele é um **mapa de expansão consciente**, que permite:
- crescer sem improvisar
- priorizar com clareza
- manter coerência arquitetural

Ferramentas só devem ser implementadas quando houver **necessidade real de uso**.
