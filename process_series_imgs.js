const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const outDir = 'd:/jinyuliangyuan/assets/series';
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const seriesConfig = [
  {
    key: 'xishangmeishao',
    name: '喜上眉梢 · 香云纱斜襟套装',
    images: ['喜上眉梢｜香云纱斜襟套装1.jpg', '喜上眉梢｜香云纱斜襟套装2.jpg', '喜上眉梢｜香云纱斜襟套装3.jpg', '喜上眉梢｜香云纱斜襟套装4.jpg']
  },
  {
    key: 'moranhuajing',
    name: '墨染花境 · 香云纱改良旗袍',
    images: ['墨染花境 · 香云纱改良旗袍1.jpg', '墨染花境 · 香云纱改良旗袍2.jpg', '墨染花境 · 香云纱改良旗袍3.jpg', '墨染花境 · 香云纱改良旗袍4.jpg']
  },
  {
    key: 'zhuohuamudan',
    name: '灼华牡丹 · 香云纱重工马甲',
    images: ['灼华牡丹｜香云纱重工马甲1.jpg', '灼华牡丹｜香云纱重工马甲2.jpg', '灼华牡丹｜香云纱重工马甲3.jpg', '灼华牡丹｜香云纱重工马甲4.jpg']
  },
  {
    key: 'jintingfeitang',
    name: '金庭绯棠 · 香云纱西装马甲套装',
    images: ['金庭绯棠｜香云纱西装马甲套装1.jpg', '金庭绯棠｜香云纱西装马甲套装2.jpg', '金庭绯棠｜香云纱西装马甲套装3.jpg', '金庭绯棠｜香云纱西装马甲套装4.jpg']
  }
];

const imgDir = 'd:/jinyuliangyuan/官网素材/模特上身图';

async function processImages() {
  for (let s of seriesConfig) {
    console.log('Processing without distortion:', s.name);
    let idx = 1;
    for (let imgName of s.images) {
      const srcPath = path.join(imgDir, imgName);
      if (fs.existsSync(srcPath)) {
        const destFileName = `${s.key}_${idx}.jpg`;
        const destPath = path.join(outDir, destFileName);
        
        // Preserve aspect ratio: resize to max 1400px width/height without cropping or distorting
        await sharp(srcPath)
          .resize(1400, 1400, { fit: 'inside', withoutEnlargement: true })
          .jpeg({ quality: 88 })
          .toFile(destPath);
          
        const stat = fs.statSync(destPath);
        console.log(` -> ${destFileName} (${Math.round(stat.size/1024)}KB)`);
        idx++;
      } else {
        console.log(` WARN: ${srcPath} not found!`);
      }
    }
  }
}

processImages().catch(console.error);
