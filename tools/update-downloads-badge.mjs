import fs from 'node:fs/promises';

const owner = 'NocCorporation';
const repo = 'NocLauncher';

const headers = {
  'User-Agent': 'noclauncher-badge-updater',
  'Accept': 'application/vnd.github+json'
};

async function fetchJson(url) {
  const r = await fetch(url, { headers });
  if (!r.ok) throw new Error(`HTTP ${r.status} for ${url}`);
  return r.json();
}

const release = await fetchJson(`https://api.github.com/repos/${owner}/${repo}/releases/latest`);
const assets = Array.isArray(release.assets) ? release.assets : [];
const total = assets.reduce((s, a) => s + Number(a.download_count || 0), 0);

const badge = {
  schemaVersion: 1,
  label: 'downloads all',
  message: String(total),
  color: '0e9f6e',
  namedLogo: 'github'
};

await fs.mkdir('docs/badges', { recursive: true });
await fs.writeFile('docs/badges/downloads-total.json', JSON.stringify(badge, null, 2) + '\n', 'utf8');

console.log(`Updated downloads-total badge: ${total}`);
