from CommandsDB.link import *
from Handler.commands import *

@command("/linkassemblycomponent")
def handle_link_assembly_component(text):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        product_id, component_id = rest.split(",", 1)
        link_assembly_component(int(product_id.strip()), int(component_id.strip()))
        return "Сборка и комплектующий связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkassemblycomponent <product_id>, <component_id>'."

@command("/linkcomponentsupplier")
def handle_link_component_supplier(text):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        component_id, supplier_id = rest.split(",", 1)
        link_component_supplier(int(component_id.strip()), int(supplier_id.strip()))
        return "Комплектующий и поставщик связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkcomponentsupplier <component_id>, <supplier_id>'."