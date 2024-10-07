from django.apps import AppConfig


class TrackMyDocsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'track_my_docs'

    def ready(self):
        import track_my_docs.signals