/**
 * gen_favorite_style_pptx.js
 * 渲染 ppt_favorite_style.html 并截图转换为 PPTX
 * 输出至 d:\jinyuliangyuan\宣传用PPT\今遇莨缘_香云纱品牌宣传_经典画风版.pptx
 */

const puppeteer = require("puppeteer");
const PptxGenJS = require("pptxgenjs");
const path = require("path");
const fs = require("fs");

const HTML_PATH = path.join(__dirname, "ppt_favorite_style.html");
const SLIDES_DIR = path.join(__dirname, "favorite_screenshots");
const OUTPUT_DIR = path.join(__dirname, "宣传用PPT");
const OUTPUT_PPTX = path.join(OUTPUT_DIR, "今遇莨缘_香云纱品牌宣传_经典画风版.pptx");
const TOTAL_SLIDES = 13;

async function main() {
  if (!fs.existsSync(SLIDES_DIR)) fs.mkdirSync(SLIDES_DIR, { recursive: true });
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  console.log("🚀 启动浏览器渲染经典画风 PPT HTML...");
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
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2.0 });

  const fileUrl = "file:///" + HTML_PATH.replace(/\\/g, "/");
  console.log("📂 正在打开：" + fileUrl);
  await page.goto(fileUrl, { waitUntil: "networkidle0", timeout: 30000 });
  await new Promise(r => setTimeout(r, 2000));

  const screenshots = [];

  for (let i = 1; i <= TOTAL_SLIDES; i++) {
    console.log(`📸 截图第 ${i}/${TOTAL_SLIDES} 页...`);

    await page.evaluate((n) => {
      if (typeof goToSlide === "function") goToSlide(n);
    }, i);

    await new Promise(r => setTimeout(r, 800));

    const imgPath = path.join(SLIDES_DIR, `slide_${String(i).padStart(2, "0")}.png`);
    await page.screenshot({ path: imgPath, type: "png" });
    screenshots.push(imgPath);
    console.log(`   ✅ 截图成功：${imgPath}`);
  }

  await browser.close();

  console.log("\n🎨 正在打包并生成 PPTX 文件...");
  const pptx = new PptxGenJS();
  pptx.layout = "LAYOUT_WIDE";
  pptx.title = "今遇莨缘 · 香云纱品牌宣传 (经典美学画风版)";
  pptx.author = "今遇莨缘";

  for (let i = 0; i < screenshots.length; i++) {
    const slide = pptx.addSlide();
    slide.addImage({
      path: screenshots[i],
      x: 0, y: 0,
      w: "100%", h: "100%",
    });

    // 渐变过渡
    const isSpecial = (i === 0 || i === 4 || i === 11);
    slide.transition = { type: "fade", dur: isSpecial ? 1200 : 900 };
  }

  await pptx.writeFile({ fileName: OUTPUT_PPTX });
  console.log("\n🎉 成功生成 PPTX 文件：");
  console.log("   👉 " + OUTPUT_PPTX);
}

main().catch((err) => {
  console.error("❌ 生成失败：", err);
  process.exit(1);
});
