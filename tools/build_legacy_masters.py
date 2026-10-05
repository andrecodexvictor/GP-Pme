"""Deriva três manuais completos nos caminhos anteriores, com perfis de leitura.

A seleção de capítulos resulta da revisão dos três mestres de 02/06/2026.
Não executar sobre outros documentos históricos: têm conteúdo próprio.
"""
from pathlib import Path
import re
from tools.editorial import ROOT, slug

def excerpt(path, target):
    source=ROOT/'framework'/path
    text=source.read_text(encoding='utf-8')
    def link(m):
        value=m[2]
        if '://' in value or value.startswith('#'):return m[0]
        file,sep,anchor=value.partition('#')
        import os
        relative=Path(os.path.relpath((source.parent/file).resolve(),target.parent)).as_posix()
        return f'[{m[1]}](<{relative}{sep}{anchor}>)'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)

def heading_shift(text, level=1):
    return re.sub(r'^(#{1,5}) ',lambda m:'#'*level+m[1]+' ',text,flags=re.M)

LEIGO='''## Começar pela rotina

GEAR ajuda uma equipe pequena a registrar necessidades, decidir prioridades e verificar entregas. Direção define recursos e riscos; TI organiza a execução; o dono do processo explica o problema e aceita o resultado. Uma pessoa pode acumular funções, desde que isso fique visível.

Não é necessário comprar uma plataforma ou usar IA. Um quadro e registros consultáveis podem apoiar a gestão; backup e proteção de contas continuam exigindo tecnologia apropriada. O método não garante aumento de faturamento, proteção integral ou promoção do profissional de TI.

## Entender as três frentes

| Frente | Decisão prática | Registro útil |
| --- | --- | --- |
| Governança e direção | O que fazer, por qual motivo e com qual recurso | Prioridade, responsável e prazo |
| Execução e serviços | O que iniciar e como verificar a saída | Quadro, critério de conclusão e aceite |
| Segurança e continuidade | O que precisa continuar e como recuperar | Dependências, controles e teste |

Adoção, indicadores e maturidade ajudam a rever essas frentes. IA pode preparar minutas e cálculos, sob revisão humana; seu uso é opcional inclusive no nível máximo de maturidade.

## Direção: decidir e acompanhar

O manual anterior chamava essa participação de DAA: direcionar, agir e acompanhar. Na prática, direção decide a prioridade, TI executa o autorizado e ambos confrontam o resultado com evidências. ADM-Lite é o nome local de avaliar, dirigir e monitorar; não é o método ADM do TOGAF.

A revisão CD-TI Lite reúne direção, TI e dono do processo. Quinze dias e 30 minutos são um começo possível, ajustável à necessidade. A pauta pode distribuir cinco minutos para indicadores, quinze para prioridades, cinco para riscos e cinco para decisões. Uma emergência pode exigir decisão antes da reunião.

Registrar decisão, motivo, alternativas, aprovador, executor, prazo e próxima revisão. Se a mesma pessoa executa e aprova uma ação relevante, declarar o acúmulo e definir segunda conferência quando necessária. O registro deve permitir que uma pessoa ausente entenda o acordo.

A Matriz 4 Quadrantes relaciona iniciativas a receita, custos, experiência e resiliência. Configurar Pix pode ter hipótese de receita; rever licenças, hipótese de custo; preparar uma orientação, hipótese de experiência; testar recuperação, finalidade de continuidade. Nenhuma dessas classificações prova um benefício.

## Execução: tornar o trabalho visível

Use um registro oficial para a fila, com solicitante, executor, prioridade e saída esperada. Pedidos recebidos por telefone ou mensagem são registrados; uma emergência é atendida e entra na fila assim que viável. “Canal único” não significa recusar ajuda porque o formulário está indisponível.

| Estado | Significado |
| --- | --- |
| A Fazer | Ainda não iniciado |
| Em Andamento | Trabalho iniciado |
| Em Teste | Verificação técnica ou de negócio pendente |
| Concluído | Saída aceita ou encerramento justificado |

Comece com até três itens iniciados por executor, contando andamento, teste e bloqueio. Esse limite é parâmetro local de capacidade, não garantia de rapidez. Uma equipe de uma pessoa mantém foco em uma atividade de cada vez. Bloquear ou suspender um cartão conserva seu início e seu histórico.

Para uma emergência, registrar quem decidiu interromper, qual trabalho foi suspenso e que capacidade ficou comprometida. Depois da recuperação, decidir quando retomar o item. Uma quarta tarefa comum aguarda capacidade.

Uma melhoria começa com um PRD curto: problema, beneficiário, escopo, exclusões e critério de aceite. Uma ou duas semanas podem delimitar um piloto; se a entrega não couber, renegociar prazo ou escopo. TI verifica a solução e o dono do processo aceita o resultado. Aceite técnico não comprova retorno financeiro.

## Continuidade: conhecer dependências e testar

Identifique o serviço que precisa continuar, seus dados, contas, equipamentos e fornecedores. Comece pelas dependências críticas e registre o que falta mapear. O nome antigo “Inventário 80/20” expressava priorização; não prova que 20% dos ativos geram 80% do faturamento.

Contas individuais, acesso necessário e MFA reduzem exposições específicas, sem impedir todo ataque. Registre cobertura e exceções. MFA é autenticação multifator; um código de celular é apenas uma implementação possível, não a definição completa.

Combine frequência e retenção de backup com a perda de dados tolerável. Proteja a cópia e teste restauração em ambiente autorizado. Um arquivo recuperado não comprova recuperação do serviço inteiro. Os antigos parâmetros de backup diário, teste trimestral e 30 minutos precisam de justificativa local.

Prepare o PRI com contatos conferidos, autoridade para contenção, comunicação e passos de recuperação. No incidente, preserve evidências e confirme serviço e dados com seu dono. Formatação e desligamento não são instruções universais. Obrigações legais vão à competência responsável.

## Verificar sem confundir documento com resultado

- [ ] As demandas têm responsável, prioridade e critério de saída?
- [ ] O quadro mostra testes, bloqueios e exceções de capacidade?
- [ ] As decisões têm aprovador e próxima revisão?
- [ ] As dependências críticas têm proprietário e lacunas registradas?
- [ ] O teste de restauração registra escopo, resultado e limitações?
- [ ] Os contatos e alçadas do PRI foram conferidos em exercício?

Disponibilidade, tempo de restauração e satisfação são indicadores candidatos, escolhidos conforme a decisão. Informar período e origem. As antigas metas de 99,5% e 4,5/5 são referências locais, não exigências universais. Sem respostas, satisfação é dado insuficiente; sem incidentes restaurados, não existe média de restauração calculável.

## Usar IA quando for útil

Fornecer tarefa, dados autorizados, restrições e saída pretendida. Conferir fontes, cálculos e lacunas. A resposta deve separar informação fornecida, hipótese e recomendação. A pessoa com alçada decide se a saída pode ser usada. Um prompt não elimina erros; a equipe pode executar a mesma tarefa sem IA.

Quatro funções conceituais organizam a assistência: direção, entrega, segurança e auditoria. O software histórico tem um orquestrador e oito especialistas. As contagens descrevem camadas distintas e não criam novos domínios.

## Planejar os primeiros 30 dias

| Janela local | Foco | Evidência esperada |
| --- | --- | --- |
| Semana 1 | Registrar demandas e capacidade | Fila real, responsáveis e prioridades |
| Semana 2 | Conhecer dependências e testar recuperação | Inventário inicial e teste com limites |
| Semana 3 | Decidir prioridades e exercitar resposta | Decisão e PRI com contatos conferidos |
| Semana 4 | Rever evidências e pendências | Comparação por pergunta e próxima revisão |

Trinta dias são planejamento, sem garantir implantação ou avanço de maturidade. Períodos antigos de 31–90 e 91–180 dias exprimiam expansão pretendida; hoje a próxima etapa depende das lacunas e da capacidade. Não há ganho automático de 80% do suporte.

O IM-TI soma dez práticas verificadas, de 0 a 10. As faixas locais descrevem a rotina e ajudam a localizar lacunas; não certificam segurança nem comparam organizações diferentes. As perguntas foram revistas; resultados antigos exigem reaplicação. IA não é condição de resposta positiva.

## Termos para consulta

| Termo | Uso neste manual |
| --- | --- |
| Kanban | Quadro para tornar fila e trabalho iniciado visíveis |
| WIP | Trabalho iniciado sob responsabilidade do executor |
| PRD | Registro de problema, escopo e critérios de uma melhoria |
| PRI | Plano de resposta com contatos, alçadas e recuperação |
| RTO e RPO | Tolerâncias de tempo de recuperação e perda de dados |
| MVP | Recorte de solução para testar uma hipótese |
| Frame-sim | Nome histórico de proposta de simulação, sem equivalência com validação de campo |
| DAN e COT | Estimativa local de dívida e investimento de otimização, com premissas explícitas |

## Fontes e próxima tarefa

Conceitos de continuidade: NIST CSF 2.0 e guia para pequenas empresas, F01–F02. Desenvolvimento incremental: Scrum Guide 2020, F03; retirar elementos impede chamar o método de Scrum integral. Adaptação de governança e serviço: páginas oficiais COBIT e ITIL, F09–F10. Documentação: Diátaxis, F08. Referências completas e limites constam da lista vinculada abaixo. Cadências, WIP e IM-TI são propostas locais do GEAR.
'''

