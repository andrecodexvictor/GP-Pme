"""Índice compatível com o acervo anterior, sem promessas de resultados."""
import xml.etree.ElementTree as ET
from tools.editorial import ROOT

GROUPS = [
    ('Manuais e guias técnicos', [
        ('Manual consolidado', 'Arquitetura e regras', 'Conhecer o método', 'GP-PME_Documento_Mestre_Consolidado.md'),
        ('Governança e direção', 'Alçadas, ciclo e revisão', 'Decidir com o negócio', 'Guides/Guia_Pilar_1_Governanca_Essencial.md'),
        ('Execução e serviços', 'Fila, capacidade e aceite', 'Organizar a rotina', 'Guides/Guia_Pilar_2_Execucao_Agil.md'),
        ('Segurança e continuidade', 'Dependências, acesso e recuperação', 'Verificar exposição e resposta', 'Guides/Guia_Pilar_3_Seguranca_Critica.md'),
        ('Assistência opcional', 'Quatro funções e revisão', 'Preparar minutas com IA', 'Guides/Guia_Pilar_4_Assistencia_IA_e_Agentes.md'),
        ('Adoção inicial', 'Agenda e evidências', 'Distribuir primeiras ações', 'Guides/Guia_de_Implementacao_Fase_Zero.md'),
        ('Indicadores e primeiras melhorias', 'Métricas, comparação e cenários', 'Conferir premissas e resultados', 'Guides/Guia_KPIs_e_Quick_Wins.md'),
        ('Maturidade', 'Questionário e fichas', 'Localizar lacunas', 'Guides/Guia_Modelo_de_Maturidade.md'),
    ]),
    ('Leitura introdutória', [
        ('Visão inicial', 'Governança e gestão', 'Começar a leitura', 'guide-for-dummies/Guia_GP-PME_para_Leigos.md'),
        ('Decisões', 'Pauta e finalidades', 'Participar da revisão', 'guide-for-dummies/Guia_Leigo_Pilar_1.md'),
        ('Fila e melhoria', 'Quadro e pequeno piloto', 'Acompanhar trabalho', 'guide-for-dummies/Guia_Leigo_Pilar_2.md'),
        ('Continuidade', 'Controles e evidências', 'Conferir com TI', 'guide-for-dummies/Guia_Leigo_Pilar_3.md'),
    ]),
    ('Registros e prompts', [
        ('Biblioteca completa', 'Oito grupos de registros', 'Escolher um modelo', 'Templates_GP-PME.md'),
        ('Instrução de tarefa', 'FAI e prompt mestre', 'Delegar ou pedir minuta', 'Templates/Prompts/Template_Prompt_Mestre.md'),
        ('Prompt de requisitos', 'Contexto, escopo e critérios', 'Preparar PRD', 'Templates/Prompts/Template_Prompt_PRD.md'),
        ('Prompt de risco', 'Evidência, alternativas e alçada', 'Preparar análise', 'Templates/Prompts/Template_Prompt_Risco.md'),
        ('PRD completo', 'Requisitos e aceite', 'Delimitar melhoria', 'Templates/PRDs/Template_PRD_Completo.md'),
        ('Lista de tarefas', 'Passos e verificação', 'Atribuir execução', 'Templates/Tasklists/Template_Tasklist_Operacional.md'),
        ('Contratos por função', 'Direção, entrega, segurança e revisão', 'Configurar assistência', 'Templates/AI-Skills-and-Agents/Template_System_Prompt_Agentes.md'),
        ('Revisão humana', 'Critérios por tipo de saída', 'Conferir antes do uso', 'Templates/AI-Skills-and-Agents/Template_Checklist_Auditoria_HITL.md'),
        ('Registro de maturidade', 'Evidência e plano', 'Avaliar a rotina', 'Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md'),
    ]),
    ('Interface e integrações', [
        ('Portal', 'Documentação, blog e biblioteca', 'Navegar pelo método', '../GP-Pme Article/index.html'),
        ('Busca lexical', 'Palavras e contexto do corpus revisado', 'Encontrar uma seção', '../GP-Pme Article/busca.html'),
        ('Ferramentas locais', 'Cálculos e quadro de exercício', 'Conferir fórmulas e capacidade', '../GP-Pme Article/ferramentas.html'),
        ('Busca em Python', 'BM25 e opção de embeddings', 'Integrar recuperação', '../search/README.md'),
        ('Agentes ADK', 'Orquestrador e oito especialistas', 'Examinar implementação e adapters', '../agents/gp-pme-adk/README.md'),
        ('Contratos Markdown', 'Nove instruções de assistência', 'Consultar instruções existentes', 'Templates/AI-Skills-and-Agents/Agentes_Prontos/'),
        ('Skills existentes', 'Oito comandos de compatibilidade', 'Consultar a integração antiga', '../.claude/skills/'),
        ('MCP e API', 'Ferramentas e núcleo determinístico', 'Integrar funções', '../server/README.md'),
        ('Grafo histórico', 'Artefato gerado anteriormente', 'Consultar relações antigas', '../graphify-out/graph.html'),
    ]),
    ('Cenários e proposta comercial', [
        ('Simulações', 'Quatro perfis e hipóteses', 'Comparar premissas', '../Simulacao/README.md'),
        ('Proposta de valor', 'Escopo e limites', 'Discutir adequação', '../Comercial/Proposta_de_Valor.md'),
        ('Apresentação comercial', 'Síntese do produto', 'Preparar conversa', '../Comercial/One_Pager_Vendas.md'),
        ('Precificação', 'Composição e hipóteses de preço', 'Preparar proposta', '../Comercial/Modelo_de_Precificacao.md'),
        ('Adoção com cliente', 'Responsáveis e acompanhamento', 'Planejar entrada', '../Comercial/Onboarding_Cliente.md'),
    ]),
]


