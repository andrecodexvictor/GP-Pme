// Browser QA in an isolated owned profile. Does not attach to the user's browser.
const puppeteer = require('puppeteer-core');
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const root = path.resolve(__dirname, '..');
async function main() {
  const out = path.join(root, '.context', 'gear-execution', 'browser'); fs.mkdirSync(out, { recursive: true });
  const profile = fs.mkdtempSync(path.join(out, 'profile-'));
  const browser = await puppeteer.launch({ executablePath: process.env.GEAR_BROWSER || 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', userDataDir: profile, headless: true, args: ['--no-first-run','--disable-extensions'] });
  const results = [];
  try {
    const page = await browser.newPage();
    page.on('pageerror', e => results.push({ error: e.message }));
    for (const width of [320, 390, 768, 1024, 1440]) {
      await page.setViewport({ width, height: 1000 });
      for (const file of ['index.html','docs/adocao/primeiros-30-dias.html','docs/indicadores/financeiros.html','biblioteca.html','blog/retorno.html','busca.html','ferramentas.html','docs/adocao/fichas-maturidade.html','docs/adocao/preparacao-cronograma.html','docs/indicadores/negocio-comparacao.html','docs/templates/tasklist.html','docs/templates/inventario-dependencias.html','docs/templates/instrucao-assistencia.html','docs/templates/painel-indicadores.html','docs/guias/fluxos-de-trabalho.html','docs/indicadores/assistencia.html','docs/fundamentos/evolucao-indicadores.html','docs/templates/prompts-revisao-operacional.html']) {
        await page.goto(pathToFileURL(path.join(root,'GP-Pme Article',file)).href);
        await page.evaluate(async () => { await document.fonts.load('18px "Public Sans"'); await document.fonts.load('18px "Source Serif"'); await document.fonts.ready; });
        const data = await page.evaluate(() => ({ title: document.title, overflow: document.documentElement.scrollWidth > innerWidth + 1, heading: document.querySelector('h1')?.textContent, fonts: document.fonts.check('18px "Public Sans"') && document.fonts.check('18px "Source Serif"') }));
        results.push({ width, file, ...data });
        await page.screenshot({ path: path.join(out, width+'-'+file.replace(/[/.]/g,'-')+'.png'), fullPage: true });
      }
    }
    await page.setViewport({ width: 390, height: 900 });
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','busca.html')).href);
    await page.type('#query','restauração'); await page.click('button[type=submit]');
    const matches = await page.$$eval('#search-results a', nodes => nodes.map(n => ({ href:n.href, label:n.textContent })));
    results.push({ journey:'offline-search', matches:matches.length, first:matches[0] });
    if (!matches.length) throw new Error('Busca sem resultados para restauração');
    await page.click('#search-results a');
    results.push({ journey:'search-section', anchor:await page.evaluate(() => ({ hash:location.hash, exists:!!document.getElementById(decodeURIComponent(location.hash.slice(1))) })) });
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','index.html')).href);
    await page.keyboard.press('Tab');
    results.push({ journey:'keyboard-skip', label:await page.evaluate(() => document.activeElement.textContent) });
    await page.keyboard.press('Enter');
    await page.click('.mobile-nav summary');
    await page.keyboard.press('Escape');
    results.push({ journey:'menu-escape', closed:await page.$eval('.mobile-nav', n => !n.open), focus:await page.evaluate(() => document.activeElement.tagName) });
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','ferramentas.html')).href);
    await page.click('#roi-form button');
    let calculation=await page.$eval('#roi-result',n=>n.textContent);
    if(!calculation.includes('233,333%') || !calculation.includes('3,6 meses')) throw new Error('ROI ou payback incorreto');
    await page.$eval('#recurring',n=>n.value='3000');
    await page.click('#roi-form button');
    if(!(await page.$eval('#roi-result',n=>n.textContent)).includes('Sem payback simples finito')) throw new Error('Payback sem fronteira');
    results.push({journey:'financial-boundary',passed:true});
    for(const [id,value] of [['hours','20'],['people','3'],['hourly','50']]) await page.$eval('#'+id,(n,v)=>n.value=v,value);
    await page.click('#capacity-form button');
    if(!(await page.$eval('#capacity-result',n=>n.textContent)).includes('3.000,00')) throw new Error('Capacidade incorreta');
    for(const [id,value] of [['debt-hours','180'],['debt-hourly','50'],['budget','30000']]) await page.$eval('#'+id,(n,v)=>n.value=v,value);
    await page.click('#dan-form button');
    if(!(await page.$eval('#dan-result',n=>n.textContent)).includes('0,3 (30%')) throw new Error('DAN incorreto');
    for(let i=0;i<4;i++) {
      await page.$eval('#task-title',(n,v)=>n.value=v,'Exercício '+i);
      await page.$eval('#executor',n=>n.value='TI');
      await page.click('#board-form button');
    }
    const start=async()=>page.$eval('#board section:first-child button',n=>n.click());
    await start(); await start(); await start();
    await page.$eval('#board section:nth-child(2) button',n=>n.click()); // One in testing still counts.
    await page.$eval('#board section:nth-child(2) article button:nth-of-type(2)',n=>n.click()); // One blocked still counts.
    await start();
    const status=await page.$eval('#board-status',n=>n.textContent);
    if(!status.includes('três itens iniciados')) throw new Error('WIP excedeu o limite');
    results.push({journey:'wip-testing-and-blocked',passed:true});
    await page.click('#board-reset');
    if(await page.$$eval('.exercise-task',n=>n.length)) throw new Error('Reset não limpou o exercício');
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','docs/templates/prd-aceite.html')).href);
    await page.click('.template-source summary');
    const copyButtons=await page.$$eval('.copy-code',n=>n.length);
    if(!copyButtons) throw new Error('Controle de cópia ausente');
    await page.click('.copy-code');
    await page.waitForFunction(()=>document.querySelector('.copy-code').textContent!=='Copiar modelo');
    const copyFeedback=await page.$eval('.copy-code',n=>n.textContent);
    if(!copyFeedback.includes('Copiado') && !copyFeedback.includes('Texto selecionado')) throw new Error('Cópia sem retorno');
    results.push({journey:'copy-control',buttons:copyButtons,feedback:copyFeedback});
    // Reflow equivalent of a 1280px display at 400% zoom; then enlarged text.
    await page.setViewport({ width: 320, height: 900 });
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','docs/adocao/primeiros-30-dias.html')).href);
    await page.addStyleTag({ content:'html{font-size:200%}p{line-height:1.5;letter-spacing:.12em;word-spacing:.16em}p{margin-bottom:2em}' });
    results.push({ journey:'text-spacing-and-size', overflow:await page.evaluate(() => document.documentElement.scrollWidth > innerWidth+1) });
    await page.screenshot({ path:path.join(out,'texto-ampliado.png'), fullPage:true });
    for (const file of ['docs/templates/prd-aceite.html','docs/indicadores/negocio-comparacao.html','docs/templates/instrucao-assistencia.html']) {
      await page.goto(pathToFileURL(path.join(root,'GP-Pme Article',file)).href);
      await page.addStyleTag({ content:'html{font-size:200%}p{line-height:1.5;letter-spacing:.12em;word-spacing:.16em}p{margin-bottom:2em}' });
      results.push({ journey:'enriched-text-spacing',file,overflow:await page.evaluate(() => document.documentElement.scrollWidth > innerWidth+1) });
    }
    await page.setViewport({ width:390, height:900 });
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','docs/templates/inventario-dependencias.html')).href);
    await page.focus('.table-wrap');
    await page.keyboard.press('ArrowRight');
    await page.waitForFunction(()=>document.querySelector('.table-wrap').scrollLeft>0);
    results.push({journey:'table-keyboard-scroll',passed:true});
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','docs/guias/fluxos-de-trabalho.html')).href);
    await page.focus('.diagram-scroll');
    await page.keyboard.press('ArrowRight');
    await page.waitForFunction(()=>document.querySelector('.diagram-scroll').scrollLeft>0);
    results.push({journey:'diagram-keyboard-scroll',passed:true});
    await page.goto(pathToFileURL(path.join(root,'GP-Pme Article','busca.html')).href);
    await page.type('#query','zzzzzzzzzzzz');await page.click('button[type=submit]');
    if(await page.$$eval('#search-results a',n=>n.length))throw new Error('Busca vazia apresenta resultados indevidos');
    results.push({journey:'empty-search',passed:true,status:await page.$eval('#search-status',n=>n.textContent)});
    fs.writeFileSync(path.join(out,'verificacao.json'), JSON.stringify(results,null,2));
    if (results.some(r => r.overflow || r.error || (r.anchor && !r.anchor.exists))) throw new Error('Falha de layout, script ou âncora; consultar verificacao.json');
    console.log(`Browser QA: ${results.length} verificações; perfil isolado ${profile}`);
  } finally { await browser.close(); }
}
main().catch(error => { console.error(error); process.exitCode=1; });
