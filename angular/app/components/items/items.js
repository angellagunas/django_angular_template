var app = angular.module('angular_template');

app.controller('ItemController', function(Item, Area) {
    var vm = this;

    Item.query({}, function(items){ vm.items = items; });
    Area.query({}, function(areas){ vm.areas = areas; });

    vm.detail = function(event, item){
        vm.itemSelected = item;
    }

    vm.update = function(event){
        console.info(vm.itemSelected);
    }

    return vm;
});
