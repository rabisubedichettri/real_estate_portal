from django.core.exceptions import ValidationError

def validate_selector(value):
    value=value.lower()
    if value == 's' or value =="select":
        raise ValidationError(
           'you have to select value.'
        )

def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))