#!/usr/bin/env python3
"""Map changed site Markdown paths to their upstream manifest names."""
import csv
import sys
from pathlib import Path


def main():
    mapping = {}
    with Path(sys.argv[1]).open(encoding='utf-8', newline='') as manifest:
        for row in csv.reader((line for line in manifest if not line.startswith('#') and line.strip()), delimiter='\t'):
            if len(row) != 3 or not row[0] or not row[1] or row[1] in mapping:
                raise ValueError('Invalid or duplicate manifest mapping')
            mapping[row[1]] = row[0]
    guides = set()
    for line in sys.stdin:
        path = line.rstrip('\n')
        if path.startswith('docs/') and path.endswith('.md'):
            site = path.removeprefix('docs/')
            if site not in mapping:
                raise ValueError(f'No manifest mapping for {path}')
            guides.add(mapping[site])
    print('\n'.join(sorted(guides)))


if __name__ == '__main__':
    main()
