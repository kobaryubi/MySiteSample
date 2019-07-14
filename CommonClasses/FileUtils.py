
class FileUtils():
    def __init__(self):
        pass

    @staticmethod
    def get_image_path(app_name, instance, filename):
        return '{0}/{1}/images/{2}/'.format(
            app_name,
            instance.submitter.id,
            filename
        )

    @staticmethod
    def get_favs_share_app_image_path(instance, filename):
        return FileUtils.get_image_path(
            "favs_share_app",
            instance,
            filename
        )