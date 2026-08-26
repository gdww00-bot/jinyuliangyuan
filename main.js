/* ─ main.js ─ 今遇莨缘香云纱官网交互脚本 ─ */

document.addEventListener('DOMContentLoaded', () => {

  /* ══ 1. Navbar scroll effect ══ */
  const navbar = document.getElementById('navbar');
  const onScroll = () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ══ 2. Mobile nav toggle ══ */
  const toggle = document.getElementById('nav-toggle');
  const menu   = document.getElementById('nav-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      menu.classList.toggle('open');
      const spans = toggle.querySelectorAll('span');
      if (menu.classList.contains('open')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity   = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity   = '';
        spans[2].style.transform = '';
      }
    });
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.remove('open');
        const spans = toggle.querySelectorAll('span');
        if (spans.length >= 3) {
          spans[0].style.transform = '';
          spans[1].style.opacity   = '';
          spans[2].style.transform = '';
        }
      });
    });
  }

  /* ══ 3. Hero particles ══ */
  const particlesContainer = document.getElementById('hero-particles');
  if (particlesContainer) {
    const PARTICLE_COUNT = 35;
    for (let i = 0; i < PARTICLE_COUNT; i++) {
      const p = document.createElement('div');
      p.className = 'particle';
      const size = Math.random() * 2.5 + 1;
      p.style.cssText = `
        left: ${Math.random() * 100}%;
        bottom: ${Math.random() * 60}%;
        width: ${size}px;
        height: ${size}px;
        animation-duration: ${Math.random() * 8 + 6}s;
        animation-delay: ${Math.random() * 8}s;
      `;
      particlesContainer.appendChild(p);
    }
  }

  /* ══ 4. Scroll reveal animations ══ */
  const revealEls = [
    { el: '#about-image-wrap', delay: 0 },
    { el: '#about-content',    delay: 1 },
    { el: '#step-1', delay: 0 },
    { el: '#step-2', delay: 1 },
    { el: '#step-3', delay: 2 },
    { el: '#step-4', delay: 3 },
    { el: '#step-5', delay: 4 },
    { el: '#step-6', delay: 5 },
    { el: '#product-1', delay: 0 },
    { el: '#product-2', delay: 1 },
    { el: '#product-3', delay: 2 },
    { el: '#product-4', delay: 3 },
    { el: '#heritage-content', delay: 0 },
    { el: '#heritage-visual',  delay: 1 },
    { el: '#why-1', delay: 0 },
    { el: '#why-2', delay: 1 },
    { el: '#why-3', delay: 2 },
    { el: '#why-4', delay: 3 },
    { el: '#h-stat-1', delay: 0 },
    { el: '#h-stat-2', delay: 1 },
    { el: '#h-stat-3', delay: 2 },
    { el: '#h-stat-4', delay: 3 },
    { el: '#contact-info',      delay: 0 },
    { el: '#contact-form-wrap', delay: 1 },
  ];

  revealEls.forEach(({ el, delay }) => {
    const element = document.querySelector(el);
    if (!element) return;
    element.classList.add('reveal');
    if (delay) element.classList.add(`reveal-delay-${delay}`);
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  /* ══ 5. Active nav link on scroll ══ */
  const sections = ['products','about','showroom','contact'];
  const navLinks  = document.querySelectorAll('.nav-link');
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          }
        });
      }
    });
  }, { threshold: 0.4 });
  sections.forEach(id => {
    const el = document.getElementById(id);
    if (el) sectionObserver.observe(el);
  });

  /* ══ 6. Counter animation ══ */
  function animateCounter(el, target, suffix = '', duration = 2000) {
    const start = performance.now();
    const isFloat = target.toString().includes('.');
    const update = (time) => {
      const elapsed = Math.min((time - start) / duration, 1);
      const eased = 1 - Math.pow(1 - elapsed, 3);
      const current = isFloat
        ? (eased * parseFloat(target)).toFixed(1)
        : Math.round(eased * parseInt(target));
      el.textContent = current + suffix;
      if (elapsed < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
  }

  const statObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const statNum = el.querySelector('.h-stat-num, .strip-num');
        if (statNum && !el.dataset.counted) {
          el.dataset.counted = 'true';
          const text = statNum.textContent.trim();
          const num  = parseFloat(text.replace(/[^0-9.]/g,''));
          const suffix = text.replace(/[0-9.]/g,'');
          if (!isNaN(num) && num > 0) {
            animateCounter(statNum, num, suffix);
          }
        }
        statObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.h-stat, .strip-item').forEach(el => statObserver.observe(el));

  /* ══ 7. Contact form ══ */
  window.handleFormSubmit = function(e) {
    e.preventDefault();
    const form    = document.getElementById('contact-form');
    const success = document.getElementById('form-success');
    const btn     = document.getElementById('btn-submit');
    if (btn) {
      btn.textContent = '提交中...';
      btn.disabled    = true;
    }
    setTimeout(() => {
      if (form) form.style.display = 'none';
      if (success) {
        success.style.display = 'block';
        success.style.animation = 'fadeUp 0.6s ease both';
      }
    }, 1200);
  };

  /* ══ 8. Parallax on hero image ══ */
  const heroBgImg = document.querySelector('.hero-bg-img');
  window.addEventListener('scroll', () => {
    if (heroBgImg) {
      const y = window.scrollY * 0.25;
      heroBgImg.style.transform = `scale(1.08) translateY(${y}px)`;
    }
  }, { passive: true });

  console.log('✨ 今遇莨缘香云纱官网 已启动');
});

