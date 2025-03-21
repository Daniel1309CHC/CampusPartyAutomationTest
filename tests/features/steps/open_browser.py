from behave import given, then

@given("el usuario abre el navegador")
def step_open_browser(context):
    context.url = "https://example.com"  # Guardamos la URL en context
    context.driver.get(context.url)  # Usamos el driver almacenado en context

@then("la página debe cargarse correctamente")
def step_verify_page(context):
    assert context.driver.current_url == context.url, "La página no cargó correctamente"