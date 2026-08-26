/**
 * 今遇莨缘 · 香云纱 品牌宣传PPT 生成脚本
 * 使用 pptxgenjs 生成 .pptx 文件
 */

const PptxGenJS = require("pptxgenjs");
const fs = require("fs");
const path = require("path");

const pptx = new PptxGenJS();

pptx.layout = "LAYOUT_WIDE";
pptx.title = "今遇莨缘 · 香云纱品牌宣传";
pptx.subject = "岭南非遗 · 东方软黄金";
pptx.author = "今遇莨缘";

const C = {
  black:     "0A0806",
  dark:      "141008",
  darkMid:   "1E160C",
  brownDark: "2C1A0E",
  brown:     "5C3219",
  amber:     "8B5E3C",
  gold:      "C9A96E",
  goldLight: "E8D5A3",
  cream:     "F5EDE0",
  white:     "FDF8F2",
  muted:     "8B7355",
};

const FONT_SERIF = "楷体";
const FONT_SANS  = "微软雅黑";

const IMG_FASHION  = path.join(__dirname, "xiangyunsha_fashion.jpg");
const IMG_TEXTURE  = path.join(__dirname, "xiangyunsha_texture.jpg");
const IMG_CRAFT    = path.join(__dirname, "xiangyunsha_craft.jpg");
const IMG_PRODUCTS = path.join(__dirname, "xiangyunsha_products.jpg");

function addBg(slide, color1, color2, angle) {
  slide.addShape(pptx.ShapeType.rect, {
    x: 0, y: 0, w: "100%", h: "100%",
    fill: { type: "grad", stops: [
      { position: 0,   color: color1, transparency: 0 },
      { position: 100, color: color2, transparency: 0 },
    ], angle: angle || 135 },
  });
}

function addLine(slide, x, y, w) {
  slide.addShape(pptx.ShapeType.line, {
    x, y, w, h: 0,
    line: { color: C.gold, width: 0.8, transparency: 30 },
  });
}

function addLabel(slide, text, x, y, color) {
  slide.addText("— " + text, {
    x, y, w: 4, h: 0.3,
    fontSize: 10, color: color || C.gold,
    fontFace: FONT_SANS, charSpacing: 5,
  });
}

// ══════════════════════════════════════════════
// SLIDE 1 — 封面
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.dark, C.brownDark, 160);

  s.addShape(pptx.ShapeType.ellipse, {
    x: 3.5, y: 0.5, w: 6.5, h: 6.5,
    fill: { color: C.brownDark, transparency: 70 },
    line: { color: C.gold, transparency: 75, width: 0.5 },
  });
  s.addShape(pptx.ShapeType.ellipse, {
    x: 4.0, y: 1.0, w: 5.5, h: 5.5,
    fill: { color: "FFFFFF", transparency: 100 },
    line: { color: C.gold, transparency: 80, width: 0.3 },
  });

  s.addText("岭南非物质文化遗产 · 传世匠心", {
    x: 0, y: 1.0, w: "100%", h: 0.4,
    align: "center", fontSize: 11,
    color: C.gold, fontFace: FONT_SANS, charSpacing: 6,
  });

  s.addText("今遇莨缘", {
    x: 0, y: 1.8, w: "100%", h: 1.6,
    align: "center", fontSize: 72,
    color: C.cream, fontFace: FONT_SERIF, bold: true, charSpacing: 12,
    shadow: { type: "outer", color: "000000", blur: 8, offset: 4, angle: 45, opacity: 0.5 },
  });

  s.addText("香 云 纱", {
    x: 0, y: 3.5, w: "100%", h: 0.7,
    align: "center", fontSize: 28,
    color: C.gold, fontFace: FONT_SERIF, charSpacing: 20,
  });

  addLine(s, 3.2, 4.35, 3.1);
  s.addShape(pptx.ShapeType.diamond, {
    x: 6.55, y: 4.2, w: 0.2, h: 0.2,
    fill: { color: C.gold }, line: { color: C.gold, width: 0.5 },
  });

  s.addText("天地共染 · 薯莨为墨 · 岁月为韵", {
    x: 0, y: 4.6, w: "100%", h: 0.5,
    align: "center", fontSize: 16,
    color: C.goldLight, fontFace: FONT_SERIF, charSpacing: 5,
  });

  s.addText("The Softest Gold of the Orient", {
    x: 0, y: 5.2, w: "100%", h: 0.4,
    align: "center", fontSize: 12,
    color: C.muted, fontFace: "Times New Roman", italic: true,
  });

  addLine(s, 0.5, 6.8, 12.5);
  s.addText("2026  ·  今遇莨缘品牌宣传", {
    x: 0, y: 6.9, w: "100%", h: 0.3,
    align: "center", fontSize: 9,
    color: C.muted, fontFace: FONT_SANS, charSpacing: 3,
  });
}());

