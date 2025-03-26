Feature: Pruebas de API

  Como usuario
  quiero enviar solicitudes REST
  para obtener respuesta mediante API

@api @GetUsuarios
  Scenario: Solicitud GET all al endpoint de usuarios
    Given que el usuario tiene acceso al token de autenticacion
    When envía una solicitud GET al endpoint de usuarios
    Then la respuesta debe contener los datos de los usuarios

