const puppeteer = require('puppeteer');
const PptxGenJS = require('pptxgenjs');
const path = require('path');
const fs = require('fs');

const HTML_PATH = path.join(__dirname, 'ppt_perfect.html');
const SLIDES_DIR = path.join(__dirname, 'perfect_screenshots');
const OUTPUT_PPTX = path.join(__dirname, '宣传用PPT', '今遇莨缘香云纱_完美版.pptx');
const TOTAL_SLIDES = 12;

async function main() {
  if (!fs.existsSync(SLIDES_DIR)) fs.mkdirSync(SLIDES_DIR);
  if (!fs.existsSync(path.join(__dirname, '宣传用PPT'))) fs.mkdirSync(path.join(__dirname, '宣传用PPT'));
  
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox','--disable-setuid-sandbox','--disable-web-security','--allow-file-access-from-files','--font-render-hinting=none'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1.5 });
  const fileUrl = 'file:///' + HTML_PATH.replace(/\\/g, '/');
  await page.goto(fileUrl, { waitUntil: 'networkidle0', timeout: 30000 });
  await new Promise(r => setTimeout(r, 2500));
  const screenshots = [];
  for (let i = 1; i <= TOTAL_SLIDES; i++) {
    console.log('截图第 ' + i + '/' + TOTAL_SLIDES + ' 页...');
    await page.evaluate(function(n) { if(typeof goToSlide==='function') goToSlide(n); }, i);
    await new Promise(r => setTimeout(r, 1000));
    const imgPath = path.join(SLIDES_DIR, 'slide_' + String(i).padStart(2,'0') + '.png');
    await page.screenshot({ path: imgPath, type: 'png' });
    screenshots.push(imgPath);
    console.log('  已保存: ' + imgPath);
  }
  await browser.close();
  const pptx = new PptxGenJS();
  pptx.layout = 'LAYOUT_WIDE';
  pptx.title = '今遇莨缘香云纱品牌宣传';
  for (var i = 0; i < screenshots.length; i++) {
    var slide = pptx.addSlide();
    slide.addImage({ path: screenshots[i], x: 0, y: 0, w: '100%', h: '100%' });
    slide.transition = { type: 'fade', dur: i === 0 || i === screenshots.length-1 ? 1400 : 1000 };
    console.log('幻灯片 ' + (i+1) + ' 已添加');
  }
  await pptx.writeFile({ fileName: OUTPUT_PPTX });
  console.log('PPTX已生成: ' + OUTPUT_PPTX);
}
main().catch(function(e) { console.error(e); process.exit(1); });