// ══════════════════════════════════════════════
// SLIDE 2 — 品牌故事
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.black, C.darkMid, 135);

  s.addShape(pptx.ShapeType.rect, {
    x: 0, y: 0, w: 0.06, h: "100%",
    fill: { type: "grad", stops: [
      { position: 0,   color: C.gold, transparency: 60 },
      { position: 100, color: C.gold, transparency: 20 },
    ], angle: 90 },
  });

  addLabel(s, "品牌故事", 0.5, 0.5);

  s.addText("今遇莨缘", {
    x: 0.5, y: 0.9, w: 5.5, h: 0.9,
    fontSize: 42, color: C.cream, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("此刻相遇，皆是缘", {
    x: 0.5, y: 1.75, w: 5.5, h: 0.45,
    fontSize: 18, color: C.gold, fontFace: FONT_SERIF,
  });

  addLine(s, 0.5, 2.35, 3.0);

  // 使用 Unicode 替代中文引号
  s.addText(
    "\u201c今遇\u201d\u2014\u2014今日得遇，是命运最美的安排；\n\u201c莨缘\u201d\u2014\u2014以莨为缘，延续千年的岭南风华。",
    {
      x: 0.5, y: 2.6, w: 5.8, h: 0.9,
      fontSize: 13, color: C.cream,
      fontFace: FONT_SERIF, lineSpacingMultiple: 1.8,
    }
  );

  s.addText(
    "品牌诞生于对岭南传统文化的深情热爱与当代生活美学的探索之间。我们相信，每一匹香云纱都是一段故事，每一位穿着者，都是与这段故事相遇的有缘人。",
    {
      x: 0.5, y: 3.55, w: 5.8, h: 0.9,
      fontSize: 12.5, color: C.goldLight,
      fontFace: FONT_SERIF, lineSpacingMultiple: 1.85,
    }
  );

  var stats = [
    { num: "500+", label: "年历史传承" },
    { num: "36",   label: "道手工工序" },
    { num: "国家级", label: "非物质文化遗产" },
  ];
  addLine(s, 0.5, 4.7, 5.5);
  stats.forEach(function(st, i) {
    var x = 0.5 + i * 1.95;
    s.addText(st.num, { x: x, y: 4.9,  w: 1.8, h: 0.65, fontSize: 26, color: C.gold, fontFace: FONT_SERIF, bold: true });
    s.addText(st.label, { x: x, y: 5.55, w: 1.8, h: 0.35, fontSize: 10, color: C.muted, fontFace: FONT_SANS, charSpacing: 2 });
  });

  if (fs.existsSync(IMG_FASHION)) {
    s.addImage({ path: IMG_FASHION, x: 6.8, y: 0.3, w: 6.0, h: 7.0 });
    s.addShape(pptx.ShapeType.rect, {
      x: 6.5, y: 0.1, w: 6.0, h: 7.0,
      fill: { color: "FFFFFF", transparency: 100 },
      line: { color: C.gold, width: 1, transparency: 55 },
    });
    s.addText("东方风华 · 低调奢华", {
      x: 7.0, y: 7.2, w: 5.5, h: 0.35,
      fontSize: 10, color: C.gold, fontFace: FONT_SANS, charSpacing: 4,
    });
  }
}());

