# Testar restauração

Este guia verifica um recorte definido da capacidade de recuperar dados ou um serviço. Use antes de depender de um backup, após alteração relevante da solução e na cadência acordada para o serviço. Responsável técnico prepara o teste; dono do processo valida a saída. Entrada: cópia disponível, ambiente apropriado, autorização, dependências e objetivos de recuperação. Saída: evidência do teste e plano de correção de lacunas.

## Definir o recorte

Especificar serviço ou conjunto de dados, versão, momento da cópia, dependências, condição de sucesso e limite do teste. Um arquivo restaurado não demonstra a restauração completa de ERP, identidade, rede e integrações.

Definir RTO e RPO com o negócio. A referência histórica de restauração em 30 minutos não é meta universal; a necessidade do processo e os recursos disponíveis orientam o requisito.

## Executar

1. Confirmar acesso à cópia e às chaves necessárias, seguindo as permissões e controles da organização.
2. Preparar ambiente isolado ou autorizado, sem sobrescrever a operação por conveniência do teste.
3. Restaurar o recorte, registrando início, fim, versão e erros.
4. Verificar integridade e funcionalidade com o dono do processo.
5. Comparar tempo e perda de dados com os objetivos acordados.
6. Registrar escopo aprovado, limitações, evidências e correções com responsável e prazo.

## Interpretar

“Backup executado” indica execução do mecanismo. “Arquivo restaurado” indica recuperação daquele recorte. “Serviço recuperado” exige verificação das dependências e da funcionalidade definida. Preservar essa diferença na ata e nos indicadores.

Se faltou credencial, a cópia não existia ou o tempo excedeu o objetivo, registrar a falha e rever o plano. Não substituir o resultado por sucesso estimado.

A orientação NIST para pequenas empresas inclui recuperação e ações ligadas à continuidade. A implementação do teste e sua frequência precisam considerar o contexto. [F01](../referencias/fontes.md#f01)

Modelo: [Risco e continuidade](../templates/risco-continuidade.md). Próxima leitura: [Indicadores operacionais](../indicadores/operacionais.md).
