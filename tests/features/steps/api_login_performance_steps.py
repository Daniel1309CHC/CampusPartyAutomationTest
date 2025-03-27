from behave import given, when, then
from concurrent.futures import ThreadPoolExecutor
import time
from tests.pages.api_auth_page import APIAuthPage  # Usamos APIAuthPage para login_invalid

@given("que se simulan múltiples usuarios con credenciales inválidas")
def step_setup_invalid_credentials(context):
    # Instanciamos la clase de autenticación que contiene el método login_invalid
    context.api_auth = APIAuthPage()
    # Definimos varios conjuntos de credenciales inválidas.
    context.invalid_credentials_list = [
        {"email": "", "password": "123"},                # Correo vacío
        {"email": "usuario.com", "password": "123"},       # Correo con formato incorrecto
        {"email": "noexiste@mail.com", "password": ""},    # Contraseña vacía
        {"email": "fake@mail.com", "password": "wrong"}    # Correo no registrado / contraseña incorrecta
    ]
    # Establece la cantidad de solicitudes a enviar
    context.requests_to_send = 50


@when("se envían solicitudes POST concurrentes al endpoint de autenticación")
def step_send_concurrent_requests(context):
    def login_request(creds):
        start_time = time.time()
        # Usar context.api_auth en lugar de context.performance_page
        response = context.api_auth.login_invalid(creds)
        end_time = time.time()
        return {
            "status_code": response.status_code,
            "elapsed_time": end_time - start_time,
            "creds": creds
        }

    # Preparar la lista de solicitudes a enviar
    all_requests = []
    idx = 0
    while idx < context.requests_to_send:
        creds = context.invalid_credentials_list[idx % len(context.invalid_credentials_list)]
        all_requests.append(creds)
        idx += 1

    context.results = []
    # Enviar solicitudes en paralelo utilizando 10 hilos
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(login_request, creds) for creds in all_requests]
        for future in futures:
            context.results.append(future.result())


@then("el sistema debe responder con errores adecuados y mantener un tiempo de respuesta aceptable")
def step_validate_performance(context):
    max_acceptable_time = 0.5  # Tiempo máximo aceptable (500 ms)
    error_codes = [400, 401, 403, 404]  # Códigos de error esperados para credenciales inválidas


    scenario = getattr(context, "scenario", None)  # Maneja versiones donde no existe

    total_requests = len(context.results)
    slow_responses = 0
    unexpected_success = 0
    total_time = 0.0

    for result in context.results:
        total_time += result["elapsed_time"]
        if result["status_code"] not in error_codes:
            unexpected_success += 1
        if result["elapsed_time"] > max_acceptable_time:
            slow_responses += 1

    print(f"Total de solicitudes: {total_requests}")
    print(f"Respuestas más lentas que {max_acceptable_time} s: {slow_responses}")
    print(f"Solicitudes con status code no esperado: {unexpected_success}")
    print(f"Tiempo total de ejecución: {total_time:.3f} segundos")

    # Texto de métricas
    metrics_text = (
        f"Total de solicitudes: {total_requests}\n"
        f"Respuestas más lentas que {max_acceptable_time} s: {slow_responses}\n"
        f"Solicitudes con status code no esperado: {unexpected_success}\n"
        f"Tiempo total de ejecución: {total_time:.3f} segundos\n"
    )


    # Concatenar al scenario.description
    scenario.description = (scenario.description or "") + "\n" + metrics_text


    # Validar que todas las solicitudes devuelvan un código de error esperado
    assert unexpected_success == 0, f"Hubo {unexpected_success} solicitudes que no fallaron como se esperaba."
    # Validar que la mayoría de las respuestas estén dentro del tiempo aceptable
    assert slow_responses < (0.1 * total_requests), "Muchas respuestas fueron demasiado lentas."