// ══════════════════════════════════════════════
// SLIDE 3 — 认识香云纱
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.black, C.dark, 180);

  if (fs.existsSync(IMG_TEXTURE)) {
    s.addImage({ path: IMG_TEXTURE, x: 0, y: 0, w: "100%", h: "100%", transparency: 75 });
  }
  s.addShape(pptx.ShapeType.rect, {
    x: 0, y: 0, w: "100%", h: "100%",
    fill: { type: "grad", stops: [
      { position: 0,   color: C.black, transparency: 10 },
      { position: 100, color: C.dark,  transparency: 20 },
    ], angle: 180 },
  });

  addLabel(s, "认识香云纱", 0.4, 0.4, C.gold);

  s.addText("纺织界的", {
    x: 0, y: 0.75, w: "100%", h: 0.75,
    align: "center", fontSize: 36, color: C.cream,
    fontFace: FONT_SERIF, bold: true,
  });
  s.addText("软 黄 金", {
    x: 0, y: 1.45, w: "100%", h: 0.65,
    align: "center", fontSize: 34, color: C.gold,
    fontFace: FONT_SERIF, bold: true, charSpacing: 10,
  });
  s.addText("中国现存唯一以纯植物染料工艺制作的丝绸面料，被誉为\u300c软黄金\u300d", {
    x: 1.5, y: 2.15, w: 10.5, h: 0.45,
    align: "center", fontSize: 13, color: C.goldLight,
    fontFace: FONT_SERIF,
  });

  var cards = [
    { icon: "🌿", title: "天然植物染", desc: "以薯莨汁液为染料\n纯天然无化学添加\n中国唯一纯植物染丝绸" },
    { icon: "🌊", title: "珠三角河泥", desc: "取珠江流域特有塘泥\n富含铁离子与薯莨单宁\n发生独特化学反应" },
    { icon: "☀️", title: "天光日晒成色", desc: "在阳光下自然晒莨\n色泽深浅因天气而异\n每匹均是独一无二" },
    { icon: "🎋", title: "双面呈色",   desc: "正面乌黑发亮\n反面赤褐温润\n一布双色大自然馈赠" },
  ];
  cards.forEach(function(c, i) {
    var x = 0.45 + i * 3.25;
    s.addShape(pptx.ShapeType.rect, {
      x: x, y: 2.85, w: 3.05, h: 4.3,
      fill: { color: C.dark, transparency: 20 },
      line: { color: C.gold, width: 0.8, transparency: 60 },
    });
    s.addText(c.icon, { x: x, y: 3.05, w: 3.05, h: 0.7, align: "center", fontSize: 32 });
    s.addText(c.title, {
      x: x, y: 3.85, w: 3.05, h: 0.5,
      align: "center", fontSize: 16,
      color: C.goldLight, fontFace: FONT_SERIF, bold: true,
    });
    s.addText(c.desc, {
      x: x + 0.15, y: 4.5, w: 2.75, h: 2.4,
      align: "center", fontSize: 12,
      color: C.cream, fontFace: FONT_SANS, lineSpacingMultiple: 1.9,
    });
  });
}());

// ══════════════════════════════════════════════
// SLIDE 4 — 匠心工艺
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.black, C.brownDark, 135);

  addLabel(s, "匠心工艺", 0.5, 0.4);

  s.addText("三蒸九煮十八晒", {
    x: 0.5, y: 0.75, w: 6.5, h: 0.95,
    fontSize: 40, color: C.cream, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("36道纯手工工序，\u300c天、地、人\u300d共同协作的艺术", {
    x: 0.5, y: 1.7, w: 6.5, h: 0.45,
    fontSize: 13, color: C.muted, fontFace: FONT_SERIF, charSpacing: 2,
  });

  var steps = [
    { n: "01", title: "选坯", desc: "甄选优质桑蚕丝坯绸，以纯天然真丝为基底" },
    { n: "02", title: "浸莨", desc: "将坯绸浸泡入薯莨汁液，反复浸染十余次，使单宁充分渗透丝纤维" },
    { n: "03", title: "晒莨", desc: "将染后绸缎摊铺草地上，在阳光下自然晒干，最依赖天气的工序" },
    { n: "04", title: "过乌", desc: "覆河泥于绸缎，铁离子与单宁反应，形成黑色光泽涂层" },
    { n: "05", title: "水洗晾晒", desc: "清水洗净，反复晾晒，形成一面乌黑、一面赤褐的独特双色效果" },
  ];
  steps.forEach(function(st, i) {
    var y = 2.35 + i * 0.98;
    s.addShape(pptx.ShapeType.line, {
      x: 0.5, y: y, w: 0, h: 0.75,
      line: { color: C.gold, width: 1.5, transparency: 50 },
    });
    s.addText(st.n, { x: 0.7, y: y + 0.05, w: 0.55, h: 0.45, fontSize: 18, color: C.gold, fontFace: FONT_SERIF, bold: true });
    s.addText(st.title, { x: 1.35, y: y + 0.05, w: 1.1, h: 0.45, fontSize: 14, color: C.goldLight, fontFace: FONT_SERIF, bold: true });
    s.addText(st.desc,  { x: 2.55, y: y + 0.05, w: 4.0, h: 0.45, fontSize: 11.5, color: C.cream, fontFace: FONT_SANS });
  });

  if (fs.existsSync(IMG_CRAFT)) {
    s.addImage({ path: IMG_CRAFT, x: 7.2, y: 0.3, w: 5.8, h: 6.8 });
    s.addText("广东顺德 · 传统晒莨场", {
      x: 7.2, y: 7.0, w: 5.8, h: 0.35,
      align: "center", fontSize: 10, color: C.gold, fontFace: FONT_SANS, charSpacing: 4,
    });
  }
}());

