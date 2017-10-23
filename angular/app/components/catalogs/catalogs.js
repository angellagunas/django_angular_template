var app = angular.module('angular_template');

app.controller('CatalogController', function(Catalog) {
    var vm = this;

    Catalog.query({}, function(catalogs){
        vm.catalogs = catalogs;
    });

    return vm;
});
