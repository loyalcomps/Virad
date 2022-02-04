odoo.define('pos_customer_required.PaymentScreen', function (require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const PosCustomerRequiredPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            async validateOrder(isForceValidate) {
                if(this.env.pos.config.require_customer != 'no' && !this.currentOrder.get_client()){
                    await this.showPopup('ErrorPopup', {
                        title: this.env._t('An anonymous order cannot be confirmed'),
                        body: this.env._t('Please select a customer for this order.'),
                    });
                }
                else{
                    return super.validateOrder(...arguments);
                }
            }

        };

    Registries.Component.extend(PaymentScreen, PosCustomerRequiredPaymentScreen);

    return PaymentScreen;
//    var screens = require('point_of_sale.screens');
//    var gui = require('point_of_sale.gui');
//    var core = require('web.core');
//    var _t = core._t;

//
//    /*
//        Because of clientlist screen behaviour, it is not possible to simply
//        use: set_default_screen('clientlist') + remove cancel button on
//        customer screen.
//
//        Instead of,
//        - we overload the function : show_screen(screen_name,params,refresh),
//        - and we replace the required screen by the 'clientlist' screen if the
//        current PoS Order has no Customer.
//    */
//
//    var _show_screen_ = gui.Gui.prototype.show_screen;
//    gui.Gui.prototype.show_screen = function(screen_name, params, refresh){
//        if(this.pos.config.require_customer == 'order'
//                && !this.pos.get_order().get_client()
//                && screen_name != 'clientlist'){
//            // We call first the original screen, to avoid to break the
//            // 'previous screen' mecanism
//            _show_screen_.call(this, screen_name, params, refresh);
//            screen_name = 'clientlist';
//        }
//        _show_screen_.call(this, screen_name, params, refresh);
//    };

});
