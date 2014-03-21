from fanstatic import Library, Resource

from js.jquery import jquery

library = Library('uploadify', 'resources')

uploadify_css = Resource(
    library, 'uploadify.css',
)

uploadify = Resource(
    library, 'jquery.uploadify.js',
    depends=[
        uploadify_css,
        jquery,
    ],
)
