# Google Stitch Design System Prompt for GP-PME Article

This document contains a structured design-system prompt ready to be fed to an AI front-end developer or UI styling engine to apply the **Google Stitch** design pattern to the GP-PME interactive article.

---

## The Prompt

```text
Atuar como um designer de interface sênior especialista em CSS moderno e no padrão de design "Google Stitch" (Stitch Design Pattern). Seu objetivo é re-estilizar o arquivo HTML da página do GP-PME utilizando exclusivamente CSS puro de alto nível e as diretrizes estéticas estipuladas abaixo.

---

## 1. Diretrizes de Cores (Paleta HSL Tailored)
Substitua cores primárias puras por variações sofisticadas em HSL, garantindo alto contraste de legibilidade e estética premium no modo escuro:
- Background Primário: HSL(220, 25%, 10%) - Azul Acinzentado escuro profundo (Charcoal).
- Background Secundário/Superfície: HSL(220, 25%, 14%) - Tons de Obsidian.
- Elemento de Card: HSLA(220, 25%, 18%, 0.6) com Blur de Glassmorphism.
- Borda Ativa: HSLA(220, 20%, 30%, 0.4).
- Acento de Governança (Pilar 1): HSL(210, 100%, 55%) - Azul Material Vivo.
- Acento de Execução (Pilar 2): HSL(145, 80%, 45%) - Verde Esmeralda Macio.
- Acento de Segurança (Pilar 3): HSL(35, 90%, 50%) - Âmbar Quente.
- Acento de IA (Pilar 4): HSL(270, 85%, 60%) - Roxo Real Elétrico.

---

## 2. Tipografia (Google Fonts)
- Carregue do Google Fonts as fontes 'Outfit' (para títulos impactantes) e 'Inter' (para textos de leitura fluida).
- H1: font-family: 'Outfit'; font-weight: 800; letter-spacing: -0.03em; background: linear-gradient;
- Parágrafos: font-family: 'Inter'; font-weight: 400; line-height: 1.6; color: HSL(210, 15%, 75%).

---

## 3. Estrutura de Grid e Spacing (Google Stitch Grid System)
- Siga uma grade base estrita de 8px para margens e paddings.
- Use Flexbox e CSS Grid Responsivo (`repeat(auto-fit, minmax(300px, 1fr))`) para o alinhamento de colunas dos pilares.
- Os cards devem possuir bordas arredondadas suaves (`border-radius: 16px`), sombras projetadas leves para simular profundidade material (`box-shadow: 0 8px 30px 0 rgba(0,0,0,0.3)`) e bordas internas sutis (`border: 1px solid var(--border-color)`).

---

## 4. Efeitos e Micro-interações
- Efeito Hover nos Cards: Use transições suaves (`transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)`). Ao passar o mouse, o card deve subir 5px (`transform: translateY(-5px)`) e a cor da borda deve clarear ligeiramente.
- Indicador Lateral nos Cards (Design Pattern Stitch): Cada card deve possuir um friso ou borda lateral esquerda de 4px sólida utilizando a cor de acento de seu respectivo pilar (azul, verde, âmbar ou roxo).
- Efeito Glassmorphism: Utilize filtros de desfoque de fundo (`backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px)`) nas superfícies dos cards para simular profundidade de vidro fosco.

---

Gere as classes CSS e monte a folha de estilo de forma totalmente limpa e organizada, sem adicionar dependências externas ou JavaScript, garantindo compatibilidade total com navegadores modernos e visualização impecável.
```
