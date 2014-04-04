# -*- coding: utf-8 -*-

from mfr.core import FileHandler, get_file_extension
from mfr.code.render import render_html

from mfr.code.export import CodeExporter

EXTENSIONS = ['.rb',
 '.cs',
 '.ahk',
 '.rs',
 '.c9search_results',
 '.scm',
 '.vhd',
 '.vbs',
 '.twig',
 '.jack',
 '.jl',
 '.js',
 '.matlab',
 '.tcl',
 '.dot',
 '.plg',
 '.clj',
 '.rd',
 '.pl',
 '.ejs',
 '.scad',
 '.lisp',
 '.py',
 '.cpp',
 '.snippets',
 '.css',
 '.vm',
 '.groovy',
 '.liquid',
 '.xq',
 '.proto',
 '.php',
 '.asm',
 '.sh',
 '.curly',
 '.hs',
 '.hx',
 '.tex',
 '.sjs',
 '.mysql',
 '.html',
 '.space',
 '.haml',
 '.cbl',
 '.styl',
 '.ada',
 '.lucene',
 '.pas',
 '.tmsnippet',
 '.ps1',
 '.yaml',
 '.soy',
 '.sass',
 '.scala',
 '.scss',
 '.ini',
 '.bat',
 '.glsl',
 '.diff',
 '.frt',
 '.less',
 '.erl',
 '.erb',
 '.toml',
 '.hbs',
 '.m',
 '.sql',
 '.json',
 '.d',
 '.lua',
 '.as',
 '.nix',
 '.txt',
 '.r',
 '.v',
 '.jade',
 '.go',
 '.ts',
 '.md',
 '.jq',
 '.mc',
 '.xml',
 '.rhtml',
 '.ml',
 '.dart',
 '.pgsql',
 '.coffee',
 '.lp',
 '.ls',
 '.jsx',
 '.asciidoc',
 '.jsp',
 '.logic',
 '.properties',
 '.textile',
 '.lsl',
 '.abap',
 '.ftl',
 '.java',
 '.cfm']



class CodeFileHandler(FileHandler):
    # Renderers and exporters can be callables
    renderers = {
        # like functions
        'html': render_html,
    }

    exporters = {
        # Or instance methods
        'text': CodeExporter().export_txt,
        # ...
    }

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