def build():
    specs=[
        ('GP-PME/GP-PME_Documento_Mestre_Completo_Leigos.md','Manual introdutório','6.0','leigo',[]),
        ('GP-PME/GP-PME_Documento_Mestre_Completo_Tecnico.md','Manual técnico completo','6.0','tecnico',[
            'nucleo/escopo-principios.md','nucleo/governanca.md','nucleo/execucao-servicos.md',
            'nucleo/seguranca-continuidade.md','indicadores/operacionais.md','indicadores/financeiros.md',
            'guias/usar-ia.md','guias/priorizar-demandas.md','guias/entregar-melhoria.md',
            'guias/tratar-incidentes.md','guias/testar-restauracao.md','guias/conduzir-revisao.md',
            'adocao/primeiros-30-dias.md','adocao/maturidade.md','fundamentos/origens-adaptacoes.md','glossario.md','referencias/fontes.md']),
        ('GP-PME antigravity/GP-PME_Documento_Mestre_Consolidado.md','Manual consolidado','5.2','consolidado',[
            'nucleo/escopo-principios.md','nucleo/governanca.md','nucleo/execucao-servicos.md',
            'nucleo/seguranca-continuidade.md','indicadores/financeiros.md','guias/usar-ia.md',
            'adocao/maturidade.md','adocao/primeiros-30-dias.md','fundamentos/origens-adaptacoes.md'])]
    for name,title,version,profile,chapters in specs:
        target=ROOT/name
        text=f'# GEAR: {title}\n\nFramework de governança e gestão de TI para pequenas e médias empresas.\n\nEdição editorial: GEAR 2026.10, 05/10/2026. Origem: GP-PME {version}, 02/06/2026. Crédito declarado na versão de origem: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md; a revisão não altera permissões. O caminho anterior foi mantido para compatibilidade.\n\n'
        text+='Esta versão conserva um manual completo para seu público. Regras compartilhadas são derivadas das fontes modulares vigentes; as contribuições próprias dos mestres foram incorporadas aos fundamentos e ao guia de assistência. A preservação da versão de origem e o mapa de seções constam da matriz de proveniência em `.context/gear-execution/`.\n\n'
        if profile=='leigo':text+=LEIGO
        else:
            text+='## Percurso de leitura\n\n'
            for path in chapters:
                chapter=excerpt(path,target)
                label=chapter.splitlines()[0].removeprefix('# ')
                text+=f'- [{label}](#{slug(label)})\n'
            text+='\n'
            for path in chapters:text+=heading_shift(excerpt(path,target))+'\n\n'
        import os
        rel=Path(os.path.relpath(ROOT/'framework',target.parent)).as_posix()
        text+=f'\nDocumentação modular: [GEAR](<{rel}/README.md>). Referências completas: [Fontes e limites](<{rel}/referencias/fontes.md>). Tarefa inicial: [Primeiros 30 dias](<{rel}/adocao/primeiros-30-dias.md>).\n'
        target.write_text(text,encoding='utf-8')
        print(name, len(text),'caracteres')

    chapter_specs=[
        ('Capitulo_1_Arquitetura_e_Principios.md','Arquitetura e princípios',
         ['nucleo/escopo-principios.md','fundamentos/origens-adaptacoes.md'],''),
        ('Capitulo_2_Governanca_Essencial_ADM_Lite.md','Governança e direção',
         ['nucleo/governanca.md','guias/conduzir-revisao.md','templates/responsabilidades.md','indicadores/operacionais.md'],''),
        ('Capitulo_3_Execucao_Agil_Ciclo_Micro_Adaptativo.md','Execução e serviços',
         ['nucleo/execucao-servicos.md','guias/priorizar-demandas.md','guias/entregar-melhoria.md','templates/prd-aceite.md'],MATRIZ),
        ('Capitulo_4_Seguranca_Critica_NIST_Lite.md','Segurança e continuidade',
         ['nucleo/seguranca-continuidade.md','guias/tratar-incidentes.md','guias/testar-restauracao.md','templates/incidente.md'],SEGURANCA),
        ('Capitulo_5_Metricas_Avancadas_DAN_e_COT.md','Indicadores e decisão financeira',
         ['indicadores/financeiros.md','indicadores/operacionais.md'],COT),
        ('Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md','Assistência opcional e prompts',
         ['guias/usar-ia.md','templates/prompts-assistencia.md','templates/revisao-ia.md'],''),
    ]
    for name,title,chapters,extra in chapter_specs:
        target=ROOT/'GP-PME antigravity/GP-Pme complete'/name
        text=f'# GEAR: {title}\n\nEdição editorial 2026.10. Caminho GP-PME preservado para compatibilidade. Capítulo revisto a partir do acervo anterior; práticas locais não constituem certificação. Direitos conforme LICENSE.md.\n\n'
        text+='\n\n'.join(heading_shift(excerpt(p,target)) for p in chapters)
        text+='\n\n'+extra
        text+='\nConsulta: [fontes e limites](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md).\n'
        target.write_text(text,encoding='utf-8')
        print(name,len(text),'caracteres')

