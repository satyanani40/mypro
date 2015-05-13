'use strict';

/**
 * @ngdoc function
 * @name sampleAppApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the sampleAppApp
 */
angular.module('sampleAppApp')
  .controller('LoginCtrl', function ($scope, $http) {
        $scope.submitLogin = function() {
            $http({
                method: 'POST',
                url: '/login',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: {
                    email : $scope.formData.email,
                    password: $scope.formData.password
                },

            })
           .success(function (out) {
               console.log(out);
            })
            .error(function (data, status) {

            });
		};
  });
