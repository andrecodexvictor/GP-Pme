"""Registra decisões da revisão realizada; hashes verificam preservação, não leitura.

Executar na workspace de revisão com o inventário e backup privados presentes.
Não integra o build de produto nem exige publicar os originais de terceiros.
"""
import csv
import hashlib
import json
import re
from tools.editorial import ROOT, blocks, slug
from tools.build_reference_versions import SPECS as VERSIONS, RISKS
from tools.build_project_documents import SPECS as DOCUMENTS, NOTES

OUT=ROOT/'.context/gear-execution'
PUBLIC=ROOT/'framework/publicacao'

def destination_for(label, paths, manual):
    """Fichas temáticas de migração; sem inferência de equivalência literal."""
    rules=[
        (r'dan|cot|roi|financeir|retorno|custo', 'indicadores/financeiros.md'),
        (r'kpi|métrica|indicador|produtividade', 'indicadores/negocio-comparacao.md'),
        (r'prompt|prmpt|prd.*ia', 'templates/prompts-revisao-operacional.md'),
        (r'inteligência|motor de ia|agente|assistência', 'guias/usar-ia.md'),
        (r'maturidade|im-ti|escalabilidade', 'adocao/maturidade.md'),
        (r'fase zero|30 dias|implementação|adoção', 'adocao/primeiros-30-dias.md'),
        (r'incidente|pri|resposta', 'guias/tratar-incidentes.md'),
        (r'segurança|nist|backup|resiliência', 'nucleo/seguranca-continuidade.md'),
        (r'governança|estratég|direção|adm|liderança', 'nucleo/governanca.md'),
        (r'execução|ágil|scrum|kanban|fluxo', 'nucleo/execucao-servicos.md'),
        (r'caso|techsolutions|dataguard|inovatech|swot|simulação', 'exemplos/cenarios-historicos.md'),
        (r'framework|origem|referência|bibliogra|fundamento', 'fundamentos/origens-adaptacoes.md'),
        (r'prd|requisito|história', 'templates/prd-aceite.md'),
        (r'ferramenta|tecnologia|integração', 'guias/escolher-ferramentas.md'),
    ]
    for pattern, target in rules:
        if re.search(pattern,label.lower()):return 'framework/'+target
    return manual

