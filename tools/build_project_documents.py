"""Consolida sínteses autorais e documentos de manutenção, sem editar terceiros."""
from pathlib import Path
import re
from tools.editorial import ROOT
from tools.build_legacy_masters import excerpt,heading_shift
from tools.publication_origin import origin

SPECS={
 'Docs/PRD.md':('Requisitos do GEAR',['nucleo/escopo-principios.md','nucleo/governanca.md','nucleo/execucao-servicos.md','nucleo/seguranca-continuidade.md','templates/revisao-ia.md','indicadores/financeiros.md','indicadores/assistencia.md']),
 'Docs/Roadmap.md':('Adoção e manutenção',['adocao/primeiros-30-dias.md','adocao/preparacao-cronograma.md','adocao/maturidade.md','templates/carteira-iniciativas.md']),
 'Docs/Tasklist.md':('Tarefas e critérios de conclusão',['templates/tasklist.md','adocao/preparacao-cronograma.md','templates/inventario-dependencias.md','templates/revisao-ia.md']),
 'Docs/Specialist_Agents.md':('Funções de assistência e contratos',['guias/usar-ia.md','templates/prompts-assistencia.md','templates/instrucao-assistencia.md','indicadores/assistencia.md']),
 'References/Análise Consolidada_ Referencial Teórico e Trabalhos Correlatos (Novos Documentos).md':('Referencial: conceitos e limites',['fundamentos/origens-adaptacoes.md','referencias/fontes.md']),
 'References/checklist_10_controles_nist.md':('Verificações locais de segurança',['templates/risco-continuidade.md','nucleo/seguranca-continuidade.md']),
 'References/Dados da Conversa do Claude.md':('Registro da modelagem em conversa',['fundamentos/origens-adaptacoes.md','nucleo/escopo-principios.md']),
 'References/Dados das Conversas do Gemini.md':('Registro de requisitos de pesquisa',['fundamentos/origens-adaptacoes.md','indicadores/assistencia.md']),
 'References/Dados do Repositório GitHub_ Frame-sim.md':('Frame-sim: proposta histórica e limites',['exemplos/cenarios-historicos.md','indicadores/financeiros.md']),
 'References/Notebook 1_ Adaptive IT Governance_ AI for SME Agility.md':('Notebook: temas de governança e arquitetura',['templates/carteira-iniciativas.md','fundamentos/origens-adaptacoes.md']),
 'References/Notebook 2_ Gestão e Governança de TI para PMEs com IA.md':('Notebook: modelagem de governança',['nucleo/escopo-principios.md','guias/usar-ia.md']),
 'References/Notebook 3_ GP-PME Framework de Intra-inovação para Governança Adaptativa em PMEs.md':('Notebook: melhoria, fontes e assistência',['guias/entregar-melhoria.md','referencias/fontes.md']),
 'References/Relatório de Consolidação de Dados_ Projeto GP-PME e Frame-sim.md':('Consolidação: método e proposta de avaliação',['nucleo/escopo-principios.md','exemplos/cenarios-historicos.md','indicadores/assistencia.md']),
 'References/Visão Consolidada do Modelo GP-PME (Governança Prática para PMEs).md':('Visão consolidada do método',['nucleo/escopo-principios.md','adocao/primeiros-30-dias.md','templates/carteira-iniciativas.md','guias/usar-ia.md']),
}
NOTES={
 'Docs/PRD.md':'Crédito declarado no PRD de 02/06/2026: Antigravity AI, sob direção de Andre Victor. A declaração antiga de prontidão de mercado não é evidência de implantação. O produto consiste em documentação e software de apoio; segurança, operação e recuperação dependem de tecnologia e competência apropriadas, mesmo sem IA. Uma página ou duas são preferências de síntese, não critérios suficientes de qualidade.',
 'Docs/Roadmap.md':'As janelas antigas de 31–90, 91–180 e 181–210 dias eram planejamento. A fase de desacoplamento e publicação descrevia produção documental, distinta da adoção por uma empresa. Marcações de concluído não comprovavam marcos organizacionais. Urgência e segurança podem exigir ação anterior à sequência; a próxima etapa depende de evidências e capacidade.',
 'Docs/Tasklist.md':'Os checkboxes antigos não tinham evidência de execução em empresa e foram substituídos por modelos não preenchidos. Teste de restauração usa cópia e ambiente autorizados, sem apagar arquivo real para demonstrar o método. Convite aceito, assinatura de plano e movimentação de cartão não comprovam governança, continuidade ou efeito. Itens bloqueados permanecem no histórico e no WIP quando iniciados.',
 'Docs/Specialist_Agents.md':'Quatro funções conceituais: direção, entrega, segurança e auditoria. A implementação tem um orquestrador e oito especialistas; não são quatro agentes já implantados. Entradas e instruções completas estão abaixo. A revisão verifica dados, fontes e efeitos; não exige exposição de raciocínio interno. Sem orçamento, informar estimativa de horas com unidade e origem, sem fabricar DAN financeira. Ação real requer alçada, permissão e execução conferidas.',
 'References/Análise Consolidada_ Referencial Teórico e Trabalhos Correlatos (Novos Documentos).md':'A síntese anterior atribuía “Baseline Mechanisms” a Silva et al. A seção Bibliografia e acesso limitado corrige autoria pelo DOI 10.1109/CBI.2018.10044. Listas de princípios extraídas de normas fechadas não são reproduzidas como transcrição verificada. Referências conceituais não confirmam a viabilidade ou eficácia do GEAR. NIST Privacy Framework permanece menção histórica, sem mapeamento detalhado adotado.',
 'References/checklist_10_controles_nist.md':'A lista de dez itens era seleção autoral, não numeração oficial de controles CIS nem implementação integral de IG1. Hardware, software, contas, configuração, vulnerabilidades, logs, e-mail, malware, backup e orientação permanecem como verificações locais abaixo. Frequência, cobertura, correção e exceções exigem contexto; preencher checklist não comprova conformidade.',
 'References/Dados da Conversa do Claude.md':'Registro histórico da intenção de produzir um framework modular e possivelmente comercial. A descrição da conversa não é validação nem fonte normativa; o link foi preservado como origem declarada, sem nova consulta. As cinco partes antigas eram módulos editoriais, distintos dos três domínios. Originalidade e disponibilidade de marca não foram comprovadas.',
 'References/Dados das Conversas do Gemini.md':'Registro histórico do desenho revisão/modelagem/PoC/SWOT dupla. As menções a Peng 2023 e Brynjolfsson 2023 precisam das versões e populações próprias; consultar a bibliografia do manuscrito, sem misturar a versão NBER de 2023 com a publicação QJE de 2025. A SWOT pode organizar apreciações sobre o método e assistência; não mede causalidade ou democratização. A avaliação vigente é prospectiva no manuscrito multifile.',
 'References/Dados do Repositório GitHub_ Frame-sim.md':'A síntese anterior descrevia v5.0, engine Multi-LLM, ChromaDB, CriticAgent, warmup, agent racing, React/TypeScript/Vite e custos com ruído ±10%. Essas capacidades e versões não foram verificadas nesta reforma; ficam como descrição histórica, não contrato atual. Nenhuma execução externa foi feita. O dataset local é preservado sem alteração; simulação não demonstra comportamento humano nem eficácia organizacional.',
 'References/Notebook 1_ Adaptive IT Governance_ AI for SME Agility.md':'O registro citava projeto de pesquisa e modelo de apresentação TCC1, junto a microsserviços orientados a eventos, Moodle, containers e escalabilidade. São temas de investigação, sem recomendação automática de arquitetura ou vantagem demonstrada. O notebook não foi consultado novamente. Avaliar alternativa e custo de transição conforme a necessidade real.',
 'References/Notebook 2_ Gestão e Governança de TI para PMEs com IA.md':'O registro citava TCC1 GP-PME, Design Brutalista v10 e modelo de pesquisa ABNT 2025. Descrevia contingência, três frentes e modelagem qualitativa. Uso de IA na criação ou avaliação do texto não comprova a eficácia do método. Documentos de submissão são históricos; o manuscrito atual mantém seu protocolo prospectivo.',
 'References/Notebook 3_ GP-PME Framework de Intra-inovação para Governança Adaptativa em PMEs.md':'O registro declarava 35 fontes e reunia intra-inovação, TI enxuta, prompts e transformação digital. A contagem histórica não comprova fontes verificadas; consultar fichas da edição vigente. ISO 27001, literatura de transformação digital e outras obras locais não implicam conformidade ou incorporação integral. As três frentes e o piloto de melhoria foram preservados.',
 'References/Relatório de Consolidação de Dados_ Projeto GP-PME e Frame-sim.md':'A síntese reunia NotebookLM, Gemini, Claude e GitHub. A proposta de minimundo e SWOT dupla fica separada do resultado de pesquisa. A descrição de agentes CFO/CTO/CEO, RAG, Curva J e custo de não qualidade não confirma implementação nesta edição. Documentação de software, cálculo condicional e avaliação do método são evidências diferentes.',
 'References/Visão Consolidada do Modelo GP-PME (Governança Prática para PMEs).md':'Foram preservados três domínios, comunicação entre TI e direção, contexto/restrições/revisão, adoção gradual e piloto. O cargo “orquestrador de valor” não implica promoção a CIO nem dispensa alçada. Migração para microsserviços depende de necessidade e custo; assistência não é obrigatória. Frame-sim permanece proposta externa, sem resultado de campo.',
}

def build():
    for path,(title,chapters) in SPECS.items():
        target=ROOT/path;original=ROOT/'.context/originais/gear-2026-10-04'/path
        old=original.read_text(encoding='utf-8') if original.exists() else ''
        urls=list(dict.fromkeys(re.findall(r'https?://[^\s)]+',old))) if old else origin(path).get('urls',[])
        text=f'# {title}\n\nEdição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.\n\n## Origem e decisão editorial\n\n'+NOTES[path]+'\n\n'
        if urls:text+='Origem declarada no registro anterior, sem nova consulta:\n\n'+'\n'.join('- '+url for url in urls)+'\n\n'
        text+='\n\n'.join(heading_shift(excerpt(p,target)) for p in chapters)+'\n'
        target.write_text(text,encoding='utf-8')
    print('14 sínteses e documentos de manutenção consolidados.')

if __name__=='__main__':build()
