const {spawnSync} = require('node:child_process');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname,'..');
const bundled = path.join(process.env.USERPROFILE || '', '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe');
const python = process.env.GEAR_PYTHON || (fs.existsSync(bundled) ? bundled : 'python');
const actions = {
  build: [['-m','tools.build_flowcharts'],['-m','tools.build_simulations'],['-m','tools.build_legacy_masters'],['-m','tools.build_intro_guides'],['-m','tools.build_technical_guides'],['-m','tools.build_legacy_templates'],['-m','tools.build_legacy_index'],['-m','tools.build_agent_contracts'],['-m','tools.build_existing_skills'],['-m','tools.build_reference_versions'],['-m','tools.build_project_documents'],['-m','tools.build_portal'],['-m','search.ingest'],['-m','search.build_index','--bm25-only'],['-m','search.export_web'],['-m','tools.build_book']],
  test: [['-m','unittest','discover','-s','tests','-v']],
  figures: [['-m','tools.build_figures']]
};
const selected=actions[process.argv[2]];
if(!selected) throw new Error('Use build, test ou figures.');
for(const args of selected){
  const result=spawnSync(python,args,{cwd:root,stdio:'inherit',env:{...process.env,PYTHONIOENCODING:'utf-8'}});
  if(result.error)throw result.error;
  if(result.status!==0){process.exitCode=result.status || 1;break;}
}