// ══════════════════════════════════════════════
// SLIDE 5 — 面料特性
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.dark, C.black, 180);

  addLabel(s, "面料特性", 0.5, 0.4);
  s.addText("为何选择", {
    x: 0.5, y: 0.75, w: 6, h: 0.75,
    fontSize: 40, color: C.cream, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("香 云 纱", {
    x: 0.5, y: 1.4, w: 3.5, h: 0.65,
    fontSize: 36, color: C.gold, fontFace: FONT_SERIF, bold: true, charSpacing: 8,
  });

  var feats = [
    { icon: "❄️", title: "凉爽透气",   desc: "真丝天然透气，穿着凉爽宜人，\n尤适春夏，贴肤不沾身" },
    { icon: "💧", title: "防水易护理", desc: "天然涂层具有防水性，\n易洗快干，护理简单" },
    { icon: "✨", title: "越穿越柔",   desc: "随穿着次数增多愈发柔软亲肤，\n是会成长的面料" },
    { icon: "🍃", title: "纯天然环保", desc: "全程植物染料与天然河泥，\n可持续时尚的典范" },
    { icon: "🎨", title: "独一无二",   desc: "每匹受天气影响，色泽细节不同，\n世界上没有两匹完全相同" },
    { icon: "👑", title: "低调奢华",   desc: "宋庆龄、张爱玲钟爱的面料，\n东方贵族气质的象征" },
  ];

  feats.forEach(function(f, i) {
    var col = i % 3;
    var row = Math.floor(i / 3);
    var x = 0.4 + col * 4.33;
    var y = 2.3 + row * 2.55;
    s.addShape(pptx.ShapeType.rect, {
      x: x, y: y, w: 4.1, h: 2.3,
      fill: { color: C.darkMid, transparency: 10 },
      line: { color: C.gold, width: 0.6, transparency: 65 },
    });
    s.addText(f.icon, { x: x + 0.2, y: y + 0.25, w: 0.7, h: 0.7, fontSize: 28 });
    s.addText(f.title, {
      x: x + 0.95, y: y + 0.3, w: 3.0, h: 0.5,
      fontSize: 17, color: C.goldLight, fontFace: FONT_SERIF, bold: true,
    });
    s.addText(f.desc, {
      x: x + 0.2, y: y + 0.95, w: 3.7, h: 1.1,
      fontSize: 11.5, color: C.cream, fontFace: FONT_SANS, lineSpacingMultiple: 1.85,
    });
  });
}());