MATRIZ='''## Alternativa local: três graus de impacto e urgência

O capítulo anterior também continha uma matriz de nove combinações. Ela é uma alternativa didática à matriz de duas faixas, não uma tabela de SLA validada. Definir os graus com exemplos do serviço; urgência é consequência de adiar, não sinônimo de dificuldade. O dono do processo confirma impacto; a autoridade decide prioridade; TI confere capacidade e dependências.

| Impacto | Urgência alta | Urgência média | Urgência baixa |
| --- | --- | --- | --- |
| Alto | Avaliar resposta imediata e alçada de emergência | Acordar prazo conforme consequência | Planejar com capacidade e dependências |
| Médio | Conferir prazo e serviço afetado | Ordenar com as demandas concorrentes | Manter fila com responsável |
| Baixo | Verificar se há obrigação ou risco que altera a ordem | Comparar com prioridades vigentes | Questionar necessidade; registrar decisão |

Os antigos rótulos “resolver hoje” e “descarte” foram retirados: contexto, risco e obrigação podem exigir outra decisão. Impacto individual não autoriza eliminar automaticamente uma demanda. Registrar decisão, motivo e comunicação ao solicitante.
'''

SEGURANCA='''## Assistência opcional e exercício de resposta

Uma equipe pode usar IA para preparar orientações contra phishing, examinar um relatório de permissões autorizado ou representar um incidente em exercício de mesa. Os dados devem ser adequados ao acesso da ferramenta. Menção textual a uma conta não comprova configuração, vulnerabilidade nem risco medido; a verificação depende de evidência técnica.

No exercício, escolher serviço, cenário, participantes e autoridade. Registrar quem reconhece o problema, aciona contatos, decide contenção, comunica e verifica recuperação. Discutir lacunas e atribuir correção. A IA pode narrar o cenário; não autoriza ações no ambiente real. O exercício não comprova capacidade sob qualquer incidente nem conformidade legal.
'''

