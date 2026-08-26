/**
 * screenshot_slides.js
 * 用 Puppeteer 截取网页PPT每一张幻灯片，然后打包成 PPTX
 */

const puppeteer = require("puppeteer");
const PptxGenJS = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

const HTML_PATH = path.join(__dirname, "index.html");
const SLIDES_DIR = path.join(__dirname, "slide_screenshots");
const OUTPUT_PPTX = path.join(__dirname, "今遇莨缘_香云纱品牌宣传.pptx");
const TOTAL_SLIDES = 8;

// 幻灯片尺寸 (16:9, 1920x1080)
const WIDTH  = 1920;
const HEIGHT = 1080;

async function main() {
  // 创建截图目录
  if (!fs.existsSync(SLIDES_DIR)) fs.mkdirSync(SLIDES_DIR);

  console.log("🚀 启动浏览器...");
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      "--no-sandbox",
      "--disable-setuid-sandbox",
      "--disable-web-security",
      "--allow-file-access-from-files",
      "--font-render-hinting=none",
    ],
  });

  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1.5 });

  const fileUrl = "file:///" + HTML_PATH.replace(/\\/g, "/");
  console.log("📂 加载页面：" + fileUrl);
  await page.goto(fileUrl, { waitUntil: "networkidle0", timeout: 30000 });

  // 等待字体和动画加载完成
  await new Promise(r => setTimeout(r, 2000));

  const screenshots = [];

  for (let i = 1; i <= TOTAL_SLIDES; i++) {
    console.log(`📸 截图第 ${i}/${TOTAL_SLIDES} 页...`);

    // 通过 JS 跳转到指定幻灯片
    await page.evaluate((slideNum) => {
      if (typeof goToSlide === "function") {
        goToSlide(slideNum);
      }
    }, i);

    // 等待过渡动画完成
    await new Promise(r => setTimeout(r, 900));

    const imgPath = path.join(SLIDES_DIR, `slide_${String(i).padStart(2, "0")}.png`);
    await page.screenshot({ path: imgPath, type: "png" });
    screenshots.push(imgPath);
    console.log(`   ✅ 已保存：${imgPath}`);
  }

  await browser.close();
  console.log("\n🎨 所有截图完成，开始生成 PPTX...");

  // ── 生成 PPTX ────────────────────────────────
  const pptx = new PptxGenJS();
  pptx.layout = "LAYOUT_WIDE"; // 33.87cm x 19.05cm
  pptx.title = "今遇莨缘 · 香云纱品牌宣传";
  pptx.subject = "岭南非遗 · 东方软黄金";
  pptx.author = "今遇莨缘";

  const slideNames = [
    "封面", "品牌故事", "认识香云纱", "匠心工艺",
    "面料特性", "产品系列", "品牌理念", "结语",
  ];

  // 过渡动画类型列表（交替使用让整体更有层次感）
  const transitions = [
    { type: "fade",  dur: 1200 },  // 封面
    { type: "fade",  dur: 1000 },  // 品牌故事
    { type: "fade",  dur: 1000 },  // 认识香云纱
    { type: "fade",  dur: 1000 },  // 匠心工艺
    { type: "fade",  dur: 1000 },  // 面料特性
    { type: "fade",  dur: 1000 },  // 产品系列
    { type: "fade",  dur: 1000 },  // 品牌理念
    { type: "fade",  dur: 1400 },  // 结语（稍慢，营造回味感）
  ];

  for (let i = 0; i < screenshots.length; i++) {
    const slide = pptx.addSlide();

    // 全屏铺满截图（完美还原网页效果）
    slide.addImage({
      path: screenshots[i],
      x: 0, y: 0,
      w: "100%", h: "100%",
    });

    // 设置淡入淡出过渡动画
    slide.transition = transitions[i] || { type: "fade", dur: 1000 };

    console.log(`   📄 幻灯片 ${i + 1}：${slideNames[i]}（过渡：${transitions[i].type}）`);
  }

  await pptx.writeFile({ fileName: OUTPUT_PPTX });
  console.log("\n✅ PPTX 已生成：" + OUTPUT_PPTX);
  console.log("📊 共 " + screenshots.length + " 张幻灯片");
}

main().catch(e => {
  console.error("❌ 错误：", e);
  process.exit(1);
});
