# Archivo: tests/features/registro.feature

Feature: Registro de Usuario

  Como usuario
  quiero registrarme en el sistema
  para poder acceder a las funcionalidades del sistema

  @RegistroExitoso
  Scenario: Registro de usuario con datos válidos
    Given que el usuario accede al registro desde la pantalla de inicio
    When llena el formulario de registro con informacion valida
    Then accede al dashboard de inicio de campus party

  @RegistroFallido
  Scenario: Registro de usuario con cuenta existente
    Given que el usuario accede al registro desde la pantalla de inicio
    When intenta registrarse con un correo ya registrado
    Then recibe un mensaje de error indicando que el usuario ya existe