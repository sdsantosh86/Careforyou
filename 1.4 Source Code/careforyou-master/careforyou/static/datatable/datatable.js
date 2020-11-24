// init datatable
const table = $('#services_list').DataTable({
  "columnDefs": [
    { "visible": false, "targets": 0 }
  ]
});
// define a function for mouse event enter
function mouse_enter(){
    $( this ).addClass('bg-gray-200 text-gray-900')
}
// define a function for mouse event out
function mouse_out(){
    $( this ).removeClass('bg-gray-200 text-gray-900')
}
// add mouse hover event on each row
$('#services_list tbody tr').hover( mouse_enter, mouse_out )
// add mouse click event on each row
$('#services_list tbody').on( "click","tr",function (){
    const data = table.row(this).data();
    window.open('details?id='+data[0])
} );