"""Cenários didáticos: premissas históricas, cálculos locais e limites explícitos."""
from pathlib import Path
from server.core import calcular_cot

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Simulacao'
# Premissas do acervo original. Não são amostras de empresas nem resultados medidos.
PROFILES = [
    dict(id='A', file='Perfil_A_TI_Solo.md', title='TI de uma pessoa', people=10,
         sector='Contabilidade e serviços profissionais', revenue=1800000,
         team='Um técnico de TI que acumula suporte, infraestrutura e cópias de segurança; salário de referência de R$ 5.000.',
         budget=108000, stack='Google Workspace, ERP contábil local (exemplos históricos: Domínio ou Alterdata), Wi-Fi, 12 notebooks e cópia manual em HD externo.',
         pain='Pedidos chegam pelo telefone pessoal, corredor e mensagens. Um sócio não consegue acompanhar o pedido; uma interrupção de 40 minutos no ERP impede a emissão de guias. A equipe não possui registro de teste de restauração.',
         cost=44, hours=2500, ti=(40,15), rework=(30,12), affected=8, downtime=(62.5,12.5),
         tmpr=(9,4), isu=(3.4,4.5), incidents=360, debt=480, dan_after=.10, maturity=(1,6),
         weeks=(10,8,5,5), total_hours=70, training=1000, backup=1200, platforms=0,
         improvement='Automatizar o relatório mensal de honorários e examinar a substituição ou correção do servidor instável.',
         faq='Senha, Wi-Fi, impressora, VPN e e-mail', focus='ERP, dados contábeis e notebooks dos sócios',
         interim='Hipóteses históricas para 90 dias: TMpR de 5,5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes.',
         risk=(.18,.05,40000), risk_context='Uma paralisação pode afetar obrigações fiscais e contratos de clientes.',
         control_context='ERP e Workspace; MFA nas contas críticas e bancárias; proteção das estações e firewall do sistema e roteador.'),
    dict(id='B', file='Perfil_B_25_Funcionarios.md', title='TI com analista e estagiário', people=25,
         sector='Comércio e distribuição regional com comércio eletrônico', revenue=8000000,
         team='Um analista pleno (salário de referência de R$ 6.000) e um estagiário em meio período.',
         budget=220000, stack='ERP híbrido, comércio eletrônico integrado ao checkout, Microsoft 365, servidor de arquivos e 25 estações.',
         pain='Chamados do checkout chegam por três canais. O ERP possui cerca de 40 integrações e rotinas manuais, sem análise de custo. Uma queda do servidor interrompe o faturamento de 13 pessoas. As cópias ainda não têm teste registrado.',
         cost=53, hours=3500, ti=(60,20), rework=(70,25), affected=13, downtime=(87.5,17.5),
         tmpr=(8,4), isu=(3.3,4.5), incidents=744, debt=800, dan_after=.12, maturity=(2,9),
         weeks=(14,12,7,7), total_hours=90, training=3000, backup=1800, platforms=0,
         improvement='Automatizar as planilhas de entrada do ERP com PRD e teste de aceite; investigar cada integração antes de removê-la.',
         faq='Senha, VPN, checkout, nota fiscal e impressora', focus='ERP, servidor de arquivos e comércio eletrônico',
         interim='Hipóteses históricas para 90 dias: TMpR de 5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes.',
         risk=(.20,.05,80000), risk_context='Uma paralisação afeta faturamento, estoque e pedidos do comércio eletrônico.',
         control_context='ERP, Microsoft 365 e plataforma de vendas; MFA no financeiro e contas administrativas; atualização do ERP e segmentação básica.'),
    dict(id='C', file='Perfil_C_50_Funcionarios.md', title='Primeiro gestor de TI', people=50,
         sector='Indústria leve com distribuição própria', revenue=20000000,
         team='Um analista pleno, um técnico júnior e um gestor (salário de referência de R$ 10.000) que também atende demandas.',
         budget=500000, stack='ERP industrial, MES, Microsoft 365, servidor de arquivos, coletores, aproximadamente 50 estações e VPN para duas filiais.',
         pain='O técnico registra pedidos em caderno, o analista recebe mensagens e a produção liga diretamente para a equipe. Falhas no MES interrompem apontamentos; expedição alimenta o ERP por planilhas. O gestor não dispõe de uma linha de base confiável.',
         cost=62, hours=3600, ti=(100,39), rework=(145,48), affected=30, downtime=(90,18),
         tmpr=(8,4), isu=(3.3,4.5), incidents=1320, debt=1500, dan_after=.12, maturity=(2,9),
         weeks=(18,14,12,8), total_hours=140, training=6000, backup=3600, platforms=2400,
         improvement='Automatizar a planilha de expedição e estudar as dependências ERP–MES; o gestor coordena prioridades e os técnicos verificam execução.',
         faq='Senha, VPN, coletor, MES e impressora', focus='ERP, MES, servidor de arquivos e coletores',
         interim='Hipóteses históricas para 90 dias: TMpR de 5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes.',
         risk=(.20,.05,120000), risk_context='Uma paralisação pode interromper apontamento de produção e expedição, com exposição a atrasos contratuais.',
         control_context='ERP, MES e Microsoft 365; proteção gerenciada das estações; segmentação entre chão de fábrica e escritório.'),
    dict(id='D', file='Perfil_D_100_Funcionarios.md', title='Serviços com dados pessoais', people=100,
         sector='Serviços B2B com dados pessoais, como saúde, finanças ou educação', revenue=45000000,
         team='Seis pessoas: coordenador, três analistas de suporte e infraestrutura, desenvolvedor de integrações e especialista de segurança. Faixa histórica de cinco a oito pessoas. O papel de encarregado de dados exige definição própria.',
         budget=1200000, stack='ERP e CRM em nuvem, atendimento próprio, Microsoft 365, ambiente de dados com acesso restrito, mais de 100 estações, APIs e duas filiais.',
         pain='Há um canal oficial, mas gerentes também ligam ao coordenador. Cada analista prioriza sem regra comum. Integrações entre CRM, atendimento e ERP falham. O inventário de dados e a revisão de acesso são insuficientes para examinar o tratamento de dados pessoais.',
         cost=70, hours=4500, ti=(180,60), rework=(260,70), affected=80, downtime=(67.5,13.5),
         tmpr=(6.5,3.5), isu=(3.6,4.6), incidents=2400, debt=3000, dan_after=.11, maturity=(4,10),
         weeks=(30,24,20,16), total_hours=540, training=10000, backup=10000, platforms=8000,
         improvement='Reduzir digitação entre CRM e ERP, catalogar integrações e revisar decisões a partir de indicadores. Aprovar e verificar mudanças que envolvam dados pessoais.',
         faq='Senha, acesso, CRM, ERP e atendimento', focus='ERP, CRM, plataforma de atendimento, APIs e dados pessoais',
         interim='Hipóteses históricas para 90 dias: TMpR de 4,5 h, disponibilidade de 99,3% e autoatendimento de 45% das dúvidas recorrentes.',
         risk=(.20,.04,250000), risk_context='O cenário combina recuperação operacional, comunicação de incidente e possível exposição de dados pessoais; sanção e reputação não são perdas certas.',
         control_context='ERP, CRM, Microsoft 365 e APIs; acesso por necessidade; proteção gerenciada, segregação de ambientes e catálogo de dados pessoais.'),
]

