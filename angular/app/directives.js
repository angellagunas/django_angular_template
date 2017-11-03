(function() {
    angular.module('angular_template')

        .directive('profileInfoSidebar', [
            '$localStorage', '$content',
            function($localStorage, $content) {
                return {
                  restrict: 'E',
                  templateUrl: $content.url('app/shared/partials/profile-sidebar.html'),
                  link: function(scope) {

                    // Placing a placeholder, when thumbnail is not given.
                    scope.profile = $localStorage.profile;
                    scope.profile.thumbnail = 'http://placehold.it/95x95';

                    return scope;
                  }
                };
            }
        ])
        .directive('routeName', function() {
            return {
              restrict: 'E',
              template: '<span>{{name}}</span>',
              controller: ["$scope", "$rootScope", function($scope, $rootScope) {
                var currentState, setStateNameHeader;
                setStateNameHeader = function(state) {
                  switch (state) {
                    case 'admin.events':
                      return $scope.name = 'Lista de eventos';
                    default:
                      return $scope.name = ':/';
                  }
                };
                currentState = $rootScope.$state.current.name;
                setStateNameHeader(currentState);
                return $rootScope.$on('$stateChangeSuccess', function(event, toState, toParams, fromState, fromParams) {
                  var state;
                  state = toState.name;
                  return setStateNameHeader(state);
                });
              }]
            };
        })
        .directive('passwordMatch', function() {
            var directive, linkFunc;
            linkFunc = function(scope, elem, attrs, ctrl) {
              var firstPassword;
              firstPassword = "." + attrs.passwordMatch;
              elem.add(firstPassword).on('keyup', function() {
                return scope.$apply(function() {
                  var v;
                  v = elem.val() === $(firstPassword).val();
                  return ctrl.$setValidity('pwmatch', v);
                });
              });
            };
            return directive = {
              require: 'ngModel',
              link: linkFunc
            };
        })
        .directive('fileUpload', ["$parse", function($parse) {
            var directive, linkFunc;
            linkFunc = function(scope, element, attrs) {
                var onChangeHandler = scope.$eval(attrs.fileUpload);
                element.bind('change', onChangeHandler);
            };
            return directive = {
              restrict: 'A',
              link: linkFunc
            };
        }])

        .directive('file', ["$parse", "$rootScope", function($parse, $rootScope) {
            var link;
            link = function(scope, element, attrs) {
              return element.bind('change', function(event) {
                var file;
                file = event.target.files[0];
                scope.file = file != null ? file : {
                  file: void 0
                };
                return scope.$apply();
              });
            };
            return {
              link: link,
              scope: {
                file: '='
              }
            };
        }]);
}).call(this);
