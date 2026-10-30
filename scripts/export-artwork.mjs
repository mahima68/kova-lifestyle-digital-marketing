import fs from 'node:fs/promises';
import path from 'node:path';
const sharp=(await import(process.env.KOVA_SHARP_MODULE || 'sharp')).default;
const files=(await fs.readdir('dist/creatives')).filter(f=>f.endsWith('.svg'));
for(const file of files){await sharp(path.join('dist/creatives',file)).png().toFile(path.join('dist/creatives',file.replace('.svg','.png')));}
console.log(`Exported ${files.length} original vector designs as PNGs.`);
