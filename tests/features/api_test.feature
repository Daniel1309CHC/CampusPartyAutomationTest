Feature: Pruebas de API

  Como usuario
  quiero enviar solicitudes REST
  para obtener respuesta mediante API

@api @GetUsuarios
  Scenario: Solicitud GET all al endpoint de usuarios
    Given que el usuario tiene acceso al token de autenticacion
    When envía una solicitud GET al endpoint de usuarios
    Then la respuesta debe contener los datos de los usuarios

@api @AuthUsuario
  Scenario: Solicitud POST al endpoint de autenticación
    Given que el usuario proporciona credenciales válidas con email "danielchaparro@gmail.com" y password "123"
    When envía una solicitud POST al endpoint de autenticación
    Then la respuesta debe contener un token de acceso y datos del usuario
