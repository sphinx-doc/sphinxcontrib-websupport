from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx import addnodes

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.util.typing import ExtensionMetadata

sys.path.append(os.path.abspath('.'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.jsmath', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.extlinks', 'ext']

jsmath_path = 'dummy.js'

templates_path = ['_templates']

master_doc = 'contents'
source_suffix = ['.txt', '.add', '.foo']

project = 'Sphinx <Tests>'
copyright = '2010-2016, Georg Brandl & Team'
# If this is changed, remember to update the versionchanges!
version = '0.6'
release = '0.6alpha1'
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build', '**/excluded.*']
keep_warnings = True
pygments_style = 'sphinx'
show_authors = True
numfig = True

rst_epilog = '.. |subst| replace:: global substitution'

html_theme = 'testtheme'
html_theme_path = ['.']
html_theme_options = {'testopt': 'testoverride'}
html_sidebars = {'**': ['customsb.html'],
                 'contents': ['contentssb.html', 'localtoc.html',
                              'globaltoc.html']}
html_style = 'default.css'
html_static_path = ['_static', 'templated.css_t']
html_extra_path = ['robots.txt']
html_last_updated_fmt = '%b %d, %Y'
html_context = {'hckey': 'hcval', 'hckey_co': 'wrong_hcval_co'}

htmlhelp_basename = 'SphinxTestsdoc'

applehelp_bundle_id = 'org.sphinx-doc.Sphinx.help'
applehelp_disable_external_tools = True

latex_documents = [
    ('contents', 'SphinxTests.tex', 'Sphinx Tests Documentation',
     'Georg Brandl \\and someone else', 'manual'),
]

latex_additional_files = ['svgimg.svg']

texinfo_documents = [
    ('contents', 'SphinxTests', 'Sphinx Tests',
     'Georg Brandl \\and someone else', 'Sphinx Testing', 'Miscellaneous'),
]

man_pages = [
    ('contents', 'SphinxTests', 'Sphinx Tests Documentation',
     'Georg Brandl and someone else', 1),
]

value_from_conf_py = 84

coverage_c_path = ['special/*.h']
coverage_c_regexes = {'function': r'^PyAPI_FUNC\(.*\)\s+([^_][\w_]+)'}

extlinks = {'issue': ('http://bugs.python.org/issue%s', 'issue '),
            'pyurl': ('http://python.org/%s', None)}

autodoc_mock_imports = [
    'missing_module',
    'missing_package1.missing_module1',
    'missing_package2.missing_module2',
    'missing_package3.missing_module3',
]

# modify tags from conf.py
tags.add('confpytag')  # NoQA: F821


# -- extension API
def userdesc_parse(env, sig, signode):
    x, y = sig.split(':')
    signode += addnodes.desc_name(x, x)
    signode += addnodes.desc_parameterlist()
    signode[-1] += addnodes.desc_parameter(y, y)
    return x


class ClassDirective(Directive):
    option_spec = {
        'opt': directives.unchanged,
    }

    def run(self):
        return [nodes.strong(text=f'from class: {self.options["opt"]}')]


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value('value_from_conf_py', 42, False)
    app.add_directive('clsdir', ClassDirective)
    app.add_object_type('userdesc', 'userdescrole', '%s (userdesc)',
                        userdesc_parse, objname='user desc')
    app.add_js_file('file://moo.js')
    return {}
