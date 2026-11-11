from django.db import migrations


IMAGE_UPDATES = {
    "neymar-talento-creatividad-y-vision": "assets/ney.jpeg",
    "dei-v-identidad-y-musica-urbana": "assets/deiv.jpeg",
    "aprender-construyendo-desarrollo-web": "assets/yo.webp",
}


def update_post_images(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    database = schema_editor.connection.alias
    for slug, media_url in IMAGE_UPDATES.items():
        Post.objects.using(database).filter(slug=slug).update(media_url=media_url)


def restore_post_images(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    database = schema_editor.connection.alias
    for slug in IMAGE_UPDATES:
        Post.objects.using(database).filter(slug=slug).update(
            media_url="assets/images.jpg"
        )


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_add_portfolio_posts"),
    ]

    operations = [
        migrations.RunPython(update_post_images, restore_post_images),
    ]
