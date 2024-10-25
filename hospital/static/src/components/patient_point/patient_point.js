/** @odoo-module **/

import {registry} from '@web/core/registry';
import {useService} from "@web/core/utils/hooks"
const {Component, useState, onWillStart, useRef,onMounted, onWillUpdateProps, onWillUnmount,onPatched} = owl;

export class PatientPoint extends Component {
    rowRef = useRef("row_name");
    modalRef = useRef("modalEdit");
    setup() {
        this.orm = useService('orm');
        this.model = 'res.partner';

        this.state = useState({'patient_list': [],
        'current_edit':0

        });
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

    edit(rowIndex) {
        /*this.rowRef.el.children[rowIndex].children[0].className='text-primary'
        debugger;*/
        this.state.current_edit=rowIndex;
        //this.state.patient_list[patientid].name=`${this.state.patient_list[patientid].name} ~`;
    }

     async confirm() {
         await this.orm.write(this.model, [this.state.patient_list[this.state.current_edit].id], this.state.patient_list[this.state.current_edit]);
         this.rowRef.el.children[this.state.current_edit].children[0].className = 'text-success';
         await this.getAllPatients();
         $('#editPatientModal').modal('hide');
    }

    // add consultation price

}

PatientPoint.template = 'hospital.PatientPoint'
registry.category("actions").add("hospital.patient_point", PatientPoint);