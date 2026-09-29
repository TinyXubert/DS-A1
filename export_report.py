"""Export the saved, executed notebook with code and outputs; never execute it."""
from pathlib import Path
import os
BASE = Path(__file__).resolve().parent
for name in ['tmp', 'jupyter', 'ipython']:
    (BASE / '.runtime' / name).mkdir(parents=True, exist_ok=True)
os.environ['TMPDIR'] = str(BASE / '.runtime/tmp')
os.environ['JUPYTER_CONFIG_DIR'] = str(BASE / '.runtime/jupyter')
os.environ['IPYTHONDIR'] = str(BASE / '.runtime/ipython')
import nbformat
from nbconvert import HTMLExporter
nb = nbformat.read(BASE / 'A1.ipynb', as_version=4)
nbformat.validate(nb)
code = [c for c in nb.cells if c.cell_type == 'code']
if any(c.execution_count is None for c in code):
    raise SystemExit(f'Not exported: run all {len(code)} code cells and SAVE A1.ipynb first.')
if any(o.output_type == 'error' for c in code for o in c.outputs):
    raise SystemExit('Not exported: notebook contains execution errors. Preserve a failed-run copy, fix, rerun, and save.')
if [c.execution_count for c in code] != sorted(set(c.execution_count for c in code)):
    raise SystemExit('Not exported: execution order is inconsistent. Preserve current notebook, restart kernel, run top to bottom and save.')
exporter = HTMLExporter(template_name='lab')
exporter.exclude_input = False
exporter.exclude_output = False
body, _ = exporter.from_notebook_node(nb)
style = '''<style>
@media print {
 @page {size: A4; margin: 13mm;}
 body {font-size: 10pt;}
 pre, code, .highlight pre {white-space: pre-wrap !important; overflow-wrap: anywhere !important;}
 .jp-OutputArea-output, .jp-RenderedHTMLCommon, .jp-OutputArea-child,
 .jp-CodeCell, .jp-Cell-outputWrapper {overflow: visible !important; max-height: none !important;}
 table {font-size: 8pt; width: 100%; table-layout: auto;}
 td, th {white-space: normal !important; overflow-wrap: anywhere;}
 img, svg {max-width: 100% !important; height: auto;}
 h1, h2, h3 {break-after: avoid;}
}
</style>'''
body = body.replace('</head>', style + '\n</head>')
path = BASE / 'A1.html'
path.write_text(body, encoding='utf-8')
print('Exported with code and saved outputs:', path)
print('Open/download HTML in your local browser, Ctrl+P -> Save as PDF -> A1.pdf.')
print('Check tables, figures, code wrapping and student reflection before submitting.')
