"""Manuais completos nos 36 caminhos históricos, após comparação editorial.

Preserva perfis e créditos; regras compartilhadas provêm do corpus canônico.
As versões anteriores são conservadas em .context/originais, nunca inferidas
como evidência empírica. Não altera fontes de terceiros.
"""
from pathlib import Path
import re
from tools.publication_origin import origin
from tools.editorial import ROOT,slug
from tools.build_legacy_masters import excerpt,heading_shift,LEIGO,MATRIZ,COT,SEGURANCA

BASE=ROOT/'References/GP-PME Versions'
CORE=['nucleo/escopo-principios.md','nucleo/governanca.md','nucleo/execucao-servicos.md','nucleo/seguranca-continuidade.md']
ADOPTION=['adocao/primeiros-30-dias.md','adocao/preparacao-cronograma.md','adocao/maturidade.md','adocao/fichas-maturidade.md']
GOV=['nucleo/governanca.md','guias/conduzir-revisao.md','templates/responsabilidades.md','templates/decisoes-prioridades.md','templates/matriz-prioridades.md','templates/painel-indicadores.md','indicadores/negocio-comparacao.md']
EXEC=['nucleo/execucao-servicos.md','guias/priorizar-demandas.md','guias/entregar-melhoria.md','templates/tasklist.md','templates/prd-aceite.md']
SEC=['nucleo/seguranca-continuidade.md','guias/tratar-incidentes.md','guias/testar-restauracao.md','templates/inventario-dependencias.md','templates/incidente.md','templates/risco-continuidade.md','templates/dados-privacidade.md']
AI=['guias/usar-ia.md','templates/instrucao-assistencia.md','templates/prompts-assistencia.md','templates/prompts-etapas.md','templates/prompts-revisao-operacional.md','templates/revisao-ia.md','indicadores/assistencia.md']
FIN=['indicadores/financeiros.md','indicadores/operacionais.md','indicadores/negocio-comparacao.md','fundamentos/evolucao-indicadores.md']
SPECS={
 'gp-pme-apendice-a-mapeamento-frameworks.md':('Fundamentos e limites das adaptações',['fundamentos/origens-adaptacoes.md','referencias/fontes.md']),
 'gp-pme-apendice-b-biblioteca-prompts.md':('Biblioteca de instruções',AI),
 'gp-pme-apendice-c-estudos-de-caso.md':('Cenários fictícios para estudo',['exemplos/cenarios-historicos.md','indicadores/negocio-comparacao.md']),
 'gp-pme-apendice-d-ferramentas-tecnologias.md':('Escolher ferramentas',['guias/escolher-ferramentas.md','templates/carteira-iniciativas.md','templates/dados-privacidade.md']),
 'gp-pme-documento-mestre-tecnico-estrutura.md':('Estrutura e percursos de leitura',['README.md','nucleo/escopo-principios.md','fundamentos/origens-adaptacoes.md']),
 'gp-pme-documento-mestre-tecnico-cap1.md':('Arquitetura e princípios',['nucleo/escopo-principios.md','fundamentos/origens-adaptacoes.md']),
 'gp-pme-documento-mestre-tecnico-cap2.md':('Governança e direção',GOV),
 'gp-pme-documento-mestre-tecnico-cap3.md':('Execução e serviços',EXEC),
 'gp-pme-documento-mestre-tecnico-cap4.md':('Segurança e continuidade',SEC),
 'gp-pme-documento-mestre-tecnico-cap5.md':('Indicadores e decisão financeira',FIN),
 'gp-pme-documento-mestre-tecnico-cap6.md':('Assistência e revisão',AI),
 'gp-pme-modulo-1-organizacao-caos.md':('Registrar e organizar demandas',EXEC[:2]+['templates/tasklist.md','indicadores/negocio-comparacao.md']),
 'gp-pme-modulo-2-governanca-minima.md':('Decidir prioridades',GOV),
 'gp-pme-modulo-3-seguranca-critica.md':('Proteger e recuperar serviços',SEC),
 'gp-pme-modulo-4-micro-inovacao.md':('Entregar uma melhoria',EXEC[2:]+AI),
 'gp-pme-modulo-5-escalabilidade.md':('Rever carteira e dependências',['templates/carteira-iniciativas.md','templates/dados-privacidade.md','guias/escolher-ferramentas.md','guias/usar-ia.md','adocao/maturidade.md']),
 'matriz_4_quadrantes.md':('Priorizar por impacto e urgência',['templates/matriz-prioridades.md','templates/decisoes-prioridades.md']),
 'modulo2_template_prd_simplificado.md':('Definir e aceitar uma entrega',['templates/prd-aceite.md']),
 'prd_simplificado.md':('PRD e aceite',['templates/prd-aceite.md']),
 'pri_1_pagina.md':('Plano de resposta a incidentes',['templates/incidente.md','guias/tratar-incidentes.md']),
 'prompt_analise_riscos_seguranca.md':('Preparar análise de risco',['templates/prompts-assistencia.md','templates/risco-continuidade.md']),
 'prompt_prd_simplificado.md':('Preparar e revisar requisitos',['templates/prompts-assistencia.md','templates/prompts-revisao-operacional.md']),
 'prompt_user_stories.md':('Preparar histórias e critérios',['templates/prompts-etapas.md','templates/prompts-revisao-operacional.md']),
 'gp-pme-academico-modular.md':('Manual modular',CORE+ADOPTION+EXEC[1:]+SEC[1:]+AI+FIN+['templates/carteira-iniciativas.md','fundamentos/origens-adaptacoes.md','glossario.md','referencias/fontes.md']),
 'gp-pme-documento-academico-final-completo.md':('Manual de aplicação e fundamentos',CORE+ADOPTION+EXEC[1:]+SEC[1:]+AI+FIN+['templates/carteira-iniciativas.md','guias/escolher-ferramentas.md','exemplos/cenarios-historicos.md','fundamentos/origens-adaptacoes.md','glossario.md','referencias/fontes.md']),
 'gp-pme-documento-mestre-marketavel.md':('Apresentação para direção',[]),
 'GP-PME_ Framework de Governança de TI para PMEs - Arquitetura Técnica e Métricas de Desempenho.md':('Manual técnico',CORE+GOV[1:]+EXEC[1:]+SEC[1:]+AI+FIN+ADOPTION+['templates/carteira-iniciativas.md','guias/escolher-ferramentas.md','fundamentos/origens-adaptacoes.md','glossario.md','referencias/fontes.md']),
 'GP-PME_ Governança Prática para Pequenas e Médias Empresas (Documento Mestre - Versão Concisa).md':('Visão essencial',CORE+['adocao/primeiros-30-dias.md','guias/usar-ia.md']),
 'GP-PME_ Governança Prática para Pequenas e Médias Empresas.md':('Manual de implementação',CORE+ADOPTION+GOV[1:]+EXEC[1:]+SEC[1:]+AI+FIN+['templates/carteira-iniciativas.md','fundamentos/origens-adaptacoes.md']),
 'GP-PME_ Guia de Implementação Fase Zero - Seus Primeiros 30 Dias.md':('Primeiros 30 dias',ADOPTION+['indicadores/negocio-comparacao.md']),
 'GP-PME_ Guia de Início Rápido para Governança de TI em PMEs.md':('Início e diagnóstico',CORE[:1]+ADOPTION+['templates/tasklist.md','templates/prd-aceite.md','templates/incidente.md','templates/matriz-prioridades.md','templates/prompts-assistencia.md']),
 'GP-PME_ Kit de Quick Start - Comece em 2 Horas.md':('Kit de preparação',['adocao/preparacao-cronograma.md','templates/prd-aceite.md','templates/incidente.md','templates/matriz-prioridades.md','templates/risco-continuidade.md','templates/prompts-assistencia.md','templates/prompts-etapas.md']),
 'GP-PME_ Seu Guia Prático para o Sucesso da TI na Pequena e Média Empresa.md':('Guia para direção',[]),
 'Guia de Suporte do Pilar 1_ Governança Essencial (Direção Estratégica).md':('Guia de governança',GOV),
 'Guia de Suporte do Pilar 2_ Execução Ágil (Entrega de Valor).md':('Guia de execução',EXEC+['guias/fluxos-de-trabalho.md']),
 'Guia de Suporte do Pilar 3_ Segurança Crítica (Proteção e Resiliência).md':('Guia de continuidade',SEC),
}
RISKS='''## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.
'''

