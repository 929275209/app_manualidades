import reflex as rx
def home():
    return rx.center(
        rx.text("Vienvenidos a la app de manualidades!!", font_size="2em"),
        rx.limk("explorar tutoriales",href="/tutoriales"),
        padding ="2em",
app = rx.App()
app.add_page(home, route="/")
app.compile()
