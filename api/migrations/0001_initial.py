
from django.db import migrations
from api.user.models import CustomUser
# write this code manually. It's not auto generated. For solving the classical Super Admin issue in django


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="hitesh", email="hitesh@lco.dev", is_staff=True,
                          is_superuser=True, phone="9876543210", gender="Male")
        user.set_password("Nishant1998@")
        user.save()

    dependencies = [


    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
