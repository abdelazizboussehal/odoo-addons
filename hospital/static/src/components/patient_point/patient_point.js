/** @odoo-module **/

import {registry} from '@web/core/registry';
import {useService} from "@web/core/utils/hooks"
const {Component, useState, onWillStart, useRef,onMounted, onWillUpdateProps, onWillUnmount,onPatched} = owl;

export class PatientPoint extends Component {
    elemnTh = useRef('name_column');

    setup() {
        this.orm = useService('orm');
        this.model = 'res.partner';

        this.state = useState({'patient_list': []});
        //this.state = {'patient_list': []};

        onWillStart(async () => {
            await this.getAllPatients();
            console.log("onWillStart");

        })

        onMounted(async () => {

            console.log("onMounted");

        });

        onWillUpdateProps(() => {
            console.log("onWillUpdateProps");
        });

        onWillUnmount(() => {
            console.log("onWillUnmount");
        });
        onPatched(() => {
            console.log("onPatched");
        });
    }


    async getAllPatients() {
        this.state.patient_list = await this.orm.searchRead(this.model, [['isPatient', '=', true]], [])
    }

    async deletePatient(patient_id) {
        console.log('result = ' + patient_id);
        await this.orm.unlink(this.model, [patient_id]);
        await this.getAllPatients();
        //this.render(); force render

    }

    edit() {
        this.elemnTh.el.className='text-primary'
        this.state.patient_list[0].name=`${this.state.patient_list[0].name} 1`;
    }

    // add consultation price

}

PatientPoint.template = 'hospital.PatientPoint'
registry.category("actions").add("hospital.patient_point", PatientPoint);