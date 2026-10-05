"""Projeta os sete guias técnicos revistos em caminhos públicos anteriores.

Cada guia mantém explicação, procedimento e artefatos completos. As fontes
canônicas incorporam as contribuições exclusivas identificadas na leitura.
"""
import re
from tools.editorial import ROOT, blocks, slug
from tools.build_legacy_masters import excerpt, heading_shift, MATRIZ, SEGURANCA

SPECS = [
    ('Guia_Pilar_1_Governanca_Essencial.md', 'Governança e direção: guia técnico', '5.2', [
        'nucleo/governanca.md', 'guias/conduzir-revisao.md',
        'templates/responsabilidades.md', 'templates/decisoes-prioridades.md',
        'indicadores/operacionais.md'], '''## Preparar uma pauta com assistência opcional

TI pode fornecer demandas, decisões anteriores e dados autorizados para uma minuta de pauta. A pessoa responsável confere origem, lacunas, alternativas e alçadas antes da revisão. Uma meta de reduzir despesa em 5% só integra a pauta quando foi acordada com o negócio; não é meta do método. Sugestões de iniciativas precisam de custo, dependência, risco e modo de verificar benefício. Não há prazo garantido de dois minutos para produzir ou conferir o briefing.

Uma página é preferência de síntese, ajustável ao contexto. Detalhes e evidências permanecem consultáveis. RACI registra responsabilidade humana; uma ferramenta de IA não assume a aprovação nem substitui o executor responsável.
'''),
    ('Guia_Pilar_2_Execucao_Agil.md', 'Execução e serviços: guia técnico', '5.2', [
        'nucleo/execucao-servicos.md', 'guias/priorizar-demandas.md',
        'guias/tratar-incidentes.md', 'guias/entregar-melhoria.md',
        'templates/prd-aceite.md', 'guias/usar-ia.md'], MATRIZ + '''
## Rever a semana e as interrupções

O responsável por TI prepara o plano com demandas, dependências e capacidade. Três a cinco cartões na semana eram uma sugestão de seleção, não limite de WIP nem compromisso universal. Uma revisão diária pode conferir concluídos, próximo trabalho e bloqueios sem criar reunião quando há um executor. Ao encerrar o ciclo, comparar plano inicial, entregas, alterações e capacidade consumida por incidentes.

Pedidos comuns são ordenados pela consequência de adiar; não precisam esperar a semana seguinte por regra automática. Emergência registra alçada, trabalho suspenso e exceção de capacidade. Trabalho iniciado não volta a ser novo nem perde o histórico. Após recuperação, rever prioridade de retomada e comunicar aos afetados.

Uma orientação ou mudança pequena pode dispensar implantação em produção. Conclusão exige o critério adequado à demanda ou encerramento justificado. O indicador de entregas em prazo e orçamento não mede sozinho utilidade ou desempenho do suporte.
'''),
    ('Guia_Pilar_3_Seguranca_Critica.md', 'Segurança e continuidade: guia técnico', '5.2', [
        'nucleo/seguranca-continuidade.md', 'guias/testar-restauracao.md',
        'guias/tratar-incidentes.md', 'templates/risco-continuidade.md',
        'templates/incidente.md'], SEGURANCA + '''
## Conferir acesso e cópias

Contas individuais e permissões necessárias reduzem exposições específicas. Separar administração e uso cotidiano quando o ambiente permitir; conferir exceções e procedimentos antes de retirar um privilégio. Privilégio mínimo não impede toda instalação ou propagação de malware. MFA é autenticação multifator, não sinônimo de SMS ou de exatamente dois fatores.

Para contas críticas, registrar cobertura, método, exceção, responsável e data de revisão. O proprietário confirma necessidade do acesso. Para cópias, registrar fonte, frequência, retenção, proteção, dependência e teste. Nuvem e automação são opções tecnológicas; sua simples presença não comprova segurança ou recuperação. Soluções nativas também podem exigir custo, operação e suporte.

As quatro práticas locais não equivalem às 56 salvaguardas do CIS IG1 [F11](../../framework/referencias/fontes.md#f11). Cobertura do NIST deve incluir lacunas de governança e detecção, sem apresentar seleção curta como implementação integral.
'''),
    ('Guia_Pilar_4_Assistencia_IA_e_Agentes.md', 'Assistência opcional por IA: guia técnico', '5.2', [
        'guias/usar-ia.md', 'templates/prompts-assistencia.md',
        'templates/revisao-ia.md'], '''## Conferir por afirmação e por efeito

Revisar cada afirmação relevante contra seu dado ou fonte. Ter três nomes de sistemas na resposta não comprova ancoragem; citar uma norma não demonstra que ela prescreve a recomendação. Conferir a referência, a versão e o trecho quando houver alegação normativa. Se não estiver acessível, restringir a afirmação e registrar o limite.

Revisar cálculos, unidade, período, configuração real e efeito proposto. Não liberar uma saída por quantidade de páginas ou fluência. Uma ferramenta pode seguir o formato e ainda errar. A revisão registra pessoa, correção, rejeição ou aprovação, com autoridade compatível com a ação.

MCP fornece uma interface de ferramentas e contexto; não garante grounding ou ausência de erro. As quatro funções conceituais são preservadas nos contratos completos acima. A implementação ADK tem oito especialistas e um orquestrador; contratos em Markdown são instruções, não agentes já instalados ou execução autônoma. A disponibilidade e permissões do runtime precisam ser verificadas separadamente.
'''),
    ('Guia_Modelo_de_Maturidade.md', 'Maturidade com evidências: guia técnico', '1.0', [
        'adocao/maturidade.md', 'adocao/fichas-maturidade.md',
        'templates/maturidade.md'], '''## Planejar reaplicações

Aplicar no início, depois de mudanças relevantes e na janela de revisão acordada. O intervalo antigo de seis meses é uma possibilidade, não requisito normativo. Preservar edição, evidência por pergunta, observações e plano; comparar somente depois de conferir diferenças de instrumento e contexto.

Direção aprova recursos e risco; dono do processo verifica efeitos; TI organiza a aplicação. O objetivo é localizar lacunas e sustentar a prática, sem promoção presumida do profissional, comprovação de segurança pelo total ou certificação por assinatura.
'''),
    ('Guia_de_Implementacao_Fase_Zero.md', 'Adoção inicial: guia técnico', '5.2', [
        'adocao/primeiros-30-dias.md', 'adocao/preparacao-cronograma.md',
        'indicadores/negocio-comparacao.md', 'templates/maturidade.md'], ''),
    ('Guia_KPIs_e_Quick_Wins.md', 'Indicadores e primeiras melhorias: guia técnico', '6.0', [
        'indicadores/operacionais.md', 'indicadores/negocio-comparacao.md',
        'indicadores/financeiros.md', 'adocao/preparacao-cronograma.md'], '''## Conferir o cenário financeiro antigo

O guia supunha três horas diárias de atividade manual para dez pessoas e atribuía R$ 3.000 por mês ao esforço. Faltavam dias de trabalho, custo-hora e proporção recuperável para derivar esse valor. Os relatos ficam preservados como premissas incompletas; a conta financeira usa R$ 3.000/mês como benefício independente hipotético, sem inferir salário ou calendário.

Com R$ 9.000 de investimento inicial, recorrência zero, benefício estabilizado por doze meses e sem duplicação, a conta condicional resulta em benefício anual de R$ 36.000, razão bruta 4, ROI líquido de 300% e payback simples de três meses. A expressão antiga de 400% era benefício bruto sobre investimento. Se apenas metade do benefício ocorrer, ROI líquido anual de 100% e payback de seis meses; com benefício nulo, ROI de −100% e sem payback finito. O exemplo com R$ 500/mês de recorrência acima mostra outra hipótese, não um custo originalmente observado.

Nem automação nem nuvem demonstram economia realizada ou eliminação da dívida. Conferir esforço, licença, manutenção, adoção e benefício observado. DAN financeira, COT e ROI são instrumentos locais; artigos sobre dívida arquitetural não validam suas fórmulas por proximidade de tema.
'''),
]


def compose(name, title, version, chapters, extra):
    target = ROOT / 'GP-PME antigravity/Guides' / name
    parts = [heading_shift(excerpt(path, target)) for path in chapters]
    body = '\n\n'.join(parts) + '\n\n' + extra.strip() + '\n'
    headings = [(kind, value) for kind, value in blocks(body) if kind == 'h2']
    # Cabeçalho e percurso não duplicam os títulos dos capítulos projetados.
    text = f'# GEAR: {title}\n\n'
    text += ('Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. '
             f'Origem: GP-PME {version}, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. '
             'Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.\n\n')
    text += '## Percurso de leitura\n\n'
    text += '\n'.join(f'- [{label}](#{slug(label)})' for _, label in headings) + '\n\n'
    text += body
    text += ('\n## Fontes e continuidade\n\n'
             'Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). '
             'Regra vigente: [documentação modular](../../framework/README.md). '
             'Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). '
             'IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.\n')
    return target, text


def build():
    for spec in SPECS:
        target, text = compose(*spec)
        target.write_text(text, encoding='utf-8')
        print(target.name, len(text), 'caracteres')


if __name__ == '__main__':
    build()
