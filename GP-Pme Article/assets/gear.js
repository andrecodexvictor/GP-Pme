// Conteúdo e navegação documental funcionam sem este script.
document.querySelectorAll('.mobile-nav a').forEach(link => link.addEventListener('click', () => {
  const menu = link.closest('details'); if (menu) menu.open = false;
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') document.querySelectorAll('.mobile-nav[open]').forEach(menu => {
    menu.open = false; menu.querySelector('summary').focus();
  });
});
// Modelos permanecem selecionáveis; cópia dá retorno também em file://.
document.querySelectorAll('pre').forEach((pre,index) => {
  const button=document.createElement('button');button.type='button';
  button.className='copy-code';
  button.textContent='Copiar modelo';button.setAttribute('aria-label',`Copiar bloco ${index+1}`);
  button.addEventListener('click',async()=>{
    try {
      if(!navigator.clipboard?.writeText) throw new Error('clipboard unavailable');
      await navigator.clipboard.writeText(pre.textContent);button.textContent='Copiado';
    } catch {
      const selection=getSelection(),range=document.createRange();range.selectNodeContents(pre);selection.removeAllRanges();selection.addRange(range);
      button.textContent='Texto selecionado; use Ctrl+C';
    }
  });
  pre.before(button);
});
