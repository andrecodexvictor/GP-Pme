/* Contas condicionais e quadro de exercício. Sem transporte ou persistência. */
(() => {
  'use strict';
  const money = new Intl.NumberFormat('pt-BR', {style:'currency',currency:'BRL'});
  const decimal = new Intl.NumberFormat('pt-BR', {maximumFractionDigits:3});
  const read = (id, positive=false) => {
    const input=document.getElementById(id);
    const n=input.valueAsNumber;
    if (!Number.isFinite(n) || n<0 || (positive && n<=0)) throw new Error('Confira os valores: números finitos, sem negativos; investimento e orçamento precisam ser positivos.');
    return n;
  };
  function bind(form, result, compute) {
    document.getElementById(form).addEventListener('submit', e => {
      e.preventDefault(); const out=document.getElementById(result);
      try { out.textContent=compute(); } catch(error) { out.textContent=error.message; }
    });
  }
  bind('roi-form','roi-result',() => {
    const i=read('investment',true),b=read('benefit'),c=read('recurring'),net=b-c;
    const roi=(net*12-i)/i*100,ratio=b*12/i,payback=net>0?i/net:null;
    if (![roi,ratio,...(payback===null?[]:[payback])].every(Number.isFinite)) throw new Error('Valores excedem a capacidade numérica. Use premissas menores.');
    return `ROI líquido anual: ${decimal.format(roi)}%. Razão benefício bruto anual/investimento: ${decimal.format(ratio)}. Benefício líquido mensal estimado: ${money.format(net)}. `+(payback===null?'Sem payback simples finito.':`Payback simples: ${decimal.format(payback)} meses.`);
  });
  bind('capacity-form','capacity-result',() => {
    const hours=read('hours'),people=read('people'),rate=read('hourly');
    if (!Number.isInteger(people)) throw new Error('Informe um número inteiro de pessoas.');
    const value=hours*people*rate;
    if (!Number.isFinite(value)) throw new Error('Valores excedem a capacidade numérica.');
    return `Capacidade potencial estimada: ${money.format(value)}/mês. Esta conta não comprova redução de despesa.`;
  });
  bind('dan-form','dan-result',() => {
    const cost=read('debt-hours')*read('debt-hourly'),ratio=cost/read('budget',true);
    if (![cost,ratio].every(Number.isFinite)) throw new Error('Valores excedem a capacidade numérica.');
    return `Custo estimado de refatoração: ${money.format(cost)}. DAN financeiro local: ${decimal.format(ratio)} (${decimal.format(ratio*100)}% do orçamento anual). Sem faixa universal de interpretação.`;
  });
  const states=['A Fazer','Em Andamento','Em Teste','Concluído'];
  let tasks=[],sequence=1;
  const status=document.getElementById('board-status');
  const active=task=>task.state===1 || task.state===2;
  const count=executor=>tasks.filter(t=>active(t) && t.executor===executor).length;
  function button(text,fn) { const b=document.createElement('button');b.type='button';b.textContent=text;b.addEventListener('click',fn);return b; }
  function renderBoard() {
    const board=document.getElementById('board');board.replaceChildren();
    states.forEach((label,index) => {
      const section=document.createElement('section');
      const h=document.createElement('h3');h.textContent=`${label} (${tasks.filter(t=>t.state===index).length})`;section.append(h);
      tasks.filter(t=>t.state===index).forEach(task => {
        const card=document.createElement('article');card.className='exercise-task';
        const title=document.createElement('h4');title.textContent=task.title;card.append(title);
        const meta=document.createElement('p');meta.textContent=`Executor: ${task.executor}. Iniciados: ${count(task.executor)}/3.`+(task.blocked?' Bloqueado; permanece na contagem.':'');card.append(meta);
        if (task.state<3) card.append(button(['Iniciar','Enviar a teste','Concluir'][task.state],() => {
          if (task.blocked) {status.textContent='Resolva o bloqueio antes de avançar.';return;}
          if (task.state===0 && count(task.executor)>=3) {status.textContent=`${task.executor} já tem três itens iniciados, incluindo testes e bloqueios.`;return;}
          task.state++;status.textContent=`${task.title}: ${states[task.state]}.`;renderBoard();
          // Redraw retains a predictable keyboard destination.
          document.getElementById('board-status').focus();
        }));
        if (active(task)) card.append(button(task.blocked?'Resolver bloqueio':'Marcar bloqueio',() => {task.blocked=!task.blocked;status.textContent=task.blocked?'Bloqueio registrado; item continua iniciado.':'Bloqueio resolvido.';renderBoard();status.focus();}));
        section.append(card);
      });
      board.append(section);
    });
  }
  status.tabIndex=-1;
  document.getElementById('board-form').addEventListener('submit',e=>{
    e.preventDefault();const title=document.getElementById('task-title').value.trim(),executor=document.getElementById('executor').value.trim();
    if(!title || !executor){status.textContent='Informe demanda e executor.';return;}
    tasks.push({id:sequence++,title,executor,state:0,blocked:false});
    status.textContent=`${title} adicionada à fila de ${executor}.`;document.getElementById('task-title').value='';renderBoard();
  });
  document.getElementById('board-reset').addEventListener('click',()=>{tasks=[];sequence=1;status.textContent='Exercício limpo.';renderBoard();});
  renderBoard();
})();
