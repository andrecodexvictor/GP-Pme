# Guia de continuidade e evidências

Edição editorial GEAR 2026.10. Documento completo no caminho anterior para compatibilidade; regras vigentes em `framework/`. Direitos conforme LICENSE.md.

Origem: versão declarada 5.2, de 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor.

## Percurso de leitura

- [Continuidade: conhecer dependências e testar](#continuidade-conhecer-dependencias-e-testar)
- [O que direção e TI precisam conferir](#o-que-direcao-e-ti-precisam-conferir)

## Continuidade: conhecer dependências e testar

Identifique o serviço que precisa continuar, seus dados, contas, equipamentos e fornecedores. Comece pelas dependências críticas e registre o que falta mapear. O nome antigo “Inventário 80/20” expressava priorização; não prova que 20% dos ativos geram 80% do faturamento.

Contas individuais, acesso necessário e MFA reduzem exposições específicas, sem impedir todo ataque. Registre cobertura e exceções. MFA é autenticação multifator; um código de celular é apenas uma implementação possível, não a definição completa.

Combine frequência e retenção de backup com a perda de dados tolerável. Proteja a cópia e teste restauração em ambiente autorizado. Um arquivo recuperado não comprova recuperação do serviço inteiro. Os antigos parâmetros de backup diário, teste trimestral e 30 minutos precisam de justificativa local.

Prepare o PRI com contatos conferidos, autoridade para contenção, comunicação e passos de recuperação. No incidente, preserve evidências e confirme serviço e dados com seu dono. Formatação e desligamento não são instruções universais. Obrigações legais vão à competência responsável.

## O que direção e TI precisam conferir

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

## Próxima tarefa e referências

- [Segurança e continuidade](<../../framework/nucleo/seguranca-continuidade.md>)
- [Risco e continuidade](<../../framework/templates/risco-continuidade.md>)

Fontes F01–F12 e limites de consulta: [referências completas](<../../framework/referencias/fontes.md>). Os originais e o registro de revisão são preservados em `.context/`.
