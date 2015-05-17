'use strict';

/**
 * @ngdoc function
 * @name sampleAppApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the sampleAppApp
 */
angular.module('sampleAppApp')
  .controller('FeedbackCtrl', function ($scope, $http) {
        $scope.submit_feedback = function(){

        $http({
            method: 'POST',
            url: '/feedback',
            headers: {
                'Content-Type': 'application/json'
            },
            data: {
                content : $scope.content
            },

        })
           .success(function (out) {
               console.log(out);
            })
            .error(function (data, status) {

            });
        };
  });