def build():
    text = '''# GEAR: índice do acervo

Gestão, Execução, Agilidade e Risco. Framework de governança e gestão de TI para pequenas e médias empresas.

Edição editorial 2026.10. Este índice conserva os caminhos do acervo GP-PME e aponta para documentos completos. A fonte vigente é a [documentação modular](../framework/README.md). Direitos conforme [LICENSE.md](../LICENSE.md). Responsável pelo método: Andre Victor; créditos declarados das versões anteriores permanecem nos documentos e no histórico preservado.

## Escolher uma primeira tarefa

Direção e TI identificam um problema observável, a pessoa que pode decidir e a evidência disponível. A primeira leitura pode preparar um acordo ou revelar uma lacuna. Tempo de leitura não comprova implantação; o percurso de 30 dias é planejamento ajustável.

| Necessidade | Começar por | Saída esperada |
| --- | --- | --- |
| Conhecer responsabilidades | [Guia introdutório](guide-for-dummies/Guia_GP-PME_para_Leigos.md) | Entender quem decide, executa e verifica |
| Iniciar a adoção | [Adoção inicial](Guides/Guia_de_Implementacao_Fase_Zero.md) | Ações, capacidade e evidências a obter |
| Localizar lacunas | [Maturidade](Guides/Guia_Modelo_de_Maturidade.md) | Respostas com evidência e plano de melhoria |
| Usar um registro | [Biblioteca](Templates_GP-PME.md) | Modelo pertinente à decisão ou tarefa |

## Como o método se organiza

Três domínios essenciais: governança e direção; execução e serviços; segurança e continuidade. Adoção, indicadores e maturidade atravessam os domínios. IA é assistência opcional em todos os níveis. As quatro letras de GEAR não criam quatro pilares adicionais.

```mermaid
flowchart TB
    G[Governança e direção] --> E[Execução e serviços]
    E --> R[Verificar e rever decisões]
    R --> G
    S[Segurança e continuidade] --- G
    S --- E
    A[Adoção, indicadores e maturidade] --- R
    I[Assistência opcional por IA] -.-> G
    I -.-> E
    I -.-> S
```

Registros podem ser manuais; proteção de acesso e recuperação exigem tecnologia adequada ao serviço. WIP começa em até três itens iniciados por executor, incluindo teste e bloqueio comprometido. Pilotos e metas dependem de capacidade, risco e acordo; o método não garante economia de 80%, retorno em 24 horas ou implantação em trinta minutos.

## Percursos por responsabilidade

- Direção ou dono do negócio: guia introdutório, governança e decisões; conferir recurso, risco aceito e acompanhamento.
- Responsável por TI: adoção, execução, continuidade e biblioteca; manter fila, critérios e evidências.
- Consultor: guias técnicos, maturidade, cenários e escopo comercial; confirmar capacidade e contexto do cliente antes de propor integração.
- Desenvolvedor ou integrador: contratos de assistência, READMEs de busca, ADK e serviços; conferir permissões, runtime e comportamento real antes do uso.

## Catálogo

'''
    for title, items in GROUPS:
        text += f'### {title}\n\n| Artefato | Conteúdo | Momento de uso | Acesso |\n| --- | --- | --- | --- |\n'
        for label, content, when, path in items:
            text += f'| {label} | {content} | {when} | [abrir](<{path}>) |\n'
        text += '\n'
    text += '''## Limites das integrações

Contratos e skills descrevem assistência; não constituem agentes já ativos. A implementação ADK tem um orquestrador e oito especialistas, distintos das quatro funções conceituais. Adapters exigem plataforma, acesso, configuração e teste; `dry-run` demonstra uma proposta de ação, sem comprovar gravação externa. O runtime ADK e integrações reais precisam de verificação específica.

A busca pública é lexical e funciona com o índice exportado. Embeddings são opção técnica separada, sem índice semântico novo validado nesta edição. O grafo listado é histórico; não representa automaticamente o corpus GEAR atual. O Graphify global de outro projeto não é usado para este acervo.

Skills existentes permanecem em seus caminhos de compatibilidade durante a revisão. Novas instalações pertencem ao escopo global do usuário. MCP é administrado pelo hub HTTP global; ferramentas e contexto não garantem respostas corretas ou aprovação humana.

## Fontes, exemplos e edição

Consultar [fontes e limites](../framework/referencias/fontes.md) e [origens e adaptações](../framework/fundamentos/origens-adaptacoes.md). DAN financeira, faixas, questionário e metas são instrumentos locais. Simulações são cenários condicionais; o artigo permanece prospectivo enquanto não houver dados documentados.

O acervo evoluiu de GP-PME e NEXUS-PME. O índice de julho de 2026 organizava percursos comerciais, catálogo, quatro camadas técnicas e metadados. A edição atual conserva essas funções de consulta e corrige nomes, contagens, arquitetura e promessas sem suporte. Originais e mapa de revisão são preservados em `.context/`.

## Metadados de consulta

O bloco conserva a interface documental anterior para indexadores que a utilizem. Ele descreve caminhos e temas; não mede desempenho de RAG nem garante recuperação.

'''
    tree = ET.Element('rag-metadata')
    ET.SubElement(tree, 'framework-name').text = 'GEAR — Gestão, Execução, Agilidade e Risco'
    arch = ET.SubElement(tree, 'decoupled-ai-architecture')
    ET.SubElement(arch, 'description').text = 'Registros manuais ou assistência opcional; tecnologia apropriada para acesso e recuperação.'
    ET.SubElement(arch, 'mandatory-pillars').text = 'Governança e direção; execução e serviços; segurança e continuidade. Tag mantida por compatibilidade: são domínios.'
    ET.SubElement(arch, 'optional-accelerator').text = 'Assistência por IA; opcional inclusive na maturidade máxima.'
    mapping = ET.SubElement(tree, 'document-mapping')
    for _, items in GROUPS:
        for label, content, when, path in items:
            doc = ET.SubElement(mapping, 'document', {'file': path})
            ET.SubElement(doc, 'topic-coverage').text = content + '. ' + when + '.'
            ET.SubElement(doc, 'keywords').text = label
    ET.indent(tree, space='    ')
    text += '```xml\n' + ET.tostring(tree, encoding='unicode') + '\n```\n'
    (ROOT / 'GP-PME antigravity/INDEX.md').write_text(text, encoding='utf-8')
    print('INDEX.md:', sum(len(rows) for _, rows in GROUPS), 'entradas')


if __name__ == '__main__':
    build()
