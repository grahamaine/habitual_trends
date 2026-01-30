import reflex as rx

config = rx.Config(
    app_name="habitual_backend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)