def number(n, places=2):
    return f'{n:,.{places}f}'.replace(',', 'X').replace('.', ',').replace('X','.')

def money(n): return 'R$ ' + number(n)

def inputs(p):
    capacity=(p['ti'][0]-p['ti'][1])*p['cost']+(p['rework'][0]-p['rework'][1])*25
    downtime=(p['downtime'][0]-p['downtime'][1])*p['affected']*25/12
    investment=p['total_hours']*p['cost']+p['training']
    recurrent=(p['backup']+p['platforms'])/12
    return investment, capacity+downtime, recurrent

def result_row(p, share):
    i,b,c=inputs(p); r=calcular_cot(i,b*share,c)
    payback='Sem payback finito' if r['payback_meses'] is None else number(r['payback_meses'])+' meses'
    return f'| {number(share*100,0)}% | {money(b*share)} | {money(b*share-c)} | {number(r["roi_anual_percent"])}% | {payback} |'

CONTROLS=[
    ('Inventário de equipamentos','Lista com responsável, serviço e lacunas de cobertura','Ativos desconhecidos ou sem manutenção'),
    ('Inventário de software e dados','Versões, licenças, integrações e fluxos de dados','Dependências desconhecidas e uso sem rastreabilidade'),
    ('Vulnerabilidades','Prioridade de correção, teste e exceções documentadas','Exploração de falhas conhecidas'),
    ('Configuração segura','Revisão de serviços expostos e teste da configuração','Exposição desnecessária e propagação'),
    ('Identidade e MFA','Cobertura de contas críticas e exceções','Comprometimento de credenciais'),
    ('Privilégio mínimo','Aprovação, revisão e remoção de acesso excedente','Uso indevido de privilégios'),
    ('Proteção contra malware','Cobertura, atualização, alertas e encaminhamento','Código malicioso e ransomware'),
    ('Cópias e recuperação','Retenção, separação e restauração do escopo escolhido','Perda de dados e recuperação inviável'),
    ('Rede e perímetro','Regras revisadas e teste de segmentação','Acesso indevido e movimento lateral'),
    ('Conscientização e resposta','Orientação, exercício, contatos e alçadas','Fraude e resposta descoordenada'),
]

