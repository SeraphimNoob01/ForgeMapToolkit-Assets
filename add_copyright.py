#!/usr/bin/env python3
"""
add_copyright.py
----------------
Prepends a copyright/license comment block to all .scmskybox files
in a folder (recursive).

Usage:
  python add_copyright.py <folder> [--dry-run]

Options:
  --dry-run   Show which files would be modified without changing them.
"""

import os
import sys
import json
import argparse
from datetime import date

COPYRIGHT_BLOCK = """\
/*
 * ============================================================
 *  ForgeMapToolkit Assets — Skybox Preset
 *  Copyright (c) {year} Seraphim-Noob
 * ============================================================
 *
 *  LICENSE: Creative Commons Attribution-NonCommercial 4.0
 *           International (CC BY-NC 4.0)
 *
 *  You are free to:
 *    - Share  — copy and redistribute this file in any medium
 *    - Adapt  — remix, transform, and build upon this material
 *
 *  Under the following terms:
 *    - Attribution   — You must give appropriate credit to
 *                      Seraphim-Noob and indicate if changes
 *                      were made. You may do so in any
 *                      reasonable manner.
 *    - NonCommercial — You may not use this material for
 *                      commercial purposes.
 *    - No additional restrictions — You may not apply legal
 *                      terms or technological measures that
 *                      legally restrict others from doing
 *                      anything the license permits.
 *
 *  This copyright block must remain intact in all copies
 *  and derivative works.
 *
 *  Full license text: https://creativecommons.org/licenses/by-nc/4.0/
 *  Repository:        https://github.com/SeraphimNoob01/ForgeMapToolkit-Assets
 * ============================================================
 */
""".format(year=date.today().year)

MARKER = "ForgeMapToolkit Assets — Skybox Preset"


def process_file(filepath: str, dry_run: bool) -> str:
    """Returns 'skipped', 'added', or 'already'."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Already has the block?
    if MARKER in content:
        return 'already'

    if dry_run:
        return 'added (dry-run)'

    new_content = COPYRIGHT_BLOCK + content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return 'added'


def main():
    parser = argparse.ArgumentParser(
        description='Prepend copyright block to .scmskybox files.'
    )
    parser.add_argument('folder', help='Root folder to search recursively')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without modifying files')
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"[!] Not a valid folder: {args.folder}")
        sys.exit(1)

    counts = {'added': 0, 'already': 0, 'error': 0}

    for root, _, files in os.walk(args.folder):
        for fname in files:
            if not fname.lower().endswith('.scmskybox'):
                continue
            filepath = os.path.join(root, fname)
            try:
                result = process_file(filepath, args.dry_run)
                rel = os.path.relpath(filepath, args.folder)
                if 'added' in result:
                    print(f"[+] {rel}")
                    counts['added'] += 1
                else:
                    print(f"[~] {rel}  (already has copyright)")
                    counts['already'] += 1
            except Exception as e:
                print(f"[!] ERROR {filepath}: {e}")
                counts['error'] += 1

    print()
    print(f"Done — {counts['added']} files updated, "
          f"{counts['already']} already had copyright, "
          f"{counts['error']} errors.")
    if args.dry_run:
        print("(dry-run — no files were actually modified)")


if __name__ == '__main__':
    main()
