/**
 * make_pptx_only.js
 * 直接用已有截图生成带过渡动画的 PPTX（无需重新截图）
 */

const PptxGenJS = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

const SLIDES_DIR  = path.join(__dirname, "slide_screenshots");
const OUTPUT_PPTX = path.join(__dirname, "今遇莨缘_香云纱品牌宣传.pptx");
const TOTAL_SLIDES = 8;

const slideNames = [
  "封面", "品牌故事", "认识香云纱", "匠心工艺",
  "面料特性", "产品系列", "品牌理念", "结语",
];

// fade 过渡：最优雅，适合高端品牌
const transitions = [
  { type: "fade", dur: 1200 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1000 },
  { type: "fade", dur: 1400 },
];

async function main() {
  const pptx = new PptxGenJS();
  pptx.layout  = "LAYOUT_WIDE";
  pptx.title   = "今遇莨缘 · 香云纱品牌宣传";
  pptx.subject = "岭南非遗 · 东方软黄金";
  pptx.author  = "今遇莨缘";

  console.log("🎨 生成带过渡动画的 PPTX...\n");

  for (let i = 1; i <= TOTAL_SLIDES; i++) {
    const imgPath = path.join(SLIDES_DIR, `slide_${String(i).padStart(2, "0")}.png`);
    if (!fs.existsSync(imgPath)) {
      console.error(`❌ 找不到截图：${imgPath}`);
      process.exit(1);
    }

    const slide = pptx.addSlide();

    // 全屏截图
    slide.addImage({ path: imgPath, x: 0, y: 0, w: "100%", h: "100%" });

    // 淡入淡出过渡动画
    slide.transition = transitions[i - 1];

    console.log(`   ✅ 幻灯片 ${i}：${slideNames[i - 1]}  → fade ${transitions[i - 1].dur}ms`);
  }

  await pptx.writeFile({ fileName: OUTPUT_PPTX });
  console.log("\n✅ PPTX 已生成：" + OUTPUT_PPTX);
}

main().catch(e => { console.error("❌", e); process.exit(1); });
