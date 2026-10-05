"""Assistência opcional GEAR: agente_seguranca.

Fonte vigente: framework/nucleo/seguranca-continuidade.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Identificar dependências críticas, tratar acessos e preparar recuperação. Uma seleção local não equivale ao CIS IG1 completo. Diferenciar job de backup, arquivo restaurado e serviço recuperado. Contenção depende de autorização e ambiente, sem apagar evidências.\nFontes: framework/README.md e guias correspondentes.\n'


def checklist_10_controles() -> list[dict]:
    """Seleção local: não equivale à cobertura integral do NIST/CIS."""
    return _core.checklist_10_controles()["controles"]


def avaliar_risco(descricao: str) -> dict:
    """Triagem lexical de menções, sem inferir probabilidade ou impacto.

    Campos históricos preservam compatibilidade; menções podem estar negadas
    ou citar outro ativo. Conferir contexto e evidência antes de agir.
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
        "privilégio administrativo a conferir": ["admin sem controle", "administrador compartilhado", "todos são administradores"],
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

    # Menções textuais não sustentam probabilidade nem criticidade medida.
    probabilidade = impacto = nivel_risco = "DADO INSUFICIENTE"

    controles_recomendados = [
        "Conferir cobertura de MFA nas contas críticas, compatibilidade e exceções.",
        "Revisar necessidade de privilégios administrativos e planejar remoção do acesso excedente.",
        "Definir frequência, retenção e proteção de backup com o serviço e testar recuperação na janela acordada.",
    ]
    if "senha padrão ou compartilhada" in vulnerabilidades or "acesso público/rede aberta" in vulnerabilidades:
        controles_recomendados.append(
            "Conferir a menção a senha compartilhada e planejar credenciais individuais quando aplicável."
        )

    resultado = {
        "descricao": descricao,
        "vulnerabilidades_detectadas": vulnerabilidades,
        "sinais_criticidade": sinais_criticidade,
        "probabilidade": probabilidade,
        "impacto": impacto,
        "nivel_risco": nivel_risco,
        "controles_recomendados": controles_recomendados,
        "limite": "Triagem lexical: menções requerem conferência local; não comprovam vulnerabilidade, probabilidade ou impacto.",
        "fonte": "framework/templates/risco-continuidade.md",
    }
    if not vulnerabilidades and not sinais_criticidade:
        resultado["aviso"] = (
            "DADO INSUFICIENTE: nenhuma vulnerabilidade ou sinal de criticidade "
            "identificado no texto — requer auditoria local do profissional de TI."
        )
    return resultado


def plano_resposta_incidente(tipo: str) -> str:
    """Prepara rascunho a completar e exercitar localmente.

    Especializa ransomware, phishing, vazamento_dados e acesso_indevido;
    demais entradas recebem orientação genérica. Não autoriza contenção,
    não verifica contatos e não decide comunicação legal.
    """
    tipo_normalizado = (tipo or "").strip().lower().replace(" ", "_")

    contencao_especifica = {
        "ransomware": (
            "Avaliar isolamento de rede com a autoridade responsável, considerando "
            "continuidade, propagação e evidências. Não presumir que manter ou "
            "desligar o equipamento seja correto em todo ambiente."
        ),
        "phishing": (
            "Conferir a conta e o possível comprometimento; avaliar revogação de "
            "sessões e troca de credenciais sob autorização, preservando registros."
        ),
        "vazamento_dados": (
            "Avaliar restrição do acesso exposto e identificar dados, titulares e "
            "escopo conhecidos; registrar incertezas e encaminhar ao controlador."
        ),
        "acesso_indevido": (
            "Confirmar indícios de uso indevido e avaliar suspensão de sessões ou "
            "credenciais com autorização e alternativa de continuidade."
        ),
    }.get(
        tipo_normalizado,
        "Identificar escopo e autoridade; avaliar contenção apropriada ao "
        "ambiente, preservação de evidências e continuidade.",
    )

    titulo = {
        "ransomware": "RANSOMWARE (Sequestro de Dados)",
        "phishing": "PHISHING (Roubo de Credenciais)",
        "vazamento_dados": "VAZAMENTO DE DADOS",
        "acesso_indevido": "ACESSO INDEVIDO / INVASÃO DE CONTA",
    }.get(tipo_normalizado, f"INCIDENTE GENÉRICO ({tipo.strip() if tipo else 'não especificado'})")

    return (
        f"PLANO DE RESPOSTA A INCIDENTES (PRI) — {titulo}\n"
        "\n"
        "1) CONTENÇÃO (avaliação e decisão autorizada)\n"
        f"   - {contencao_especifica}\n\n"
        "2) COMUNICAÇÃO (preencher contatos, meios, substitutos e alçadas)\n"
        "   - Gestor de TI / consultoria de segurança parceira.\n"
        "   - CEO / responsável legal da PME.\n"
        "   - Provedor de internet e suporte do ERP/sistema afetado.\n"
        "   - Controlador avalia comunicação legal quando houver dados pessoais.\n\n"
        "3) RESTAURO (recuperação)\n"
        "   - Confirmar autorização, ambiente e preservação de evidências antes de qualquer alteração.\n"
        "   - Recuperar a partir de condição conhecida e verificar dados, serviço e dependências.\n"
        "   - Registrar o incidente e as lições aprendidas na próxima reunião "
        "CD-TI Lite.\n\n"
        "Conferir contatos e alçadas, exercitar o plano e registrar limitações. "
        "As ações sugeridas dependem do ambiente; este rascunho não autoriza execução.\n"
    )


root_agent = Agent(
    name="agente_seguranca",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Assistência opcional em segurança e continuidade: seleção local de "
        "controles, triagem de menções e rascunho de resposta a incidentes."
    ),
    instruction=INSTRUCTION,
    tools=[checklist_10_controles, avaliar_risco, plano_resposta_incidente],
)
