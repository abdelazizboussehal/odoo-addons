/** @odoo-module */
import {KanbanController} from "@web/views/kanban/kanban_controller";
import {kanbanView} from "@web/views/kanban/kanban_view";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {onWillStart} from "@odoo/owl";

export class Custom_kanban_sidebar extends KanbanController {
    async setup() {
        super.setup();
        this.orm = useService('orm');

        onWillStart(async () => {
            this.constomLocation = await this.orm.readGroup('res.partner', [], ["state_id"], ["state_id"]);
            if (this.constomLocation[this.constomLocation.length - 1].state_id == false) {
                this.constomLocation[this.constomLocation.length - 1].state_id = [
                    -2,
                    "Other"
                ];
            }
            console.log(this.constomLocation);
        });

    }
}

Custom_kanban_sidebar.template = 'hospital.custom_kanban_sidebar_template';
export const custom_kanban_sidebar = {
    ...kanbanView,
    Controller: Custom_kanban_sidebar,
}

registry.category("views").add("hospital.custom_kanban_sidebar_id", custom_kanban_sidebar);