def profile(p):
    i,b,c=inputs(p); ident=p['id']; ti_gain=(p['ti'][0]-p['ti'][1])*p['cost']; rw_gain=(p['rework'][0]-p['rework'][1])*25
    ind_gain=(p['downtime'][0]-p['downtime'][1])*p['affected']*25/12
    before=p['ti'][0]*p['cost']+p['rework'][0]*25+p['downtime'][0]*p['affected']*25/12
    dan=p['debt']*p['cost']/p['budget']; availability=[100*(1-x/p['hours']) for x in p['downtime']]
    tables='\n'.join(f'| {label} | {number(a)} | {number(z)} | {unit} |' for label,a,z,unit in [
        ('Disponibilidade',*availability,'% da janela de serviço'),('Indisponibilidade',*p['downtime'],'h/ano'),
        ('Resolução média',*p['tmpr'],'h por chamado'),('Satisfação',*p['isu'],'média de 1 a 5'),
        ('Tempo TI não aproveitado',*p['ti'],'h/mês'),('Retrabalho do usuário',*p['rework'],'h/mês'),
        ('DAN financeiro',dan,p['dan_after'],'custo de refatoração/orçamento anual')])
    controls='\n'.join(f'| {n} | {label} | {proof} | {risk} |' for n,(label,proof,risk) in enumerate(CONTROLS,1))
    pb,pa,loss=p['risk']; expected=(pb-pa)*loss
    note=''
    if ident=='C':
        note='O custo-hora de R$ 62 é um parâmetro didático preservado. A expressão antiga `(53 + 53 + 88)/3` resulta em R$ 64,67, não R$ 62. Para uma média ponderada real, registrar as horas e os custos de cada profissional.'
    elif ident=='B':
        note='Correção desta edição: 99,5% de disponibilidade em 3.500 h corresponde a 17,5 h de indisponibilidade, não 15,5 h. O benefício foi recalculado sem arredondar parcelas intermediárias.'
    else:
        note='Os custos-hora são valores arredondados do exemplo histórico, sem pesquisa salarial. Encargos de 1,55 e jornada de 176 h/mês são hipóteses locais, a substituir pelo custo real.'
    legal=''
    if ident=='D':
        legal='''
### Dados pessoais e resposta

O plano deve identificar o controlador, quem avalia o incidente e quem comunica titulares e autoridade. O catálogo de dados, o uso de MCP e a presença de IA não comprovam conformidade com a LGPD. Não pressupor que o especialista técnico de segurança acumule automaticamente o papel de encarregado.

O prazo geral de comunicação pelo controlador à ANPD e aos titulares é de **três dias úteis**, para incidentes que possam acarretar risco ou dano relevante aos titulares, ressalvadas regras específicas. O antigo prazo de “72 horas” foi retirado. Conferir marco inicial, contagem, conteúdo e regime aplicável antes de usar um playbook operacional. ANPD, orientação CIS, pergunta 4, que reproduz os arts. 6 e 9 da Resolução CD/ANPD nº 15/2024; consulta em 04.10.2026: [Orientação oficial](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis). O acesso ao regulamento integral falhou; não foram verificadas exceções para pequeno porte.

A multa simples prevista no art. 52, II, da LGPD pode alcançar 2% do faturamento da pessoa jurídica de direito privado, grupo ou conglomerado no Brasil no último exercício, excluídos tributos, limitada a R$ 50 milhões por infração. Sua aplicação depende de processo administrativo e critérios legais. R$ 900 mil seria apenas a multiplicação de 2% pelo faturamento hipotético de R$ 45 milhões; não é multa estimada nem perda provável deste cenário. [Lei nº 13.709/2018, texto atualizado, arts. 48 e 52](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html), consulta em 04.10.2026.
'''
    return f'''# Perfil {ident} — {p['title']}

Cenário didático do GEAR para {p['people']} colaboradores. Os valores de partida e de melhoria são **premissas fictícias do acervo**, preservadas para comparar hipóteses. Não descrevem uma implantação realizada. Cálculos: [Calculadora de ROI](Calculadora_ROI.md); convenções: [indicadores financeiros](../framework/indicadores/financeiros.md).

## 1. Retrato e escopo

| Item | Premissa |
| --- | --- |
| Setor | {p['sector']} |
| Pessoas | {p['people']} |
| Faturamento anual | {money(p['revenue'])} |
| Equipe | {p['team']} |
| Orçamento anual de TI | {money(p['budget'])} |
| Ambiente | {p['stack']} |

Os valores de faturamento e orçamento situam o exercício. Não constituem benchmark de porte, pessoal ou gasto. A alocação de salários e infraestrutura do texto antigo não foi verificada como orçamento de uma empresa real.

## 2. Situação de partida

{p['pain']}

A linha de base adota custo TI de {money(p['cost'])}/h, custo de usuário de R$ 25/h e janela anual de {number(p['hours'],0)} h. Pessoas afetadas pela indisponibilidade: {p['affected']}. Volume hipotético: {number(p['incidents'],0)} incidentes/ano, equivalente a {number(p['incidents']/12)} por mês e {number(p['incidents']/12/p['people'])} por pessoa/mês.

{note}

O DAN inicial usa {number(p['debt'],0)} h de refatoração × {money(p['cost'])}/h ÷ {money(p['budget'])}: {number(dan,3)}. As antigas cores e faixas não são limites financeiros validados.

A soma dos três componentes de tempo da situação de partida é {money(before)}/mês. Esse valor representa capacidade avaliada monetariamente, sem receita perdida, impostos ou dupla contagem entre categorias. Se as horas de indisponibilidade já estiverem nas horas de retrabalho, retirar a sobreposição.

## 3. Plano inicial de 30 dias

TI organiza a execução; o dono do processo negocia prioridades e verifica entregas. [Primeiros 30 dias](../framework/adocao/primeiros-30-dias.md) define o percurso. Esforço hipotético inicial: {sum(p['weeks'])} h somadas, distribuídas abaixo; ajustar à capacidade real.

| Janela | Trabalho | Evidência de conclusão | Horas |
| --- | --- | --- | ---: |
| Dias 1–7 | Diagnóstico; canal oficial; quadro e responsáveis | Pedidos migrados e política de trabalho iniciado acordada | {p['weeks'][0]} |
| Dias 8–14 | Orientações para {p['faq'].lower()}; inventário de {p['focus'].lower()}; revisão de cópias | Escopo inventariado e teste de restauração registrado | {p['weeks'][1]} |
| Dias 15–21 | Plano de incidente; revisão conjunta de prioridades; matriz valor/esforço | Alçadas, contatos e decisões registradas | {p['weeks'][2]} |
| Dias 22–30 | Indicadores necessários; retrospectiva; reaplicação do questionário | Origem dos dados, lacunas e próximas ações | {p['weeks'][3]} |

O ponto de partida local para WIP é três itens por executor, contando execução, teste e bloqueio. Emergências têm alçada, efeito e exceção registrados. Um quadro em papel, Trello, Planner ou Jira pode servir conforme o contexto. A adoção de ferramenta não demonstra aplicação da regra.

Depois do dia 30, selecionar melhorias conforme evidência e capacidade. {p['improvement']} O acervo chamava esse percurso de Fases Um a Três; os nomes não impõem calendário anual, sprint semanal ou MVP obrigatório de duas semanas. O restante das {p['total_hours']} h de implantação inclui melhorias posteriores, e não é todo trabalho realizado no primeiro mês.

IA pode auxiliar triagem, rascunhos de PRD, consulta de fontes e organização de indicadores, com revisão responsável. ADK e MCP são opções técnicas, inclusive neste porte. Caso adotados, acrescentar seus custos e restrições de dados; nenhum resultado abaixo depende da obrigatoriedade de IA. Um teste de restauração verifica seu escopo e duração; o prazo histórico de 30 minutos não é garantia universal.

## 4. Hipóteses de melhoria

{p['interim']} Esses números não têm observações ou estudo que confirmem sua realização; não entram na conta anual. A linha posterior abaixo conserva as hipóteses usadas pelo exercício original para um estado estabilizado.

| Indicador | Partida hipotética | Estado posterior hipotético | Unidade |
| --- | ---: | ---: | --- |
{tables}

Canal oficial e quadro podem ajudar a localizar pedidos e bloqueios. Orientações podem resolver dúvidas recorrentes. Melhorias nas integrações podem reduzir digitação duplicada. Cópias verificadas podem apoiar recuperação. A contribuição de cada prática depende de aplicação, falhas, escopo e contexto; as diferenças da tabela não foram causalmente demonstradas.

O questionário histórico atribuía {p['maturity'][0]} respostas positivas à partida e sugeria {p['maturity'][1]} no horizonte anual. Nenhuma transição está assegurada. As perguntas foram revistas nesta edição: reaplicar [IM-TI com evidências](../framework/adocao/maturidade.md), sem transferir os scores antigos. Nível máximo permanece possível sem IA.

## 5. Comparação operacional e verificação

| Área | Situação descrita no cenário | Prática proposta | O que verificar |
| --- | --- | --- | --- |
| Demanda | Pedidos dispersos ou fora da regra | Canal oficial com rota para urgência | Amostra de pedidos registrados e encaminhados |
| Execução | Priorização e interrupções sem critério comum | Quadro, WIP por executor e aceite | Idade, bloqueios, testes e exceções |
| Continuidade | Cópias sem evidência suficiente | Escopo, retenção e restauração | Dependências, RTO/RPO e limitações do teste |
| Melhorias | Rotinas manuais e integrações frágeis | PRD curto e decisão valor/esforço | Teste com dono do processo e efeito observado |
| Relação com negócio | Expectativa sem decisão rastreável | Revisão conjunta de prioridades | Responsável, alçada, recurso e decisão |

```mermaid
flowchart LR
    A[Registrar a situação] --> B[Escolher prática e responsável]
    B --> C[Executar e verificar]
    C --> D[Medir na mesma janela]
    D --> E[Rever a hipótese e a decisão]
```

O diagrama representa o método de avaliação. Não expressa um antes/depois já observado.

## 6. Memória financeira e sensibilidade

| Componente | Conta | Valor |
| --- | --- | ---: |
| Capacidade TI potencial | ({p['ti'][0]} − {p['ti'][1]}) h/mês × {money(p['cost'])}/h | {money(ti_gain)}/mês |
| Capacidade do usuário potencial | ({p['rework'][0]} − {p['rework'][1]}) h/mês × R$ 25/h | {money(rw_gain)}/mês |
| Capacidade por menor indisponibilidade | ({number(p['downtime'][0])} − {number(p['downtime'][1])}) h/ano × {p['affected']} pessoas × R$ 25/h ÷ 12 | {money(ind_gain)}/mês |
| Benefício bruto condicional | Soma sem arredondamento intermediário | {money(b)}/mês |
| Investimento inicial | {p['total_hours']} h × {money(p['cost'])}/h + {money(p['training'])} de treinamento/implantação | {money(i)} |
| Operação anual incremental | Cópias {money(p['backup'])} + plataformas {money(p['platforms'])} | {money(c*12)}/ano |

As plataformas dos perfis C e D são classificadas como despesa anual recorrente neste exercício; o texto antigo não informava o período. Confirmar contratos antes de aplicar. O treinamento/licenças iniciais do perfil A foi mantido como implantação. Horas internas são custo de uso de capacidade, mesmo que a folha já seja paga. Para uma análise de caixa, separar desembolso incremental e custo de oportunidade.

Horizonte ilustrativo: 12 meses em estado estabilizado. `ROI líquido = ((benefício mensal − custo mensal) × 12 − investimento) / investimento × 100`. `Payback simples = investimento / (benefício mensal − custo mensal)`, se o denominador for positivo. Não é uma previsão de payback desde o início: benefícios graduais e trabalhos posteriores requerem fluxo mensal datado.

| Parcela do benefício realizada | Benefício bruto mensal | Benefício líquido mensal | ROI líquido em 12 meses | Payback simples |
| --- | ---: | ---: | ---: | ---: |
{chr(10).join(result_row(p,s) for s in (0,.6,1))}

As parcelas de 0%, 60% e 100% são testes de sensibilidade; não representam probabilidade, piso conservador ou resultado esperado. Nenhuma redução de despesa foi comprovada. A conta exclui inflação, impostos, valor do dinheiro no tempo, receita perdida e risco de segurança. Conferir sobreposição de horas e a realização do benefício antes de decidir.

O total histórico de custos do primeiro ano, que misturava investimento e recorrência, era {money(i+c*12)}. Sua preservação explica o número anterior; o cálculo antigo `benefício anual / total × 100` era uma razão bruta, sem subtrair investimento e operação.

## 7. Risco, controles e limites

{p['risk_context']} O exemplo histórico usava probabilidade anual de {number(pb*100,0)}% antes e {number(pa*100,0)}% depois, com perda por incidente de {money(loss)}. A conta `(p antes − p depois) × perda` resulta em {money(expected)}/ano. **As probabilidades e a perda são arbitrárias**: o valor não demonstra risco evitado, média setorial ou proteção obtida. Ele foi preservado somente como exercício de valor esperado e não é somado ao benefício financeiro.

Abaixo estão dez áreas de atenção do acervo, com evidência a coletar. Não se trata da lista completa do CIS IG1 nem de controles já implantados. Estado de todas as linhas: **não verificado neste cenário**. [Segurança e continuidade](../framework/nucleo/seguranca-continuidade.md) relaciona a seleção local ao NIST CSF 2.0; [fontes e limites](../framework/referencias/fontes.md) registra também CIS e o acesso às demais referências.

Contexto específico: {p['control_context']}

| Nº | Área | Evidência a coletar | Exposição a examinar |
| --- | --- | --- | --- |
{controls}
{legal}
Origem: perfil autoral histórico preservado em `.context/originais/gear-2026-10-04/Simulacao/`. Adaptação e fórmulas são locais; não são equações atribuídas a ISO, COBIT, ITIL, NIST ou CIS. Para usar: substituir hipóteses, registrar origem e data, conferir com finanças e dono do processo e decidir dentro da alçada.

Voltar: [Índice dos cenários](README.md). Consultar: [Calculadora](Calculadora_ROI.md).
'''

