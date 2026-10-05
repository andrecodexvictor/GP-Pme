"""Guias introdutórios revistos: dez arquivos, sem redirecionamentos vazios."""
import os,re
from pathlib import Path
from tools.editorial import ROOT,slug
from tools.build_legacy_masters import LEIGO

def section(title):
    sections=re.split(r'(?=^## )',LEIGO,flags=re.M)
    return next(s for s in sections if s.startswith('## '+title+'\n'))

GOV=section('Direção: decidir e acompanhar')+'''## Preparar e concluir a revisão

Use quando prioridades concorrem por recurso ou quando uma decisão precisa ser revista. TI prepara fila, dados e opções; dono do processo explica impacto; direção ou autoridade delegada decide. As entradas são demandas, evidências e capacidade disponível. A saída é uma decisão atribuída e comunicada.

1. Conferir decisões anteriores e o que ocorreu.
2. Examinar necessidade, alternativas, custo e risco.
3. Relacionar a proposta à finalidade principal de negócio.
4. Registrar aprovação, adiamento ou recusa, com motivo e responsável.
5. Comunicar a decisão e marcar a próxima verificação.

Concluir quando a equipe consegue localizar o acordo e sabe quem executa e aprova. Uma demanda sem vínculo explícito com receita pode ser necessária por obrigação, dependência ou risco; investigar a necessidade antes de recusá-la. A matriz não autoriza eliminar trabalho por classificação automática.

Fundamento: adaptação local com referência pública de governança contextual no COBIT, F09. DAA e ADM-Lite são linguagem do GEAR, sem equivalência com TOGAF ADM. A pauta e as durações são parâmetros locais.
'''
EXEC=section('Execução: tornar o trabalho visível')+'''## Aplicar na rotina

Use quando pedidos chegam dispersos ou a equipe inicia mais trabalho do que consegue encerrar. Responsável por TI mantém fila e capacidade; autoridade decide conflitos; usuário ou dono do processo verifica a saída. Entradas: demandas e responsáveis. Saídas: ordem de atendimento, trabalho concluído ou pendência atribuída.

1. Registrar solicitante, problema, serviço, responsável e prazo real.
2. Ordenar a fila conforme impacto, urgência e dependências; um novo pedido não vai automaticamente ao topo.
3. Conferir testes e bloqueios antes de iniciar outra tarefa.
4. Executar e verificar os critérios acordados.
5. Registrar aceite, pendência ou encerramento justificado e comunicar ao solicitante.

Um piloto precisa de ambiente, permissões, teste e retorno apropriados. O grupo participante confere a entrega; a hipótese de benefício continua a ser acompanhada. Um pedido de suporte não precisa esperar a próxima semana se o efeito de adiar justificar outra prioridade.

Concluir quando a saída foi aceita ou o motivo de encerramento está claro. Rever demandas bloqueadas e exceções na cadência combinada. Fundamento: adaptação local de fluxo e entregas curtas; Scrum Guide F03 e ITIL F10 orientam conceitos, sem validar o WIP de três nem uma implantação integral desses frameworks.
'''
SEC=section('Continuidade: conhecer dependências e testar')+'''## O que direção e TI precisam conferir

Use antes de depender de uma cópia de segurança e quando um serviço crítico muda. Direção confirma recursos e risco; dono do serviço define tolerâncias; TI organiza teste e controles. Entradas: serviço, dependências, cópia, acesso e autorização. Saída: evidência de recuperação com limites e ações atribuídas.

- [ ] Serviços e dependências prioritários estão registrados com proprietário?
- [ ] Contas críticas têm acesso necessário, MFA e exceções visíveis?
- [ ] A cópia tem proteção, retenção e frequência acordadas?
- [ ] O teste registra dados recuperados, serviço verificado, duração e limitações?
- [ ] O plano de incidente tem contatos e autoridades conferidos?
- [ ] Pendências têm responsável e próxima revisão?

Backup concluído, arquivo restaurado e serviço recuperado são evidências diferentes. Se o teste falhar, registrar a falha e planejar correção; a assinatura de uma folha não altera o resultado. Guardar o plano onde possa ser acessado durante indisponibilidade, preservando informações restritas.

No incidente, registrar sinais observados, acionar o responsável, avaliar contenção autorizada e comunicar fatos verificados. Confirmar recuperação com o negócio. Contatos não fornecidos ficam pendentes; não inventar números ou obrigações legais. Se a capacidade local for insuficiente, acionar especialista ou fornecedor previsto.

Fundamento: NIST F01–F02 e CISA F12. Quatro práticas locais não equivalem ao NIST completo nem às 56 salvaguardas CIS IG1 (F11). Não há eficácia de 98% demonstrada para essa seleção.
'''
IA=section('Usar IA quando for útil')+'''## Preparar uma solicitação

Use para rascunhar uma pauta, requisito, orientação ou cálculo que uma pessoa possa revisar. Responsável pela tarefa fornece dados autorizados; quem tem alçada decide o uso. Entrada: contexto, tarefa, restrições e fontes. Saída: minuta verificada ou lacunas explícitas.

Exemplo fictício de contexto: loja de roupas com dez computadores e vendas em nuvem. O exemplo descreve entrada, sem comprovar configuração ou segurança.

```text
Contexto: [serviço, pessoas afetadas, dependências e dados autorizados].
Tarefa: preparar uma lista breve de lacunas de continuidade.
Formato: problema, evidência, pergunta pendente, responsável e próximo passo.
Informar origem, data e limite de cada dado. Conferir fontes externas.
Separar fatos, hipótese e proposta; registrar informação insuficiente.
Autoridade humana: [quem revisa e pode aprovar efeitos organizacionais].
```

| Função de assistência | Minuta possível | Conferência humana |
| --- | --- | --- |
| Direção | Pauta e alternativas | Alçada, prioridade e recursos |
| Entrega | PRD e critérios | Viabilidade e aceite |
| Segurança | Lacunas e plano | Evidência, contenção e recuperação |
| Indicadores | Memória de cálculo | Premissas, unidades e fonte |

Concluir somente após verificar a saída e registrar aprovação, correção ou rejeição. Manter lacunas com responsável para obter o dado. A ferramenta pode errar mesmo quando segue o formato pedido; não equivale a uma equipe inteira de TI nem possui tempo garantido de resposta. A estrutura e a revisão são propostas locais; referências conceituais e limites estão nas fontes do GEAR.
'''
ROAD=section('Planejar os primeiros 30 dias')+'''## Simular antes de decidir

Frame-sim era o nome de uma proposta de exercício de cenários. O responsável por TI pode variar esforço, custo, adoção e capacidade em uma planilha para discutir alternativas com direção e financeiro. Uma conta demonstra a consequência das premissas; não prova sucesso da mudança antes da execução.

Registrar cenário, unidades, período, fontes dos valores, hipótese de benefício e sensibilidade. Conferir dados faltantes, duplicação de benefícios e recorrência. Horas recuperadas representam capacidade potencial enquanto não houver redução de despesa comprovada. Comparar o previsto ao observado posteriormente, preservando o cenário inicial.

Use a simulação para decidir o que testar e qual dado coletar. Direção autoriza recursos e riscos. Encerrar a preparação quando a proposta tem responsável, critérios, capacidade e condição de retorno. Essa verificação pré-projeto é distinta da adoção inicial de 30 dias.

Os ganhos antigos de 30–40% de interrupções não tinham medição documentada e foram retirados. Segurança e governança não aguardam o dia 31 se o serviço já precisa delas. Expansão de métricas, nuvem ou IA depende de necessidade e capacidade; nenhuma é etapa obrigatória para o nível máximo.

Fundamento de continuidade: NIST F01. A janela e a sequência semanal são propostas locais. Casos simulados são exercícios condicionais, sem resultado de campo.
'''
OVERVIEW=section('Começar pela rotina')+section('Entender as três frentes')+'''## Governança e gestão

Governança define finalidade, prioridade, recursos e risco aceito. Gestão organiza como executar o trabalho autorizado e como verificar a saída. Direção e TI precisam compartilhar o problema e os critérios de conclusão, mesmo quando uma pessoa acumula funções. A analogia antiga de uma viagem distinguia destino e condução; aqui as responsabilidades são explícitas no registro.

## Consultar no momento certo

A metáfora histórica do “Iceberg Invertido” descrevia entrada simples seguida de aprofundamento. Começar pela prática que resolve a necessidade observada; consultar fundamentos e limites quando a decisão exigir. A simplicidade do registro não dispensa compreender risco, alçada e evidências. O conhecimento técnico não fica automaticamente validado por ter sido fornecido por IA.

Organizar demandas, testar uma melhoria e rever prioridades são atividades que podem coexistir. Não formam promoção de cargo nem trajetória garantida de crescimento. “TI Enxuta” é a escolha local de adequar esforço e registro à equipe, com custo e manutenção considerados.
'''+section('Planejar os primeiros 30 dias')

