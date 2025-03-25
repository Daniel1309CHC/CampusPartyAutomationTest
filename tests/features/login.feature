Feature: Inicio de Sesión

  Como usuario registrado
  Quiero iniciar sesión con mis credenciales
  Para acceder al sistema de gestión

  @loginExitoso
  Scenario: Inicio de Sesión con Credenciales Válidas
    Given el usuario está en la página de inicio de sesión
    When ingresa su correo "danielchaparro@gmail.com" y contraseña "123"
    Then el usuario debe acceder correctamente al sistema