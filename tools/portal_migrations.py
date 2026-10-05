"""Equivalências de fragmentos documentais antigos, com destinos permanentes."""
from collections import defaultdict
from html import escape

GROUPS = [
    ('Documentação','docs/README.html',['workspace','cat-leigo-visao','cat-tecnico-overview','cat-leigo-overview']),
    ('Escopo do método','docs/nucleo/escopo-principios.html',['visao']),
    ('Guias de execução','docs/guias/README.html',['tecnico']),
    ('Adoção inicial','docs/adocao/primeiros-30-dias.html',['dummies','cat-tecnico-fasezero']),
    ('Governança e direção','docs/nucleo/governanca.html',['cat-tecnico-pilar1','cat-leigo-pilar1']),
    ('Execução e serviços','docs/nucleo/execucao-servicos.html',['cat-tecnico-pilar2','cat-leigo-pilar2','cat-tasklists','temp-tasklist-operacional']),
    ('Segurança e continuidade','docs/nucleo/seguranca-continuidade.html',['cat-tecnico-pilar3','cat-leigo-pilar3','temp-prompt-risco']),
    ('Assistência opcional por IA','docs/guias/usar-ia.html',['cat-tecnico-pilar4','cat-agentes','cat-prompts','temp-prompt-mestre','temp-system-agentes']),
    ('Indicadores','docs/indicadores/operacionais.html',['cat-tecnico-kpis']),
    ('PRD e aceite','docs/templates/prd-aceite.html',['cat-prds','temp-prd-completo','temp-prompt-prd']),
    ('Revisão de saída assistida','docs/templates/revisao-ia.html',['temp-checklist-hitl']),
    ('Biblioteca de modelos','biblioteca.html',['templates']),
    ('Ferramentas locais','ferramentas.html',['simuladores']),
]

# Controles anteriores levam à tarefa equivalente; não imitam formulários antigos.
GROUPS += [
    ('Retorno financeiro','ferramentas.html#retorno',['cotInvestment','cotPayback','cotROI']),
    ('Capacidade potencial','ferramentas.html#capacidade',['cotDowntime','cotPeople','cotRate']),
    ('Dívida financeira','ferramentas.html#divida',['danBar','danBudget','danDesc','danHourlyRate','danHours','danResultBox','danValue']),
    ('Quadro de exercício','ferramentas.html#fluxo',['col-doing','col-done','col-testing','col-todo','count-doing','count-done','count-testing','count-todo','wipAlert']),
]
for _,_,aliases in GROUPS:
    aliases += ['subtab-btn-'+a[4:] for a in list(aliases) if a.startswith('cat-')]
    aliases += ['tab-btn-'+a for a in list(aliases) if a in ('dummies','simuladores','tecnico','templates','visao')]

def migration_html():
    html='<nav class="migration" aria-label="Equivalências de leitura anteriores">'
    for label,target,aliases in GROUPS:
        anchors=''.join(f'<span id="{escape(a)}"></span>' for a in aliases)
        html+=f'<div>{anchors}<a href="{target}">{label}</a></div>'
    return html+'</nav>'