def build():
    base='GP-PME antigravity/'
    specs=[
      ('GP-Pme complete/Dummies/Bloco_1_Pilar_Estrategico.md','Decidir prioridades com o negócio',GOV,['nucleo/governanca.md','templates/decisoes-prioridades.md']),
      ('GP-Pme complete/Dummies/Bloco_2_Pilar_Execucao_Agil.md','Organizar demandas e verificar entregas',EXEC,['guias/priorizar-demandas.md','templates/prd-aceite.md']),
      ('GP-Pme complete/Dummies/Bloco_3_Pilar_Seguranca_Essencial.md','Conferir continuidade e resposta',SEC,['guias/testar-restauracao.md','templates/incidente.md']),
      ('GP-Pme complete/Dummies/Bloco_4_Motor_de_IA.md','Usar assistência opcional por IA',IA,['guias/usar-ia.md','templates/prompts-assistencia.md']),
      ('GP-Pme complete/Dummies/Bloco_5_Roadmap_e_Frame_sim.md','Planejar adoção e exercitar cenários',ROAD,['adocao/primeiros-30-dias.md','indicadores/financeiros.md']),
      ('GP-Pme complete/Dummies/Sumario_Leigo.md','Visão inicial do GEAR',OVERVIEW,['README.md','fundamentos/origens-adaptacoes.md']),
      ('guide-for-dummies/Guia_GP-PME_para_Leigos.md','Guia introdutório do GEAR',OVERVIEW,['README.md','adocao/primeiros-30-dias.md']),
      ('guide-for-dummies/Guia_Leigo_Pilar_1.md','Guia de decisões com o negócio',GOV,['guias/conduzir-revisao.md','templates/responsabilidades.md']),
      ('guide-for-dummies/Guia_Leigo_Pilar_2.md','Guia da fila de TI e de pequenas melhorias',EXEC,['nucleo/execucao-servicos.md','guias/entregar-melhoria.md']),
      ('guide-for-dummies/Guia_Leigo_Pilar_3.md','Guia de continuidade e evidências',SEC,['nucleo/seguranca-continuidade.md','templates/risco-continuidade.md']),
    ]
    for name,title,body,refs in specs:
        target=ROOT/(base+name);relative=Path(os.path.relpath(ROOT/'framework',target.parent)).as_posix()
        text=f'# {title}\n\nEdição editorial GEAR 2026.10. Documento completo no caminho anterior para compatibilidade; regras vigentes em `framework/`. Direitos conforme LICENSE.md.\n\n'
        if name.startswith('guide-for-dummies/'):
            text+='Origem: versão declarada 5.2, de 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor.\n\n'
        text+='## Percurso de leitura\n\n'
        for label in re.findall(r'^## (.+)$',body,flags=re.M):text+=f'- [{label}](#{slug(label)})\n'
        text+='\n'+body+'\n## Próxima tarefa e referências\n\n'
        for ref in refs:
            label=(ROOT/'framework'/ref).read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
            text+=f'- [{label}](<{relative}/{ref}>)\n'
        text+=f'\nFontes F01–F12 e limites de consulta: [referências completas](<{relative}/referencias/fontes.md>). Os originais e o registro de revisão são preservados em `.context/`.\n'
        target.write_text(text,encoding='utf-8');print(name,len(text),'caracteres')

if __name__=='__main__':build()
