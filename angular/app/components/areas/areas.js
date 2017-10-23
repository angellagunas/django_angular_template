var app = angular.module('angular_template');

app.controller('AreaController', function(Area) {
    var vm = this;

    Area.query({}, function(areas){
        vm.areas = areas;
    });

    return vm;
});