def build():
    assert len(SPECS)==36
    for name,(title,chapters) in SPECS.items():
        target=BASE/name
        original=ROOT/'.context/originais/gear-2026-10-04/References/GP-PME Versions'/name
        old=original.read_text(encoding='utf-8') if original.exists() else ''
        metadata=[line.strip() for line in old.splitlines() if re.match(r'^\*\*(Autor|Versão|Data)\*\*',line)]
        credit=' '.join(metadata) or origin('References/GP-PME Versions/'+name).get('credito') or 'Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.'
        text=f'# GEAR: {title}\n\nFramework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.\n\nOrigem documental: {credit}\n\nDireitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.\n\n'
        if 'academico' in name:text+='O nome histórico “acadêmico” identifica um manual de aplicação, sem dados empíricos de avaliação. O [manuscrito científico](../../GP-Pme%20Article/overleaf/README.md) tem protocolo próprio e continua prospectivo.\n\n'
        chapters=list(dict.fromkeys(chapters))
        if chapters:
            text+='## Percurso de consulta\n\n'
            for chapter in chapters:
                label=(ROOT/'framework'/chapter).read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
                text+=f'- [{label}](#{slug(label)})\n'
            text+='\n'+'\n\n'.join(heading_shift(excerpt(p,target)) for p in chapters)
        else:text+=LEIGO
        if any(k in name for k in ('modulo','academico','Governança Prática','marketavel','cap')):text+='\n\n'+RISKS
        if 'cap3' in name:text+='\n\n'+MATRIZ
        if 'cap4' in name:text+='\n\n'+SEGURANCA
        text+='\n\nConsulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).\n'
        target.write_text(text,encoding='utf-8')
    print('36 documentos históricos consolidados, com perfis e créditos de origem.')

if __name__=='__main__':build()