COT='''## Cenário histórico recalculado: serviço de arquivos

O exemplo anterior supunha oito horas de indisponibilidade mensal, dez pessoas afetadas e R$ 30 por hora. A conta é 8 × 10 × 30 = R$ 2.400/mês de capacidade potencial comprometida. Não é perda financeira realizada sem dados adicionais; conferir pessoas simultaneamente afetadas, possibilidade de realocação e custo efetivo.

A migração proposta tinha R$ 4.800 atribuídos a esforço e licenças, sem período das licenças nem recorrência claros. Não há base para confirmar ROI. Para exercitar a fórmula, assumir explicitamente R$ 4.800 de aporte inicial, custo recorrente zero e eliminação integral das oito horas durante doze meses em estado estabilizado. Benefício potencial anual: R$ 28.800; razão bruta: 6; ROI líquido condicional: (28.800 − 4.800) / 4.800 × 100 = 500%; payback simples: 4.800 / 2.400 = 2 meses.

A expressão antiga “50% de ROI ao mês” era a razão mensal benefício/investimento, não retorno líquido no horizonte anual. Se apenas metade da capacidade for recuperada, benefício potencial de R$ 1.200/mês, ROI líquido anual condicional de 200% e payback de 4 meses. Com benefício nulo, ROI é −100% na hipótese sem recorrência e não há payback finito. Incluir licenças recorrentes altera esses resultados.

Uma migração para nuvem não demonstra eliminação de indisponibilidade nem redução de DAN por si só. Comparar dependências, proteção das cópias, manutenção e alternativas; a autoridade decide investimento após conferir premissas.
'''

if __name__=='__main__':build()