/* ══ 9. Four Masterpiece Series Modal Logic (四大典藏系列交互逻辑) ══ */
window.seriesData = {
  'xishangmeishao': {
    title: '喜上眉梢 ｜ 香云纱斜襟套装',
    tag: '非遗刺绣 · 典藏套装',
    images: [
      'assets/series/xishangmeishao_1.jpg',
      'assets/series/xishangmeishao_2.jpg',
      'assets/series/xishangmeishao_3.jpg',
      'assets/series/xishangmeishao_4.jpg'
    ],
    text: `
      <p><strong>【材质设计】</strong>黑底非遗香云纱，沉淀时光的哑光油润质感，沉静而有力量。取传统吉祥纹样喜上眉梢，灵鸟栖于花枝，重工刺绣针脚细密，青蓝花色于墨色衣身徐徐绽放，寓意喜乐安康。</p>
      <p><strong>【细节剪裁】</strong>经典立领斜襟，手工盘扣顺衣襟错落排布，七分袖宽松剪裁，自在包容身形。承袭旧时衣冠风骨，又适配当代生活，雅聚、赴宴皆相宜。</p>
      <ul>
        <li>古法多重固色，久穿不易泛旧</li>
        <li>可成套上身，也可拆分混搭</li>
        <li>把中式美好祝愿穿在身上</li>
      </ul>
    `
  },
  'moranhuajing': {
    title: '墨染花境 ｜ 香云纱改良旗袍',
    tag: '顺德非遗 · 国风经典',
    images: [
      'assets/series/moranhuajing_1.jpg',
      'assets/series/moranhuajing_2.jpg',
      'assets/series/moranhuajing_3.jpg',
      'assets/series/moranhuajing_4.jpg'
    ],
    text: `
      <p><strong>【材质工艺】</strong>顺德非遗香云纱，薯莨浸染，河泥覆晒，历经多道日晒工序，自带独有的哑光柔润肌理。</p>
      <p><strong>【细节剪裁】</strong>暗纹底布暗藏风华，衣身蓝红撞色刺绣，灵动雅致。中式立领搭配手工盘扣，无袖垂坠版型，显瘦包容，勾勒东方气韵。</p>
      <ul>
        <li>古法多重固色，不易掉色泛白</li>
        <li>透气舒适四季可穿</li>
        <li>通勤、宴会皆可，一件陪伴很久的国风经典</li>
      </ul>
    `
  },
  'zhuohuamudan': {
    title: '灼华牡丹 ｜ 香云纱重工马甲',
    tag: '复古红棕 · 满身重工',
    images: [
      'assets/series/zhuohuamudan_1.jpg',
      'assets/series/zhuohuamudan_2.jpg',
      'assets/series/zhuohuamudan_3.jpg',
      'assets/series/zhuohuamudan_4.jpg'
    ],
    text: `
      <p><strong>【材质美感】</strong>顺德非遗香云纱，自带复古红棕调的温润光泽。满身重工牡丹刺绣，层次饱满立体，花开灼灼，古韵盎然。</p>
      <p><strong>【搭配场景】</strong>中式斜襟手工盘扣，利落无袖版型，不挑身材。可搭新中式内搭，亦可混搭牛仔裤，国风与休闲碰撞，日常也能穿出高级感。</p>
      <ul>
        <li>古法多重固色，耐穿不易泛白</li>
        <li>一件马甲解锁多种百搭穿搭</li>
        <li>国风衣橱里的百搭宝藏</li>
      </ul>
    `
  },
  'jintingfeitang': {
    title: '金庭绯棠 ｜ 香云纱西装马甲套装',
    tag: '新中式西装 · 鎏金华贵',
    images: [
      'assets/series/jintingfeitang_1.jpg',
      'assets/series/jintingfeitang_2.jpg',
      'assets/series/jintingfeitang_3.jpg',
      'assets/series/jintingfeitang_4.jpg'
    ],
    text: `
      <p><strong>【材质设计】</strong>鎏金调非遗香云纱，自带时光沉淀的华贵光泽。大朵牡丹重工刺绣，红花翠叶，富丽却不张扬。</p>
      <p><strong>【现代廓形】</strong>打破传统中式形制，西装翻领设计，利落飒爽。同面料阔腿裤，垂坠舒展，气场十足。混搭简约白衬衫，新中式与现代西装感碰撞，松弛又贵气。</p>
      <ul>
        <li>古法多重固色，质感耐得住岁月</li>
        <li>西装翻领 + 垂坠阔腿裤高端设计</li>
        <li>松弛又贵气，气场十足</li>
      </ul>
    `
  }
};

