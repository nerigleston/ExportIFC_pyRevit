# -- coding: utf-8 --

from pyrevit import revit, DB, forms
from Autodesk.Revit.DB import IFCExportOptions, Transaction


def select_ifc_version():

    # Solicita ao usuário que selecione a versão desejada do IFC.
    # Retorna a versão correspondente com base na seleção do usuário.

    ifc_version_mapping = {
        "IFC2x2 Singapore BCA e-Plan Check": DB.IFCVersion.IFCBCA,
        "IFC2x2 Coordination View": DB.IFCVersion.IFC2x2,
        "IFC2x3 Coordination View": DB.IFCVersion.IFC2x3,
        "IFC2x3 COBie 2.4 Design Deliverable": DB.IFCVersion.IFCCOBIE,
        "IFC2x3 Coordination View 2.0": DB.IFCVersion.IFC2x3CV2,
        "IFC4 Reference View": DB.IFCVersion.IFC4RV,
        "IFC4 Design Transfer View": DB.IFCVersion.IFC4DTV,
        "IFC2x3 Basic FM Handover View": DB.IFCVersion.IFC2x3BFM
    }

    selected_version = forms.SelectFromList.show(
        ifc_version_mapping.keys(),
        title="Selecione a versão do IFC",
        multiselect=False
    )

    if not selected_version:
        forms.alert("Exportação IFC cancelada.")
        return None

    return ifc_version_mapping[selected_version]


def choose_ifc_path():

    # Permite ao usuário escolher o tipo de caminho para a exportação IFC.
    # Retorna o caminho selecionado com base na escolha do usuário.

    path_choices = ["Exportar diretamente para pasta de Downloads",
                    "Escolha o caminho da exportação"]
    selected_path = forms.SelectFromList.show(
        path_choices,
        title="Escolha o tipo de caminho para exportação IFC",
        multiselect=False
    )

    if selected_path == "Exportar diretamente para pasta de Downloads":
        return "C:/Users/neri/Downloads/"
    else:
        return forms.pick_folder(title="Selecione a pasta de destino para exportação IFC")


def export_ifc(ifc_version, ifc_path):

    # Exporta o modelo Revit para o formato IFC com base na versão e caminho fornecidos.
    # Exibe mensagens de conclusão ou erro.

    active_view = revit.doc.ActiveView
    options = IFCExportOptions()
    options.FileVersion = ifc_version

    with Transaction(revit.doc, 'Export IFC') as t:
        try:
            t.Start()
            revit.doc.Export(ifc_path, active_view.Name, options)
            print('Exportação IFC concluída para ' + str(ifc_path))
        except Exception as e:
            t.RollBack()
            print("Erro durante a exportação IFC: " + str(e))


def main():

    # Função principal que coordena a seleção da versão do IFC e do caminho de exportação,
    # e inicia o processo de exportação IFC.

    ifc_version = select_ifc_version()
    if not ifc_version:
        return

    ifc_path = choose_ifc_path()
    if not ifc_path:
        forms.alert("Exportação IFC cancelada.")
        return

    export_ifc(ifc_version, ifc_path)


if __name__ == "__main__":
    main()
