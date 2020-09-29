# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1601412639.9279747
_enable_loop = True
_template_filename = '/usr/local/lib/python3.8/dist-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content', 'extra_head', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='ui_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('post_helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'post_helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        lang = context.get('lang', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        galleries_use_thumbnail = context.get('galleries_use_thumbnail', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        _link = context.get('_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        post = context.get('post', UNDEFINED)
        photo_array = context.get('photo_array', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        enable_comments = context.get('enable_comments', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        len = context.get('len', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        galleries_use_thumbnail = context.get('galleries_use_thumbnail', UNDEFINED)
        crumbs = context.get('crumbs', UNDEFINED)
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        ui = _mako_get_namespace(context, 'ui')
        photo_array = context.get('photo_array', UNDEFINED)
        enable_comments = context.get('enable_comments', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        folders = context.get('folders', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.breadcrumbs(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            if galleries_use_thumbnail:
                for (folder, ftitle, fpost) in folders:
                    __M_writer('            <div class="thumnbnail-container">\n                <a href="')
                    __M_writer(str(folder))
                    __M_writer('" class="thumbnail image-reference" title="')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('">\n')
                    if fpost and fpost.previewimage:
                        __M_writer('                        <img src="')
                        __M_writer(str(url_replacer(fpost.permalink(), fpost.previewimage, lang, 'full_path')))
                        __M_writer('" alt="')
                        __M_writer(filters.html_escape(str(ftitle)))
                        __M_writer('" loading="lazy" style="max-width:')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; max-height:')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px;" />\n')
                    else:
                        __M_writer('                        <div style="height: ')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; width: ')
                        __M_writer(str(thumbnail_size))
                        __M_writer('px; background-color: #eee;"></div>\n')
                    __M_writer('                <p class="thumbnail-caption">')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('</p>\n                </a>\n            </div>\n')
            else:
                __M_writer('            <ul>\n')
                for folder, ftitle in folders:
                    __M_writer('                <li><a href="')
                    __M_writer(str(folder))
                    __M_writer('">📂&nbsp;')
                    __M_writer(filters.html_escape(str(ftitle)))
                    __M_writer('</a></li>\n')
                __M_writer('            </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" loading="lazy" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        post = context.get('post', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        post_helper = _mako_get_namespace(context, 'post_helper')
        _link = context.get('_link', UNDEFINED)
        gallery_path = context.get('gallery_path', UNDEFINED)
        len = context.get('len', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    #gallery_container {\n        position: relative;\n    }\n    .image-block {\n        position: absolute;\n    }\n</style>\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang:
                    __M_writer('             <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(_link('gallery', gallery_path, langname)))
                    __M_writer('">\n')
        __M_writer('<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        if post:
            __M_writer('    ')
            __M_writer(str(post_helper.open_graph_metadata(post)))
            __M_writer('\n    ')
            __M_writer(str(post_helper.twitter_card_information(post)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        thumbnail_size = context.get('thumbnail_size', UNDEFINED)
        photo_array_json = context.get('photo_array_json', UNDEFINED)
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/justified-layout.min.js"></script>\n<script src="/assets/js/gallery.min.js"></script>\n<script>\nvar jsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\nvar thumbnailSize = ')
        __M_writer(str(thumbnail_size))
        __M_writer(";\nrenderGallery(jsonContent, thumbnailSize);\nwindow.addEventListener('resize', function(){renderGallery(jsonContent, thumbnailSize)});\n</script>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/usr/local/lib/python3.8/dist-packages/nikola/data/themes/base/templates/gallery.tmpl", "uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "35": 0, "69": 2, "70": 3, "71": 4, "72": 5, "77": 6, "82": 55, "87": 80, "92": 91, "98": 6, "109": 8, "129": 8, "130": 9, "131": 9, "132": 10, "133": 11, "134": 11, "135": 11, "136": 13, "137": 14, "138": 15, "139": 15, "140": 18, "141": 19, "142": 20, "143": 21, "144": 22, "145": 22, "146": 22, "147": 22, "148": 23, "149": 24, "150": 24, "151": 24, "152": 24, "153": 24, "154": 24, "155": 24, "156": 24, "157": 24, "158": 25, "159": 26, "160": 26, "161": 26, "162": 26, "163": 26, "164": 28, "165": 28, "166": 28, "167": 32, "168": 33, "169": 34, "170": 35, "171": 35, "172": 35, "173": 35, "174": 35, "175": 37, "176": 40, "177": 42, "178": 43, "179": 45, "180": 46, "181": 46, "182": 46, "183": 46, "184": 46, "185": 47, "186": 47, "187": 47, "188": 47, "189": 49, "190": 52, "191": 53, "192": 53, "193": 53, "199": 57, "213": 57, "214": 58, "215": 58, "216": 68, "217": 69, "218": 70, "219": 71, "220": 71, "221": 71, "222": 71, "223": 71, "224": 75, "225": 76, "226": 77, "227": 77, "228": 77, "229": 78, "230": 78, "236": 82, "244": 82, "245": 86, "246": 86, "247": 87, "248": 87, "254": 248}}
__M_END_METADATA
"""
