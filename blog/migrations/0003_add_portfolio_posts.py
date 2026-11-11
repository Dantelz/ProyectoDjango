from django.db import migrations


POSTS = [
    {
        "title": "Neymar: talento, creatividad y visión de juego",
        "slug": "neymar-talento-creatividad-y-vision",
        "excerpt": "Una mirada personal a la creatividad, la técnica y la capacidad de resolver de manera diferente dentro de la cancha.",
        "content": (
            "Neymar Jr. es uno de los futbolistas que más me llaman la atención "
            "por su técnica, su creatividad en espacios reducidos y su capacidad "
            "para intentar soluciones diferentes durante un partido.\n\n"
            "Más allá de una jugada puntual, me interesa cómo la imaginación "
            "puede convertirse en una herramienta para abrir espacios y generar "
            "alternativas. Su manera de jugar me recuerda que la confianza y la "
            "preparación pueden convivir: probar algo distinto también requiere "
            "entender el momento del partido.\n\n"
            "Lo tomo como una referencia futbolística por esa combinación de "
            "talento y creatividad, y por la forma en que una identidad de juego "
            "puede dejar una marca propia."
        ),
        "media_url": "assets/ney.jpeg",
    },
    {
        "title": "Dei V: identidad y energía en la música urbana",
        "slug": "dei-v-identidad-y-musica-urbana",
        "excerpt": "Una reflexión sobre la identidad sonora y la energía que hacen reconocible una propuesta musical.",
        "content": (
            "También encuentro inspiración en la música de Dei V, artista "
            "puertorriqueño vinculado a la escena urbana. Me interesa cómo el "
            "ritmo, la interpretación y una identidad sonora definida pueden "
            "darle carácter a una propuesta.\n\n"
            "Esa idea va más allá de la música: en cualquier proyecto creativo, "
            "los detalles y la coherencia ayudan a que el resultado tenga una "
            "personalidad reconocible. Es una mirada que me acompaña tanto al "
            "escuchar como al pensar en mis propios proyectos."
        ),
        "media_url": "assets/deiv.jpeg",
    },
    {
        "title": "Cómo desarrollé mis primeros juegos",
        "slug": "desarrollo-de-mis-juegos-anteriores",
        "excerpt": "Un recorrido por tres proyectos que me permitieron explorar la lógica, la interacción y el diseño de juegos.",
        "content": (
            "Desarrollar juegos fue una forma concreta de transformar ideas en "
            "experiencias interactivas. Cada proyecto me llevó a pensar cómo "
            "responde el juego a las acciones de quien lo juega y cómo presentar "
            "esa experiencia de manera clara.\n\n"
            "En Save Obama trabajé sobre una propuesta de acción en 2D. Slither "
            "GZ reinterpreta la dinámica de Slither.io e incorpora serpientes "
            "enemigas controladas por inteligencia artificial. En El Verdadero "
            "Pokémon reuní pantallas de juego y una Pokédex propia.\n\n"
            "Mirar estos proyectos en conjunto me permite reconocer cuánto "
            "aprendí en el proceso: pasar de una idea inicial a organizar sus "
            "reglas, sus pantallas y la experiencia completa."
        ),
        "media_url": "assets/obamamenu.jpg",
    },
    {
        "title": "Jugar de nueve: mi perfil como delantero",
        "slug": "mi-perfil-como-delantero-centro",
        "excerpt": "Lo que significa para mí jugar como delantero centro y asumir un papel decisivo en el ataque.",
        "content": (
            "Me identifico con el puesto de delantero centro, el nueve del "
            "equipo. Es una posición que exige atención constante: interpretar "
            "los espacios, acompañar las jugadas y estar preparado para "
            "convertir una oportunidad en una acción concreta.\n\n"
            "Disfruto ese desafío y confío en mis condiciones para aportar en "
            "ataque. También entiendo que un delantero forma parte de un "
            "colectivo: el movimiento, la comunicación y el trabajo con sus "
            "compañeros son tan importantes como la definición.\n\n"
            "Seguir creciendo en este puesto significa entrenar, aprender de "
            "cada partido y mantener la concentración para estar disponible "
            "cuando el equipo me necesita."
        ),
        "media_url": "assets/images.jpg",
    },
    {
        "title": "Aprender construyendo: mi camino en el desarrollo web",
        "slug": "aprender-construyendo-desarrollo-web",
        "excerpt": "Mi manera de aprender programación: convertir ideas en proyectos y mejorar en cada iteración.",
        "content": (
            "Soy estudiante y desarrollador web, y una de las formas que más "
            "disfruto para aprender es construir. Cada proyecto me plantea "
            "preguntas distintas: cómo organizar la información, cómo hacer "
            "que una interfaz sea clara y cómo conectar las piezas para que "
            "todo funcione como una experiencia.\n\n"
            "En mi recorrido trabajé con tecnologías como Python, HTML, CSS y "
            "Bootstrap, además de explorar la lógica de juegos. No veo cada "
            "proyecto como un punto final, sino como una oportunidad para "
            "probar, revisar decisiones y mejorar.\n\n"
            "Ese proceso es lo que quiero seguir desarrollando: transformar "
            "ideas en productos digitales útiles, aprender de los desafíos y "
            "compartir el trabajo que hay detrás de cada resultado."
        ),
        "media_url": "assets/yo.webp",
    },
]


def add_portfolio_posts(apps, schema_editor):
    Post = apps.get_model("blog", "Post")
    for post_data in POSTS:
        slug = post_data["slug"]
        defaults = {key: value for key, value in post_data.items() if key != "slug"}
        Post.objects.using(schema_editor.connection.alias).get_or_create(
            slug=slug,
            defaults=defaults,
        )


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_comment_author_email_alter_comment_author_name_and_more"),
    ]

    operations = [
        migrations.RunPython(add_portfolio_posts, migrations.RunPython.noop),
    ]
