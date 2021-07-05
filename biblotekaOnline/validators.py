from typing import List


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions: List[str] = ['.mp3','.mp4','.wav','.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validPdf(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension it shoud be .pdf,.doc or .docx')


def validImg(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid = ['.jpg', '.png']
    if not ext.lower() in valid:
        raise ValidationError("Unsupported image extension it shoud be .jpg or png")

