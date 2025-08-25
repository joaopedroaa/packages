# gerador.py
import os
from apps import *

# --- CONFIGURAÇÃO PRINCIPAL ---
SCRIPT_CONFIG = {
    # "nome_do_arquivo": ["Nome para o Título", "Comando de Instalação", variavel_com_os_apps]
    "10-system":    ["System",    "yay -S", system],
    "20-dev":       ["Dev",       "yay -S", development],
    "30-plasma":    ["Plasma",    "yay -S", plasma],
    "40-xfce":      ["XFCE",      "yay -S", xfce],
}

WRITE_LOCATION = "./build"


def generate_script_content(script_name, install_command, app_categories):
    """
    Gera o conteúdo de um script shell para uma categoria de aplicativos.
    """
    lines = []

    for category_path, apps in app_categories.items():
        count = len(apps)
        title_parts = [word.capitalize() for word in category_path.split("/")]
        title = f" / ".join(title_parts)

        header = f"=============== {script_name} / {title} ({count}) ==============="
        lines.append(f"echo \"{header}\"")

        apps_string = " ".join(apps)
        lines.append(f"{install_command} {apps_string} --noconfirm")
        lines.append("clear\n")

    return "\n".join(lines)


def save_scripts(scripts_to_write, output_dir):
    """
    Salva múltiplos scripts em um diretório de destino.
    O diretório é criado se não existir.
    """
    os.makedirs(output_dir, exist_ok=True)

    print(f"Salvando arquivos em '{os.path.abspath(output_dir)}'...")

    for filename, content in scripts_to_write.items():
        filepath = os.path.join(output_dir, f"{filename}.sh")
        try:
            with open(filepath, 'w') as file:
                file.write(content)
            print(f"✅ Arquivo salvo: {filename}.sh")
        except IOError as e:
            print(f"❌ Erro ao salvar {filename}.sh: {e}")


def main():
    """
    Função principal que orquestra a geração e salvamento dos scripts.
    """
    generated_scripts = {}

    # 1. Gera o conteúdo para cada arquivo individual
    for filename, config in SCRIPT_CONFIG.items():
        script_name, install_command, app_data = config
        content = generate_script_content(script_name, install_command, app_data)
        generated_scripts[filename] = content

    # --- NOVO TRECHO ADICIONADO ---
    # 2. Gera o conteúdo do arquivo com todos os aplicativos em uma única linha
    all_apps = set()
    for _, config in SCRIPT_CONFIG.items():
        app_data = config[2]
        for apps_list in app_data.values():
            all_apps.update(apps_list)

    apps_string = " ".join(sorted(list(all_apps)))

    single_line_content = f"""#!/bin/bash

echo "==========================================================="
echo "==  Iniciando a instalação de todos os pacotes em um só comando... =="
echo "==========================================================="

yay -S {apps_string} --noconfirm

echo ""
echo "==========================================================="
echo "==  Instalação de todos os pacotes concluída!  =="
echo "==========================================================="
"""
    generated_scripts["01-install-single-line"] = single_line_content
    # --- FIM DO NOVO TRECHO ---


    # 3. Cria o conteúdo do arquivo "install-all" (o original, com categorias separadas)
    all_content = []
    all_content.append("#!/bin/bash\n")
    all_content.append('echo "======================================================="')
    all_content.append('echo "==       Iniciando a instalação de todos os pacotes      =="')
    all_content.append('echo "======================================================="')
    all_content.append("clear\n")

    for filename in sorted(generated_scripts.keys()):
        if filename != "01-install-single-line": # Para evitar a duplicação do novo arquivo
            all_content.append(f"# --- Conteúdo de {filename}.sh ---\n")
            all_content.append(generated_scripts[filename])
            all_content.append("\n")

    all_content.append('echo "======================================================="')
    all_content.append('echo "==          Instalação de todos os pacotes concluída!          =="')
    all_content.append('======================================================="')

    generated_scripts["00-install-all"] = "\n".join(all_content)

    # 4. Salva todos os arquivos de uma vez
    save_scripts(generated_scripts, WRITE_LOCATION)

    print("\nProcesso finalizado!")


if __name__ == "__main__":
    main()
