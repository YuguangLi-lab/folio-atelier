"""Verify the published theme payload and its offline validation records."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[1]
checks = json.loads((root / 'SHA256SUMS.json').read_text())
for name, expected in checks.items():
    file = (root / name).resolve()
    assert file.is_relative_to(root), name
    assert hashlib.sha256(file.read_bytes()).hexdigest() == expected, name
manifest = json.loads((root / 'manifest.json').read_text())
versions = json.loads((root / 'versions.json').read_text())
assert versions[manifest['version']] == manifest['minAppVersion']
summary = json.loads((root / 'validation/summary.json').read_text())
assert summary['pass'] and summary['version'] == manifest['version']
assert summary['themeSHA256'] == checks['theme.css']
print(f"Verified {len(checks)} distribution files for Folio Atelier {manifest['version']}")
