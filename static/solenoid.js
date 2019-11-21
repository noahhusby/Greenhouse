$(function() {
    $.ajax({
        url: '/solenoid/info',
        success: function(data) {
            console.log('get info');
            $('#info').html(JSON.stringify(data, null, '   '));
            $('#time').html(data['time']);
			$("#testHeader").text(data['time']);
        }
    });
});