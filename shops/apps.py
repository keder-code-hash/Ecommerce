from django.apps import AppConfig


class ShopsConfig(AppConfig):
    name = 'shops'


# db config for using multiple db 

class ShopRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a shop database.
        """
        return 'shop'

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        return 'shop'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {'shop'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True