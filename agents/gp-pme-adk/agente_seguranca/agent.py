"""Agente Segurança — Guardião de Segurança (Pilar 3: NIST-Lite).

Consultor virtual de cibersegurança para PMEs, destilado do modelo
NIST-Lite (simplificação do NIST CSF 2.0 e do CIS Controls v8, Grupo de
Implementação 1 — IG1). Gera checklist dos controles mínimos, avalia
riscos de ativos críticos (probabilidade x impacto) e produz Planos de
Resposta a Incidentes (PRI) de 1 página.

Fontes:
GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md
GP-PME antigravity/Templates/Prompts/Template_Prompt_Risco.md
"""
from __future__ import annotations

import os

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Guardião de Segurança (NIST/CIS)" do framework GP-PME — um
Engenheiro de Segurança da Informação Sênior e Auditor de Riscos virtual,
especialista em destilar o NIST CSF 2.0 e o CIS Controls v8 (Grupo de
Implementação 1 — IG1) para a realidade de Pequenas e Médias Empresas
brasileiras. Você fala com o Gestor de TI (muitas vezes um profissional
único, "One-Man-Band") e, quando necessário, traduz riscos técnicos para
o CEO em linguagem de negócio.

CONTEXTO DO FRAMEWORK:
O Pilar 3 (Segurança Crítica) opera sob o modelo NIST-Lite: 4 controles
mínimos, 100% operáveis de forma manual, que entregam a máxima proteção
com o menor custo e esforço possíveis:
1. IDENTIFICAR — Inventário 80/20 de Ativos Críticos (planilha manual dos
   20% de sistemas/dados que, se pararem, paralisam 80% do faturamento).
2. PROTEGER — Privilégio Mínimo (LUA: remover admin local das contas do
   dia a dia) e MFA mandatório em e-mail e sistemas financeiros.
3. PROTEGER — Backups diários automatizados em nuvem (regra 3-2-1),
   testados com restauração real a cada 3 meses.
4. RESPONDER/RECUPERAR — Plano de Resposta a Incidentes (PRI) de 1 página:
   Contenção (desplugar rede sem desligar a máquina), Comunicação
   (contatos de emergência) e Restauro (etapas de recuperação via backup).
A segurança na TI Enxuta não é burocracia: é a bússola que blinda o
crescimento acelerado das Fases 1 e 2 do framework contra incidentes
catastróficos.

O QUE VOCÊ FAZ:
1. Gera o checklist dos 10 controles mínimos NIST-Lite/CIS IG1 (derivados
   dos 4 controles-pilar + desdobramentos de proteção de contas e
   conscientização) com status inicial "pendente", usando a tool
   `checklist_10_controles`.
2. Avalia o risco de um ativo de informação descrito em texto livre,
   aplicando a Matriz 80/20 (Probabilidade x Impacto) do Template de
   Prompt de Risco, usando a tool `avaliar_risco`.
3. Gera um Plano de Resposta a Incidentes (PRI) de 1 página para um tipo
   de incidente (ransomware, phishing, vazamento de dados, acesso
   indevido, ou incidente genérico), usando a tool
   `plano_resposta_incidente`.

COMO RESPONDE:
- Português direto, sem jargão técnico desnecessário — o objetivo é que
  o Gestor de TI (ou o CEO) consiga agir imediatamente.
- Toda recomendação de controle é de custo zero ou mínimo (MFA, LUA,
  backup, senha forte); nunca sugere firewalls corporativos caros, SOC ou
  ferramentas que a PME não declarou possuir.
- Não assume a existência de firewalls de borda, sistemas de monitoramento
  SOC ou infraestrutura sofisticada, a menos que o usuário informe.
- Não inventa nomes de malwares ou vulnerabilidades de dia zero teóricas;
  foca em ameaças reais e comuns de PMEs (phishing, ransomware, vazamento
  de credenciais, erro humano).
- Estrutura saídas em blocos objetivos (checklist, tabela ou roteiro
  numerado), nunca em prosa longa.

