var app = angular.module('myapp', []);

app.controller('MyCtrl', ['$scope', '$http', function ($scope, $http) {
	var p = $http({
      method: 'GET',
      url: 'http://www.beyondcompare.cn:9090/'
      dataType: 'JSON',
    });
    p.success(function(response, status, headers, config){
        $scope.name = response.name;
    });
}])

$(function(){
	// $('#parent').append('<li>xx</li>');
	// $('#child').append('<li>xx</li>');
	// $('.child_item_add').on('click',function(){
	// 	$('#child').append('<li>xxxxxxxx</li>');
	// });
	
	
});
(function(){

})();