// ══════════════════════════════════════════════
// SLIDE 6 — 产品系列
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.darkMid, C.black, 160);

  addLabel(s, "产品系列", 0.5, 0.4);
  s.addText("今遇莨缘", {
    x: 0.5, y: 0.75, w: 5, h: 0.75,
    fontSize: 40, color: C.cream, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("系列臻品", {
    x: 0.5, y: 1.45, w: 3.2, h: 0.6,
    fontSize: 32, color: C.gold, fontFace: FONT_SERIF, bold: true,
  });

  var cats = [
    { icon: "👗", name: "旗袍 · 礼服" },
    { icon: "🧥", name: "日常服饰" },
    { icon: "👜", name: "配饰精品" },
    { icon: "🎁", name: "面料礼盒" },
  ];
  cats.forEach(function(c, i) {
    var y = 2.25 + i * 1.25;
    s.addShape(pptx.ShapeType.rect, {
      x: 0.5, y: y, w: 2.8, h: 1.1,
      fill: { color: i === 0 ? C.gold : C.darkMid, transparency: i === 0 ? 75 : 15 },
      line: { color: C.gold, width: 0.8, transparency: i === 0 ? 30 : 60 },
    });
    s.addText(c.icon + "  " + c.name, {
      x: 0.65, y: y + 0.3, w: 2.55, h: 0.5,
      fontSize: 14, color: i === 0 ? C.goldLight : C.muted,
      fontFace: FONT_SERIF, bold: i === 0,
    });
  });

  if (fs.existsSync(IMG_PRODUCTS)) {
    s.addImage({ path: IMG_PRODUCTS, x: 3.6, y: 0.3, w: 5.5, h: 6.9 });
  }

  s.addText("旗袍 · 礼服系列", {
    x: 9.4, y: 1.2, w: 3.9, h: 0.6,
    fontSize: 22, color: C.goldLight, fontFace: FONT_SERIF, bold: true,
  });
  s.addText(
    "以香云纱为魂，融合传统旗袍剪裁与现代审美，打造兼具东方神韵与时代气息的礼服精品。乌亮的面料映衬肤色，是重要场合最优雅的选择。",
    {
      x: 9.4, y: 1.95, w: 3.9, h: 1.6,
      fontSize: 12.5, color: C.cream, fontFace: FONT_SERIF, lineSpacingMultiple: 1.9,
    }
  );
  ["定制版型 · 量体裁衣", "手工盘扣 · 传统工艺", "可搭配刺绣 · 个性定制"].forEach(function(f, i) {
    s.addText("◆  " + f, {
      x: 9.4, y: 3.7 + i * 0.55, w: 3.9, h: 0.45,
      fontSize: 12, color: C.gold, fontFace: FONT_SANS,
    });
  });
}());

// ══════════════════════════════════════════════
// SLIDE 7 — 品牌理念
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.dark, C.black, 135);

  addLabel(s, "品牌理念", 0.5, 0.4, C.gold);
  s.addText("我们相信的", {
    x: 0.5, y: 0.75, w: 5, h: 0.75,
    fontSize: 38, color: C.white, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("价 值", {
    x: 0.5, y: 1.45, w: 2.5, h: 0.65,
    fontSize: 36, color: C.gold, fontFace: FONT_SERIF, bold: true, charSpacing: 8,
  });

  var vals = [
    { num: "一", title: "传承之美", desc: "500年岭南匠心，每一道工序都是对时间的致敬。我们守护非遗，让古老技艺在当代延续，让中华文化的精华永久流传。" },
    { num: "二", title: "自然之道", desc: "薯莨为染，日晒为媒，河泥为色。顺应自然、返璞归真，这是香云纱给予我们的人生哲学。" },
    { num: "三", title: "创新之韵", desc: "以传统面料为媒介，融合现代设计语言，让香云纱走上国际舞台，成为东方可持续时尚的旗帜。" },
    { num: "四", title: "缘分之道", desc: "每一位今遇莨缘的顾客，都是与这段岭南千年文化的有缘相遇。我们珍视每一次相遇，每一段缘分。" },
  ];
  vals.forEach(function(v, i) {
    var col = i % 2;
    var row = Math.floor(i / 2);
    var x = 0.4 + col * 6.6;
    var y = 2.3 + row * 2.55;
    s.addShape(pptx.ShapeType.rect, {
      x: x, y: y, w: 6.3, h: 2.3,
      fill: { color: C.dark, transparency: 15 },
      line: { color: C.gold, width: 0.7, transparency: 65 },
    });
    s.addText(v.num, {
      x: x + 0.2, y: y + 0.2, w: 0.8, h: 1.0,
      fontSize: 48, color: C.gold, fontFace: "楷体",
    });
    s.addText(v.title, {
      x: x + 1.2, y: y + 0.3, w: 4.8, h: 0.5,
      fontSize: 20, color: C.goldLight, fontFace: FONT_SERIF, bold: true,
    });
    s.addText(v.desc, {
      x: x + 0.2, y: y + 0.95, w: 5.9, h: 1.15,
      fontSize: 12, color: C.cream, fontFace: FONT_SERIF, lineSpacingMultiple: 1.8,
    });
  });
}());

