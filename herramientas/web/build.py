"""Genera una página HTML única con todo el contenido del plan de estudios.

Uso: python3 herramientas/web/build.py [repo] [salida.html]
Por defecto lee este repositorio y escribe herramientas/web/build/consultor-odoo-20.html.
Requiere markdown-it-py y mdit-py-plugins (ver README.md de esta carpeta).
"""
import csv, html, io, os, re, subprocess, sys, unicodedata
from urllib.parse import unquote

HERE = os.path.dirname(os.path.abspath(__file__))
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin

REPO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..'))
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'build', 'consultor-odoo-20.html')
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
GITHUB = 'https://github.com/olanoit/odoo-functional-consultant/blob/20.0/'

FASES = {
    1: 'Fundamentos', 2: 'Ventas y CRM', 3: 'Compras e Inventario', 4: 'Contabilidad y Finanzas',
    5: 'Manufactura y Calidad', 6: 'Servicios y Proyectos', 7: 'Recursos Humanos',
    8: 'Web, eCommerce y Marketing', 9: 'Productividad, Studio y Datos',
    10: 'Localización PE y Administración', 11: 'Metodología de implementación', 12: 'Capstone y certificación',
}


def git(*args):
    return subprocess.run(['git', '-C', REPO, *args], capture_output=True, text=True).stdout


FILES = [f for f in git('ls-files').split() if not f.startswith('herramientas/')]
MDS = sorted(f for f in FILES if f.endswith('.md'))
CSVS = sorted(f for f in FILES if f.endswith('.csv'))


def slug(text):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode().lower()
    t = re.sub(r'[^a-z0-9 _-]', '', t).strip()
    return re.sub(r'\s', '-', t) or 'seccion'


def docid(path):
    return path[:-3].replace('/', '--') if path.endswith('.md') else path.replace('/', '--')


INDEX_DIRS = {'fases': 'idx-fases', 'plantillas': 'idx-plantillas', 'ejemplos': 'idx-ejemplos', '': 'inicio', '.': 'inicio'}


def resolve(href, src):
    """Convierte un enlace relativo del repositorio en un token de hash de la página."""
    path, _, anchor = href.partition('#')
    anchor = unquote(anchor)
    if path:
        target = os.path.normpath(os.path.join(os.path.dirname(src), path))
        target = '' if target == '.' else target
        if target in INDEX_DIRS:
            did = INDEX_DIRS[target]
        elif target + '/README.md' in FILES:
            did = docid(target + '/README.md')
        elif target in FILES:
            did = docid(target)
        else:
            print('ENLACE SIN DESTINO', src, href, file=sys.stderr)
            return None
    else:
        did = docid(src)
    return '#' + did + ('~' + slug(anchor) if anchor else '')


def render_md(path):
    text = open(os.path.join(REPO, path), encoding='utf-8').read()
    did = docid(path)
    md = MarkdownIt('commonmark', {'html': False, 'linkify': False, 'typographer': False}).enable(['table', 'strikethrough'])
    seen = {}

    def hslug(s):
        base = did + '~' + slug(s)
        n = seen.get(base, 0)
        seen[base] = n + 1
        return base if n == 0 else f'{base}-{n}'

    anchors_plugin(md, min_level=1, max_level=6, slug_func=hslug, permalink=False)
    tokens = md.parse(text)

    def walk(toks):
        for t in toks:
            if t.type == 'link_open':
                href = t.attrGet('href') or ''
                if re.match(r'^(https?:|mailto:)', href):
                    t.attrSet('target', '_blank')
                    t.attrSet('rel', 'noopener')
                else:
                    new = resolve(href, path)
                    if new:
                        t.attrSet('href', new)
            if t.children:
                walk(t.children)

    walk(tokens)
    out = md.renderer.render(tokens, md.options, {})
    out = out.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    m = re.search(r'^#\s+(.+)$', text, re.M)
    title = re.sub(r'[`*]', '', m.group(1)).strip() if m else path
    return title, out


