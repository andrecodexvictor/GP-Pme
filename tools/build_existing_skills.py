"""Revisa as oito skills existentes; não instala nem cria outra coleção.

Identificadores são compatibilidade. Procedimentos apontam para a fonte
canônica; referências específicas e exemplos preservam o recorte original.
"""
from pathlib import Path
from tools.editorial import ROOT
from tools.build_agent_contracts import SPECS, link

BASE = ROOT / '.claude/skills'

# O último campo preserva os exemplos próprios das skills, não os agentes.
SKILLS = [
    ('consultor', 0, 'Triagem e próximo passo',
     'Use quando precisar escolher por onde começar no GEAR ou encaminhar uma demanda entre adoção, governança, execução, segurança, requisitos, indicadores e maturidade.',
     '''1. Identificar o problema dominante e seu efeito no serviço ou negócio. Uma tarefa já delimitada segue para a especialidade pertinente.
2. Se houver incidente ativo, encaminhar resposta e alçada imediatamente; quadro ou questionário não são pré-requisitos para proteger o serviço.
3. Para visão conjunta, consultar o questionário vigente. Somente informar IM-TI após conferir as dez respostas e suas evidências; relato parcial permite orientação, sem pontuação presumida.
4. Escolher uma primeira ação por risco, dependência e capacidade. A pontuação ajuda a discutir lacunas, sem impor sequência universal.
5. Entregar situação conhecida, fundamento da rota, arquivo ou skill, responsável e checkpoint. Declarar diagnóstico não realizado ou informação ausente.
6. Encerrar a triagem quando a próxima ação e sua conferência estiverem identificadas. Pedido de diagnóstico aprofundado segue para `gp-pme-maturidade`.
''', [
     ('Direção não participa; verba demora semanas.', 'Encaminhar pauta, responsabilidades e alçada para governança; não bloquear a revisão por ausência de Kanban.'),
     ('Dono de PME desconhece a rotina; avaliação fictícia tem dois pontos.', 'Registrar as dez respostas antes de confirmar o total. Sugerir adoção pelas lacunas, sem declarar urgência absoluta ou avanço garantido.'),
     ]),
    ('fase-zero', 6, 'Agenda inicial de adoção',
     'Use para preparar ou acompanhar os primeiros trinta dias de adoção do GEAR, adaptar calendário ou retomar ações pendentes.',
     '''1. Identificar o recorte: adoção inicial, retomada de pendências ou verificação pré-projeto. Avaliação inicial ajuda a comparar, mas falta de score não bloqueia resposta urgente.
2. Conferir responsáveis, capacidade, dependências e data de início. Sem data, usar dias relativos; dia 1 é a data informada e dia 30 é início mais 29 dias.
3. Consultar a agenda de nove passos e produzir ações com executor, autoridade, critério e evidência. As quatro semanas são agrupamentos ajustáveis; itens já comprovados permanecem registrados.
4. Preparar registro oficial e quadro, orientação recorrente, inventário e restauração, PRI e revisão de direção, indicadores e comparação. Capturar contatos informais e emergências.
5. Ao acompanhar, distinguir configurado, utilizado e verificado. Backup executado exige teste apropriado de restauração; PRI exige contatos e acesso durante a crise, em meio adequado.
6. Registrar antes/depois com coleta real e períodos comparáveis. Pendências têm dono e próxima ação; reaplicar as dez perguntas para o IM-TI final.
7. Concluir o acompanhamento com ações verificadas, lacunas e continuidade acordada. Trinta dias, assinatura ou score não certificam transição sustentada.
''', [
     ('Diagnóstico concluído; começar na segunda-feira seguinte.', 'Confirmar a data civil ou usar dia relativo, aproveitar evidências válidas e preparar a agenda ajustável.'),
     ('Quadro e registro em uso há duas semanas; restauração nunca testada.', 'Conferir uso efetivo e priorizar teste autorizado com escopo, RTO/RPO e dependências. Não certificar recuperação pelo job nem exigir retorno ao início.'),
     ]),
    ('governanca', 1, 'Pauta, decisões e responsabilidades',
     'Use para preparar pauta ou ata do CD-TI Lite, classificar finalidades de iniciativas ou acordar responsabilidades e alçadas.',
     '''1. Identificar o artefato pedido: pauta, classificação de finalidade, RACI ou registro de decisão. Usar somente decisões relatadas e dados com origem.
2. Para pauta, consultar a agenda 5/15/5/5: indicadores, prioridades, riscos, decisões. Trinta minutos e quinzena são parâmetros ajustáveis; ausência de KPI vira pendência, sem impedir reunião.
3. Para cada iniciativa, registrar finalidade principal, efeitos secundários, hipótese de benefício e decisão necessária. As quatro finalidades não substituem impacto e urgência.
4. Para RACI, atribuir executor, aprovador com alçada, consultados e informados úteis por atividade. Tornar visível acúmulo de funções e necessidade de segunda conferência. IA pode auxiliar, sem responder pela alçada.
5. Para ata, conservar data e presentes conhecidos, alternativas, decisão, motivo, recurso, risco, aprovador, executor, prazo e revisão. Campo ausente permanece pendente; minuta não é aprovação realizada.
6. Separar decisões de negócio dos detalhes de implementação, mantendo informação técnica necessária para avaliar alternativas. Encerrar com artefato conferível e pendências atribuídas.
''', [
     ('Primeira reunião com a direção; números ainda ausentes.', 'Preparar pauta e coleta inicial, com iniciativas reais e hipótese de benefício. A reunião não precisa aguardar todos os indicadores.'),
     ('Demandas urgentes travam porque ninguém sabe quem aprova.', 'Propor RACI para priorização com limites e escalonamento. As pessoas com alçada confirmam a atribuição.'),
     ]),
    ('kanban', 2, 'Fila, capacidade e interrupções',
     'Use para montar o quadro, planejar trabalho, investigar gargalos ou tratar interrupções e emergências na execução do GEAR.',
     '''1. Distinguir montagem, planejamento, diagnóstico ou emergência. Identificar cartões, executores, capacidade, serviço e critérios disponíveis.
2. Consultar os quatro estados e registrar bloqueio/suspensão. Contar trabalho iniciado por executor, incluindo teste e bloqueio comprometido; três é parâmetro inicial ajustável, sem inferir cumprimento pela soma da equipe.
3. Definir registro oficial e capturar pedidos recebidos por telefone, conversa ou mensagem. Atender emergência e registrar assim que viável.
4. Ordenar por impacto, urgência, risco e dependência. Usar a matriz acordada; classificação não autoriza apagar demanda. Finalidade comercial não é sinônimo de prioridade operacional.
5. Planejar conforme capacidade; 15/5/15 minutos e três a cinco cartões são antigas opções de agenda, sem meta universal de entregas ou 80% obrigatório.
6. Na emergência, confirmar alçada, registrar trabalho suspenso, motivo e capacidade. Conduzir resposta apropriada, verificar recuperação e decidir retomada. Histórico e relógio permanecem; mover para backlog não apaga compromisso iniciado.
7. Investigar gargalos como hipóteses: espera de teste, capacidade, bloqueio, chegada de demandas ou prioridade. Conferir evidências antes de atribuir causa.
8. Em melhoria, ligar ideia, PRD, execução, piloto e feedback. Suporte e projeto usam a mesma capacidade. Duração do piloto depende do recorte; propor ajuste de escopo ou prazo para acordo.
9. Encerrar com fila proposta ou diagnóstico, critérios e pendências. Sem ferramenta executada, não declarar quadro gravado.
''', [
     ('Adoção ocorreu há meses; quadro ainda é planilha desorganizada.', 'Conferir registro existente e itens, propor estados, responsáveis e ordenação; adoção passada não comprova canal ativo.'),
     ('ERP caiu; técnico tem três tarefas iniciadas.', 'Conferir impacto e autoridade, registrar suspensão e exceção de capacidade, responder e verificar recuperação antes da retomada. Evitar suspensão que só esconde WIP.'),
     ]),
    ('maturidade', 5, 'Diagnóstico com evidências',
     'Use para aplicar o questionário IM-TI, conferir pontuação, discutir fichas por domínio ou preparar ações de desenvolvimento e revisão.',
     '''1. Consultar as dez perguntas vigentes e o registro de maturidade. Manter origem, data, edição e evidência por pergunta; edições antigas precisam de reaplicação para comparação.
2. Contar 1 para prática com evidência e 0 quando ausente ou insuficiente. Registrar não verificado na observação, como zero provisório. Relato parcial permanece incompleto.
3. Somar somente após as dez respostas. Conferir faixa local e exibir resultado por pergunta junto ao total. IA é opcional também no nível máximo.
4. Quando solicitado, usar as cinco fichas por domínio para descrever entradas, saídas e medidas. Ficha não acrescenta condição à pontuação nem obriga desenvolvimento uniforme.
5. Escolher até três ações por efeito, dependência e capacidade. Registrar executor, autoridade, prazo e evidência; ação urgente não aguarda outra etapa de maturidade.
6. Encerrar com avaliação, limites e pendências, deixando aprovação para a pessoa com alçada. Mudança de score e transição sustentada são conclusões diferentes; observar a rotina no período acordado.
''', [
     ('Primeira avaliação; quatro respostas positivas comprovadas nas dez.', 'IM-TI 4, nível descritivo 1; manter lacunas visíveis e escolher ações pelo efeito.'),
     ('Após trinta dias, relato confirma canal, quadro, FAQ e reunião; inventário e restauração faltam.', 'Há evidência parcial para quatro práticas, não total final de quatro. Conferir demais respostas e validade das evidências antes de calcular.'),
     ('Oito pontos; pode começar uma melhoria?', 'Score não autoriza ou impede projeto. Conferir risco, dependências, capacidade e aceite; não declarar pronto para inovar pela faixa.'),
     ]),
    ('metricas', 4, 'Cálculos e painel de indicadores',
     'Use para calcular indicadores operacionais, DAN financeira local, COT, ROI ou payback, preparar painel e comparar períodos com premissas explícitas.',
     '''1. Identificar a medida e sua decisão: disponibilidade, restauração, satisfação, composição de inventário, custo, retorno ou comparação. Projeção autorizada é cenário condicional identificado.
2. Conferir origem, unidade, janela, amostra, denominador e premissas. Ausência ou zero incompatível com a fórmula é dado insuficiente; não preencher com média presumida.
3. Consultar a convenção pertinente e mostrar fórmula, substituição, resultado e arredondamento. Fechamento administrativo não é restauração; proporção de legados não é DAN financeira.
4. Comparar somente com tolerância informada e manter sentido de desigualdade. Faixas históricas não demonstram probabilidade de ataque ou parada.
5. Para investimento, separar inicial e recorrência, horizonte e benefício. Horas liberadas são capacidade potencial até comprovar mudança de gasto. Apresentar sensibilidade e limite do payback simples.
6. Para painel, registrar valor, origem, período, tolerância, interpretação e ação. Média de notas, proporção de satisfeitos e NPS são medidas distintas; acesso a FAQ não comprova resolução.
7. Encerrar com memória de cálculo e lacunas. Cálculo favorável prepara decisão humana, sem aprovar investimento ou comprovar efeito do método.
''', [
     ('Quatro horas indisponíveis em 220 horas comerciais.', 'IDSC 98,18%, se as horas têm a mesma janela e exclusões. Comparar com tolerância acordada; 99,5% era referência local.'),
     ('300 horas de refatoração a R$ 80; orçamento anual de R$ 96.000.', 'DAN financeira estimada 0,25, com escopo e incerteza. O valor não classifica risco de paralisação.'),
     ('Migrar custa R$ 9.000 e benefício proposto é R$ 3.000/mês.', 'Pedir recorrência e horizonte. No exercício de recorrência zero e doze meses estabilizados: razão bruta 4, ROI líquido 300% e payback três meses; benefício pela metade dá 100% e seis meses.'),
     ('IDSC 98,9%; média 5,2 h em 40 chamados; notas somam 176 em 40 respostas.', 'ISU 4,4 se notas válidas de 1 a 5. Só chamar a média TMpR se forem durações de restauração; conferir janela e tolerância antes de classificar.'),
     ]),
    ('prd', 7, 'Requisitos e critérios de aceite',
     'Use para gerar ou revisar PRD, histórias, escopo e exclusões, requisitos operacionais e critérios Dado/Quando/Então no GEAR.',
     '''1. Distinguir criação, entrevista, histórias ou revisão. Consultar modelo e registrar problema, beneficiário e dados disponíveis antes da solução.
2. Quando necessário, preparar entrevista breve sobre tarefa, efeito, frequência, alternativa e restrição. Dez minutos e três frases são opções de síntese, sem eliminar informação material.
3. Organizar as sete partes: identificação/problema/valor; histórias; critérios; escopo/exclusões; requisitos operacionais; hipótese e medida; revisão técnica e aceite. Quantidade de histórias segue a necessidade.
4. Conferir capacidade e dependências antes de propor recorte. Excluir app, integração ou BI exige justificativa e acordo; duas semanas e duas páginas não são limites universais.
5. Conferir critérios observáveis, cenários pertinentes, acesso, falhas e retorno. Desempenho precisa de carga, rede, dispositivo e amostra; uma tela ou regra desconhecida fica pendente.
6. Na revisão, apresentar lacunas por seção e correção proposta. Escopo negativo pode registrar nenhuma exclusão relevante, com motivo; não inventar dois itens para preencher formato.
7. Encerrar a minuta quando escopo, critérios e pendências forem consultáveis. A pessoa com alçada aceita o recorte; aprovação fica separada do teste e do efeito financeiro.
''', [
     ('Vendedores respondem leads do site após dois dias e relatam perda de venda.', 'Preparar hipótese de tempo de primeiro contato; conferir canal, acesso e regras. WhatsApp, CRM ou dashboard não são escolhas automáticas.'),
     ('Revisar PRD colado pelo solicitante.', 'Registrar lacunas reais, incluindo critério sem resultado observável e fronteiras de escopo; não reescrever tudo sem necessidade.'),
     ('Documentar conciliação de boletos a partir do problema.', 'Preparar entrevista e recorte. Upload manual pode ser alternativa a comparar, sem afirmar integração bancária inviável por princípio.'),
     ]),
    ('seguranca', 3, 'Controles, risco e resposta',
     'Use para conferir controles de segurança, mapear risco de dependências, preparar recuperação ou resposta a incidente e resumo para decisão.',
     '''1. Distinguir verificação de controles, análise de dependência, recuperação, incidente ativo ou resumo. Incidente ativo segue para acionamento e decisão apropriados ao ambiente, sem aguardar checklist completo.
2. Consultar verificações complementares locais e evidência de cada controle. Registrar implementado no recorte verificado, em andamento, ausente ou não verificado; intenção não confirma configuração.
3. Identificar serviço, proprietário, ativos, dados e dependências. Conferir impacto, exposição e controles antes de estimar categoria de probabilidade. Classificação só usa critérios acordados, com incerteza.
4. Usar três perguntas iniciais quando útil: identidade/MFA, privilégio e recuperação. Elas ajudam a encontrar lacunas, sem substituir todos os controles. Escolher ações por exposição, consequência e capacidade, sem ordem rígida ou quatro itens obrigatórios.
5. Para PRI, conferir contatos, autoridade, comunicação, preservação de evidências, recuperação e aceite. Contenção concreta exige contexto e alçada; evitar comandos universais de desligar, isolar ou formatar.
6. Registrar frequência de revisão, cobertura, responsável e teste conforme risco e requisito local. Mensal, trimestral ou semestral são opções, sem obrigação normativa do GEAR. O plano precisa ser acessível na crise, em meio adequado.
7. Para resumo, informar cobertura conhecida, lacunas, consequência, alternativa e decisão necessária. Quantidade implementada não é certificação NIST ou CIS IG1.
8. Encerrar a minuta com evidências e ações atribuídas. Investigação fora da capacidade exige encaminhamento a profissional apropriado; orçamento pequeno não reduz a consequência possível.
''', [
     ('Backup em nuvem não testado; senha de administrador compartilhada.', 'Registrar relatos e cobertura desconhecida; conferir contas, privilégios e teste de restauração. Não atribuir probabilidade ou prazo de quinze dias por palavras.'),
     ('ERP SaaS com CPF e dados bancários de cinco mil clientes; senha padrão.', 'Conferir acesso, MFA, permissões, dados e dependências. Manter hipótese separada de exposição confirmada.'),
     ('Relato de arquivos sendo criptografados por ransomware.', 'Acionar responsável e autoridade urgentemente, avaliar contenção no ambiente e preservar evidências. Recuperação depende de cópia e serviço verificados.'),
     ('Preparar resumo para reunião de direção amanhã.', 'Usar somente controles e riscos documentados; sete de dez e verba R$ X do exemplo antigo são cenário fictício, sem preencher a empresa atual.'),
     ('Começar segurança sem diagnóstico prévio.', 'Começar pelo serviço e lacunas de inventário, acesso, cópia e resposta; demais controles permanecem visíveis, sem adiamento universal.'),
     ]),
]


