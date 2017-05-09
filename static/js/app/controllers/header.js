'use strict';

angular.module('shortioApp')
    .controller('HeaderCtrl', function ($scope, $modal, AuthUser) {
        $scope.username = AuthUser.username;
        $scope.doLogin = function () {
            $modal.open({templateUrl: "/tpl/login"});
        }
    });
