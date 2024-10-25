/** @odoo-module */

import { registry } from '@web/core/registry';

import {CharField,charField} from "@web/views/fields/char/char_field";


export class CustomCharField extends CharField {}
CustomCharField.template = 'hospital.char_field';



export const customCharField = {
    ...charField,
    component: CustomCharField,
};



registry.category("fields").add("hospital_CustomCharField", customCharField);


