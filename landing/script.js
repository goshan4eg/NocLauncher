const revealItems = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
revealItems.forEach((el) => io.observe(el));

const parallax = document.querySelector('.parallax');
window.addEventListener('mousemove', (e) => {
  if (!parallax) return;
  const depth = Number(parallax.dataset.depth || 12);
  const x = (window.innerWidth / 2 - e.clientX) / depth;
  const y = (window.innerHeight / 2 - e.clientY) / depth;
  parallax.style.transform = `translate(${x}px, ${y}px)`;
});

const petalsWrap = document.querySelector('.petals');
if (petalsWrap) {
  const count = Math.min(26, Math.max(12, Math.floor(window.innerWidth / 70)));
  for (let i = 0; i < count; i++) {
    const p = document.createElement('span');
    p.className = 'petal';
    p.style.left = `${Math.random() * 100}vw`;
    p.style.setProperty('--size', `${14 + Math.random() * 26}px`);
    p.style.setProperty('--dur', `${10 + Math.random() * 14}s`);
    p.style.setProperty('--drift', `${-90 + Math.random() * 180}px`);
    p.style.setProperty('--alpha', `${0.2 + Math.random() * 0.45}`);
    p.style.animationDelay = `${-Math.random() * 20}s`;
    petalsWrap.appendChild(p);
  }
}