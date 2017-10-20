angular.module('angular_template')
    .factory('Auth', [
        '$resource',
        function ($resource) {
            return $resource('/api/v1/signin');
        }
    ])
    .factory('Profile', [
        '$resource',
        function ($resource) {
            return $resource('/api/v1/me');
        }
    ])
    .service('GlobalService', ["$http", "$state", "$localStorage", "$base64", "baseUrl", function($http, $state, $localStorage, $base64, baseUrl) {
        'ngInject';
        var logout;
        this.baseUrl = baseUrl;
        
        logout = function() {
          delete $localStorage.token;
          delete $localStorage.profileInfo;
          delete $localStorage.placeInfo;
          delete $localStorage.userId;
          $state.go('public.login');
        };
        
        this.logout = logout;
    }]);
