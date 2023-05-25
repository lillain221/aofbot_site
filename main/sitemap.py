from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index']  # トップページのURL名を返します

    def location(self, item):
        return '/'  # トップページのURLを返します