// ══════════════════════════════════════════════
// SLIDE 8 — 结语
// ══════════════════════════════════════════════
(function() {
  var s = pptx.addSlide();
  addBg(s, C.dark, C.brownDark, 160);

  s.addShape(pptx.ShapeType.ellipse, {
    x: 3.0, y: 0.2, w: 7.5, h: 7.5,
    fill: { color: C.brownDark, transparency: 80 },
    line: { color: C.gold, transparency: 80, width: 0.5 },
  });
  s.addShape(pptx.ShapeType.ellipse, {
    x: 3.8, y: 1.0, w: 5.9, h: 5.9,
    fill: { color: "FFFFFF", transparency: 100 },
    line: { color: C.gold, transparency: 85, width: 0.3 },
  });

  s.addShape(pptx.ShapeType.ellipse, {
    x: 5.85, y: 0.5, w: 1.8, h: 1.8,
    fill: { color: C.brownDark, transparency: 40 },
    line: { color: C.gold, width: 1, transparency: 40 },
  });
  s.addText("缘", {
    x: 5.85, y: 0.62, w: 1.8, h: 1.5,
    align: "center", fontSize: 36, color: C.gold, fontFace: "楷体",
  });

  s.addText("有缘今日遇", {
    x: 0, y: 2.55, w: "100%", h: 0.85,
    align: "center", fontSize: 46, color: C.cream, fontFace: FONT_SERIF, bold: true,
  });
  s.addText("莨缘一世情", {
    x: 0, y: 3.35, w: "100%", h: 0.85,
    align: "center", fontSize: 44, color: C.gold, fontFace: FONT_SERIF, bold: true,
  });

  addLine(s, 3.5, 4.35, 6.5);
  s.addShape(pptx.ShapeType.diamond, {
    x: 6.8, y: 4.2, w: 0.18, h: 0.18,
    fill: { color: C.gold }, line: { color: C.gold, width: 0.5 },
  });

  s.addText(
    "每一匹香云纱，都是岭南大地与时间的共同馈赠\n每一次穿着，都是与五百年历史的深情相遇",
    {
      x: 1, y: 4.55, w: 11.5, h: 1.0,
      align: "center", fontSize: 14, color: C.goldLight,
      fontFace: FONT_SERIF, lineSpacingMultiple: 1.9,
    }
  );

  s.addShape(pptx.ShapeType.rect, {
    x: 1.5, y: 5.75, w: 10.5, h: 0.7,
    fill: { color: C.gold, transparency: 88 },
    line: { color: C.gold, width: 0.6, transparency: 55 },
  });
  s.addText("广东 · 岭南    |    今遇莨缘香云纱    |    非遗 · 定制 · 传承", {
    x: 1.5, y: 5.82, w: 10.5, h: 0.55,
    align: "center", fontSize: 12, color: C.muted, fontFace: FONT_SANS, charSpacing: 2,
  });

  s.addText("今遇莨缘  ·  香云纱  ·  天地共染，岁月为韵", {
    x: 0, y: 6.65, w: "100%", h: 0.45,
    align: "center", fontSize: 12, color: C.gold,
    fontFace: FONT_SERIF, charSpacing: 4,
  });
}());

// ══════════════════════════════════════════════
// 输出 PPTX
// ══════════════════════════════════════════════
var OUTPUT = path.join(__dirname, "今遇莨缘_香云纱品牌宣传.pptx");
pptx.writeFile({ fileName: OUTPUT })
  .then(function() { console.log("✅ PPTX 已生成：" + OUTPUT); })
  .catch(function(e) { console.error("❌ 生成失败：", e); process.exit(1); });
