from django.core.validators import RegexValidator
AlphanumericValidator=RegexValidator(regex=r'^[a-zA-Z]*$',message="Only alphabet is allowed")