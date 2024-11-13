$(document).ready(function(){
    $('.ui.dropdown').dropdown();
    $('.ui.fluid.dropdown').dropdown();
    $('#leave_request').click(function(){
        $('.tiny.modal').modal('show');
    });
    // Active Attendance Button 
    $('.ui.checkbox').checkbox();

    // For sorting table
    $('table').tablesort();
    $('#back').click(function(){
        window.history.back();
    });
});