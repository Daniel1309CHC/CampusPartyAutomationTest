Feature: Abrir el navegador

  Scenario: Abrir Chrome y verificar que la página carga
    Given el usuario abre el navegador
    Then la página debe cargarse correctamente