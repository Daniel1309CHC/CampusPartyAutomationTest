import argparse
import os
import subprocess
# import pdb
# pdb.set_trace()

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
    parser.add_argument(
        "--report",
        help="Generar reporte de ejecución en la carpeta reports (True/False)",
        action="store_true"
    )

    args = parser.parse_args()

    # 1. Establecer variables de entorno
    os.environ["BROWSER"] = args.browser
    os.environ["HEADLESS"] = "True" if args.headless else "False"

    # 2. Construir el comando de Behave
    command = ["behave", "tests/features"]

    if args.report:
        # Si se activa --report, se genera el reporte en formato pretty y junit
        command.extend([
            "-f", "pretty", "-o", "reports/pretty.output",
            "-f", "json", "-o", "reports/report.json",
            "-f", "junit", "-o", "reports/junit-report.xml"
        ])

    command = ["behave"]
    if args.tags:
        command.extend(["--tags", args.tags])
    else:
        command.append("tests/features")  # Solo si no hay tags, ejecuta todo

    # 3. Ejecutar Behave
    print(f"\n[INFO] Ejecutando Behave con navegador={args.browser}, headless={args.headless}, tags={args.tags}, report={args.report}")
    subprocess.run(command)

if __name__ == "__main__":
    main()