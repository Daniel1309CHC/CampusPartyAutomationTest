# runner.py
import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Runner para pruebas Behave con configuraciones dinámicas.")

    parser.add_argument(
        "--browser",
        help="Selecciona el navegador: chrome, firefox o edge",
        default="chrome"
    )
    parser.add_argument(
        "--headless",
        help="Ejecutar en modo headless (True/False)",
        action="store_true"
    )
    parser.add_argument(
        "--tags",
        help="Filtrar escenarios por etiqueta. Ej: @smoke, @regression",
        default=None
    )

    args = parser.parse_args()

    # 1. Establecer variables de entorno para que environment.py las use
    os.environ["BROWSER"] = args.browser
    os.environ["HEADLESS"] = "True" if args.headless else "False"

    # 2. Construir el comando de Behave
    command = [
        "behave",
        "tests/features",
        "-f", "allure_behave.formatter:AllureFormatter",  # 🟢 Agregar Allure como formatter
        "-o", "reports"  # 🟢 Guardar reportes en la carpeta "reports"
    ]

    if args.tags:
        # Permite filtrar por etiqueta(s)
        # Puedes usar varias etiquetas con --tags=@tag1 --tags=@tag2
        command.extend(["--tags", args.tags])

    # 3. Ejecutar Behave
    print(f"\n[INFO] Ejecutando Behave con navegador={args.browser}, headless={args.headless}, tags={args.tags}")
    subprocess.run(command)

if __name__ == "__main__":
    main()