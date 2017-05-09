'use strict'

angular.module('shortioApp')
    .factory('UrlResource', function ($resource) {
        return $resource('/api/urls/:id', {id: '@id'});
    });
