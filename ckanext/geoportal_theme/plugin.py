import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class GeoportalThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
#    plugins.implements(plugins.IRoutes, inherit=True)
    # IConfigurer

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        #toolkit.add_resource('public', 'ckanext-publicamundi')
        toolkit.add_resource('fanstatic', 'ckanext-geoportal_theme')
#    def before_map(self, m):
#        m.redirect('/', '/dataset')
#        return m
