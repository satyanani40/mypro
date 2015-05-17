'use strict';

/**
 * @ngdoc overview
 * @name sampleAppApp
 * @description
 * # sampleAppApp
 *
 * Main module of the application.
 */
angular
  .module('sampleAppApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
  })
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'static/bower_components/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'static/bower_components/templates/about.html',
        controller: 'AboutCtrl'
      })
      .when('/login', {
        templateUrl: 'static/bower_components/templates/login.html',
        controller: 'LoginCtrl'
      })
      .when('/register', {
        templateUrl: 'static/bower_components/templates/register.html',
        controller: 'RegisterCtrl'
      })
      .when('/courses', {
        templateUrl: 'static/bower_components/templates/courses.html',
        controller: 'AboutCtrl'
      })
      .when('/feedback', {
        templateUrl: 'static/bower_components/templates/feedback.html',
        controller: 'FeedbackCtrl'
      })
      .when('/courses/:categeory', {
        templateUrl: 'static/bower_components/templates/wind-energy.html',
        controller: 'AboutCtrl'
      })
      .when('/courses/:categeory/tutorials', {
        templateUrl: 'static/bower_components/templates/tutorials.html',
        controller: 'ChapterListCtrl'
      })

      .when('/courses/:categeory/tutorials/chapter_pdf/:path', {
        templateUrl: 'static/bower_components/templates/tutorials.html',
        controller: 'ChapterListCtrl'
      })
      .when('/courses/:categeory/tutorials/create-chapter', {
        templateUrl: 'static/bower_components/templates/create-chapter.html',
        controller: 'CreateChapterCtrl'
      })
      .when('/courses/:categeory/assessments/create_assessment', {
        templateUrl: 'static/bower_components/templates/create_assessment.html',
        controller: 'createAssessmentCtrl'
      })
      .when('/courses/:categeory/assessments', {
        templateUrl: 'static/bower_components/templates/assessments.html',
        controller: 'assessmentsCtrl'
      })
      .when('/courses/:categeory/assessments/:exam_name', {
        templateUrl: 'static/bower_components/templates/online.html',
        controller: 'OnlineCtrl'
      })
      .when('/admin', {
        templateUrl: 'static/bower_components/templates/admin.html',
        controller: 'adminCtrl' //located in login.js
      })
      .when('/exam_submit', {
        templateUrl: 'static/bower_components/templates/exam_submit.html',
        controller: 'submitExam' //located in login.js
      })
       .when('/logout', {
        templateUrl: 'static/bower_components/templates/admin.html',
        controller: 'logoutCtrl' //located in login.js
      })
      .otherwise({
        redirectTo: '/'
      });
  });