RESTRIÇÕES:
- Se faltar dado sobre a rede ou o ativo da empresa, marque explicitamente
  "DADO INSUFICIENTE: requer auditoria local do profissional de TI para
  validar [o que falta]" em vez de presumir.
- Nunca inventa estatísticas de mercado ou promessas de proteção 100%
  garantida — segurança é redução de risco, não eliminação.
- Decisões de investimento em segurança e aprovação final do PRI são
  sempre humanas (Human-in-the-loop); você prepara e recomenda, o Gestor
  de TI e o CD-TI Lite decidem e assinam.
- Toda análise de risco e todo PRI gerados por você passam pelo Checklist
  de Auditoria HITL (Bloco 3: Segurança e Resiliência) antes de qualquer
  implantação real.

FONTES:
GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md
GP-PME antigravity/Templates/Prompts/Template_Prompt_Risco.md
"""


def checklist_10_controles() -> list[dict]:
    """Gera o checklist dos 10 controles mínimos do modelo NIST-Lite/CIS IG1.

    Desdobra os 4 controles-pilar do Guia de Segurança Crítica (Inventário
    80/20, Privilégio Mínimo, MFA, Backups testados, PRI) em 10 itens
    acionáveis, cada um mapeado à função do NIST CSF 2.0 correspondente
    (Identificar, Proteger, Detectar, Responder, Recuperar) e à referência
    do CIS Controls v8 (IG1). Todos os itens nascem com status "pendente"
    — a auditoria de conclusão é sempre humana.

    Returns:
        Lista de 10 dicts, cada um com "id", "controle", "funcao_nist",
        "referencia_cis" e "status" (sempre "pendente" nesta geração).
    """
    itens = [
        ("Inventário 80/20 de Ativos Críticos registrado em planilha",
         "Identificar", "CIS 1 (Inventário de Ativos Corporativos)"),
        ("Privilégio Mínimo (LUA): remoção de admin local das contas do dia a dia",
         "Proteger", "CIS 5 (Gestão de Contas)"),
        ("MFA ativo em 100% das contas de e-mail",
         "Proteger", "CIS 6 (Gestão de Controle de Acesso)"),
        ("MFA ativo em 100% dos sistemas financeiros",
         "Proteger", "CIS 6 (Gestão de Controle de Acesso)"),
        ("Senha individual forte por colaborador (sem contas compartilhadas)",
         "Proteger", "CIS 5 (Gestão de Contas)"),
        ("Backups diários automatizados em nuvem (regra 3-2-1)",
         "Proteger", "CIS 11 (Recuperação de Dados)"),
        ("Teste de restauração de backup a cada 3 meses, com registro em ata",
         "Recuperar", "CIS 11 (Recuperação de Dados)"),
        ("Revisão periódica de contas ociosas ou com privilégios excessivos",
         "Detectar", "CIS 5 (Gestão de Contas)"),
        ("Checklist de higiene cibernética (senhas, phishing) treinado com a equipe",
         "Proteger", "CIS 14 (Conscientização e Treinamento em Segurança)"),
        ("PRI de 1 página preenchido, assinado pelo CEO e fixado na TI",
         "Responder", "CIS 17 (Gestão de Resposta a Incidentes)"),
    ]
    return [
        {
            "id": i + 1,
            "controle": controle,
            "funcao_nist": funcao,
            "referencia_cis": referencia,
            "status": "pendente",
        }
        for i, (controle, funcao, referencia) in enumerate(itens)
    ]


def avaliar_risco(descricao: str) -> dict:
    """Avalia o risco de um ativo de informação (Matriz 80/20 de Probabilidade x Impacto).

    Aplica a lógica do Template de Prompt de Risco (NIST-Lite/CIS IG1):
    varre a descrição em texto livre em busca de vulnerabilidades comuns de
    PMEs (ausência de MFA, contas administrador, sem backup, senha padrão
    ou compartilhada) e de sinais de criticidade de negócio (dados
    financeiros, de clientes ou de faturamento), estimando Probabilidade e
    Impacto e cruzando-os na matriz de Nível de Risco.

    Args:
        descricao: descrição livre do ativo de informação e seu contexto
            de uso (ex.: "Servidor de arquivos compartilhado sem senha,
            guarda folha de pagamento").

    Returns:
        dict com "descricao", "vulnerabilidades_detectadas" (lista),
        "sinais_criticidade" (lista), "probabilidade" (Baixa/Média/Alta),
        "impacto" (Baixo/Médio/Alto), "nivel_risco" (Baixo/Médio/Alto/
        Crítico) e "controles_recomendados" (lista de 3-4 ações NIST-Lite
        de custo zero/mínimo). Se a descrição for vazia, todos os campos
        analíticos retornam "DADO INSUFICIENTE".
    """
    descricao = (descricao or "").strip()
    if not descricao:
        return {
            "descricao": "DADO INSUFICIENTE",
            "vulnerabilidades_detectadas": [],
            "sinais_criticidade": [],
            "probabilidade": "DADO INSUFICIENTE",
            "impacto": "DADO INSUFICIENTE",
            "nivel_risco": "DADO INSUFICIENTE",
            "controles_recomendados": [],
            "aviso": "Requer descrição do ativo pelo profissional de TI.",
        }

    texto = descricao.lower()

    vulnerabilidades_mapa = {
        "sem mfa": ["sem mfa", "sem autenticação de dois fatores", "sem 2fa"],
        "conta administrador local exposta": ["admin", "administrador"],
        "sem backup": ["sem backup", "sem cópia de segurança", "não possui backup"],
        "senha padrão ou compartilhada": ["senha padrão", "sem senha", "compartilhada"],
        "acesso público/rede aberta": ["rede aberta", "acesso público", "wi-fi sem senha"],
    }
    vulnerabilidades = [
        nome
        for nome, termos in vulnerabilidades_mapa.items()
        if any(termo in texto for termo in termos)
    ]

    sinais_criticidade_mapa = {
        "dados financeiros/bancários": ["financeiro", "bancário", "banc", "faturamento", "pagamento"],
        "dados pessoais de clientes (CPF/LGPD)": ["cpf", "cliente", "dados pessoais"],
        "sistema de produção/faturamento": ["erp", "produção", "checkout", "vendas"],
    }
    sinais_criticidade = [
        nome
        for nome, termos in sinais_criticidade_mapa.items()
        if any(termo in texto for termo in termos)
    ]

    n_vuln = len(vulnerabilidades)
    if n_vuln >= 3:
        probabilidade = "Alta"
    elif n_vuln >= 1:
        probabilidade = "Média"
    else:
        probabilidade = "Baixa"

    impacto = "Alto" if sinais_criticidade else "Médio"

    matriz_nivel = {
        ("Alta", "Alto"): "Crítico",
        ("Alta", "Médio"): "Alto",
        ("Alta", "Baixo"): "Médio",
        ("Média", "Alto"): "Alto",
        ("Média", "Médio"): "Médio",
        ("Média", "Baixo"): "Baixo",
        ("Baixa", "Alto"): "Médio",
        ("Baixa", "Médio"): "Baixo",
        ("Baixa", "Baixo"): "Baixo",
    }
    nivel_risco = matriz_nivel[(probabilidade, impacto)]

    controles_recomendados = [
        "Ativar MFA em todas as contas de e-mail e sistemas financeiros do ativo.",
        "Remover privilégio de administrador local das contas de uso diário (LUA).",
        "Configurar backup automático diário em nuvem com teste de restauração trimestral.",
    ]
    if "senha padrão ou compartilhada" in vulnerabilidades or "acesso público/rede aberta" in vulnerabilidades:
        controles_recomendados.append(
            "Trocar senhas padrão/compartilhadas por senha individual forte por colaborador."
        )

    resultado = {
        "descricao": descricao,
        "vulnerabilidades_detectadas": vulnerabilidades,
        "sinais_criticidade": sinais_criticidade,
        "probabilidade": probabilidade,
        "impacto": impacto,
        "nivel_risco": nivel_risco,
        "controles_recomendados": controles_recomendados,
    }
    if not vulnerabilidades and not sinais_criticidade:
        resultado["aviso"] = (
            "DADO INSUFICIENTE: nenhuma vulnerabilidade ou sinal de criticidade "
            "identificado no texto — requer auditoria local do profissional de TI."
        )
    return resultado


def plano_resposta_incidente(tipo: str) -> str:
    """Gera um Plano de Resposta a Incidentes (PRI) de 1 página para um tipo de incidente.

    Segue os 3 blocos fixos do PRI do GP-PME (Contenção, Comunicação,
    Restauro), especializados para o tipo de incidente informado.

    Args:
        tipo: tipo de incidente. Aceita (case-insensitive, com ou sem
            acento): "ransomware", "phishing", "vazamento_dados" (ou
            "vazamento de dados"), "acesso_indevido" (ou "acesso
            indevido"). Qualquer outro valor gera o PRI genérico.

    Returns:
        Texto do PRI de 1 página, pronto para impressão/afixação física.
    """
    tipo_normalizado = (tipo or "").strip().lower().replace(" ", "_")

    contencao_especifica = {
        "ransomware": (
            "Desplugue fisicamente o cabo de rede e desative o Wi-Fi das "
            "máquinas afetadas SEM desligá-las (preserva logs em memória RAM "
            "e evita alastramento do sequestro de dados)."
        ),
        "phishing": (
            "Isole a conta de e-mail/sistema comprometido: force logout, "
            "troque a senha imediatamente e revogue sessões ativas."
        ),
        "vazamento_dados": (
            "Bloqueie o acesso externo ao sistema/arquivo vazado e identifique "
            "o volume e o tipo de dados expostos (CPF, financeiro, etc.)."
        ),
        "acesso_indevido": (
            "Revogue imediatamente as credenciais da conta com acesso indevido "
            "e desative temporariamente contas administradoras suspeitas."
        ),
    }.get(
        tipo_normalizado,
        "Isole fisicamente ou logicamente o ativo afetado sem desligá-lo, "
        "evitando perda de evidências e propagação do incidente.",
    )

    titulo = {
        "ransomware": "RANSOMWARE (Sequestro de Dados)",
        "phishing": "PHISHING (Roubo de Credenciais)",
        "vazamento_dados": "VAZAMENTO DE DADOS",
        "acesso_indevido": "ACESSO INDEVIDO / INVASÃO DE CONTA",
    }.get(tipo_normalizado, f"INCIDENTE GENÉRICO ({tipo.strip() if tipo else 'não especificado'})")

    return (
        f"PLANO DE RESPOSTA A INCIDENTES (PRI) — {titulo}\n"
        "=====================================================\n\n"
        "1) CONTENÇÃO (ação imediata, primeiros minutos)\n"
        f"   - {contencao_especifica}\n\n"
        "2) COMUNICAÇÃO (relação de contatos de emergência)\n"
        "   - Gestor de TI / consultoria de segurança parceira.\n"
        "   - CEO / responsável legal da PME.\n"
        "   - Provedor de internet e suporte do ERP/sistema afetado.\n\n"
        "3) RESTAURO (recuperação)\n"
        "   - Formatar/isolar o ativo comprometido antes de reconectar à rede.\n"
        "   - Restaurar dados a partir do backup em nuvem mais recente testado.\n"
        "   - Registrar o incidente e as lições aprendidas na próxima reunião "
        "CD-TI Lite.\n\n"
        "NOTA: este PRI deve ser impresso, assinado pelo CEO e fixado "
        "fisicamente na sala de TI (checklist de emergência de 1 página).\n"
    )


root_agent = Agent(
    name="agente_seguranca",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Guardião de Segurança do Pilar 3 (NIST-Lite): checklist de controles "
        "mínimos, avaliação de risco de ativos e Plano de Resposta a "
        "Incidentes para PMEs."
    ),
    instruction=INSTRUCTION,
    tools=[checklist_10_controles, avaliar_risco, plano_resposta_incidente],
)
