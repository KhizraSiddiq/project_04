from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