def main():
    for p in PROFILES: (OUT/p['file']).write_text(profile(p),encoding='utf-8')
    rows=[]
    for p in PROFILES:
        i,b,c=inputs(p); r=calcular_cot(i,b,c)
        rows.append(f'| [{p["id"]} — {p["title"]}]({p["file"]}) | {p["people"]} | {money(i)} | {money(c*12)} | {money(b)} | {number(r["roi_anual_percent"])}% |')
    (OUT/'README.md').write_text('''# GEAR — cenários condicionais por porte

Quatro exercícios completos preservam retratos, problemas, planos, indicadores, cálculos e áreas de controle do acervo GP-PME. As empresas, valores e estados de melhoria são fictícios. Não há observações de implantação ou retorno medido.

Leia a [Calculadora](Calculadora_ROI.md), escolha um perfil e substitua as hipóteses por dados documentados. Cada perfil contém sete seções: contexto, partida, plano inicial, hipóteses de melhoria, verificação operacional, memória financeira e risco. Os perfis não constituem benchmark de equipe ou receita.

| Perfil | Pessoas | Investimento inicial | Operação anual incremental | Benefício mensal potencial | ROI líquido condicional, 12 meses |
| --- | ---: | ---: | ---: | ---: | ---: |
'''+ '\n'.join(rows)+'''

O ROI supõe benefício integral e constante por 12 meses em estado estabilizado. A análise desde o início exige fluxos datados. Os perfis trazem sensibilidade a 0%, 60% e 100% de realização do benefício. Tempo liberado pode ser realocado, sem reduzir despesa paga; retirar dupla contagem entre retrabalho e indisponibilidade.

Nesta edição, investimento e recorrência foram separados, o ROI passou a ser líquido e o perfil B foi corrigido para 17,5 h de indisponibilidade a 99,5% em 3.500 h. R$ 62/h no perfil C é um parâmetro, sem média salarial comprovada. IA permanece opcional em todos os portes; maturidade e conformidade dependem de evidências.

As probabilidades de incidente dos exemplos antigos são arbitrárias e aparecem apenas como exercício isolado, sem integrar o retorno. Controles estão “não verificados”, com evidência a coletar. Consulte as [fontes do método](../framework/referencias/fontes.md) e as referências legais do perfil D.

Fontes editáveis e contas: `tools/build_simulations.py`. Os originais possuem manifesto e hashes em `.context/originais/gear-2026-10-04/`. O arquivo `dataset_framesim_nexus.json` é dado preservado do usuário e não é transformado pelo gerador.
''',encoding='utf-8')
    print('Quatro cenários e índice gerados; dataset preservado.')

if __name__=='__main__':main()
