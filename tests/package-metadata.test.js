import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const rootDir = path.resolve(__dirname, '..');

test('package metadata exposes the irum-imagen commands and repository', async () => {
  const packageJson = JSON.parse(
    await fs.readFile(path.join(rootDir, 'package.json'), 'utf8')
  );
  const version = (await fs.readFile(path.join(rootDir, 'VERSION'), 'utf8')).trim();

  assert.equal(packageJson.name, 'irum-imagen');
  assert.equal(packageJson.version, version);
  assert.equal(packageJson.bin['irum-imagen'], './src/cli/generate.js');
  assert.equal(packageJson.bin.iim, './src/cli/generate.js');
  assert.equal(
    packageJson.repository.url,
    'https://github.com/IrumHahn/irum-imagen.git'
  );
  assert.ok(packageJson.files.includes('skills/irum-imagen/'));
  assert.ok(packageJson.files.includes('NOTICE.md'));
});
