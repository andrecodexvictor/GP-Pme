# GEAR

**Gestão, Execução, Agilidade e Risco.** Framework de governança e gestão de TI para pequenas e médias empresas, de Andre Victor.

GEAR organiza prioridades, trabalho e riscos quando poucas pessoas acumulam funções. Há três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade. Adoção, indicadores e maturidade são transversais. Assistência por IA é opcional, inclusive no nível máximo de maturidade.

## Começar a leitura

| Necessidade | Percurso |
| --- | --- |
| Conhecer o método | [Escopo e princípios](framework/nucleo/escopo-principios.md) |
| Iniciar a rotina | [Primeiros 30 dias](framework/adocao/primeiros-30-dias.md) |
| Resolver uma tarefa | [Guias](framework/guias/README.md) |
| Consultar um registro | [Templates](framework/templates/README.md) |
| Entender uma conta | [Indicadores financeiros](framework/indicadores/financeiros.md) |
| Ler no navegador | [Portal](GP-Pme%20Article/index.html), [biblioteca](GP-Pme%20Article/biblioteca.html) e [notas de aplicação](GP-Pme%20Article/blog/index.html) |

## Fluxo de trabalho

Registrar necessidade e responsável; decidir prioridade com o negócio; selecionar trabalho compatível com capacidade; executar; verificar resultado acordado; revisar risco e próxima ação. O limite inicial é três itens iniciados por executor, contando andamento, teste e bloqueio. Emergências são atendidas e registradas, com autorização para exceções e histórico do trabalho interrompido.

O canal oficial reúne os registros; não impede ajuda a quem recebeu urgência por telefone ou mensagem. Prazo de piloto, duração de reunião e metas são parâmetros locais, ajustados com motivo. O método não garante retorno em 24 horas, redução percentual de esforço ou recuperação de qualquer serviço em prazo fixo.

## Fontes e evidência

A [edição canônica](framework/README.md) distingue referências externas, adaptações locais e hipóteses. O [registro de fontes](framework/referencias/fontes.md) informa versões, consulta e limites. Cenários são ilustrativos; não representam resultado de campo. O [manuscrito científico](GP-Pme%20Article/overleaf/README.md) descreve a pesquisa assistida por IA e a auditoria de conteúdo durante a produção. A prova de conceito com 25 empresas sintéticas e 75 execuções pareadas no [FrameSim](https://github.com/andrecodexvictor/Frame-sim) permanece futura.

A edição GEAR 2026.10 consolida núcleo, interface, regras determinísticas e versões autorais. O [registro de publicação](framework/publicacao/README.md) documenta preservação, verificações e limites. GP-PME e NEXUS-PME são nomes históricos. Identificadores de software e caminhos antigos podem permanecer por compatibilidade, sem definir pilares adicionais ou versões concorrentes.

## Estrutura e capacidades

| Diretório | Conteúdo e manutenção |
| --- | --- |
| `framework/` | Fonte editorial vigente: editar regras, guias, indicadores e modelos aqui |
| `GP-Pme Article/` | Portal estático derivado e manuscrito LaTeX próprio |
| `book/` e `tools/` | Fontes derivadas e geradores; PDFs em `GP-Pme Article/output/pdf/`; verificação local em `.context/publicacoes/` |
| `GP-PME/` e `GP-PME antigravity/` | Manuais completos derivados do núcleo, com caminhos preservados |
| `References/GP-PME Versions/` | Versões consolidadas por perfil, com créditos de origem |
| `References/` | Fontes externas e sínteses com proveniência; não reescrever textos de terceiros |
| `Docs/` | [Diretrizes e decisões](Docs/README.md) |
| `agents/` | [Orquestrador, oito especialistas e cinco adaptadores](agents/README.md) |
| `server/` | Regras comuns e fachadas API/MCP, com nomes GP-PME compatíveis |
| `search/` | Ingestão canônica, BM25 e exportação lexical |
| `Simulacao/` e `Comercial/` | Cenários condicionais e materiais comerciais revisados |
| `.claude/skills/` | Oito fluxos locais históricos; novas skills seguem o escopo global do usuário |
| `graphify-out/` | Grafo histórico local; não representa automaticamente o núcleo atualizado |

Agentes e adaptadores mantêm revisão humana para efeitos organizacionais. Modo simulado não comprova operação real nas plataformas. Novos MCPs devem seguir o hub global descrito em AGENTS.md; a reforma não instala um servidor por terminal nem usa o grafo de outro projeto.

## Gerar e verificar

Instalar dependências Node com `npm install`. O launcher usa Python configurado em `GEAR_PYTHON`; quando disponível, encontra o runtime documental do Codex no usuário. Em outro ambiente, usar Python 3.10 ou superior e as bibliotecas documentais do fluxo, incluindo `reportlab` e `pypdf` para o teste de publicação. Fontes tipográficas licenciadas acompanham o portal.

```text
npm run build
npm run test
npm run check:web
npm run build:figures
```

`build` gera páginas, corpus, BM25, índice web, mestre e livro. `test` usa unittest para testes de comportamento. `check:web` usa Puppeteer/Edge em perfil isolado; configurar `GEAR_BROWSER` para outro executável compatível. O artigo tem [compilação própria](GP-Pme%20Article/overleaf/README.md), com fontes múltiplas.

A busca web é lexical e funciona offline com JavaScript e índice local. Conteúdo e navegação documental funcionam sem JavaScript. Busca semântica exige reconstrução dos embeddings e correspondência de hash com o corpus; vetores históricos não são misturados com dados novos.

## Publicações

- [Livro GEAR](GP-Pme%20Article/output/pdf/GEAR_livro_2026-10.pdf)
- [Artigo prospectivo](GP-Pme%20Article/output/pdf/GEAR_artigo_2026-10.pdf)
- [Goal executável e decisões](Docs/GOAL-GEAR.md)

## Direitos

© 2026 Andre Victor. Todos os direitos reservados. Uso e distribuição seguem [LICENSE.md](LICENSE.md), sem alteração nesta reforma. Fontes tipográficas conservam as licenças de seus titulares, incluídas nos ativos.
