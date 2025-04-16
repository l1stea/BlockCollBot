from CommandsDB.link import *

def handle_link_assembly_component(text):
    try:
        _, product_id, component_id = text.split(",", 2)
        link_assembly_component(int(product_id.strip()), int(component_id.strip()))
        return "Сборка и комплектующий связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkassemblycomponent <product_id>, <component_id>'."

def handle_link_component_supplier(text):
    try:
        _, component_id, supplier_id = text.split(",", 2)
        link_component_supplier(int(component_id.strip()), int(supplier_id.strip()))
        return "Комплектующий и поставщик связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkcomponentsupplier <component_id>, <supplier_id>'."