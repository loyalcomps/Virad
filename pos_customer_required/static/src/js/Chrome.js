odoo.define('pos_customer_required.chrome', function (require) {
    'use strict';

    const Chrome = require('point_of_sale.Chrome');
    const Registries = require('point_of_sale.Registries');

    const PosCustomerRequiredChrome = (Chrome) =>
        class extends Chrome {

//            get startScreen() {
//            if (this.state.uiState !== 'READY') {
//                console.warn(
//                    `Accessing startScreen of Chrome component before 'state.uiState' to be 'READY' is not recommended.`
//                );
//            }
//            if(this.env.pos.config.require_customer == 'order'){
//                return { name: 'ClientListScreen' };
//            }
//            else{
//                return { name: 'ProductScreen' };
//            }
//
//        }

//            _showStartScreen() {
//                if(this.env.pos.config.require_customer == 'order' && !this.env.pos.get_order().get_client()
//                    && this.startScreen.name != 'ClientListScreen')
//                {
//                    super._showStartScreen();
//                    const { name, props } = { name: 'ClientListScreen' };
//                    this.showScreen(name, props);
//                }
//            }

//            __showScreen() {
//                super.__showScreen(...arguments);
//                if(this.env.pos.config.require_customer == 'order' && !this.env.pos.get_order().get_client()
//                    && this.mainScreen.name != 'ClientListScreen')
//                    {
//                        const { name, props } = { name: 'ClientListScreen' };
//                        this.showScreen(name, props);
////                        super.__showScreen(...arguments);
////                        const { name, props } = { name: 'ClientListScreen' };
//
//                    }
//
//                this.__showScreen(name, props);
//            }

        };

    Registries.Component.extend(Chrome,PosCustomerRequiredChrome);

    return Chrome;
});