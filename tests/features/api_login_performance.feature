Feature: Prueba de rendimiento en la API de login con credenciales inválidas

  Como usuario
  quiero enviar múltiples solicitudes con credenciales inválidas
  para verificar la capacidad de la API de rechazar el acceso y medir su rendimiento

  @api @AuthPerformance
  Scenario: Solicitud POST al endpoint de autenticación con credenciales inválidas en alta concurrencia
    Given que se simulan múltiples usuarios con credenciales inválidas
    When se envían solicitudes POST concurrentes al endpoint de autenticación
    Then el sistema debe responder con errores adecuados y mantener un tiempo de respuesta aceptable