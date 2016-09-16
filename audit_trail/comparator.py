from django.utils.encoding import force_text


class ModelFieldComparator(object):

    custom_compare_methods = {}

    @classmethod
    def compare(cls, field, old_value, new_value):
        field_class = field.__class__

        if field_class in cls.custom_compare_methods:
            comparator = cls.custom_compare_methods[field_class]

            return comparator(old_value, new_value)
        else:
            return cls.default_comparator(old_value, new_value)

    @staticmethod
    def default_comparator(old_value, new_value):
        return force_text(old_value) == force_text(new_value)

    @classmethod
    def add_comparator(cls, field_class, callback):
        cls.custom_compare_methods[field_class] = callback