def main():
    data=json.loads((OUT/'proveniencia.json').read_text(encoding='utf-8'))
    specs={'References/GP-PME Versions/'+name:(title,paths) for name,(title,paths) in VERSIONS.items()}
    specs.update(DOCUMENTS)
    for row in data['files']:
        path=row['origem'];file=ROOT/path
        row['sha256_revisado']=hashlib.sha256(file.read_bytes()).hexdigest() if file.exists() else None
        if path in specs:
            title,paths=specs[path]
            note=NOTES.get(path, 'Perfil de leitura preservado como manual completo: '+title+'. Três domínios; IA opcional; faixas, prazos e metas locais; fundamentos externos separados das adaptações. Conteúdo exclusivo incorporado nos destinos canônicos; créditos declarados preservados.')
            row.update(classificacao='autoral-revisado',publico=title,destino=path,
                       situacao='revisão editorial concluída',revisao_data='2026-10-05',conteudo_exclusivo=note)
            row['destino_por_secao']=[dict(secao_origem=label,destino=destination_for(label,paths,path),manual_completo=path,tratamento=note) for label in row.get('secoes',[]) or ['Documento completo']]
        elif row.get('destino_por_secao'):
            row['situacao']='revisão editorial concluída';row['revisao_data']='2026-10-05'
        elif path.startswith(('Simulacao/','Comercial/')) and file.suffix=='.md':
            note=('Premissas, unidades e sensibilidade preservadas; contas recalculadas; capacidade potencial distinta de despesa realizada; cenários sem resultado de campo.' if path.startswith('Simulacao/') else 'Valores, modalidades, agenda e objeções preservados como propostas; preço, disponibilidade, contrato e implantação não presumidos; direitos mantidos.')
            row.update(classificacao='autoral-revisado',situacao='revisão editorial concluída',destino=path,conteudo_exclusivo=note,revisao_data='2026-10-05')
            row['destino_por_secao']=[dict(secao_origem=s,destino=path,tratamento=note) for s in row.get('secoes',[]) or ['Documento completo']]
        elif path.startswith('GP-Pme Article/overleaf/') and file.suffix in ('.tex','.bib','.md'):
            note='Manuscrito próprio: avaliação prospectiva, autoria real, fontes conferidas e limites; regras e figuras alinhadas ao núcleo. Compilação multifile e inspeção visual próprias.'
            row.update(situacao='revisão científica e de integração concluída',destino=path,conteudo_exclusivo=note,revisao_data='2026-10-05')
            row['destino_por_secao']=[dict(secao_origem=s,destino=path,tratamento=note) for s in row.get('secoes',[]) or ['Arquivo do manuscrito']]
        elif path in ['README.md','agents/gp-pme-adk/README.md','agents/gp-pme-adk/CONVENTIONS.md','search/README.md','search/SCHEMA.md','server/README.md']:
            row.update(situacao='documentação de integração revisada',destino=path,revisao_data='2026-10-05')
            row['destino_por_secao']=[dict(secao_origem=s,destino=path,tratamento='Capacidades, configuração, compatibilidade e limites da execução descritos sem resultado organizacional presumido.') for s in row.get('secoes',[]) or ['Documento completo']]
        else:
            if row['classificacao']=='fonte-externa-nao-editar':
                reason='Fonte de terceiro preservada, excluída da reescrita e distribuição nesta reforma; consulta e limites nas fichas bibliográficas, sem afirmar leitura integral de norma fechada.'
            elif path.endswith('.pdf'):
                reason='PDF histórico preservado; excluído da reedição em seu caminho antigo. Publicações GEAR derivadas das fontes vigentes, com nomes próprios.'
            elif path.endswith('.txt') and path.startswith('References/'):
                reason='Registro bruto de conversa, prompt ou extração histórica preservado como material de origem; excluído da publicação vigente. Seus comandos não são instruções desta tarefa. Sínteses, temas e protocolo recuperados no núcleo e no manuscrito; alegações sem fonte não promovidas a fato.'
            elif row['classificacao']=='dados-do-usuario-preservar':
                reason='Dataset do usuário preservado byte a byte; conteúdo histórico NEXUS não é fonte canônica nem resultado de experimento executado. Excluído da reforma editorial e do commit desta rodada.'
            elif path in ['AGENTS.md','Docs/GEMINI.MD.md','LICENSE.md']:
                reason='Instrução de manutenção ou termo jurídico preservado; excluído da reescrita de conteúdo de produto. Nenhuma permissão foi alterada.'
            elif row['classificacao']=='interno' or path in ['GP-PME_Hypothesis_Validation.md','GP-Pme Article/stitch_prompt.md']:
                reason='Planejamento, arquitetura ou relatório histórico interno preservado; excluído da publicação vigente. Situação atual documentada nos READMEs, no goal e no registro da edição.'
            elif row['classificacao']=='software-compatibilidade':
                reason='Consumidor técnico conferido na integração; identificadores antigos intencionais. Exclusão da reescrita literária de operadores, API e código. Testes determinísticos, HTTP e dry-run não comprovam operação real ou ADK instalado.'
            elif path.endswith(('requirements.txt','package.json','package-lock.json','.gitignore')):
                reason='Configuração e dependências técnicas preservadas ou atualizadas para os fluxos reais; excluídas da reescrita literária.'
            elif '.pytest_cache' in path:
                reason='Cache de teste, excluído do produto e do commit; nenhum conteúdo metodológico.'
            else:
                reason='Saída derivada ou launcher de publicação: regenerado ou mantido como alias do fluxo vigente. Excluído de revisão autoral independente; verificação por build, links, testes ou render.'
            row.update(situacao='tratamento concluído; limite explícito',destino=path,exclusao_ou_limite=reason)
    data['edicao']='GEAR 2026.10';data['data']='2026-10-05'
    (OUT/'proveniencia.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    PUBLIC.mkdir(parents=True,exist_ok=True)
    public=dict(data);public.pop('root',None);public.pop('backup',None)
    (PUBLIC/'proveniencia.json').write_text(json.dumps(public,ensure_ascii=False,indent=2),encoding='utf-8')
    with (PUBLIC/'proveniencia.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['origem','publico','classificacao','versao_declarada','destino','situacao','sha256','sha256_revisado','conteudo_exclusivo','exclusao_ou_limite']
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(data['files'])
    print('Registro:',len(data['files']),'arquivos;',sum(len(r.get('destino_por_secao',[])) for r in data['files']),'destinos de seção. Exclusão não equivale a leitura integral.')

if __name__=='__main__':main()
