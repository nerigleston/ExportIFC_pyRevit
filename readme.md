# Revit - pyRevit
## [Estrutura do Código](https://github.com/nerigleston/ExportIFC_pyRevit/blob/main/IFC.pushbutton/IFC_script.py)
### O script está organizado em quatro funções:

- select_ifc_version: Permite ao usuário selecionar a versão desejada do IFC a partir de uma lista predefinida.

- choose_ifc_path: Oferece ao usuário a escolha entre exportar diretamente para a pasta de Downloads ou selecionar manualmente o diretório de destino.

- export_ifc: Realiza a exportação do modelo para o formato IFC com base na versão e caminho fornecidos. Lida com mensagens de conclusão ou erro.

- A função principal, main, coordena o processo, chamando as funções acima na ordem apropriada.