def render_csv(path):
    raw = open(os.path.join(REPO, path), encoding='utf-8').read()
    rows = list(csv.reader(io.StringIO(raw)))
    head, body = rows[0], rows[1:]
    th = ''.join(f'<th><code>{html.escape(c)}</code></th>' for c in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{html.escape(c)}</td>' for c in r) + '</tr>' for r in body)
    name = os.path.basename(path)
    intro = (f'<p class="csvmeta"><span>{len(body)} filas</span><span>{len(head)} columnas</span>'
             f'<span>UTF-8 · separador coma</span></p>'
             '<p>Archivo listo para importar en Odoo 20. Las columnas son los nombres técnicos de los campos; '
             'las que terminan en <code>/id</code> enlazan registros por su ID externo. '
             'Descárgalo desde el repositorio con el enlace de arriba.</p>')
    return name, f'<h1 id="{docid(path)}~top">{html.escape(name)}</h1>{intro}<div class="tbl csv"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


# ---------- estructura de navegación ----------
docs = {}       # id -> dict(title, html, path, group)
order = []      # orden lineal de lectura


def add_md(path, label=None, crumbs=()):
    title, body = render_md(path)
    did = docid(path)
    docs[did] = dict(title=title, label=label or title, html=body, path=path, crumbs=crumbs)
    order.append(did)
    return did


def add_csv(path, crumbs=()):
    title, body = render_csv(path)
    did = docid(path)
    docs[did] = dict(title=title, label=title, html=body, path=path, crumbs=crumbs)
    order.append(did)
    return did


def short(title):
    """'G2 — Laboratorio de listas de precios' -> ('G2', 'Laboratorio de listas de precios')."""
    m = re.match(r'^([A-Z]\d+)\s+—\s+(.*)$', title)
    if m:
        return m.group(1), m.group(2)
    return None, re.sub(r'^Soluciones\s+—\s+', '', title)


nav = []
nav.append(('Empezar', [('inicio', 'Portada', None)]))
start = []
for p, lab in [('README.md', 'Plan de estudios'), ('00-metodo-y-entorno.md', 'Método y entorno'),
               ('recursos.md', 'Recursos verificados'), ('seguimiento.md', 'Seguimiento')]:
    start.append((add_md(p, lab, ('Empezar',)), lab, None))
nav[0][1].extend(start)

phase_nav = []
for n in range(1, 13):
    ff = next(f for f in MDS if f.startswith(f'fases/fase-{n:02d}-'))
    crumbs = (f'Fase {n}',)
    items = [(add_md(ff, 'Guía de la fase', crumbs), 'Guía de la fase', None)]
    base = f'ejemplos/fase-{n:02d}/'
    items.append((add_md(base + 'README.md', 'Cuaderno de ejemplos', crumbs), 'Cuaderno de ejemplos', None))
    for sub, sublabel in [('guias', 'Guías'), ('casos', 'Casos'), ('simulacro', 'Simulacro'), ('soluciones', 'Soluciones')]:
        files = [f for f in MDS if f.startswith(base + sub + '/')]
        for f in files:
            title, _ = render_md(f)
            code, rest = short(title)
            label = (code + ' · ' + rest) if code else rest
            items.append((add_md(f, label, crumbs + (sublabel,)), label, sublabel))
    csvs = [f for f in CSVS if f.startswith(base)]
    for f in csvs:
        items.append((add_csv(f, crumbs + ('Datos',)), os.path.basename(f), 'Datos'))
    phase_nav.append((n, items))

plant = []
for f in MDS:
    if f.startswith('plantillas/'):
        title, _ = render_md(f)
        plant.append((add_md(f, title, ('Plantillas',)), title, None))

missing = [f for f in MDS if docid(f) not in docs] + [f for f in CSVS if docid(f) not in docs]
assert not missing, missing


# ---------- índices de carpetas ----------
def index_section(did, title, intro, entries):
    li = ''.join(f'<li><a href="#{e}">{html.escape(l)}</a></li>' for e, l in entries)
    docs[did] = dict(title=title, label=title, html=f'<h1 id="{did}~top">{title}</h1><p>{intro}</p><ul class="idx">{li}</ul>',
                     path=None, crumbs=())


index_section('idx-fases', 'Las 12 fases', 'Cada fase es autocontenida: qué estudiar, dónde, qué laboratorio hacer, cómo validar y cuándo avanzar.',
              [(items[0][0], f'Fase {n} — {FASES[n]}') for n, items in phase_nav])
index_section('idx-ejemplos', 'Cuadernos de ejemplos', 'Datos listos para importar, laboratorios guiados, errores provocados a propósito y soluciones. Uno por fase.',
              [(items[1][0], f'Fase {n} — {FASES[n]}') for n, items in phase_nav])
index_section('idx-plantillas', 'Plantillas de consultoría', 'Documentos de trabajo reales. Se usan desde la Fase 1, no al final.',
              [(d, l) for d, l, _ in plant])


# ---------- datos de portada ----------
readme = open(os.path.join(REPO, 'README.md'), encoding='utf-8').read()
phase_rows = []
for line in readme.splitlines():
    m = re.match(r'^\|\s*(\d+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\|\s*(\d+)–(\d+) h\s*\|\s*([^|]+)\|', line)
    if m:
        phase_rows.append(dict(n=int(m.group(1)), name=m.group(2), foco=m.group(4).strip(),
                               lo=int(m.group(5)), hi=int(m.group(6)), ent=m.group(7).strip(),
                               did=docid(m.group(3))))
assert len(phase_rows) == 12, len(phase_rows)
tot_lo, tot_hi = sum(r['lo'] for r in phase_rows), sum(r['hi'] for r in phase_rows)
HMAX = 60

commits = git('log', '--format=%h|%ad|%s', '--date=format:%d-%m-%Y', '-6').strip().splitlines()
head_sha = git('rev-parse', '--short', 'HEAD').strip()

f12 = docid('ejemplos/fase-12/README.md')
anchor_v20 = f12 + '~' + slug('Los cambios de v20 que hay que llevar frescos al examen')
assert anchor_v20 in docs[f12]['html'], 'ancla de la tabla de cambios v20 no encontrada'


def phase_link(n):
    return dict(phase_nav)[n][0][0]


def bar(r):
    left = r['lo'] / HMAX * 100
    width = (r['hi'] - r['lo']) / HMAX * 100
    return (f'<div class="hbar" role="img" aria-label="{r["lo"]} a {r["hi"]} horas">'
            f'<span class="hb-base" style="width:{left:.2f}%"></span>'
            f'<span class="hb-range" style="left:{left:.2f}%;width:{max(width,1.2):.2f}%"></span></div>')


rows_html = ''.join(
    f'<li class="ph"><a class="ph-n" href="#{r["did"]}">{r["n"]}</a>'
    f'<div class="ph-main"><a class="ph-name" href="#{r["did"]}">{html.escape(r["name"])}</a>'
    f'<p class="ph-foco">{html.escape(r["foco"])}</p></div>'
    f'<div class="ph-hours"><span class="ph-h">{r["lo"]}–{r["hi"]} h</span>{bar(r)}</div>'
    f'<p class="ph-ent"><span class="lbl">Entregable</span>{html.escape(r["ent"])}</p></li>'
    for r in phase_rows)

ticks = ''.join(f'<span style="left:{h / HMAX * 100:.2f}%">{h}</span>' for h in (0, 20, 40, 60))


def chip(n):
    return f'<a class="chip" href="#{phase_link(n)}"><b>{n}</b>{html.escape(FASES[n])}</a>'


V20 = [
    ('Contactos', 'Desaparece el «tipo de identificación». El RUC va en <code>vat</code> y el DNI en <code>additional_identifiers</code>.'),
    ('Punto de venta', 'Cada sesión genera una <b>factura resumen</b> al cliente por defecto, no un asiento.'),
    ('Listas de precios', 'Reglas <i>Descuento / Recargo / Precio fijo</i>; desaparece <code>percent_price</code>.'),
    ('Inventario', '<code>tracking</code> pierde el valor <code>none</code>; nuevo campo <code>store_by</code>. Valoración movida al módulo <code>account</code>.'),
    ('Ventas', '<code>require_payment</code> eliminado: el pago en línea se exige con un anticipo mayor que cero.'),
    ('Servicio de campo', 'Funciona sobre Planeación (<code>planning_field_service</code>), sin <code>industry_fsm</code>.'),
    ('Conciliación', 'Vuelve <code>rule_type</code>: reglas de coincidencia y modelos de conciliación.'),
    ('RR. HH.', 'Horas extra con <code>hr.time.rule</code>; asistencias con estado.'),
]
v20_html = ''.join(f'<li><span class="v-area">{a}</span><span class="v-txt">{t}</span></li>' for a, t in V20)

steps = [
    ('Leer el método', docid('00-metodo-y-entorno.md'), 'Método de estudio, entorno de práctica y cómo se valida cada fase. Unos 30 minutos.'),
    ('Montar el entorno', docid('00-metodo-y-entorno.md'), 'Las bases DEMO, LAB y PE que se describen ahí. Entre 1 y 2 horas.'),
    ('Abrir la bitácora', docid('plantillas/07-bitacora-de-estudio.md'), 'Copia la plantilla como <code>bitacora.md</code> y regístrala cada día.'),
    ('Empezar la Fase 1', phase_link(1), 'Ejecuta el Bloque 1.1 con el cuaderno de ejemplos al lado.'),
    ('Marcar el avance', docid('seguimiento.md'), 'Casillas por fase y registro de horas.'),
]
steps_html = ''.join(f'<li><a href="#{d}">{t}</a><p>{x}</p></li>' for t, d, x in steps)

commits_html = ''.join(
    f'<li><code>{c.split("|")[0]}</code><span>{c.split("|")[1]}</span><span>{html.escape(c.split("|", 2)[2])}</span></li>'
    for c in commits)

n_guias = sum(1 for f in MDS if '/guias/' in f or '/casos/' in f)
landing = f'''
<header class="hero">
  <p class="eyebrow">Plan de estudios · Odoo 20.0 · edición Perú</p>
  <h1>Consultor Funcional Odoo&nbsp;20</h1>
  <p class="lede">Ruta completa, por fases, para pasar de usuario que conoce Odoo a consultor capaz de
  levantar, diseñar, configurar, probar, capacitar y poner en marcha una implementación.</p>
  <ul class="facts">
    <li><b>12</b> fases</li>
    <li><b>{tot_lo}–{tot_hi}</b> horas efectivas</li>
    <li><b>{n_guias}</b> guías y casos</li>
    <li><b>{len(CSVS)}</b> archivos de datos</li>
    <li><b>60</b> preguntas de simulacro</li>
  </ul>
  <p class="hero-cta"><a class="btn" href="#{phase_link(1)}">Empezar por la Fase 1</a>
  <a class="btn ghost" href="#{docid('README.md')}">Leer el plan completo</a></p>
</header>

<section class="block" aria-labelledby="mapa">
  <h2 id="mapa">Mapa de fases</h2>
  <p class="sub">Horas estimadas por fase, en la misma escala. Nunca se avanza por calendario: solo cuando se cumple el criterio de validación.</p>
  <div class="phases-head"><span></span><span>Fase y foco</span><span class="ticks" aria-hidden="true">{ticks}</span><span>Entregable</span></div>
  <ol class="phases">{rows_html}</ol>
</section>

<section class="block" aria-labelledby="orden">
  <h2 id="orden">Orden y dependencias</h2>
  <div class="flow">
    <div class="lane"><span class="lane-t">Base</span><div class="lane-c">{chip(1)}</div></div>
    <div class="lane"><span class="lane-t">Ciclo comercial y logístico</span>
      <div class="lane-c">{chip(2)}{chip(3)}<span class="arr" aria-hidden="true">→</span>{chip(4)}</div>
      <p class="lane-n">Contabilidad necesita ver ventas, compras e inventario. Manufactura ({chip(5)}) necesita Inventario.</p></div>
    <div class="lane"><span class="lane-t">Independientes entre sí</span><div class="lane-c">{chip(6)}{chip(7)}{chip(8)}</div>
      <p class="lane-n">Se reordenan según el mercado objetivo.</p></div>
    <div class="lane"><span class="lane-t">Núcleo final</span>
      <div class="lane-c">{chip(9)}<span class="arr" aria-hidden="true">→</span>{chip(10)}<span class="arr" aria-hidden="true">→</span>{chip(11)}<span class="arr" aria-hidden="true">→</span>{chip(12)}</div></div>
  </div>
  <p class="note">Las fases 1, 4, 9, 11 y 12 no se saltan nunca: son el núcleo del perfil funcional.</p>
</section>

<div class="two">
<section class="block case" aria-labelledby="caso">
  <h2 id="caso">El caso: ANDINA GOURMET S.A.C.</h2>
  <p>Todos los laboratorios usan la misma empresa, para que las fases se acumulen en un caso coherente.
  La Fase 12 la implementa completa como si fuera un cliente real.</p>
  <dl>
    <dt>Qué hace</dt><dd>Conservas y snacks andinos de quinua, kiwicha y aguaymanto. Lima, Perú.</dd>
    <dt>Canales</dt><dd>Mayorista B2B, tienda propia con punto de venta y tienda en línea.</dd>
    <dt>Operación</dt><dd>1 planta, almacenes en Lima y Arequipa, 18 empleados.</dd>
    <dt>Moneda</dt><dd>PEN, con compras de insumos en USD. Plan contable PCGE.</dd>
    <dt>Dolores</dt><dd>Lotes y vencimientos en Excel, costos «a ojo», facturación electrónica en un portal externo, sin rentabilidad por producto.</dd>
  </dl>
</section>

<section class="block" aria-labelledby="empezar">
  <h2 id="empezar">Cómo empezar hoy</h2>
  <ol class="steps">{steps_html}</ol>
</section>
</div>

<section class="block" aria-labelledby="v20">
  <h2 id="v20">Lo que cambia en Odoo 20</h2>
  <p class="sub">Los cambios que más afectan a un consultor que viene de versiones anteriores. La tabla completa,
  con los cambios de v19 que siguen vigentes, está en el <a href="#{anchor_v20}">cuaderno de la Fase 12</a>.</p>
  <ul class="v20">{v20_html}</ul>
</section>

<section class="block verify" aria-labelledby="verif">
  <h2 id="verif">Cómo se verificó este material</h2>
  <div class="vgrid">
    <div><h3>Contra el código</h3><p>Cada modelo, campo, menú y comportamiento se contrastó con el código fuente de Odoo 20.0
    (Community y Enterprise) y se comparó con saas-19.4.</p></div>
    <div><h3>En una base real</h3><p>Base Odoo 20 creada desde cero con la empresa peruana y el plan contable PCGE: todos los CSV importan
    y los laboratorios G2, G3, H2, H3, H4, I1, I3, J1, K1, la migración de la Fase 9 y el simulacro dan las cifras del material.
    <b>540 comprobaciones, 0 fallos.</b></p></div>
    <div><h3>Enlaces</h3><p>247 enlaces externos comprobados el 04-10-2026. La documentación oficial apunta a la 20.0 en inglés:
    la traducción al español aún no está publicada.</p></div>
  </div>
  <h3 class="clog">Últimos cambios del repositorio</h3>
  <ul class="commits">{commits_html}</ul>
</section>
'''
docs['inicio'] = dict(title='Portada', label='Portada', html=landing, path=None, crumbs=())


# ---------- navegación lateral ----------
def nav_item(did, label, cls=''):
    return f'<li><a href="#{did}" data-doc="{did}" class="{cls}">{html.escape(label)}</a></li>'


side = ['<nav class="side" id="side" aria-label="Índice"><div class="side-in">']
side.append('<p class="grp">Empezar</p><ul>' + ''.join(nav_item(d, l) for d, l, _ in nav[0][1]) + '</ul>')
side.append('<p class="grp">Fases</p>')
for n, items in phase_nav:
    sub = []
    current = None
    for d, l, g in items:
        if g != current and g:
            sub.append(f'<li class="sg">{g}</li>')
            current = g
        sub.append(nav_item(d, l, 'csvlink' if g == 'Datos' else ''))
    side.append(f'<details class="ph-nav" data-phase="{n}"><summary><b>{n}</b>{html.escape(FASES[n])}</summary><ul>{"".join(sub)}</ul></details>')
side.append('<p class="grp">Plantillas</p><ul>' + ''.join(nav_item(d, l) for d, l, _ in plant) + '</ul>')
side.append('</div></nav>')

# fase a la que pertenece cada documento (para abrir su grupo en el índice)
phase_of = {}
for n, items in phase_nav:
    for d, _, _ in items:
        phase_of[d] = n

seq = ['inicio'] + order
sections = []
for did in ['inicio'] + order + ['idx-fases', 'idx-ejemplos', 'idx-plantillas']:
    d = docs[did]
    meta = ''
    pager = ''
    if did != 'inicio':
        crumbs = ' › '.join(html.escape(c) for c in d['crumbs'])
        src = (f'<a class="src" href="{GITHUB}{d["path"]}" target="_blank" rel="noopener"><code>{html.escape(d["path"])}</code></a>'
               if d['path'] else '')
        meta = f'<div class="meta">{"<span>" + crumbs + "</span>" if crumbs else ""}{src}</div>'
        if did in seq:
            i = seq.index(did)
            prev_d = seq[i - 1] if i > 0 else None
            next_d = seq[i + 1] if i + 1 < len(seq) else None
            pager = '<nav class="pager" aria-label="Documento anterior y siguiente">'
            if prev_d:
                pager += f'<a href="#{prev_d}"><span>Anterior</span>{html.escape(docs[prev_d]["label"])}</a>'
            if next_d:
                pager += f'<a class="nx" href="#{next_d}"><span>Siguiente</span>{html.escape(docs[next_d]["label"])}</a>'
            pager += '</nav>'
    ph = phase_of.get(did, '')
    hidden = '' if did == 'inicio' else ' hidden'
    sections.append(f'<article class="doc{" home" if did == "inicio" else ""}" id="{did}" data-title="{html.escape(d["title"])}" data-phase="{ph}"{hidden}>'
                    f'{meta}<div class="prose">{d["html"]}</div>{pager}</article>')

tmpl = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
page = (tmpl.replace('%%SIDE%%', ''.join(side))
            .replace('%%DOCS%%', '\n'.join(sections))
            .replace('%%SHA%%', head_sha))
open(OUT, 'w', encoding='utf-8').write(page)
print('documentos', len(docs), 'bytes', len(page.encode()), '->', OUT)
