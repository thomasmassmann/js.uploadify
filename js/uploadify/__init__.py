from fanstatic import Group, Library, Resource

from js.jquery import jquery

library = Library('uploadify', 'resources')

uploadify_css = Resource(
    library, 'uploadify.css',
)

swfobject_js = Resource(
    library, 'swfobject.js',
)

uploadify_js = Resource(
    library, 'jquery.uploadify.js',
    minified='jquery.uploadify.min.js',
    depends=[
        jquery,
        swfobject_js,
        uploadify_css,
    ],
)

uploadify = Group([uploadify_js, uploadify_css])
