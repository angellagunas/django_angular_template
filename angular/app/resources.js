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
    .factory('Catalog', [
        '$resource',
        function ($resource) {
            return $resource(
                '/api/v1/catalogs/:id',
                {
                    id: '@id'
                },
                {
                    'query': {
                        method: 'GET',
                        isArray: true
                    },
                    'update': {
                        method: 'patch'
                    }
                }
            );
        }
    ])
    .factory('Area', [
        '$resource',
        function ($resource) {
            return $resource(
                '/api/v1/areas/:id',
                {
                    id: '@id'
                },
                {
                    'query': {
                        method: 'GET',
                        isArray: true
                    },
                    'update': {
                        method: 'patch'
                    }
                }
            );
        }
    ])
    .factory('Item', [
        '$resource',
        function ($resource) {
            return $resource(
                '/api/v1/items/:id',
                {
                    id: '@id'
                },
                {
                    'query': {
                        method: 'GET',
                        isArray: true
                    },
                    'update': {
                        method: 'patch'
                    }
                }
            );
        }
    ])
    .service('GlobalService', ["$http", "$state", "$localStorage", "$base64", "baseUrl", function($http, $state, $localStorage, $base64, baseUrl) {
        'ngInject';
        var logout;
        this.baseUrl = baseUrl;
        
        logout = function() {
          delete $localStorage.token;
          delete $localStorage.profile;
          $state.go('public.login');
        };
        
        this.logout = logout;
    }]);
