from CommandsDB.link import *
from Handler.commands import *
from Converter.converter import to_mysql_date

@command("/linkassemblycomponent", description="Связать сборку с комплектующим. Поля: product_id (int) | component_id (int)\nПример: /linkassemblycomponent 1 | 2")
def handle_link_assembly_component(text):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        product_id, component_id = rest.split("|", 1)
        link_assembly_component(int(product_id.strip()), int(component_id.strip()))
        return "Сборка и комплектующий связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате '/linkassemblycomponent <product_id> | <component_id>'."

@command("/linkcomponentsupplier", description="Связать комплектующий с поставщиком. Поля: component_id (int) | supplier_id (int) | supply_date (date) | quantity_delivered (int)\nПример: /linkcomponentsupplier 1 | 2 | 2023-01-01 | 100")
def handle_link_component_supplier(text):
    try:
        # Сначала делим по первому пробелу
        _, rest = text.split(" ", 1)
        # Теперь делим оставшееся по запятым
        component_id, supplier_id, supply_date, quantity_delivered = rest.split("|", 3)
        link_component_supplier(int(component_id.strip()), int(supplier_id.strip()), to_mysql_date(supply_date.strip()), int(quantity_delivered.strip()))
        return "Комплектующий и поставщик связаны!"
    except ValueError:
        return "Ошибка: команда должна быть в формате" \
        " '/linkcomponentsupplier <component_id> | <supplier_id> | <supply_date> | <quantity_delivered>'."