"""Biblioteca e oito templates revistos, derivados do corpus canônico."""
import re
from tools.editorial import ROOT, blocks, slug
from tools.build_legacy_masters import excerpt, heading_shift

TEMPLATES = [
    ('Prompts/Template_Prompt_Mestre.md', 'Instrução de tarefa e prompt mestre', ['templates/instrucao-assistencia.md']),
    ('Prompts/Template_Prompt_PRD.md', 'Prompt para preparar requisitos', ['templates/prompts-assistencia.md', 'templates/prd-aceite.md']),
    ('Prompts/Template_Prompt_Risco.md', 'Prompt para análise de risco', ['templates/risco-continuidade.md']),
    ('PRDs/Template_PRD_Completo.md', 'PRD e critérios de aceite', ['templates/prd-aceite.md']),
    ('Tasklists/Template_Tasklist_Operacional.md', 'Lista de tarefas e verificação', ['templates/tasklist.md']),
    ('AI-Skills-and-Agents/Template_System_Prompt_Agentes.md', 'Contratos de assistência por função', ['templates/prompts-assistencia.md', 'guias/usar-ia.md']),
    ('AI-Skills-and-Agents/Template_Checklist_Auditoria_HITL.md', 'Conferência humana de saídas assistidas', ['templates/revisao-ia.md']),
    ('Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md', 'Questionário e registro de maturidade', ['adocao/maturidade.md', 'templates/maturidade.md']),
]

LIBRARY = [
    ('1: responsabilidades e RACI-Lite', 'templates/responsabilidades.md'),
    ('2: quatro finalidades e decisão', 'templates/decisoes-prioridades.md'),
    ('3: painel de indicadores', 'templates/painel-indicadores.md'),
    ('4: PRD e aceite', 'templates/prd-aceite.md'),
    ('5: impacto e urgência', 'templates/matriz-prioridades.md'),
    ('6: ativos e dependências', 'templates/inventario-dependencias.md'),
    ('7: resposta a incidentes', 'templates/incidente.md'),
    ('8: maturidade e plano de melhoria', 'templates/maturidade.md'),
]


def intro(title):
    return (f'# GEAR: {title}\n\nEdição editorial GEAR 2026.10. '
            'Caminho GP-PME preservado para compatibilidade. Modelos completos, '
            'revistos a partir da biblioteca anterior; preencher com dados reais e '
            'registrar lacunas. IA é opcional. Direitos conforme LICENSE.md.\n\n')


def compose(target, title, sources):
    body = '\n\n'.join(heading_shift(excerpt(path, target)) for path in sources)
    nav = '\n'.join(f'- [{v}](#{slug(v)})' for k, v in blocks(body) if k == 'h2')
    return intro(title) + '## Percurso de leitura\n\n' + nav + '\n\n' + body + '\n'


def build():
    base = ROOT / 'GP-PME antigravity/Templates'
    for name, title, sources in TEMPLATES:
        target = base / name
        text = compose(target, title, sources)
        if name.endswith('Template_Prompt_PRD.md'):
            prompt = excerpt('templates/prompts-assistencia.md', target)
            prompt = re.search(r'^## Requisitos e entrega\n(.*?)(?=^## |\Z)', prompt, re.M | re.S)[1]
            text = compose(target, title, ['templates/prd-aceite.md'])
            text += '\n## Prompt para copiar\n' + prompt
            text += ('\nO contrato prepara uma proposta de requisitos; não autoriza '
                     'decisões de acesso ou investimento. Exemplos de entrada são fictícios.\n')
        if name.endswith('Template_System_Prompt_Agentes.md'):
            text += ('\n## Configurar uma assistência\n\nSelecionar a função necessária, '
                     'conferir as permissões do provedor e fornecer o corpus canônico pertinente. '
                     'Testar um caso delimitado e revisar a saída antes do uso. Não é necessário '
                     'criar quatro assistentes. Carregar documentos não garante que serão '
                     'recuperados corretamente. Uma auditoria por IA continua sujeita a '
                     'conferência humana; não assume a aprovação final.\n')
        target.write_text(text, encoding='utf-8')
        print(name, len(text), 'caracteres')
    target = ROOT / 'GP-PME antigravity/Templates_GP-PME.md'
    text = intro('Biblioteca de registros essenciais')
    text += ('Esta biblioteca reúne oito grupos de registros do índice anterior. '
             'Uma ou duas páginas são preferência de síntese, sem apagar evidências '
             'necessárias. Templates são instrumentos locais, sem certificação normativa. '
             'Modelos complementares e contratos de IA permanecem na biblioteca modular.\n\n'
             '## Escolher um registro\n\n')
    for title, source in LIBRARY:
        text += f'- [Template {title}](#template-{slug(title)})\n'
    text += '\n'
    for title, source in LIBRARY:
        text += f'## Template {title}\n\n' + heading_shift(excerpt(source, target), 2) + '\n\n'
        text += ('Assistência opcional: fornecer somente dados autorizados, pedir uma '
                 'minuta e registrar lacunas. Quem tem responsabilidade confere a saída '
                 'e aprova o uso; o modelo não determina configuração ou alçada real.\n\n')
    text += ('Consulta: [biblioteca modular](../framework/templates/README.md), '
             '[instrução de tarefa](../framework/templates/instrucao-assistencia.md) e '
             '[contratos específicos](../framework/templates/prompts-assistencia.md). '
             'Fontes: [referências e limites](../framework/referencias/fontes.md).\n')
    target.write_text(text, encoding='utf-8')
    print(target.name, len(text), 'caracteres')


if __name__ == '__main__':
    build()
