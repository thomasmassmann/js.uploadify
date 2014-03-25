from fanstatic import Group, Library, Resource

from js.jquery import jquery

library = Library('uploadify', 'resources')

uploadify_css = Resource(
    library, 'uploadify.css',
)

uploadify_js = Resource(
    library, 'jquery.uploadify.js',
    minified='jquery.uploadify.min.js',
    depends=[
        jquery,
        uploadify_css,
    ],
)

uploadify = Group([uploadify_js, uploadify_css])