def build(base=BASE):
    for suffix, index, title, description, steps, examples in SKILLS:
        identifier = 'gp-pme-' + suffix
        target = Path(base) / identifier / 'SKILL.md'
        _, _, _, _, sources, _, _ = SPECS[index]
        target.parent.mkdir(parents=True, exist_ok=True)
        text = f'---\nname: {identifier}\ndescription: {description}\n---\n\n# GEAR: {title.lower()}\n\n'
        text += ('Identificador GP-PME preservado para chamadas existentes. Edição editorial '
                 '2026.10; escopo consultivo e IA opcional. O método tem três '
                 'domínios e camadas transversais de adoção, indicadores e maturidade.\n\n')
        text += '## Executar a tarefa\n\n' + steps + '\n'
        text += '## Consultar conforme o pedido\n\n'
        for source in sources:
            path = ROOT / 'framework' / source
            label = path.read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
            text += '- ' + link(target, path, label) + ': abrir quando a tarefa exigir esse assunto.\n'
        if suffix == 'consultor':
            text += '\n| Assunto | Skill existente |\n| --- | --- |\n'
            for name, _, label, *_ in SKILLS[1:]:
                text += '| ' + label + ' | ' + link(target, Path(base)/('gp-pme-'+name)/'SKILL.md', 'gp-pme-'+name) + ' |\n'
            text += '\nO encaminhamento é recomendação. Acionamento real depende da disponibilidade e da tarefa autorizada.\n'
        if suffix == 'kanban':
            text += '\nA alternativa local de nove combinações continua no ' + link(target, ROOT/'GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md', 'guia técnico de execução') + '; prazos e descarte não decorrem automaticamente de categoria.\n'
        if suffix == 'seguranca':
            text += '\nLista e grade históricas: ' + link(target, ROOT/'framework/templates/risco-continuidade.md', 'verificações complementares locais') + '. Usar somente com critérios e cobertura explícitos.\n'
        text += ('\nAs fontes canônicas distinguem referência primária, adaptação e hipótese. '
                 'Quando a plataforma não acessar os arquivos, solicitar os trechos pertinentes '
                 'e registrar o limite. Arquivo anexado não garante recuperação correta.\n\n')
        text += '## Entregar e conferir\n\n'
        text += ('Entregar artefato adequado ao recorte, dados com origem e período, '
                 'memória dos cálculos pertinentes, fontes de pesquisa junto à afirmação '
                 'e lacunas atribuídas. Informação ausente fica como DADO INSUFICIENTE, '
                 'com próximo passo necessário. Exemplos são fictícios.\n\n'
                 'Minuta, cálculo e diagnóstico textual não comprovam execução no ambiente. '
                 'Usar somente ferramentas disponíveis para efeitos autorizados e registrar '
                 'entrada, resultado e limite. Aprovação, recurso, contenção, comunicação '
                 'externa, implantação e publicação pertencem à autoridade humana indicada. '
                 'Revisão por outro modelo é assistência.\n\n')
        text += link(target, ROOT/'framework/templates/revisao-ia.md', 'Registro de revisão') + ': consultar quando houver saída assistida com efeito material.\n\n'
        text += '## Exemplos fictícios para conferência\n\n'
        for i, (context, expected) in enumerate(examples, 1):
            text += f'### Caso {i}\n\nEntrada: {context}\n\nConferência esperada: {expected}\n\n'
        text += ('Concluir quando artefato, evidências disponíveis e pendências tiverem '
                 'responsável e próximo passo. Campos de decisão ficam para quem tem alçada.\n')
        target.write_text(text, encoding='utf-8')
        print(identifier, len(text), 'caracteres')


if __name__ == '__main__':
    build()
