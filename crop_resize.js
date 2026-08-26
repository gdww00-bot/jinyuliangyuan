const sharp = require('sharp');

const inputPath = 'C:\\Users\\Administrator\\.gemini\\antigravity\\brain\\5bf79cfa-1f60-47b8-b019-34b2ad265365\\media__1782958067107.jpg';
const outputDir = 'C:\\Users\\Administrator\\.gemini\\antigravity\\brain\\5bf79cfa-1f60-47b8-b019-34b2ad265365\\';

// Original: 1024 x 419, Target: 600 x 450
// 
// The challenge: original is very wide (2.44:1) but target is taller (1.33:1)
// 
// Best approach: use generate_image style approach - 
// crop the width to keep important content, resize to 600 wide, 
// pad top/bottom symmetrically with content-aware background

async function generateVersions() {
  const image = sharp(inputPath);
  const metadata = await image.metadata();
  console.log('Original:', metadata.width, 'x', metadata.height);

  // Version A: Crop to ~720px wide (text + hamper + partial washer), 
  // resize to 600 wide, pad top/bottom
  const cropW_A = 720;
  const resizedW = 600;
  const resizedH_A = Math.round(metadata.height * (resizedW / cropW_A)); // ~349
  const padTotal = 450 - resizedH_A; // ~101
  const padTop = Math.round(padTotal * 0.3); // Less pad on top, more on bottom
  const padBottom = padTotal - padTop;

  const croppedBuf_A = await sharp(inputPath)
    .extract({ left: 0, top: 0, width: cropW_A, height: metadata.height })
    .resize(resizedW, resizedH_A)
    .toBuffer();

  // Get colors from top and bottom edges for padding
  const { data: rawA, info: infoA } = await sharp(croppedBuf_A)
    .raw()
    .toBuffer({ resolveWithObject: true });

  // Sample top-center pixel for top background
  const topIdx = (2 * infoA.width + Math.round(resizedW * 0.7)) * infoA.channels;
  const topR = rawA[topIdx], topG = rawA[topIdx+1], topB = rawA[topIdx+2];

  // Sample bottom-center pixel for bottom background
  const botIdx = ((resizedH_A - 2) * infoA.width + Math.round(resizedW * 0.5)) * infoA.channels;
  const botR = rawA[botIdx], botG = rawA[botIdx+1], botB = rawA[botIdx+2];

  console.log('Top BG:', topR, topG, topB, '| Bottom BG:', botR, botG, botB);

  // Create top padding strip
  const topPadBuf = await sharp({
    create: { width: resizedW, height: padTop, channels: 3, background: { r: topR, g: topG, b: topB } }
  }).png().toBuffer();

  // Create bottom padding strip with gradient from bottom edge color
  const botGradBuf = Buffer.alloc(resizedW * padBottom * 3);
  for (let x = 0; x < resizedW; x++) {
    const bIdx = ((resizedH_A - 1) * infoA.width + x) * infoA.channels;
    const pr = rawA[bIdx], pg = rawA[bIdx+1], pb = rawA[bIdx+2];
    for (let y = 0; y < padBottom; y++) {
      const i = (y * resizedW + x) * 3;
      botGradBuf[i] = pr;
      botGradBuf[i+1] = pg;
      botGradBuf[i+2] = pb;
    }
  }
  const botPadBuf = await sharp(botGradBuf, {
    raw: { width: resizedW, height: padBottom, channels: 3 }
  }).png().toBuffer();

  await sharp({
    create: { width: 600, height: 450, channels: 3, background: { r: topR, g: topG, b: topB } }
  })
    .composite([
      { input: topPadBuf, top: 0, left: 0 },
      { input: croppedBuf_A, top: padTop, left: 0 },
      { input: botPadBuf, top: padTop + resizedH_A, left: 0 }
    ])
    .jpeg({ quality: 95 })
    .toFile(outputDir + 'hamper_v_A.jpg');

  console.log('Version A saved (720px crop + padded)');

  // Version B: Wider crop ~780px to show more washer
  const cropW_B = 780;
  const resizedH_B = Math.round(metadata.height * (resizedW / cropW_B)); // ~322
  const padTotal_B = 450 - resizedH_B;
  const padTop_B = Math.round(padTotal_B * 0.3);
  const padBottom_B = padTotal_B - padTop_B;

  const croppedBuf_B = await sharp(inputPath)
    .extract({ left: 0, top: 0, width: cropW_B, height: metadata.height })
    .resize(resizedW, resizedH_B)
    .toBuffer();

  const { data: rawB, info: infoB } = await sharp(croppedBuf_B)
    .raw()
    .toBuffer({ resolveWithObject: true });

  const topIdx_B = (2 * infoB.width + Math.round(resizedW * 0.7)) * infoB.channels;
  const topR_B = rawB[topIdx_B], topG_B = rawB[topIdx_B+1], topB_B = rawB[topIdx_B+2];

  const topPadBuf_B = await sharp({
    create: { width: resizedW, height: padTop_B, channels: 3, background: { r: topR_B, g: topG_B, b: topB_B } }
  }).png().toBuffer();

  const botGradBuf_B = Buffer.alloc(resizedW * padBottom_B * 3);
  for (let x = 0; x < resizedW; x++) {
    const bIdx = ((resizedH_B - 1) * infoB.width + x) * infoB.channels;
    const pr = rawB[bIdx], pg = rawB[bIdx+1], pb = rawB[bIdx+2];
    for (let y = 0; y < padBottom_B; y++) {
      const i = (y * resizedW + x) * 3;
      botGradBuf_B[i] = pr;
      botGradBuf_B[i+1] = pg;
      botGradBuf_B[i+2] = pb;
    }
  }
  const botPadBuf_B = await sharp(botGradBuf_B, {
    raw: { width: resizedW, height: padBottom_B, channels: 3 }
  }).png().toBuffer();

  await sharp({
    create: { width: 600, height: 450, channels: 3, background: { r: topR_B, g: topG_B, b: topB_B } }
  })
    .composite([
      { input: topPadBuf_B, top: 0, left: 0 },
      { input: croppedBuf_B, top: padTop_B, left: 0 },
      { input: botPadBuf_B, top: padTop_B + resizedH_B, left: 0 }
    ])
    .jpeg({ quality: 95 })
    .toFile(outputDir + 'hamper_v_B.jpg');

  console.log('Version B saved (780px crop + padded)');

  // Version C: Use full height without any padding - 
  // Fill the canvas with a background, then scale image to fit width=600 
  // and vertically center
  const resizedH_C = Math.round(metadata.height * (resizedW / cropW_A));
  const croppedBuf_C = await sharp(inputPath)
    .extract({ left: 0, top: 0, width: cropW_A, height: metadata.height })
    .resize(resizedW, resizedH_C)
    .toBuffer();

  // Place vertically centered
  const centerTop = Math.round((450 - resizedH_C) / 2);

  // Use averaged background color
  const bgR_C = Math.round((topR + botR) / 2);
  const bgG_C = Math.round((topG + botG) / 2);
  const bgB_C = Math.round((topB + botB) / 2);

  await sharp({
    create: { width: 600, height: 450, channels: 3, background: { r: bgR_C, g: bgG_C, b: bgB_C } }
  })
    .composite([
      { input: croppedBuf_C, top: centerTop, left: 0 }
    ])
    .jpeg({ quality: 95 })
    .toFile(outputDir + 'hamper_v_C.jpg');

  console.log('Version C saved (centered, 720px crop)');
}

generateVersions().catch(console.error);
