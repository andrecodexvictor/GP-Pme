// Entrada antiga mantida para compatibilidade de comandos locais.
const {spawnSync}=require('node:child_process');
const fs=require('node:fs');
const path=require('node:path');
const bundled=path.join(process.env.USERPROFILE || '', '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe');
const python=process.env.GEAR_PYTHON || (fs.existsSync(bundled) ? bundled : 'python');
const result=spawnSync(python,['-m','tools.build_book',...process.argv.slice(2)],{cwd:path.resolve(__dirname,'..'),stdio:'inherit',env:{...process.env,PYTHONIOENCODING:'utf-8'}});
if(result.error)throw result.error;
process.exitCode=result.status || 0;
