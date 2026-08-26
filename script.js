// ================================================
//  今遇莨缘 · 香云纱  |  PPT 交互脚本
// ================================================

const TOTAL_SLIDES = 8;
let currentSlide = 1;
let isAnimating = false;

// ── Init ──────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  buildDots();
  updateNav();
  spawnParticles('coverParticles', 30);
  spawnParticles('closingParticles', 20);
  setStaggerIndices();
  document.addEventListener('keydown', onKeyDown);
  document.addEventListener('wheel', debounce(onWheel, 300), { passive: false });
  initTouchSwipe();
});

// ── Dots ──────────────────────────────────────
function buildDots() {
  const container = document.getElementById('slideDots');
  for (let i = 1; i <= TOTAL_SLIDES; i++) {
    const dot = document.createElement('div');
    dot.className = 'dot' + (i === 1 ? ' active' : '');
    dot.setAttribute('id', `dot-${i}`);
    dot.setAttribute('title', getSlideName(i));
    dot.addEventListener('click', () => goToSlide(i));
    container.appendChild(dot);
  }
}

function getSlideName(n) {
  const names = ['封面','品牌故事','认识香云纱','匠心工艺','面料特性','产品系列','品牌理念','结语'];
  return names[n - 1] || '';
}

// ── Navigation ────────────────────────────────
function changeSlide(dir) {
  goToSlide(currentSlide + dir);
}

function goToSlide(target) {
  if (isAnimating || target < 1 || target > TOTAL_SLIDES || target === currentSlide) return;
  isAnimating = true;

  const leaving = document.getElementById(`slide-${currentSlide}`);
  const entering = document.getElementById(`slide-${target}`);
  const dir = target > currentSlide ? 1 : -1;

  // Reset entering slide (it might be coming from either direction)
  entering.style.transition = 'none';
  entering.style.opacity = '0';
  entering.style.transform = `translateX(${dir * 60}px)`;
  entering.classList.remove('active', 'exit-left');

  // Force reflow
  entering.getBoundingClientRect();
  entering.style.transition = '';

  // Exit current
  leaving.style.transform = `translateX(${dir * -60}px)`;
  leaving.style.opacity = '0';
  leaving.classList.remove('active');

  // Enter new
  entering.classList.add('active');
  entering.style.transform = 'translateX(0)';
  entering.style.opacity = '1';

  setTimeout(() => {
    leaving.style.transform = '';
    leaving.style.opacity = '';
    isAnimating = false;
  }, 700);

  currentSlide = target;
  updateNav();
}

function updateNav() {
  document.getElementById('prevBtn').disabled = currentSlide === 1;
  document.getElementById('nextBtn').disabled = currentSlide === TOTAL_SLIDES;
  document.getElementById('slideCounter').textContent = `${currentSlide} / ${TOTAL_SLIDES}`;

  // Dots
  document.querySelectorAll('.dot').forEach((d, i) => {
    d.classList.toggle('active', i + 1 === currentSlide);
  });

  // Progress bar
  const pct = (currentSlide / TOTAL_SLIDES) * 100;
  document.getElementById('progressFill').style.width = pct + '%';
}

// ── Keyboard ──────────────────────────────────
function onKeyDown(e) {
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ' || e.key === 'PageDown') {
    e.preventDefault();
    changeSlide(1);
  } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'PageUp') {
    e.preventDefault();
    changeSlide(-1);
  } else if (e.key === 'Home') {
    goToSlide(1);
  } else if (e.key === 'End') {
    goToSlide(TOTAL_SLIDES);
  }
}

// ── Mouse Wheel ───────────────────────────────
function onWheel(e) {
  e.preventDefault();
  if (e.deltaY > 0) changeSlide(1);
  else changeSlide(-1);
}

// ── Touch Swipe ───────────────────────────────
function initTouchSwipe() {
  let startX = 0;
  document.addEventListener('touchstart', e => { startX = e.touches[0].clientX; });
  document.addEventListener('touchend', e => {
    const diff = startX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 60) changeSlide(diff > 0 ? 1 : -1);
  });
}

// ── Particles ─────────────────────────────────
function spawnParticles(containerId, count) {
  const container = document.getElementById(containerId);
  if (!container) return;
  for (let i = 0; i < count; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    const size = Math.random() * 3 + 1;
    p.style.cssText = `
      left: ${Math.random() * 100}%;
      bottom: ${Math.random() * 40}%;
      width: ${size}px;
      height: ${size}px;
      --dur: ${Math.random() * 8 + 6}s;
      --delay: ${Math.random() * -10}s;
      opacity: 0;
    `;
    container.appendChild(p);
  }
}

// ── Product category switcher ─────────────────
function selectCategory(el, category) {
  document.querySelectorAll('.product-cat').forEach(c => c.classList.remove('active'));
  el.classList.add('active');

  document.querySelectorAll('.product-desc').forEach(d => d.classList.add('hidden'));
  const target = document.getElementById(`prod-${category}`);
  if (target) {
    target.classList.remove('hidden');
    target.style.animation = 'fadeInUp 0.4s ease both';
    setTimeout(() => { target.style.animation = ''; }, 400);
  }
}

// ── Stagger animation indices ──────────────────
function setStaggerIndices() {
  document.querySelectorAll('.about-card').forEach((el, i) => el.style.setProperty('--i', i));
  document.querySelectorAll('.craft-step').forEach((el, i) => el.style.setProperty('--i', i));
  document.querySelectorAll('.feature-item').forEach((el, i) => el.style.setProperty('--i', i));
  document.querySelectorAll('.value-card').forEach((el, i) => el.style.setProperty('--i', i));
}

// ── Utilities ─────────────────────────────────
function debounce(fn, wait) {
  let timer;
  return function(...args) {
    if (timer) return;
    fn.apply(this, args);
    timer = setTimeout(() => { timer = null; }, wait);
  };
}