window.openSeriesModal = function(key) {
  const data = window.seriesData[key];
  if (!data) return;
  
  const modal = document.getElementById('seriesModalOverlay');
  const modalTitle = document.getElementById('modalTitle');
  const modalTag = document.getElementById('modalTag');
  const modalText = document.getElementById('modalText');
  const modalMainImg = document.getElementById('modalMainImg');
  const modalThumbs = document.getElementById('modalThumbs');
  
  if (!modal) return;

  modalTitle.textContent = data.title;
  modalTag.textContent = data.tag;
  modalText.innerHTML = data.text;
  
  modalMainImg.src = data.images[0];
  modalThumbs.innerHTML = '';
  
  data.images.forEach((imgSrc, idx) => {
    const thumb = document.createElement('div');
    thumb.className = 'series-modal-thumb' + (idx === 0 ? ' active' : '');
    thumb.innerHTML = `<img src="${imgSrc}" alt="缩略图 ${idx + 1}" />`;
    thumb.onclick = () => {
      modalMainImg.style.opacity = '0.3';
      setTimeout(() => {
        modalMainImg.src = imgSrc;
        modalMainImg.style.opacity = '1';
      }, 150);
      document.querySelectorAll('.series-modal-thumb').forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');
    };
    modalThumbs.appendChild(thumb);
  });
  
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
};

window.closeSeriesModal = function(e) {
  if (!e || e.target.id === 'seriesModalOverlay' || e.target.classList.contains('series-modal-close')) {
    const modal = document.getElementById('seriesModalOverlay');
    if (modal) modal.classList.remove('active');
    document.body.style.overflow = '';
  }
};

/* Switch main image on thumbnail click in vertical series layout */
window.switchVImg = function(key, src, el) {
  const mainImg = document.getElementById('vImg-' + key);
  if (mainImg) {
    mainImg.style.opacity = '0.3';
    setTimeout(() => {
      mainImg.src = src;
      mainImg.style.opacity = '1';
    }, 120);
  }
  if (el && el.parentElement) {
    el.parentElement.querySelectorAll('.v-thumb').forEach(t => t.classList.remove('active'));
    el.classList.add('active');
  }
};
